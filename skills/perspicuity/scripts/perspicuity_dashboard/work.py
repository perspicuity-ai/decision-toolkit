#!/usr/bin/env python3
"""List current work records without changing records or dispatching work."""

import argparse
from collections import defaultdict
from datetime import date
import json
import os
from pathlib import Path
import re

import yaml


FORMAT = "perspicuity-work/1"
DEFAULT_SOURCES = ("Decisions", "docs/initiatives", "docs/outreach")
RECORD_STATES = {"open", "closed"}
WORK_STATES = {"not_started", "active", "waiting", "submitted", "in_review", "accepted", "stopped"}
QUEUE_STATES = ("blocked", "needs_you", "ready", "waiting", "in_review", "done", "closed", "unclassified")
PRINCIPALS = {"david", "laura"}
REVIEW_FOLLOW_UP_STATES = {"in_review", "submitted"}
READY_STATES = {"active", "not_started"}
EXCLUDED_DIRS = {
    "archive", "archived", "archives", "historical", "history", "copied", "copies",
    "preserved", "retained", "sources", "source", "store", "stores", "snapshot",
    "snapshots", "versions", "example", "examples", "template", "templates",
    "trial", "trials", "fixture", "fixtures", ".git", "__pycache__",
    "node_modules", ".venv", "venv", ".env", ".cache", ".codex", ".agents",
    "skills", "site-packages", "dist", "build", ".next", ".tox",
}
SNAPSHOT_DIR = re.compile(r"(?:[rv]\d+(?:[._-]\d+)*|(?:version|revision|snapshot)[-_].+)$", re.I)
NOTICE = (
    "Dated source evidence, not live agent telemetry or authority. "
    "Queue state, blocked and waiting-on-you are derived from recorded fields. "
    "Checks are mechanical. This command performs no dispatch or writes."
)


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate mapping keys, including keys outside the required fields."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        if key_node.value == "<<":
            raise ValueError("YAML merge keys are unsupported")
        key = loader.construct_object(key_node, deep=True)
        if not isinstance(key, str):
            raise ValueError("header keys must be strings")
        if key in result:
            raise ValueError(f"duplicate header key: {key}")
        result[key] = loader.construct_object(value_node, deep=True)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return None, ""
    for index, line in enumerate(lines[1:], 1):
        if line == "---":
            return "\n".join(lines[1:index]), "\n".join(lines[index + 1:])
    return "\n".join(lines[1:]), None


def current_format(header):
    """Inspect the format node before strict loading, so legacy records stay out."""
    try:
        node = yaml.compose(header, Loader=yaml.SafeLoader)
    except yaml.YAMLError:
        # An exact plain/quoted marker lets malformed current headers remain visible.
        return bool(re.search(
            r"(?m)^format:[ \t]*(['\"]?)perspicuity-work/1\1[ \t]*(?:#.*)?$", header
        ))
    return isinstance(node, yaml.MappingNode) and any(
        isinstance(key, yaml.ScalarNode) and key.value == "format"
        and isinstance(value, yaml.ScalarNode) and value.value == FORMAT
        for key, value in node.value
    )


LABELS = (
    "Principal and decider", "Principal", "Decider", "Work owner", "Decision",
    "Work scope", "Work", "Outcome", "Next", "Blocked", "Waiting on", "Dependency", "Review due", "Next check", "Budget", "Closure",
)
FIELD = re.compile(
    r"(?:^|[ \t]+)\*{0,2}(" + "|".join(LABELS) + r")\*{0,2}:\*{0,2}[ \t]*",
    re.M,
)


def body_field(body, name, current_only=True):
    if current_only:
        match = re.search(r"(?m)^## Current position[ \t]*$", body)
        if not match:
            return "unknown"
        body = body[match.end():]
        body = re.split(r"(?m)^## ", body, maxsplit=1)[0]
    fields = list(FIELD.finditer(body))
    for index, match in enumerate(fields):
        if match.group(1) == name:
            end = fields[index + 1].start() if index + 1 < len(fields) else len(body)
            value = re.split(r"\n\s*\n|\n#{1,6} ", body[match.end():end], maxsplit=1)[0]
            return " ".join(value.split()) or "unknown"
    return "unknown"


