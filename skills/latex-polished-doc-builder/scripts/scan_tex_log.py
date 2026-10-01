#!/usr/bin/env python3
"""Scan a LaTeX log for issues that usually require fixing before delivery."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SEVERE_PATTERNS = {
    "latex_error": re.compile(r"^! (LaTeX|Package|Class|pdfTeX|XeTeX|LuaTeX) Error:|^! Emergency stop|^! Fatal error", re.M),
    "missing_character": re.compile(r"Missing character:", re.I),
    "overfull": re.compile(r"Overfull \\[hv]box", re.I),
    "undefined_refs": re.compile(r"undefined references|Reference .* undefined|Citation .* undefined", re.I),
}

NOTICE_PATTERNS = {
    "underfull": re.compile(r"Underfull \\[hv]box", re.I),
    "warnings": re.compile(r"Warning:", re.I),
}


def collect_matches(text: str, patterns: dict[str, re.Pattern[str]]) -> dict[str, list[str]]:
    lines = text.splitlines()
    results: dict[str, list[str]] = {}
    for name, pattern in patterns.items():
        hits: list[str] = []
        for idx, line in enumerate(lines, start=1):
            if pattern.search(line):
                hits.append(f"{idx}: {line.strip()}")
        results[name] = hits
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan a LaTeX log for delivery-blocking issues.")
    parser.add_argument("log", type=Path, help="Path to .log file")
    parser.add_argument("--max-lines", type=int, default=12, help="Maximum lines to print per issue category")
    args = parser.parse_args()

    if not args.log.exists():
        print(f"ERROR: log file not found: {args.log}", file=sys.stderr)
        return 2

    text = args.log.read_text(errors="replace")
    severe = collect_matches(text, SEVERE_PATTERNS)
    notices = collect_matches(text, NOTICE_PATTERNS)

    severe_count = sum(len(v) for v in severe.values())
    notice_count = sum(len(v) for v in notices.values())

    if severe_count == 0:
        print("No severe LaTeX log issues found.")
    else:
        print(f"Severe LaTeX log issues found: {severe_count}")
        for name, hits in severe.items():
            if not hits:
                continue
            print(f"\n[{name}]")
            for hit in hits[: args.max_lines]:
                print(hit)
            if len(hits) > args.max_lines:
                print(f"... {len(hits) - args.max_lines} more")

    if notice_count:
        print(f"\nNotices found: {notice_count}")
        for name, hits in notices.items():
            if not hits:
                continue
            print(f"\n[{name}]")
            limit = min(args.max_lines, 6)
            for hit in hits[:limit]:
                print(hit)
            if len(hits) > limit:
                print(f"... {len(hits) - limit} more")

    return 1 if severe_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
