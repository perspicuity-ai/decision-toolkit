#!/usr/bin/env python3
"""Check that each record's Current position fits the five-minute brief.

The brief is the Current position section of a perspicuity-work/1 record or a
perspicuity-plan/1 plan. From skill 0.8.0 it carries the required slots, keeps
each line to 280 rendered characters, keeps the section to 600 words, and
glosses each identifier (O1, U4, D11) where it first appears.
Exit 0 when every checked record passes, 1 when any fails, 2 on a usage error.
"""

import argparse
from pathlib import Path
import re
import sys


FORMATS = ("perspicuity-work/1", "perspicuity-plan/1")
CHECKS_FROM = (0, 8, 0)
LINE_LIMIT = 280
WORD_LIMIT = 600
REQUIRED = ("Ask", "Objectives", "Decision", "Needs from you", "Next")

FRONT_MATTER = re.compile(r"\A---[ \t]*\n(.*?)\n---[ \t]*(?:\n|\Z)", re.S)
HEADER_VALUE = r"(?m)^{}:[ \t]*['\"]?([^'\"\n#]+?)['\"]?[ \t]*(?:#.*)?$"
SECTION = re.compile(r"(?m)^## Current position[ \t]*$")
NEXT_SECTION = re.compile(r"(?m)^## ")
COMMENT = re.compile(r"<!--.*?-->", re.S)
IMAGE_OR_LINK = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
REFERENCE_LINK = re.compile(r"\[([^\]]+)\]\[[^\]]*\]")
AUTOLINK = re.compile(r"<(https?://[^>]+)>")
EMPHASIS = re.compile(r"[*_`]+")
SLOT = r"(?m)^[ \t]*(?:[-*+][ \t]+)?[*_]{{0,2}}{}[*_]{{0,2}}:"
IDENTIFIER = re.compile(r"\b[A-Z]{1,2}\d{1,2}\b")
# Text that shows an identifier was used without saying what it names.
BARE_AFTER = re.compile(
    r"[ \t]*(?:$|[,.;:\]·/–-]|(?:and|or|to|through|then|is|are|was|were|in|on|at|for|by|of|from|with)\b"
    r"|[A-Z]{1,2}\d{1,2}\b)")


def header(text, name):
    match = FRONT_MATTER.match(text)
    if not match:
        return None
    value = re.search(HEADER_VALUE.format(re.escape(name)), match.group(1))
    return value.group(1).strip() if value else None


def version(value):
    parts = re.findall(r"\d+", value or "")
    return tuple(int(part) for part in parts[:3]) if parts else None


def rendered(line):
    """Return the line as a reader sees it: link text without its address, no markup."""
    line = IMAGE_OR_LINK.sub(r"\1", line)
    line = REFERENCE_LINK.sub(r"\1", line)
    line = AUTOLINK.sub(r"\1", line)
    return EMPHASIS.sub("", line).strip()


def current_position(text):
    """Return (first line number, body) of the section, with comments blanked in place."""
    match = SECTION.search(text)
    if not match:
        return None, None
    body = text[match.end():]
    end = NEXT_SECTION.search(body)
    body = body[:end.start()] if end else body
    body = COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), body)
    return text[:match.end()].count("\n") + 1, body


def bare_identifiers(section):
    """Return identifiers whose first use in the section carries no gloss."""
    text = "\n".join(rendered(line) for line in section.split("\n"))
    seen, bare = set(), []
    for match in IDENTIFIER.finditer(text):
        name = match.group(0)
        if name in seen:
            continue
        seen.add(name)
        after = text[match.end():match.end() + 24]
        if after.startswith(")") and text[:match.start()].endswith("("):
            continue
        if after.startswith(")") or BARE_AFTER.match(after):
            bare.append(name)
    return bare


def check_text(text, any_version=False):
    """Return (checked, problems) for one file's text."""
    if header(text, "format") not in FORMATS:
        return False, []
    skill = version(header(text, "skill_version"))
    if not any_version and (skill is None or skill < CHECKS_FROM):
        return False, []
    first, section = current_position(text)
    if section is None:
        return True, ["no Current position section"]
    problems = []
    for slot in REQUIRED:
        if not re.search(SLOT.format(re.escape(slot)), section):
            problems.append(f"missing slot: {slot}")
    for offset, line in enumerate(section.split("\n")):
        shown = rendered(line)
        if len(shown) > LINE_LIMIT:
            problems.append(f"line {first + offset}: {len(shown)} characters (limit {LINE_LIMIT}): {shown[:60]}…")
    bare = bare_identifiers(section)
    if bare:
        problems.append("identifiers without a gloss at first use: " + ", ".join(bare))
    words = len(rendered(section).split())
    if words > WORD_LIMIT:
        problems.append(f"section: {words} words (limit {WORD_LIMIT})")
    return True, problems


def files(paths):
    for path in paths:
        if path.is_dir():
            yield from sorted(p for p in path.rglob("*.md") if p.is_file())
        else:
            yield path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="+", type=Path, help="records, plans or directories")
    parser.add_argument("--any-version", action="store_true",
                        help="also check records written before skill 0.8.0")
    args = parser.parse_args(argv)
    missing = [str(path) for path in args.paths if not path.exists()]
    if missing:
        print("not found: " + ", ".join(missing), file=sys.stderr)
        return 2
    checked = failed = 0
    for path in files(args.paths):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            print(f"{path}: unreadable: {error}", file=sys.stderr)
            failed += 1
            continue
        was_checked, problems = check_text(text, args.any_version)
        checked += was_checked
        if problems:
            failed += 1
            print(f"{path}")
            for problem in problems:
                print(f"  {problem}")
    print(f"{checked} checked, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
