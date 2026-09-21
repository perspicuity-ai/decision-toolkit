"""Serve one project's saved records and local task evidence."""

from datetime import datetime, timezone
from html import escape
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import secrets
from threading import Thread
from urllib.parse import parse_qs, urlsplit

from .records import read_records, read_record
from .tasks import read_tasks

VERSION = "0.2.5"
ASSETS = Path(__file__).resolve().parents[2] / "assets/dashboard"
FILES = {"/": ("index.html", "text/html"), "/app.js": ("app.js", "text/javascript"),
         "/style.css": ("style.css", "text/css"), "/navigation.css": ("navigation.css", "text/css")}
FILES.update({"/vendor/" + name: ("vendor/" + name, "text/javascript")
              for name in ("marked.umd.js", "purify.min.js")})


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def send(self, code, content, kind="application/json"):
        if isinstance(content, (dict, list)):
            content = json.dumps(content, ensure_ascii=False).encode()
        elif isinstance(content, str):
            content = content.encode()
        self.send_response(code)
        self.send_header("Content-Type", kind + ("; charset=utf-8" if kind.startswith("text/") or kind == "application/json" else ""))
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self' data:; object-src 'none'; frame-ancestors 'none'; base-uri 'none'; form-action 'none'")
        self.end_headers()
        self.wfile.write(content)

    def valid_request(self):
        hosts = {f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"}
        if (self.headers.get("Host") not in hosts
                or self.headers.get("Origin") not in {None, *(f"http://{host}" for host in hosts)}
                or self.headers.get("Sec-Fetch-Site") == "cross-site"):
            self.send(403, {"error": "Open this dashboard through its local address."})
            return False
        return True

    def do_GET(self):
        if not self.valid_request():
            return
        url = urlsplit(self.path)
        path = url.path
        if path == "/operations" or path.startswith("/operations/"):
            path = path[len("/operations"):] or "/"
        try:
            if path == "/api/identity":
                return self.send(200, self.server.identity)
            if path == "/api/overview":
                return self.send(200, {
                    "generated_at": datetime.now(timezone.utc).isoformat(),
                    "project": {"name": self.server.root.name, "root": str(self.server.root)},
                    "records": read_records(self.server.root, ["."]),
                    "tasks": read_tasks(self.server.root, self.server.codex_home),
                })
            if path == "/source":
                query = parse_qs(url.query)
                requested = query.get("path", [""])[0]
                try:
                    record = read_record(self.server.root, requested, ["."])
                except ValueError:
                    return self.send(404, {"error": "This source is outside the project's current records."})
                if query.get("format") == ["json"]:
                    return self.send(200, record)
                return self.send(200, record["source"], "text/plain")
            if path in FILES:
                filename, kind = FILES[path]
                content = (ASSETS / filename).read_bytes()
                if filename == "index.html":
                    header = ('<header class="dashboardHeader"><a class="dashboardBrand" href="/operations/">'
                              '<span class="dashboardMark">P</span>Perspicuity</a>'
                              '<nav class="dashboardNav" aria-label="Dashboards"><a href="/operations/" '
                              'aria-current="page">Operations</a></nav><span class="dashboardPrivate">'
                              + escape(self.server.root.name) + '</span></header>')
                    content = content.decode().replace("<!-- dashboard-navigation -->", header)
                    content = content.replace("</head>", '<link rel="stylesheet" href="/navigation.css"></head>')
                return self.send(200, content, kind)
            self.send(404, {"error": "This dashboard page does not exist."})
        except (OSError, ValueError, RuntimeError, UnicodeError) as error:
            self.send(503, {"error": "A local source could not be read.", "reason": type(error).__name__})

    def do_POST(self):
        if not self.valid_request():
            return
        if self.path != "/api/shutdown":
            return self.send(404, {"error": "This action does not exist."})
        expected = "Bearer " + self.server.token
        if not secrets.compare_digest(self.headers.get("Authorization", ""), expected):
            return self.send(403, {"error": "Use the local launcher to stop this dashboard."})
        self.send(200, {"stopping": True})
        Thread(target=self.server.shutdown, daemon=True).start()


def make_server(root, port=0, codex_home=None):
    root = Path(root).expanduser().resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Select an existing project directory.")
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    server.root = root
    server.codex_home = codex_home
    server.token = secrets.token_urlsafe(32)
    server.identity = {"application": "perspicuity-operations", "version": VERSION,
                       "root": str(root), "instance": secrets.token_hex(16)}
    return server
