"""Derive dashboard data from the maintained current-work reader."""

from datetime import datetime, timezone
from pathlib import Path
import re
from urllib.parse import quote, unquote, urlsplit


from . import work as _reader

# Current records use inline Markdown links. Reference definitions and bare paths
# do not create graph edges. A single parenthesis pair is supported in paths.
INLINE_LINK = re.compile(
    r"(?<!!)\[([^\]\n]+)\]\(\s*"
    r"(<[^>\n]+>|(?:\\.|[^\\\s()]|\((?:\\.|[^\\()])*\))+)"
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
DATE_SUFFIX = re.compile(r"-\d{4}-\d{2}-\d{2}$")


def prose(text):
    """Ignore fenced examples and inline code when discovering source links."""
    lines = []
    fence = None
    for line in text.splitlines():
        match = FENCE.match(line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            lines.append("")
        elif fence is None:
            lines.append(re.sub(r"(`+).*?\1", "", line))
        else:
            lines.append("")
    return "\n".join(lines)


def title_for(body, fallback):
    for line in prose(body).splitlines():
        if re.match(r"^#\s+", line):
            return re.sub(r"\s+#+\s*$", "", line[2:].strip()) or fallback
    return fallback


def area_for(path):
    parts = Path(path).parts
    if len(parts) >= 3 and parts[:2] == ("docs", "initiatives"):
        return DATE_SUFFIX.sub("", parts[2]).replace("-", " ").capitalize()
    if parts[:2] == ("docs", "outreach"):
        return "Outreach"
    return "Decisions" if parts[0] == "Decisions" else parts[0]


def resolve_link(root, source, destination):
    """Return a contained, non-symlink local Markdown path and its fragment."""
    destination = destination.strip("<>")
    destination = re.sub(r"\\([\\`*_{}\[\]()#+.!<>-])", r"\1", destination)
    try:
        url = urlsplit(destination)
        path = unquote(url.path)
    except (ValueError, UnicodeError):
        return None
    if url.scheme or url.netloc or not path or path.startswith("/") or "\\" in path or "\x00" in path:
        return None
    # Reject symlinks before normalizing .. components, including paths that
    # leave through a symlink and then appear to return to the repository.
    candidate = root / Path(source).parent / path
    cursor = root
    for part in candidate.relative_to(root).parts:
        if part == "..":
            cursor = cursor.parent
        elif part != ".":
            cursor = cursor / part
        try:
            cursor.relative_to(root)
        except ValueError:
            return None
        if cursor.is_symlink():
            return None
    try:
        relative = candidate.resolve().relative_to(root)
    except (OSError, RuntimeError, ValueError):
        return None
    if relative.suffix.lower() != ".md":
        return None
    return relative.as_posix(), unquote(url.fragment)


def links_in(text, root, source):
    for match in INLINE_LINK.finditer(prose(text)):
        resolved = resolve_link(root, source, match.group(2))
        if resolved is not None:
            target, fragment = resolved
            yield {"target": target, "label": match.group(1), "fragment": fragment}


def read_records(root: Path, sources=None):
    """Read current records without writing an index or interpreting authority."""
    root = Path(root).expanduser().absolute()
    result = _reader.scan(root, sources)
    records = result["records"]
    keys = {record["path"] for record in records}
    edges = {}
    for record in records:
        path = record["path"]
        record.update({
            "key": path,
            "title": record["id"] or Path(path).stem,
            "area": area_for(path),
            "modified_at": None,
            "source_url": "/source?path=" + quote(path, safe=""),
        })
        try:
            source = root / path
            text = source.read_text(encoding="utf-8")
            record["modified_at"] = datetime.fromtimestamp(
                source.stat().st_mtime, timezone.utc
            ).isoformat()
        except (OSError, UnicodeError) as error:
            message = f"Source changed or became unreadable during dashboard read: {error}"
            result["warnings"].append({"path": path, "message": message})
            continue
        _, body = _reader.frontmatter(text)
        body = body or ""
        record["title"] = title_for(body, record["title"])
        dependency_targets = {
            link["target"] for link in links_in(record["dependency"], root, path)
        }
        for link in links_in(body, root, path):
            target = link["target"]
            if target not in keys or target == path:
                continue
            key = (path, target)
            if key not in edges:
                edges[key] = {
                    "source": path,
                    "target": target,
                    "kind": "dependency" if target in dependency_targets else "reference",
                    "label": link["label"],
                    "fragments": [],
                }
            if link["fragment"] and link["fragment"] not in edges[key]["fragments"]:
                edges[key]["fragments"].append(link["fragment"])
    result["edges"] = list(edges.values())
    return result


def read_record(root, requested, sources=None):
    """Return the complete source and front matter without imposing body fields."""
    root = Path(root).resolve()
    records = read_records(root, sources)["records"]
    source = root / requested
    if (requested not in {record["path"] for record in records}
            or source.resolve() != source.absolute() or not source.is_file()):
        raise ValueError("This source is outside the project's current records.")
    text = source.read_text(encoding="utf-8")
    header, body = _reader.frontmatter(text)
    issues = []
    try:
        if header is None:
            raise ValueError("The record changed during this read.")
        metadata = _reader.yaml.load(header, Loader=_reader.UniqueLoader)
        if not isinstance(metadata, dict):
            metadata = {}
    except (_reader.yaml.YAMLError, ValueError, TypeError) as error:
        metadata = {}
        issues.append("Front matter could not be parsed. Inspect the Markdown source.")

    def json_value(value, ancestors=()):
        if isinstance(value, (dict, list)):
            if id(value) in ancestors or len(ancestors) > 20:
                return "[recursive or deeply nested value]"
            parents = (*ancestors, id(value))
            if isinstance(value, dict):
                return {str(k): json_value(v, parents) for k, v in value.items()}
            return [json_value(v, parents) for v in value]
        if value is None or isinstance(value, (str, bool, int)):
            return value
        # Dates, non-finite floats and other YAML values retain readable forms.
        if isinstance(value, float):
            import math
            if math.isfinite(value):
                return value
        return str(value)

    return {"path": requested, "metadata": json_value(metadata),
            "body": body if header is not None and body is not None else text, "source": text, "issues": issues}
