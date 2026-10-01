#!/usr/bin/env python3
"""Structural QA for 毛概/毛中特 review DOCX pairs."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def extract_docx_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    if not zipfile.is_zipfile(path):
        raise ValueError(f"not a valid zip/docx file: {path}")

    chunks: list[str] = []
    with zipfile.ZipFile(path) as zf:
        names = [
            name
            for name in zf.namelist()
            if name.startswith("word/")
            and name.endswith(".xml")
            and (
                name == "word/document.xml"
                or name.startswith("word/header")
                or name.startswith("word/footer")
            )
        ]
        for name in sorted(names):
            root = ET.fromstring(zf.read(name))
            for node in root.findall(".//w:t", NS):
                if node.text:
                    chunks.append(node.text)
            chunks.append("\n")
    return "".join(chunks)


def count(pattern: str, text: str) -> int:
    return len(re.findall(pattern, text))


def fail(msg: str, failures: list[str]) -> None:
    failures.append(msg)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser()
    parser.add_argument("--practice", required=True, help="题目练习版 DOCX")
    parser.add_argument("--answers", required=True, help="答案解析版 DOCX")
    parser.add_argument("--chapters", type=int, required=True, help="expected chapter count")
    parser.add_argument("--min-dist", type=int, default=2, help="min 辨析题 per chapter")
    parser.add_argument("--min-short", type=int, default=4, help="min 简答题 per chapter")
    parser.add_argument("--min-material", type=int, default=1, help="min 材料分析题 per chapter")
    args = parser.parse_args()

    practice = Path(args.practice).resolve()
    answers = Path(args.answers).resolve()
    p_text = extract_docx_text(practice)
    a_text = extract_docx_text(answers)

    expected_question_items = args.chapters * (args.min_dist + args.min_short + args.min_material)

    metrics = {
        "practice_chars": len(p_text),
        "answers_chars": len(a_text),
        "chapter_reviews": p_text.count("本章知识复习和重点回顾"),
        "dist_sections": count(r"一、辨析题", p_text),
        "short_sections": count(r"二、简答题", p_text),
        "material_sections": count(r"三、材料分析题", p_text),
        "practice_stars": p_text.count("★"),
        "answer_points": a_text.count("【考点定位】"),
        "answer_refs": a_text.count("【参考答案】"),
        "answer_analysis": a_text.count("【作答解析】"),
        "practice_blanks": p_text.count("作答区"),
    }

    failures: list[str] = []
    if metrics["chapter_reviews"] < args.chapters:
        fail("practice doc has too few chapter review sections", failures)
    if metrics["dist_sections"] < args.chapters:
        fail("practice doc has too few 辨析题 sections", failures)
    if metrics["short_sections"] < args.chapters:
        fail("practice doc has too few 简答题 sections", failures)
    if metrics["material_sections"] < args.chapters:
        fail("practice doc has too few 材料分析题 sections", failures)
    if metrics["practice_stars"] < expected_question_items:
        fail("practice doc has too few star markers", failures)
    if metrics["answer_points"] < expected_question_items:
        fail("answer doc has too few 考点定位 entries", failures)
    if metrics["answer_refs"] < expected_question_items:
        fail("answer doc has too few 参考答案 entries", failures)
    if metrics["answer_analysis"] < expected_question_items:
        fail("answer doc has too few 作答解析 entries", failures)

    forbidden = ["TODO", "??", "？？？", "[TODO"]
    for token in forbidden:
        if token in p_text or token in a_text:
            fail(f"found placeholder/suspicious token: {token}", failures)

    for key, value in metrics.items():
        print(f"{key}={value}")

    if failures:
        print("STRUCTURAL_QA_FAIL", file=sys.stderr)
        for item in failures:
            print(f"- {item}", file=sys.stderr)
        return 1

    print("STRUCTURAL_QA_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
