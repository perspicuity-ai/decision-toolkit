"""Read project task metadata and bounded saved turn evidence from local Codex."""

from __future__ import annotations

import json
import os
from pathlib import Path
import sqlite3
import stat
from datetime import datetime, timedelta, timezone
from urllib.parse import quote


ROLLOUT_TAIL_BYTES = 512 * 1024
RECENT_WORKER_HOURS = 24
STALE_START_MINUTES = 30
NOTICE = (
    "Shows unarchived project tasks and spawned workers updated within 24 hours, "
    "including recently archived workers. Internal guardian tasks are omitted. "
    "Turn state comes from the last 512 KiB of a saved session. A start older than "
    "30 minutes is stale evidence. Saved events do not prove that a process is "
    "running or that the work is complete. Task links and worker relationships "
    "come from Codex metadata; record relationships are not inferred from titles. "
    "Worker labels use saved agent paths when no task name exists."
)


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def _timestamp(value: object) -> datetime | None:
    try:
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return datetime.fromtimestamp(value, timezone.utc)
        if isinstance(value, str):
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if parsed.tzinfo is not None:
                return parsed.astimezone(timezone.utc)
    except (ValueError, OverflowError, OSError):
        pass
    return None


def _safe_tail(raw_path: object, codex_home: Path) -> bytes:
    """Reject outside paths and symlinks, including parent-directory symlinks."""
    if not isinstance(raw_path, str):
        raise ValueError("missing saved session path")
    path = Path(raw_path)
    if not path.is_absolute() or ".." in path.parts:
        raise ValueError("saved session path is outside the allowed directories")
    try:
        parts = path.relative_to(codex_home).parts
    except ValueError:
        raise ValueError("saved session path is outside the allowed directories") from None
    if len(parts) < 2 or parts[0] not in {"sessions", "archived_sessions"}:
        raise ValueError("saved session path is outside the allowed directories")
    if path.suffix != ".jsonl":
        raise ValueError("saved session path is not a JSONL file")

    # Some supported Python hosts do not provide directory-relative opens or
    # no-follow flags. Keep task metadata available without weakening the
    # session boundary with a path-based check followed by an unsafe open.
    required_flags = ("O_DIRECTORY", "O_NOFOLLOW", "O_NONBLOCK")
    if (
        not all(isinstance(getattr(os, flag, None), int) for flag in required_flags)
        or os.open not in getattr(os, "supports_dir_fd", ())
    ):
        raise ValueError("saved session evidence is unavailable on this platform; safe directory access is unsupported")

    directory_fd = os.open(codex_home, os.O_RDONLY | os.O_DIRECTORY)
    try:
        for component in parts[:-1]:
            next_fd = os.open(
                component, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                dir_fd=directory_fd,
            )
            os.close(directory_fd)
            directory_fd = next_fd
        file_fd = os.open(
            parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK,
            dir_fd=directory_fd,
        )
        with os.fdopen(file_fd, "rb") as session:
            info = os.fstat(session.fileno())
            if not stat.S_ISREG(info.st_mode):
                raise ValueError("saved session is not a regular file")
            offset = max(0, info.st_size - ROLLOUT_TAIL_BYTES)
            session.seek(offset)
            data = session.read(ROLLOUT_TAIL_BYTES)
            if offset:
                # The first line may start before the bounded tail.
                data = data.partition(b"\n")[2]
            return data
    finally:
        os.close(directory_fd)


def _turn_state(raw_path: object, codex_home: Path, now: datetime) -> tuple[str, str | None, list[str]]:
    try:
        data = _safe_tail(raw_path, codex_home)
    except ValueError as error:
        return "unknown", None, [str(error)]
    except NotImplementedError:
        return "unknown", None, ["saved session evidence is unavailable on this platform; safe directory access is unsupported"]
    except OSError:
        return "unknown", None, ["saved session unavailable or unsafe to read"]

    last_state = "unknown"
    state_at = None
    damaged = False
    # Only these event metadata fields leave this function. Messages and tool
    # payloads never enter the response, including on malformed input.
    states = {"task_started": "started", "task_complete": "completed", "turn_aborted": "aborted"}
    for line in data.splitlines():
        try:
            item = json.loads(line)
        except (ValueError, UnicodeError):
            damaged = True
            continue
        if not isinstance(item, dict) or item.get("type") != "event_msg":
            continue
        payload = item.get("payload")
        if not isinstance(payload, dict):
            continue
        event_type = payload.get("type")
        if not isinstance(event_type, str) or event_type not in states:
            continue
        at = _timestamp(item.get("timestamp"))
        if at is None or at > now + timedelta(minutes=5):
            damaged = True
            continue
        last_state = states[payload["type"]]
        state_at = at

    issues = []
    if damaged:
        # A damaged trailing event could contain the actual newest state.
        # Keep any earlier event timestamp as evidence, but do not claim state.
        issues.append("saved session tail contains partial or invalid events; turn state is unknown")
        return "unknown", _iso(state_at) if state_at else None, issues
    if last_state == "started" and now - state_at > timedelta(minutes=STALE_START_MINUTES):
        last_state = "started_stale"
    return last_state, _iso(state_at) if state_at else None, issues


