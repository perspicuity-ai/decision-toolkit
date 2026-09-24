#!/usr/bin/env python3
"""List current work records without changing records or dispatching work."""

import argparse
from collections import defaultdict
from datetime import date
import json
import os
from pathlib import Path
import re
import subprocess

import yaml


FORMAT = "perspicuity-work/1"
PLAN_FORMAT = "perspicuity-plan/1"
FORMATS = (FORMAT, PLAN_FORMAT)
DEFAULT_SOURCES = ("Decisions", "docs/initiatives", "docs/outreach", "docs/plans")
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
    """Return the declared format when this convention governs the document.

    Returns None for anything else, so a legacy record, an unrelated Markdown file
    and a document type added later all stay out without being read as a record.
    """
    try:
        node = yaml.compose(header, Loader=yaml.SafeLoader)
    except yaml.YAMLError:
        # An exact plain/quoted marker lets malformed current headers remain visible.
        match = re.search(
            r"(?m)^format:[ \t]*(['\"]?)(perspicuity-(?:work|plan)/1)\1[ \t]*(?:#.*)?$", header
        )
        return match.group(2) if match else None
    if not isinstance(node, yaml.MappingNode):
        return None
    for key, value in node.value:
        if (isinstance(key, yaml.ScalarNode) and key.value == "format"
                and isinstance(value, yaml.ScalarNode) and value.value in FORMATS):
            return value.value
    return None


LABELS = (
    "Mode", "Principal and decider", "Principal", "Decider", "Work owner", "Plan owner", "Decision",
    "Work scope", "Plan scope", "Ships as", "Done when", "Ship to", "Pre-run gate", "Exit", "Work", "Outcome", "Next", "Blocked",
    "Waiting on", "Dependency", "Review due", "Next check", "Budget", "Closure", "Received", "Giver", "Verdict",
)
MODES = ("plan", "run", "review", "accept")
# Records from skill 0.6.0 carry the fields below; earlier records are read as written.
FIELD_CHECKS_FROM = (0, 6, 0)
# Plans from skill 0.7.0 name their finished product in Ships as.
LOOP_CHECKS_FROM = (0, 7, 0)
# A Next line that says nothing is left, and names no actor: "None.", "none in this batch.", "No further action."
NOTHING_NEXT = re.compile(
    r"(?i)(?:none|nothing|no further (?:action|work))(?:[ \t]+(?:further|left|remaining|more))?"
    r"(?:[ \t]+(?:in|for|on)[ \t]+this\b[^.;]*)?[ \t]*(?:[.;:]|$)")
URL = re.compile(r"https?://[^\s)>\]`'\"]+")
GRANT_FIELDS = ("For", "Serves", "Intent", "Done when", "Ship to", "Includes", "Tolerances",
                "Escalate if", "Return to", "Accepted by", "Granted by")
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


def read_mode(body):
    """Read the declared working mode, so a mode is visible to the tools.

    Accepts the emphasis the corpus uses, e.g. 'Mode: **Plan.** The sequence stops...'.
    Returns None when no mode is declared, which is not an error: older records have none.
    """
    match = re.search(r"(?m)^\*{0,2}Mode\*{0,2}\s*:\s*\*{0,2}\s*([A-Za-z]+)", body)
    if not match:
        return None
    value = match.group(1).strip().strip("*").lower()
    return value if value in MODES else None


def skill_version_tuple(value):
    """Read a skill_version such as 0.6.0 as a comparable tuple, or None."""
    match = re.fullmatch(r"\s*(\d+)\.(\d+)\.(\d+)\S*\s*", str(value if value is not None else ""))
    return tuple(int(part) for part in match.groups()) if match else None


def labelled_line(text, label, table=False):
    """True when some line opens with the label, allowing a list marker and emphasis.

    With table=True a table column headed by the label also counts.
    """
    name = r"Includes(?:[ \t]*/[ \t]*Excludes)?" if label == "Includes" else re.escape(label)
    if re.search(r"(?m)^[ \t]*(?:[-*][ \t]+)?\*{0,2}" + name + r"\*{0,2}[ \t]*:", text):
        return True
    return table and bool(re.search(r"(?m)^[ \t]*\|.*\|[ \t]*\*{0,2}" + name + r"\*{0,2}[ \t]*\|", text)
                          or re.search(r"(?m)^[ \t]*\|[ \t]*\*{0,2}" + name + r"\*{0,2}[ \t]*\|", text))


