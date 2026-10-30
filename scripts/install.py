#!/usr/bin/env python3
"""Install the complete local bundle into one project's .agents/skills directory."""
import argparse
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {'node_modules', 'dist', '__pycache__', '.git'}

def inventory(folder):
    return {p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in folder.rglob('*') if p.is_file()
            and not any(part in IGNORED for part in p.relative_to(folder).parts)}

def install(project):
    project = project.resolve(strict=True)
    if not project.is_dir():
        raise ValueError('Project must be an existing directory')
    sources = sorted(p for p in (ROOT / 'skills').iterdir() if (p / 'SKILL.md').is_file())
    target_root = project / '.agents' / 'skills'
    backup_root = project / '.agents' / 'skill-backups'
    # Preflight every destination before writing; do not follow links outside the project.
    for path in [target_root, backup_root, *(target_root / s.name for s in sources)]:
        if not path.resolve().is_relative_to(project):
            raise ValueError(f'Destination resolves outside the project: {path}')
        if path.is_symlink() or (hasattr(path, 'is_junction') and path.is_junction()):
            raise ValueError(f'Existing link requires explicit review: {path}')
    target_root.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    for source in sources:
        target = target_root / source.name
        if target.is_dir() and inventory(source) == inventory(target):
            print(f'UNCHANGED {source.name}')
            continue
        backup = backup_root / stamp / source.name
        with tempfile.TemporaryDirectory(prefix='.bundle-', dir=target_root) as temp:
            staged = Path(temp) / source.name
            shutil.copytree(source, staged, ignore=shutil.ignore_patterns(*IGNORED))
            moved = False
            try:
                if target.exists():
                    backup.parent.mkdir(parents=True, exist_ok=True)
                    target.rename(backup)
                    moved = True
                staged.rename(target)
            except Exception:
                if moved and not target.exists():
                    backup.rename(target)
                raise
        print(f'INSTALLED {source.name}' + (f' (backup: {backup})' if moved else ''))
    print(f'Installed/verified {len(sources)} skills in {target_root}')
    print('Graphify and Understand Anything prepare extra runtime dependencies on first use.')
    return len(sources)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, default=Path.cwd(), help='Existing project directory (default: current directory)')
    args = parser.parse_args()
    try:
        install(args.project)
    except (OSError, ValueError) as exc:
        print(f'Installation failed: {exc}', file=sys.stderr)
        sys.exit(1)
