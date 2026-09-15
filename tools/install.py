#!/usr/bin/env python3
"""Copy the complete Perspicuity skill without replacing an existing installation."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skills-dir', type=Path, default=Path.home() / '.agents/skills')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    inventory = json.loads((root / 'COMPONENT-VERSIONS.json').read_text())
    skills = {name for name, item in inventory['components'].items() if item['kind'] == 'skill'}
    if inventory.get('layout') != 'standalone-perspicuity' or skills != {'skill:perspicuity'}:
        parser.exit(1, 'This installer requires the standalone Perspicuity package.\n')
    subprocess.run([sys.executable, str(root / 'tools/manifest.py'), 'verify'], check=True)
    source = root / 'skills/perspicuity'
    destination = args.skills_dir.expanduser().absolute() / 'perspicuity'
    if destination.exists() or destination.is_symlink():
        parser.exit(1, 'Existing installation; no files changed: ' + str(destination) + '\n')
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    print('Installed perspicuity at ' + str(destination) + '. Start a new agent session.')


if __name__ == '__main__':
    main()