def is_selected(decision):
    """True when the Decision line reports a selection, in any of the corpus's phrasings."""
    text = decision.replace("*", "").strip().lower()
    if unspecified(text):
        return False
    return (bool(re.search(r"\bselect(?:s|ed)\b", text))
            and not re.match(r"(?:pending|recommended|none|inherited)\b", text)
            and not re.search(r"\bnot\b(?:[ \t]+\w+){0,2}[ \t]+select(?:s|ed)\b", text))


def grant_blocks(body):
    """Each grant card: a line opening 'Grant <id>:' up to the next grant or heading.

    Template placeholders such as 'Grant <id>:' are not grants and are skipped.
    """
    starts = list(re.finditer(
        r"(?m)^[ \t]*\*{0,2}Grant[ \t]+([A-Za-z0-9][\w.-]*)(?:[ \t]*\([^)\n]*\))?\*{0,2}[ \t]*:", body))
    blocks = []
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(body)
        heading = re.search(r"(?m)^#{1,6} ", body[match.end():end])
        if heading:
            end = match.end() + heading.start()
        block = body[match.start():end]
        # A card names its actor; a line such as 'Grant scope: ...' is prose, not a card.
        if labelled_line(block, "For"):
            blocks.append((match.group(1), block))
    return blocks


def field_warnings(record, body, version):
    """Report missing 0.6.0 fields. These never fail --check, and older records get none."""
    if version is None or version < FIELD_CHECKS_FROM:
        return []
    messages = []
    if is_selected(record["decision"]):
        if not labelled_line(body, "Decided by", table=True):
            messages.append("a selected decision names no Decided by line")
        if not labelled_line(body, "Reconsider if", table=True):
            messages.append("a selected decision carries no Reconsider if line")
    for identifier, block in grant_blocks(body):
        missing = [label for label in GRANT_FIELDS if not labelled_line(block, label)]
        if missing:
            messages.append(f"grant {identifier} lacks: " + ", ".join(missing))
    if record["kind"] == "plan" and record.get("units"):
        for column in ("serves", "accepted by"):
            if column not in record["units"][0]:
                messages.append(f"the Units table has no {column.capitalize()} column")
    tables = (("Review", "criterion"),) if record["kind"] == "plan" else (("Act", "result"), ("Review", "criterion"))
    for heading, key in tables:
        rows = table_rows(body, heading, (key,))
        if rows and "serves" not in rows[0]:
            messages.append(f"the {heading} table has no Serves column")
    return messages


def unit_commits(root, identifier):
    """List the commits whose Perspicuity-Record trailer names this record, newest first.

    Read-only. Returns None when git cannot answer for this root.
    """
    pattern = "^Perspicuity-Record: " + identifier.replace(".", r"\.") + "$"
    try:
        completed = subprocess.run(
            ["git", "-C", str(root), "log", "-E", "--grep", pattern,
             "--format=%h%x09%aI%x09%(trailers:key=Perspicuity-Unit,valueonly,separator=%x2C)%x09%s"],
            capture_output=True, text=True, timeout=30, check=False)
    except (OSError, subprocess.SubprocessError):
        return None
    if completed.returncode != 0:
        return None
    commits = []
    for line in completed.stdout.splitlines():
        parts = line.split("\t", 3)
        if len(parts) == 4:
            commits.append({"commit": parts[0], "at": parts[1], "unit": parts[2].strip() or None,
                            "subject": parts[3]})
    return commits


def table_rows(body, heading, columns):
    """Read one Markdown table under a heading, returning a dict per row.

    Rows under the plan format only. A missing heading, a missing column or a
    placeholder cell yields nothing rather than a guess.
    """
    match = re.search(r"(?m)^##[ \t]+" + re.escape(heading) + r"[ \t]*$", body)
    if not match:
        return []
    section = re.split(r"(?m)^## ", body[match.end():], maxsplit=1)[0]
    header = None
    rows = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            if header is not None and rows:
                break
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if header is None:
            header = [cell.lower() for cell in cells]
            continue
        if all(set(cell) <= set("-: ") for cell in cells):
            continue
        if len(cells) != len(header):
            continue
        row = dict(zip(header, cells))
        if any(not plain_placeholder(row.get(name, "")) for name in columns):
            rows.append(row)
    return rows


