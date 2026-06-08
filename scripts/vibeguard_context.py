#!/usr/bin/env python3
"""Generate a short VibeGuard context pack for AI coding.

The generated pack is meant to be copied into an AI coding tool before
implementation. It prioritizes `.vibeguard/current-task.md` and includes small,
bounded snippets from the other brief files.
"""

from __future__ import annotations

import argparse
from pathlib import Path


OPTIONAL_FILES = [
    ("vision-lock.md", "Product intent"),
    ("acceptance-contract.md", "Acceptance"),
    ("context-budget.md", "Context budget"),
    ("tasks.md", "Tasks"),
]


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Generate a VibeGuard context pack.")
    parser.add_argument("--project", default=".", help="Project root directory. Defaults to current directory.")
    parser.add_argument("--snippet-chars", type=int, default=1200, help="Maximum characters from each optional file.")
    parser.add_argument("--include-review", action="store_true", help="Include review notes.")
    parser.add_argument("--include-handoff", action="store_true", help="Include handoff notes.")
    return parser.parse_args()


def read_required(path: Path) -> str:
    """Read a required text file."""
    if not path.exists():
        raise SystemExit(f"Missing required file: {path}")
    return path.read_text(encoding="utf-8").strip()


def read_optional(path: Path, limit: int) -> str:
    """Read an optional text file with a character limit."""
    if not path.exists():
        return ""
    content = path.read_text(encoding="utf-8").strip()
    if len(content) <= limit:
        return content
    return content[:limit].rstrip() + "\n\n[truncated]"


def make_section(title: str, body: str) -> str:
    """Create a markdown section if body is non-empty."""
    body = body.strip()
    if not body:
        return ""
    return f"## {title}\n\n{body}\n"


def main() -> int:
    """Print a context pack to stdout."""
    args = parse_args()
    project = Path(args.project).expanduser().resolve()
    brief_dir = project / ".vibeguard"

    if not brief_dir.exists() or not brief_dir.is_dir():
        raise SystemExit(f"Missing .vibeguard directory: {brief_dir}")

    snippet_chars = max(200, args.snippet_chars)
    current_task = read_required(brief_dir / "current-task.md")

    parts = [
        "# VibeGuard Context Pack",
        "",
        "Use this as the source of truth for the next AI coding step.",
        "Do not expand scope. Stop and ask if the task, files, or acceptance criteria are unclear.",
        "",
        make_section("Current task", current_task),
    ]

    for filename, title in OPTIONAL_FILES:
        parts.append(make_section(title, read_optional(brief_dir / filename, snippet_chars)))

    if args.include_review:
        parts.append(make_section("Review", read_optional(brief_dir / "review.md", snippet_chars)))
    if args.include_handoff:
        parts.append(make_section("Handoff", read_optional(brief_dir / "handoff.md", snippet_chars)))

    parts.append(
        "## Operating rules\n\n"
        "- Work on the current task only.\n"
        "- Stay within the allowed changes.\n"
        "- Preserve protected behavior.\n"
        "- Verify against the acceptance criteria.\n"
        "- Stop and ask before expanding scope.\n"
    )

    print("\n".join(part for part in parts if part).strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
