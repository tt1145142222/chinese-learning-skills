---
name: maogai-review-doc-builder
description: Build polished 毛概/毛中特 exam-review Word documents from a folder of course materials. Use when the user asks to generate, revise, or standardize a chapter-based 大题复习 document set with a separate 题目练习版 and 答案解析版, especially when sources include DOCX, DOC, PDF, existing 学案, 简答题 collections, chapter exercises, or exam banks.
---

# Maogai Review Doc Builder

## Purpose

Create a high-coverage but compact 毛概/毛中特大题复习 package from the user's local materials:

- one Word document for questions/practice;
- one Word document for answers, tested knowledge points, and explanations.

The output should look like an exam-oriented study guide, not a raw source merge.

## Required companion skills

When generating or editing `.docx`, also use the `documents:documents` skill. If PDFs are part of the source set, also use the `pdf:pdf` skill for extraction/inspection guidance.

If DOCX visual rendering is unavailable in the environment, do structural QA and explicitly disclose that visual render verification could not be completed.

## Workflow

### 1. Audit the source folder first

List all relevant files recursively before writing content. Use `rg --files` where available, or run:

```powershell
python scripts/source_inventory.py <workspace>
```

Include likely source formats: `.docx`, `.doc`, `.pdf`, `.txt`, `.md`, and any existing student/answer versions. Exclude generated output directories such as `work`, `成品`, `.git`, and `node_modules` unless the user explicitly points to them.

Read or extract every relevant source. Existing generated 学案/答案 files are style and structure references; chapter exercises, exam banks, notes, and 简答题 collections are content references. Do not claim all materials were reviewed unless every readable source was covered. If a legacy `.doc` or malformed file cannot be extracted, report it and use the best available fallback.

### 2. Build the content blueprint

Read `references/output-contract.md` before drafting. Unless the user overrides it, follow this default structure:

- include 导论 and every course chapter represented by the materials;
- before each chapter's questions, write a concise “本章知识复习和重点回顾”;
- include 辨析题、简答题、材料分析题 in every chapter;
- use star levels: `★★★` frequent/high-value exam重点, `★★` secondary重点, `★` lower-priority补充;
- keep each chapter compact, but not below the exam's question-type baseline.

Question selection should be evidence-based:

1. Prefer knowledge points appearing across multiple sources or in existing exam-bank style materials.
2. Preserve high-frequency textbook/teacher-note formulations where they are concise and correct.
3. Avoid duplicate questions that test the same sentence-level answer unless one is materially more exam-like.
4. Balance conceptual theory, historical logic, and contemporary application.

### 3. Draft the two-document set

Default output names:

- `毛概大题复习终极文档（题目练习版）.docx`
- `毛概大题复习终极文档（答案解析版）.docx`

Default output directory: `成品` under the current workspace.

The 题目练习版 must include:

- cover/title;
- opening usage instructions and a clear review schedule table;
- per-chapter concise key review;
- questions grouped by type;
- answer spaces sized to the expected response length.

The 答案解析版 must include:

- the full question text;
- `【考点定位】`;
- `【参考答案】`;
- `【作答解析】` or equivalent scoring/explanation guidance.

The answer document must not be answer-only.

### 4. Formatting standards

Use professional Word formatting:

- Chinese-friendly fonts such as Microsoft YaHei, SimSun, or DengXian;
- clear heading hierarchy;
- stable margins and table widths;
- moderate use of color for navigation, not decoration;
- no oversized characters, awkward spacing, or disproportionate tables;
- no obvious typos, placeholder text, or broken numbering.

For answer blanks, use consistent ruled lines or spacious blank paragraphs. The answer space should roughly match the expected answer length: shorter for 辨析题, medium for 简答题, longer for 材料分析题.

### 5. Validate before delivery

At minimum:

1. Open/check both `.docx` files as valid ZIP-based Word documents.
2. Verify chapter count and section count.
3. Verify each chapter has all required question types.
4. Verify star markers exist.
5. Verify the answer document has question text,考点定位,参考答案,解析.
6. Search for `TODO`, `??`, garbled text, and obvious extraction artifacts.

Run the bundled QA helper when applicable:

```powershell
python scripts/qa_review_docs.py `
  --practice "<题目练习版.docx>" `
  --answers "<答案解析版.docx>" `
  --chapters 15
```

If the chapter count differs, set `--chapters` accordingly.

### 6. Final response

Return direct local links to the two generated files. Include:

- output paths;
- brief statement of coverage and structure;
- validation performed;
- any extraction/rendering limitation that remains.

Do not include the full generated content in chat unless the user asks for excerpts.