def plain_placeholder(value):
    """True when a cell is empty or still holds a template placeholder."""
    text = (value or "").strip()
    return text in ("", "-") or (text.startswith("<") and text.endswith(">"))


def unit_rows(body):
    return table_rows(body, "Units", ("unit",))


def repository_rows(body):
    return table_rows(body, "Repositories", ("alias", "repository"))


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
    declared = None if header is None else current_format(header)
    if not declared:
        return None
    is_plan = declared == PLAN_FORMAT
    closed_header = body is not None
    body = body or ""
    record = {
        "path": path, "id": None, "revision": None, "updated": "unknown",
        "format": declared, "kind": "plan" if is_plan else "record",
        "record_status": "unclassified", "work_status": "unclassified",
        "plan_status": None,
        "principal": body_field(body, "Principal and decider"),
        "work_scope": body_field(body, "Plan scope" if is_plan else "Work scope"),
        "work_owner": body_field(body, "Plan owner" if is_plan else "Work owner"),
        "decision": body_field(body, "Decision"),
        "mode": read_mode(body),
        "done_when": body_field(body, "Done when"),
        "ship_to": body_field(body, "Ship to"),
        "ships_as": body_field(body, "Ships as"),
        "work": body_field(body, "Work"),
        "outcome": body_field(body, "Outcome"),
        "dependency": body_field(body, "Dependency"),
        "waiting_on": body_field(body, "Waiting on"),
        "review_due": body_field(body, "Review due"),
        "next_check": body_field(body, "Next check"),
        "next_check_date": None,
        "review_due_date": None,
        "next": body_field(body, "Next"), "issues": [],
        "skill_version": None, "field_warnings": [], "closure_warnings": [],
    }
    if is_plan:
        # A plan declares its repositories and its units; the units keep their own state.
        record["units"] = unit_rows(body)
        record["repositories"] = repository_rows(body)
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
    record["skill_version"] = None if data.get("skill_version") is None else str(data["skill_version"])
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
    for field, allowed in (("record_status", RECORD_STATES), ("work_status", WORK_STATES),
                           ("plan_status", WORK_STATES)):
        if field not in data:
            continue
        value = data[field]
        if not isinstance(value, str) or value not in allowed:
            record["issues"].append(f"invalid {field}: {value!r}")
        else:
            record[field] = value
    if is_plan:
        # A plan carries plan_status in place of work_status; the queue reads one field.
        if record["plan_status"] is not None:
            record["work_status"] = record["plan_status"]
        # A closed plan declares record_status: closed. Otherwise a plan carrying a
        # decision is open, because the plan owns the commitment rather than a record.
        if record["record_status"] == "unclassified" and not unspecified(record["decision"]):
            record["record_status"] = "open"
    classified = record["record_status"] != "unclassified" or record["work_status"] != "unclassified"
    if classified and unspecified(record["work_scope"]):
        record["issues"].append(
            "classified plans require a named Plan scope in Current position" if is_plan
            else "classified records require a named Work scope in Current position")
    if record["record_status"] == "open" and unspecified(record["next"]):
        record["issues"].append(
            "open plans require a Next action and actor in Current position" if is_plan
            else "open records require a Next action and actor in Current position")
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
    if is_plan:
        # The section must exist; its rows may still be template placeholders, which
        # are not units yet and are dropped when the table is read.
        if not re.search(r"(?m)^##[ \t]+Units[ \t]*$", body):
            record["issues"].append("a plan requires a Units section")
        # A unit's repository cell may name several aliases; local is the plan's own repository.
        named = set()
        for row in record["units"]:
            for value in re.split(r"[,;/]", row.get("repository", "")):
                value = value.strip().strip("`")
                if value and value.lower() not in ("local", "-", "—"):
                    named.add(value)
        aliases = {row.get("alias", "").strip().strip("`") for row in record["repositories"]}
        unknown = sorted(named - aliases)
        if unknown:
            record["issues"].append(
                "units name repositories the plan does not declare: " + ", ".join(unknown))
    record["field_warnings"] = field_warnings(record, body, skill_version_tuple(record["skill_version"]))
    record["closure_warnings"] = closure_warnings(record, skill_version_tuple(record["skill_version"]))
    return record


def is_placeholder(value):
    """A template placeholder such as '<the finished product>', which unspecified() also accepts."""
    return bool(re.fullmatch(r"<.*>[.]?", value.strip()))


