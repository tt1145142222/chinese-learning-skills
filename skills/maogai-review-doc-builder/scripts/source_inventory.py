#!/usr/bin/env python3
"""List likely source files for a 毛概/毛中特 review-doc build."""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path


DEFAULT_EXTS = {
    ".docx",
    ".doc",
    ".pdf",
    ".txt",
    ".md",
    ".rtf",
}

DEFAULT_SKIP_DIRS = {
    ".git",
    ".svn",
    ".hg",
    "node_modules",
    "__pycache__",
    "work",
    "成品",
    "dist",
    "build",
}


def iter_sources(root: Path, exts: set[str], skip_dirs: set[str]):
    for path in root.rglob("*"):
        if path.is_dir():
            continue
        parts = set(path.relative_to(root).parts[:-1])
        if parts & skip_dirs:
            continue
        if path.suffix.lower() in exts:
            yield path


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="workspace/source root")
    parser.add_argument(
        "--ext",
        action="append",
        default=[],
        help="extra extension to include, e.g. --ext .wps",
    )
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    exts = set(DEFAULT_EXTS) | {e.lower() if e.startswith(".") else f".{e.lower()}" for e in args.ext}
    files = sorted(iter_sources(root, exts, DEFAULT_SKIP_DIRS), key=lambda p: str(p).lower())

    by_ext: dict[str, list[Path]] = defaultdict(list)
    for file in files:
        by_ext[file.suffix.lower()].append(file)

    print(f"root={root}")
    print(f"total={len(files)}")
    for ext in sorted(by_ext):
        print(f"{ext or '<none>'}={len(by_ext[ext])}")

    print()
    for file in files:
        print(file)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
