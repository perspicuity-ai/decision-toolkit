#!/usr/bin/env python3
"""Generate or verify the complete file inventory."""
import hashlib
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def inventory():
    rows = []
    for path in sorted(ROOT.rglob('*')):
        rel = path.relative_to(ROOT)
        if any(part in ('.git', '__pycache__', '.venv') for part in rel.parts):
            continue
        if str(rel) == 'MANIFEST.json' or not (path.is_file() or path.is_symlink()):
            continue
        if path.is_symlink():
            target = os.readlink(path)
            if not path.resolve(strict=True).is_relative_to(ROOT):
                raise ValueError(f'Link escapes package: {rel}')
            data = target.encode()
            row = dict(path=str(rel), type='symlink', target=target)
        else:
            data = path.read_bytes()
            row = dict(path=str(rel), type='file', executable=bool(path.stat().st_mode & 0o111))
        row.update(sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))
        rows.append(row)
    return rows

if __name__ == '__main__':
    rows = inventory()
    path = ROOT / 'MANIFEST.json'
    if sys.argv[1:] == ['write']:
        path.write_text(json.dumps(dict(version=(ROOT/'VERSION').read_text().strip(),
            hash_rule='SHA-256 of file bytes or UTF-8 symlink target; excludes this manifest and runtime metadata',
            files=rows), indent=2) + '\n')
    elif sys.argv[1:] == ['verify']:
        expected = json.loads(path.read_text())
        if expected['files'] != rows or expected['version'] != (ROOT/'VERSION').read_text().strip():
            raise SystemExit('FAIL: content differs from MANIFEST.json')
        print(f'PASS manifest: {len(rows)} files')
    else:
        raise SystemExit('Usage: manifest.py write|verify')