def closure_text(body):
    value = body_field(body, "Closure", current_only=False)
    if value != "unknown":
        return value
    match = re.search(r"(?m)^## Closure[ \t]*$", body)
    if match:
        value = re.split(r"(?m)^## ", body[match.end():], maxsplit=1)[0].strip()
        return " ".join(value.split()) or "unknown"
    return "unknown"


def unspecified(value):
    """Recognize absent values and placeholders, without judging their meaning."""
    return value.lower().strip().rstrip(".") in {
        "", "unknown", "pending", "tbd", "todo", "none", "n/a", "not set",
    } or bool(re.fullmatch(r"<.*>[.]?", value))


def iso_date(value):
    """Accept a calendar date, excluding datetime, bool and relaxed ISO forms."""
    if type(value) is date:
        return value
    if isinstance(value, str) and re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        try:
            return date.fromisoformat(value)
        except ValueError:
            pass
    raise ValueError("expected a valid calendar date in YYYY-MM-DD form")


def leading_actor(value):
    """Return the first name-like word of an actor statement, or None."""
    word = value.strip().split(" ", 1)[0].strip(",.;:")
    return word.lower() if re.fullmatch(r"[A-Za-z][A-Za-z'’-]*", word) else None


def derive_queue(record, check_status):
    """Add derived attention fields, without interpreting prose as a state."""
    next_actor = leading_actor(record["next"])
    waiting_actor = leading_actor(record["waiting_on"])
    principal = leading_actor(record["principal"])

    def is_principal(actor):
        return bool(actor and (actor in PRINCIPALS or (principal is not None and actor == principal)))

    record["blocked"] = record["work_status"] == "waiting" and not unspecified(record["dependency"])
    if record["blocked"]:
        # A missing Waiting on line leaves the resolver unknown, so the block stays your attention.
        record["waiting_on_you"] = is_principal(waiting_actor) or (waiting_actor is None and not unspecified(record["next"]))
    else:
        record["waiting_on_you"] = is_principal(next_actor)
    if record["record_status"] == "closed":
        state = "closed"
    elif record["work_status"] == "unclassified":
        state = "unclassified"
    elif record["waiting_on_you"]:
        state = "needs_you"
    elif record["blocked"]:
        state = "blocked"
    elif record["work_status"] in REVIEW_FOLLOW_UP_STATES or check_status == "due":
        state = "waiting"
    elif record["record_status"] == "open":
        state = "ready" if record["work_status"] in READY_STATES else "in_review"
    elif record["work_status"] == "accepted":
        state = "done"
    else:
        state = "waiting"
    record["queue_state"] = state
    return record


