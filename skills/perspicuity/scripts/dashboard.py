#!/usr/bin/env python3
"""Start, inspect or stop the Operations dashboard for one project."""

import argparse
from contextlib import contextmanager, nullcontext
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import urllib.request
import webbrowser

sys.dont_write_bytecode = True


def cache_dir(root):
    if os.name == "nt":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData/Local"))
    elif sys.platform == "darwin":
        base = Path.home() / "Library/Caches"
    else:
        base = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache"))
    key = hashlib.sha256(str(root).encode()).hexdigest()
    path = base / "perspicuity/dashboards" / key
    path.mkdir(parents=True, exist_ok=True, mode=0o700)
    return path


@contextmanager
def project_lock(directory):
    with (directory / "launcher.lock").open("a+b") as lock:
        if os.name == "nt":
            import msvcrt
            lock.seek(0)
            if not lock.read(1):
                lock.write(b"0")
                lock.flush()
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_LOCK, 1)
        else:
            import fcntl
            fcntl.flock(lock, fcntl.LOCK_EX)
        try:
            yield
        finally:
            if os.name == "nt":
                lock.seek(0)
                msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(lock, fcntl.LOCK_UN)


def request(state, path, stop=False):
    port = state["port"]
    if type(port) is not int or not 0 < port < 65536:
        raise ValueError("Invalid local port")
    url = f"http://127.0.0.1:{port}{path}"
    req = urllib.request.Request(url, method="POST" if stop else "GET")
    if stop:
        req.add_header("Authorization", "Bearer " + state["token"])
    # Local control requests must not use a configured HTTP proxy.
    with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(req, timeout=2) as response:
        return json.load(response)


def running(directory, root):
    try:
        state = json.loads((directory / "server.json").read_text())
        identity = request(state, "/api/identity")
        if (identity["application"] == "perspicuity-operations"
                and identity["root"] == str(root) and identity["instance"] == state["instance"]):
            return state
    except (OSError, ValueError, KeyError, TypeError):
        pass
    return None


def serve(root, port, codex_home, directory, child=False):
    try:
        from perspicuity_dashboard.server import make_server
    except ModuleNotFoundError as error:
        if error.name == "yaml":
            raise ValueError("Install PyYAML with this Python interpreter: python -m pip install PyYAML") from error
        raise
    with nullcontext() if child else project_lock(directory):
        if not child and running(directory, root):
            raise ValueError("This project's dashboard is already running. Use status to get its address.")
        server = make_server(root, port, codex_home)
        state = {**server.identity, "port": server.server_port, "token": server.token, "pid": os.getpid()}
        path = directory / "server.json"
        temporary = directory / f"server-{os.getpid()}.tmp"
        try:
            fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
            with os.fdopen(fd, "w") as stream:
                json.dump(state, stream)
            temporary.replace(path)
        except OSError:
            server.server_close()
            raise
    try:
        print(f"http://127.0.0.1:{server.server_port}/operations/", flush=True)
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        try:
            if json.loads(path.read_text()).get("instance") == state["instance"]:
                path.unlink()
        except (OSError, ValueError):
            pass


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", nargs="?", choices=["start", "status", "stop", "serve"], default="start")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project directory; defaults to the current directory")
    parser.add_argument("--port", type=int, default=0, help="Choose a port, or use an available port by default")
    parser.add_argument("--codex-home", type=Path, help="Optional Codex data directory; defaults to CODEX_HOME or ~/.codex")
    parser.add_argument("--no-open", action="store_true", help="Print the address without opening a browser")
    parser.add_argument("--child", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    try:
        root = args.root.expanduser().resolve(strict=True)
        if not root.is_dir():
            raise ValueError("Select an existing project directory.")
        if not 0 <= args.port < 65536:
            raise ValueError("The port must be between 0 and 65535.")
        codex_home = args.codex_home.expanduser().resolve() if args.codex_home else None
        directory = cache_dir(root)
        if args.child or args.command == "serve":
            serve(root, args.port, codex_home, directory, child=args.child)
            return 0
        with project_lock(directory):
            state = running(directory, root)
            if args.command == "stop":
                if state:
                    request(state, "/api/shutdown", stop=True)
                    for _ in range(40):
                        if not running(directory, root):
                            break
                        time.sleep(0.1)
                    else:
                        raise ValueError("The dashboard did not stop. Inspect the local dashboard log.")
                print("Dashboard stopped." if state else "No dashboard is running for this project.")
                return 0
            if args.command == "status" and not state:
                print("No dashboard is running for this project.")
                return 1
            if not state:
                command = [sys.executable, str(Path(__file__).resolve()), "serve", "--child", "--root", str(root), "--port", str(args.port)]
                if codex_home:
                    command += ["--codex-home", str(codex_home)]
                options = {"creationflags": subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP} if os.name == "nt" else {"start_new_session": True}
                with (directory / "dashboard.log").open("wb") as log:
                    process = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=log, stderr=log, cwd=root, **options)
                for _ in range(100):
                    state = running(directory, root)
                    if state or process.poll() is not None:
                        break
                    time.sleep(0.1)
                if not state:
                    if process.poll() is None:
                        process.terminate()
                        process.wait(timeout=5)
                    raise ValueError(f"Dashboard startup failed. Read {directory / 'dashboard.log'}")
            url = f"http://127.0.0.1:{state['port']}/operations/"
            print(url)
            if args.command == "start" and not args.no_open:
                webbrowser.open(url)
            return 0
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
