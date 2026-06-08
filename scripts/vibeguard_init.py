#!/usr/bin/env python3
"""Initialize VibeGuard brief files in a project.

This script creates a `.vibeguard/` folder by copying the public templates
from this repository. It does not inspect source code and does not contact any
network service.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


TEMPLATE_FILES = [
    "vision-lock.md",
    "context-budget.md",
    "acceptance-contract.md",
    "tasks.md",
    "current-task.md",
    "review.md",
    "handoff.md",
]


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Initialize VibeGuard files in a project.")
    parser.add_argument("--project", default=".", help="Project root directory. Defaults to current directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing .vibeguard files.")
    return parser.parse_args()


def main() -> int:
    """Create `.vibeguard/` files from templates."""
    args = parse_args()
    project = Path(args.project).expanduser().resolve()

    if not project.exists() or not project.is_dir():
        raise SystemExit(f"Project path is not a directory: {project}")
    if project == Path(project.anchor):
        raise SystemExit("Refusing to initialize .vibeguard at filesystem root.")

    repo_root = Path(__file__).resolve().parents[1]
    template_dir = repo_root / "templates"
    if not template_dir.exists():
        raise SystemExit(f"Template directory not found: {template_dir}")

    target_dir = project / ".vibeguard"
    target_dir.mkdir(exist_ok=True)

    created = []
    skipped = []
    overwritten = []

    for filename in TEMPLATE_FILES:
        source = template_dir / filename
        target = target_dir / filename
        if not source.exists():
            raise SystemExit(f"Missing template: {source}")
        if target.exists() and not args.force:
            skipped.append(filename)
            continue
        existed = target.exists()
        shutil.copyfile(source, target)
        if existed:
            overwritten.append(filename)
        else:
            created.append(filename)

    print(f"Initialized VibeGuard files at: {target_dir}")
    if created:
        print("Created:")
        for filename in created:
            print(f"- {filename}")
    if overwritten:
        print("Overwritten:")
        for filename in overwritten:
            print(f"- {filename}")
    if skipped:
        print("Skipped existing files; use --force to overwrite:")
        for filename in skipped:
            print(f"- {filename}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