def parse_record(text, path):
    header, body = frontmatter(text)
    if header is None or not current_format(header):
        return None
    closed_header = body is not None
    body = body or ""
    record = {
        "path": path, "id": None, "revision": None, "updated": "unknown",
        "record_status": "unclassified", "work_status": "unclassified",
        "principal": body_field(body, "Principal and decider"),
        "work_scope": body_field(body, "Work scope"),
        "work_owner": body_field(body, "Work owner"),
        "decision": body_field(body, "Decision"),
        "work": body_field(body, "Work"),
        "outcome": body_field(body, "Outcome"),
        "dependency": body_field(body, "Dependency"),
        "waiting_on": body_field(body, "Waiting on"),
        "review_due": body_field(body, "Review due"),
        "next_check": body_field(body, "Next check"),
        "next_check_date": None,
        "review_due_date": None,
        "next": body_field(body, "Next"), "issues": [],
    }
    if record["dependency"] == "unknown":
        record["dependency"] = body_field(body, "Blocked")
    if record["waiting_on"] == "unknown":
        record["waiting_on"] = body_field(body, "Waiting on")
    if not closed_header:
        record["issues"].append("front matter lacks its closing delimiter")
    try:
        data = yaml.load(header, Loader=UniqueLoader)
    except (yaml.YAMLError, ValueError) as error:
        record["issues"].append(f"invalid front matter: {error}")
        return record
    if not isinstance(data, dict):
        record["issues"].append("invalid front matter: header must be a mapping")
        return record
    identifier = data.get("id")
    if not isinstance(identifier, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:-]*", identifier):
        record["issues"].append("id must be a nonempty identifier without spaces or placeholders")
    else:
        record["id"] = identifier
    revision = data.get("revision")
    if type(revision) is not int or revision < 1:
        record["issues"].append("revision must be a positive integer")
    else:
        record["revision"] = revision
    if "updated" in data:
        record["updated"] = str(data["updated"])
    if "next_check" in data:
        try:
            record["next_check_date"] = iso_date(data["next_check"]).isoformat()
        except ValueError as error:
            record["issues"].append(f"invalid next_check: {error}")
    if "review_due" in data and data["review_due"] not in (None, ""):
        try:
            record["review_due_date"] = iso_date(data["review_due"]).isoformat()
        except ValueError as error:
            record["issues"].append(f"invalid review_due: {error}")
    for field, allowed in (("record_status", RECORD_STATES), ("work_status", WORK_STATES)):
        if field not in data:
            continue
        value = data[field]
        if not isinstance(value, str) or value not in allowed:
            record["issues"].append(f"invalid {field}: {value!r}")
        else:
            record[field] = value
    classified = record["record_status"] != "unclassified" or record["work_status"] != "unclassified"
    if classified and unspecified(record["work_scope"]):
        record["issues"].append("classified records require a named Work scope in Current position")
    if record["record_status"] == "open" and unspecified(record["next"]):
        record["issues"].append("open records require a Next action and actor in Current position")
    if record["work_status"] == "waiting" and unspecified(record["dependency"]):
        record["issues"].append("blocked work requires an explicit Dependency in Current position")
    if record["work_status"] == "in_review":
        if record["next_check_date"] is None:
            record["issues"].append("in_review work requires a checkpoint date")
        elif record["review_due_date"] is None:
            record["issues"].append("in_review work requires a machine-readable review_due date")
        if unspecified(record["review_due"]):
            record["issues"].append("in_review work requires a Review due line with its evidence source and owner")
    if record["record_status"] == "closed":
        if record["next_check_date"] is not None:
            record["issues"].append("closed records must not carry a next_check date")
        if record["work_status"] not in {"accepted", "stopped"}:
            record["issues"].append("closed records require accepted or stopped work")
        closure = closure_text(body)
        if unspecified(closure):
            record["issues"].append("closed records require an explicit Closure explanation")
    return record


def excluded_component(parts):
    return next((part for part in parts if part.lower() in EXCLUDED_DIRS or SNAPSHOT_DIR.fullmatch(part)), None)


