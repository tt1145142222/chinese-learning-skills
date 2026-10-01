#!/usr/bin/env python3
"""Render a PDF to PNG pages and create a contact sheet for visual QA."""

from __future__ import annotations

import argparse
import math
import os
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw


def find_pdftoppm() -> str | None:
    candidates: list[Path] = []
    home = Path.home()
    candidates.append(
        home
        / ".cache"
        / "codex-runtimes"
        / "codex-primary-runtime"
        / "dependencies"
        / "native"
        / "poppler"
        / "Library"
        / "bin"
        / "pdftoppm.exe"
    )

    found = shutil.which("pdftoppm")
    if found:
        candidates.append(Path(found))

    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return None


def page_number(path: Path) -> int:
    tail = path.stem.split("-")[-1]
    try:
        return int(tail)
    except ValueError:
        return 0


def render_pages(pdf: Path, output_dir: Path, dpi: int) -> list[Path]:
    pdftoppm = find_pdftoppm()
    if not pdftoppm:
        raise RuntimeError("pdftoppm was not found. Install Poppler or use the Codex bundled runtime.")

    pages_dir = output_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)
    prefix = pages_dir / "page"

    env = os.environ.copy()
    poppler_bin = str(Path(pdftoppm).parent)
    env["PATH"] = poppler_bin + os.pathsep + env.get("PATH", "")

    subprocess.run(
        [pdftoppm, "-r", str(dpi), "-png", str(pdf), str(prefix)],
        check=True,
        env=env,
    )

    pages = sorted(pages_dir.glob("page-*.png"), key=page_number)
    if not pages:
        raise RuntimeError("pdftoppm completed but no rendered pages were produced.")
    return pages


def make_contact_sheet(pages: list[Path], output_path: Path, thumb_width: int, cols: int) -> None:
    thumbs: list[tuple[str, Image.Image]] = []
    for page in pages:
        image = Image.open(page).convert("RGB")
        thumb_height = int(image.height * thumb_width / image.width)
        thumbs.append((page.name, image.resize((thumb_width, thumb_height), Image.Resampling.LANCZOS)))

    gap = 26
    label_h = 26
    rows = math.ceil(len(thumbs) / cols)
    width = cols * thumb_width + (cols + 1) * gap
    height = gap
    for row in range(rows):
        start = row * cols
        end = min(start + cols, len(thumbs))
        height += max(thumbs[i][1].height for i in range(start, end)) + label_h + gap

    sheet = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(sheet)
    y = gap
    for row in range(rows):
        x = gap
        max_h = 0
        for col in range(cols):
            idx = row * cols + col
            if idx >= len(thumbs):
                break
            name, thumb = thumbs[idx]
            draw.text((x, y), name, fill=(0, 0, 0))
            sheet.paste(thumb, (x, y + label_h))
            draw.rectangle([x, y + label_h, x + thumb.width, y + label_h + thumb.height], outline=(210, 210, 210))
            max_h = max(max_h, thumb.height)
            x += thumb_width + gap
        y += max_h + label_h + gap

    output_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render PDF pages and create a contact sheet for visual QA.")
    parser.add_argument("pdf", type=Path, help="Path to final PDF")
    parser.add_argument("--output-dir", type=Path, required=True, help="Directory for rendered pages and contact sheet")
    parser.add_argument("--dpi", type=int, default=150, help="Render DPI")
    parser.add_argument("--thumb-width", type=int, default=380, help="Contact sheet thumbnail width in pixels")
    parser.add_argument("--cols", type=int, default=2, help="Number of columns in contact sheet")
    args = parser.parse_args()

    if not args.pdf.exists():
        print(f"ERROR: PDF not found: {args.pdf}", file=sys.stderr)
        return 2

    args.output_dir.mkdir(parents=True, exist_ok=True)
    pages = render_pages(args.pdf, args.output_dir, args.dpi)
    contact_sheet = args.output_dir / "contact_sheet.png"
    make_contact_sheet(pages, contact_sheet, args.thumb_width, args.cols)

    print(f"Rendered pages: {len(pages)}")
    print(f"Contact sheet: {contact_sheet.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