def closure_warnings(record, version):
    """Report what stops a record or plan from finishing. These never fail --check.

    A plan from 0.7.0, or any plan in Run, must name its finished product in Ships as and cite it
    in Done when. An open record whose Next reads none has finished its work but not closed.
    """
    messages = []
    if record["record_status"] != "open":
        return messages
    is_plan = record["kind"] == "plan"
    if is_plan and ((version is not None and version >= LOOP_CHECKS_FROM) or record["mode"] == "run"):
        ships_as, done_when = record["ships_as"], record["done_when"]
        if unspecified(ships_as) and not is_placeholder(ships_as):
            messages.append("the plan names no Ships as, so a loop cannot tell when it is finished"
                            if record["mode"] == "run" else "the plan names no Ships as")
        elif done_when == "unknown":
            messages.append("the plan names Ships as but has no Done when that cites it")
        elif not unspecified(done_when) and "ships as" not in done_when.lower():
            messages.append("the plan's Done when does not cite Ships as")
    following = record["next"].replace("*", "").strip()
    if NOTHING_NEXT.match(following) and not unspecified(following):
        messages.append("Next reads none while the " + ("plan" if is_plan else "record")
                        + " is open: close it, or name the next actor")
    return messages


def destination_keys(ship_to):
    """The destinations a Ship to line names: its addresses, else its whole normalised text."""
    urls = {url.rstrip(".,;:").rstrip("/").lower() for url in URL.findall(ship_to)}
    if urls:
        return urls
    text = " ".join(ship_to.replace("*", "").lower().split()).rstrip(".")
    return set() if unspecified(text) or is_placeholder(text) else {text}


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
        "exclusions": [], "records": [], "issues": [], "warnings": [], "field_warnings": [],
        "closure_warnings": [],
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
    # One destination has one active plan.
    holders = defaultdict(list)
    for record in result["records"]:
        if (record["kind"] == "plan" and record["record_status"] == "open"
                and record["work_status"] not in {"accepted", "stopped"}):
            for key in destination_keys(record["ship_to"]):
                holders[key].append(record)
    for key, records in sorted(holders.items()):
        if len(records) > 1:
            for record in records:
                others = ", ".join(other["path"] for other in records if other is not record)
                message = f"another open plan ships to {key}: {others}"
                if message not in record["closure_warnings"]:
                    record["closure_warnings"].append(message)
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
        for message in record["field_warnings"]:
            result["field_warnings"].append({"path": record["path"], "message": message})
        for message in record["closure_warnings"]:
            result["closure_warnings"].append({"path": record["path"], "message": message})
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
    if result.get("field_warnings"):
        lines.extend(["", "## Field warnings", "",
                      "Fields skill 0.6.0 asks for are missing. These warnings never fail --check."])
        lines.extend(f"- {item['path']}: {item['message']}" for item in result["field_warnings"])
    if result.get("closure_warnings"):
        lines.extend(["", "## Closure warnings", "",
                      "A loop cannot finish these as written. These warnings never fail --check."])
        lines.extend(f"- {item['path']}: {item['message']}" for item in result["closure_warnings"])
    if any("commits" in record for record in result["records"]):
        lines.extend(["", "## Commits by unit", "",
                      "Read from Perspicuity-Record and Perspicuity-Unit commit trailers."])
        for record in result["records"]:
            if "commits" not in record:
                continue
            if record["commits"] is None:
                lines.extend(["", "### " + cell(record["path"]), "", "Git could not be read for this root."])
            elif record["commits"]:
                lines.extend(["", "### " + cell(record["path"]), "",
                              "| Unit | Commit | At | Subject |", "|---|---|---|---|"])
                lines.extend("| " + " | ".join(cell(item[key]) for key in ("unit", "commit", "at", "subject")) + " |"
                             for item in record["commits"])
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
    parser.add_argument("--commits", action="store_true",
                        help="List each record's commits by their Perspicuity-Unit trailer")
    args = parser.parse_args(argv)
    try:
        result = scan(args.root, args.source, as_of=args.due)
    except ValueError as error:
        parser.error(str(error))
    output = filtered(result, args.record_status, args.work_status, due=args.due is not None,
                      queue_state=args.queue_state)
    if args.commits:
        for record in output["records"]:
            if record["id"]:
                record["commits"] = unit_commits(result["root"], record["id"])
    print(json.dumps(output, indent=2) if args.json else markdown(output))
    return 1 if args.check and result["issues"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