def _source_kind(source: object) -> tuple[str, str | None]:
    if not isinstance(source, str):
        raise ValueError("unsupported task source metadata")
    if not source.startswith("{"):
        return "task", None
    try:
        parsed = json.loads(source)
    except (ValueError, UnicodeError):
        raise ValueError("invalid task source metadata") from None
    if not isinstance(parsed, dict):
        raise ValueError("unsupported task source metadata")
    subagent = parsed.get("subagent")
    if subagent is None:
        return "task", None
    if not isinstance(subagent, dict):
        raise ValueError("unsupported worker source metadata")
    spawn = subagent.get("thread_spawn")
    if spawn is None:
        return "internal", None
    if not isinstance(spawn, dict):
        raise ValueError("unsupported worker source metadata")
    parent = spawn.get("parent_thread_id")
    if not isinstance(parent, str) or not parent:
        raise ValueError("worker source metadata has no explicit parent")
    return "worker", parent


def read_tasks(root: Path, codex_home: Path | None = None) -> dict:
    """Return task metadata without writing to Codex or inspecting message text."""
    now = _now()
    result = {
        "available": False, "observed_at": _iso(now), "tasks": [],
        "issues": [], "notice": NOTICE,
    }
    try:
        selected_home = codex_home if codex_home is not None else os.environ.get("CODEX_HOME") or Path.home() / ".codex"
        home = Path(selected_home).expanduser().resolve()
        database = home / "state_5.sqlite"
        if not database.is_file():
            result["issues"].append("Local Codex task database is unavailable.")
            return result
    except (OSError, RuntimeError, ValueError):
        result["issues"].append("Local Codex task directory is unavailable.")
        return result
    expected = {
        "threads": {"id", "name", "cwd", "archived", "updated_at", "rollout_path", "source", "agent_path", "thread_section_id"},
        "thread_spawn_edges": {"parent_thread_id", "child_thread_id"},
        "thread_sections": {"id", "name"},
    }
    try:
        connection = sqlite3.connect(database.as_uri() + "?mode=ro", uri=True, timeout=1)
        try:
            connection.execute("PRAGMA query_only=ON")
            for table, columns in expected.items():
                actual = {row[1] for row in connection.execute(f"PRAGMA table_info({table})")}
                if not columns <= actual:
                    result["issues"].append(f"Local Codex task schema is unsupported ({table}).")
                    return result
            connection.row_factory = sqlite3.Row
            # An exact cwd match keeps other projects outside this dashboard.
            rows = connection.execute(
                "SELECT t.id, t.name, t.archived, t.updated_at, t.rollout_path, "
                "t.source, t.agent_path, s.name AS section, e.parent_thread_id "
                "FROM threads t LEFT JOIN thread_sections s ON s.id=t.thread_section_id "
                "LEFT JOIN thread_spawn_edges e ON e.child_thread_id=t.id "
                "WHERE t.cwd=? ORDER BY t.updated_at DESC, t.id",
                (str(root.resolve()),),
            ).fetchall()
        finally:
            connection.close()
    except (sqlite3.Error, OSError, ValueError):
        result["issues"].append("Local Codex task database could not be read.")
        return result

    recent_after = now - timedelta(hours=RECENT_WORKER_HOURS)
    for row in rows:
        task_id = row["id"]
        try:
            kind, source_parent = _source_kind(row["source"])
        except ValueError as error:
            result["issues"].append(f"Task {task_id}: {error}.")
            continue
        if kind == "internal":
            continue
        edge_parent = row["parent_thread_id"]
        parent_id = edge_parent or source_parent
        if edge_parent and source_parent and edge_parent != source_parent:
            parent_id = None
            result["issues"].append(f"Task {task_id}: conflicting saved parent relationships.")
        if parent_id or (row["agent_path"] and row["agent_path"] != "/root"):
            kind = "worker"
        updated_at = _timestamp(row["updated_at"])
        if updated_at is None:
            result["issues"].append(f"Task {task_id}: invalid saved update time.")
            continue
        if kind == "worker":
            if updated_at < recent_after:
                continue
            if not parent_id:
                result["issues"].append(f"Task {task_id}: no unambiguous saved parent relationship.")
        elif row["archived"]:
            continue
        state, state_at, issues = _turn_state(row["rollout_path"], home, now)
        result["issues"].extend(f"Task {task_id}: {issue}." for issue in issues)
        result["tasks"].append({
            "id": task_id,
            # In this schema `title` duplicates the original prompt. `name` is
            # the actual sidebar title. Workers commonly have a path, no name.
            "title": row["name"] or row["agent_path"] or "",
            "kind": kind,
            "parent_id": parent_id,
            "updated_at": _iso(updated_at),
            "state": state,
            "state_at": state_at,
            "section": row["section"],
            "href": f"codex://threads/{quote(task_id, safe='')}",
        })
    result["available"] = True
    return result