def scan(root, sources=None, as_of=None):
    root = Path(root).expanduser().absolute()
    if root != root.resolve() or not root.is_dir():
        raise ValueError("root must be an existing directory reached without symlinks")
    sources = list(DEFAULT_SOURCES if sources is None else sources)
    as_of = date.today() if as_of is None else iso_date(as_of)
    result = {
        "notice": NOTICE, "root": str(root), "sources": sources,
        "as_of": as_of.isoformat(),
        "coverage": {"markdown_files": 0, "current_records": 0, "other_markdown": 0, "non_markdown": 0},
        "exclusion_policy": sorted(EXCLUDED_DIRS) + ["version/revision/snapshot directories", "symlinks", "outside root"],
        "exclusions": [], "records": [], "issues": [], "warnings": [],
    }
    visited = set()

    def exclude(path, reason):
        result["exclusions"].append({"path": str(path), "reason": reason})

    def issue(path, message):
        result["issues"].append({"path": str(path), "message": message})

    def visit(path):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            exclude(relative, "symlink")
            return
        if excluded_component(path.relative_to(root).parts):
            exclude(relative, "excluded historical, copied, example, template or trial path")
            return
        if relative in visited:
            return
        visited.add(relative)
        try:
            if path.is_dir():
                if path != root and (path / ".git").exists():
                    exclude(relative, "nested project")
                    return
                with os.scandir(path) as entries:
                    children = sorted((Path(entry.path) for entry in entries), key=str)
                for child in children:
                    visit(child)
                return
            if path.suffix.lower() != ".md":
                result["coverage"]["non_markdown"] += 1
                return
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            exclude(relative, f"unreadable: {error}")
            issue(relative, "coverage incomplete: unreadable source")
            return
        result["coverage"]["markdown_files"] += 1
        record = parse_record(text, relative)
        if record is None:
            result["coverage"]["other_markdown"] += 1
        else:
            result["records"].append(record)

    for source in sources:
        raw = Path(source)
        path = Path(os.path.abspath(root / raw))
        try:
            relative = path.relative_to(root)
        except ValueError:
            exclude(source, "outside root")
            issue(source, "coverage incomplete: source is outside root")
            continue
        cursor = root
        has_symlink = False
        for part in relative.parts:
            cursor = cursor / part
            if cursor.is_symlink():
                has_symlink = True
                break
        if has_symlink:
            exclude(source, "symlink in source path")
            continue
        if not path.exists():
            exclude(source, "source does not exist")
            issue(source, "coverage incomplete: source does not exist")
            continue
        visit(path)

    identities = defaultdict(list)
    for record in result["records"]:
        if record["id"]:
            identities[record["id"]].append(record)
    for identifier, records in identities.items():
        if len(records) > 1:
            paths = ", ".join(record["path"] for record in records)
            for record in records:
                record["issues"].append(f"duplicate id {identifier}: {paths}")
    result["records"].sort(key=lambda record: record["path"])
    for record in result["records"]:
        checkpoint = record["next_check_date"]
        record["check_status"] = (
            "unscheduled" if checkpoint is None else "due" if checkpoint <= result["as_of"] else "upcoming"
        )
        derive_queue(record, record["check_status"])
        if (checkpoint is None and record["record_status"] == "open"
                and not record["blocked"] and record["work_status"] != "in_review"):
            result["warnings"].append({
                "path": record["path"],
                "message": "No usable next_check date is recorded. Untimed work keeps this record in the open queue.",
            })
        for message in record["issues"]:
            issue(record["path"], message)
    result["coverage"]["current_records"] = len(result["records"])
    result["coverage"]["unclassified_records"] = sum(
        "unclassified" in (record["record_status"], record["work_status"])
        for record in result["records"]
    )
    for state in ("due", "upcoming", "unscheduled"):
        result["coverage"][f"{state}_open_records"] = sum(
            record["record_status"] == "open" and record["check_status"] == state
            for record in result["records"]
        )
    for state in ("blocked", "needs_you", "in_review"):
        result["coverage"][f"{state}_open_records"] = sum(
            record["record_status"] == "open" and record["queue_state"] == state
            for record in result["records"]
        )
    return result


def filtered(result, record_status=None, work_status=None, due=False, queue_state=None):
    output = dict(result)
    output["records"] = [record for record in result["records"] if (
        record["issues"] or "unclassified" in (record["record_status"], record["work_status"])
        or ((record_status is None or record["record_status"] == record_status)
            and (work_status is None or record["work_status"] == work_status)
            and (queue_state is None or record["queue_state"] == queue_state)
            and (not due or (record["record_status"] == "open"
                             and record["check_status"] in {"due", "unscheduled"})))
    )]
    output["filters"] = {"record_status": record_status, "work_status": work_status,
                         "queue_state": queue_state, "due": due}
    return output


def markdown(result):
    def cell(value):
        return str(value if value is not None else "unknown").replace("|", "\\|").replace("\n", " ")

    lines = ["# Current work records", "", NOTICE, "",
             f"Checkpoint dates evaluated as of {result['as_of']}. Dates use the local calendar unless --due supplies a date.", "",
             "Missing or invalid states stay visible under filters. No state is inferred from prose.", "",
             "| Path | Revision | Record | Work | Queue | Work scope | Next |",
             "|---|---|---|---|---|---|---|"]
    for record in result["records"]:
        lines.append("| " + " | ".join(cell(record[key]) for key in (
            "path", "revision", "record_status", "work_status", "queue_state", "work_scope", "next"
        )) + " |")
    if result["records"]:
        lines.extend(["", "## Dated checkpoints", "",
                      "The source is YAML next_check. Unscheduled means no usable date is recorded; untimed obligations may remain.", "",
                      "| Path | Source date | Check as of " + result["as_of"] + " |", "|---|---|---|"])
        for record in result["records"]:
            lines.append("| " + " | ".join(cell(record[key]) for key in (
                "path", "next_check_date", "check_status"
            )) + " |")
        lines.extend(["", "## Current position details", "",
                      "Review dates and triggers are recorded obligations, not scheduled reminders."])
        for record in result["records"]:
            lines.extend(["", "### " + cell(record["path"]), ""])
            for label, key in (
                ("Updated", "updated"), ("Work owner", "work_owner"),
                ("Decision", "decision"), ("Work", "work"), ("Outcome", "outcome"),
                ("Blocked", "dependency"), ("Review due", "review_due"), ("Next check", "next_check"),
            ):
                lines.append(f"- {label}: {cell(record[key])}")
    lines.extend(["", "## Coverage", "", "Sources: " + ", ".join(result["sources"]), "",
                  "; ".join(f"{key}: {value}" for key, value in result["coverage"].items()) + ".",
                  f"Visible records: {len(result['records'])}.", "",
                  "Excluded path rules: " + ", ".join(result["exclusion_policy"]) + "."])
    if result["exclusions"]:
        lines.extend(["", "Excluded paths:", ""])
        lines.extend(f"- {item['path']}: {item['reason']}" for item in result["exclusions"])
    if result["warnings"]:
        lines.extend(["", "## Checkpoint warnings", ""])
        lines.extend(f"- {item['path']}: {item['message']}" for item in result["warnings"])
    lines.extend(["", "## Mechanical checks", ""])
    if result["issues"]:
        lines.extend(f"- {item['path']}: {item['message']}" for item in result["issues"])
    else:
        lines.append("No mechanical errors found. This does not establish acceptance, authority or completeness.")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, epilog=(
        "Checkpoint dates are evaluated against local today unless --due supplies a date. "
        "Due means on or before that date. Unscheduled records have no usable checkpoint date. "
        "Invalid and unclassified records remain visible under every filter."
    ))
    parser.add_argument("--root", default=str(Path.cwd()))
    parser.add_argument("--source", action="append", help="Source file or directory within root; repeat as needed")
    parser.add_argument("--record-status", choices=sorted(RECORD_STATES))
    parser.add_argument("--work-status", choices=sorted(WORK_STATES))
    parser.add_argument("--queue-state", choices=sorted(QUEUE_STATES))
    parser.add_argument("--due", nargs="?", const=date.today(), type=iso_date, metavar="YYYY-MM-DD",
                        help="Show open due and unscheduled records; default date is local today")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of Markdown")
    parser.add_argument("--check", action="store_true", help="Exit 1 for mechanical errors, including hidden records")
    args = parser.parse_args(argv)
    try:
        result = scan(args.root, args.source, as_of=args.due)
    except ValueError as error:
        parser.error(str(error))
    output = filtered(result, args.record_status, args.work_status, due=args.due is not None,
                      queue_state=args.queue_state)
    print(json.dumps(output, indent=2) if args.json else markdown(output))
    return 1 if args.check and result["issues"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
