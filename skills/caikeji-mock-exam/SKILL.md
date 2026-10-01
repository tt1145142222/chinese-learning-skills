---
name: caikeji-mock-exam
description: 'Generate chapter-specific 材料科学与工程基础/材科基期末模拟卷 deliverables from local course folders containing PPT/textbook PDFs, 雨课堂题目, 章节作业, and 考试范围 screenshots. Use when the user asks for “材科基模拟卷”, “材科基单元卷”, “第X章模拟题”, “按考试规格出题”, or wants two LaTeX/PDF files: a printable student question paper and a detailed answer-analysis paper.'
---

# 材科基模拟卷

## Core Contract

Lock the deliverable list before authoring. When the user explicitly selects this skill as the primary practice workflow, generate exactly two final user-facing PDFs by default without an extra confirmation:

1. **题目卷**: printable practice paper with usage guide, point values, source labels, importance stars, answer space, and a wrong-question review table.
2. **答案解析卷**: for every question, repeat the original question first, then give detailed answer analysis. Do not provide answer-only keys.

The user's explicit "questions only" or other narrower output request overrides this default. When this skill is only an inferred helper, follow the already authorized output list instead of adding an answer booklet. Pass the same locked list to every companion skill; companion routing does not reopen the deliverable decision. All answer-side requirements below apply whenever an answer PDF is included.

Use the source hierarchy: `考试范围` > chapter PPT > `章节作业` and `长江雨课堂题目` > textbook reference. Do not include content outside the requested chapter unless the user explicitly asks.

## Conditional Supporting Skills

This Skill is the primary owner of the domain boundary, blueprint, question writing, scoring, source labels, and answer quality. Do not also invoke `math-practice-generator` for those same responsibilities.

- Use `latex-polished-doc-builder` only when actual LaTeX/PDF construction needs its production guidance; it owns compile and layout QA, not question QA.
- Use `pdf:pdf` only when the available PDF renderer is needed for page inspection.

Select only the supporting capability needed for the current stage. Do not load every companion Skill in advance, and do not reopen the locked deliverable decision.

## Source Triage

1. Inventory the workspace first with `rg --files` or equivalent.
2. Locate the requested chapter across:
   - `材科基ppt教材` / PPT PDF: main source and boundary.
   - `章节作业`: original homework questions and difficulty reference.
   - `材科基-长江雨课堂-课堂题目`: original classroom questions and answer screenshots.
   - `考试范围`: mandatory high-priority exam points, often screenshots.
   - textbook PDF: background reference only unless teacher materials are insufficient.
3. Extract PDF text where possible. For screenshots or image-only slides, render contact sheets and visually inspect them.
4. If a file appears chapter-adjacent but belongs to another chapter, exclude it and mention the exclusion if relevant.

## Exam Blueprint

Match the user's stated final-exam structure unless they override it. For the usual 材科基期末规格, prefer a 100-point, 120-minute chapter mock paper with:

- single choice and fill-in for recognition, formulas, definitions, and quick judgments;
- 5 named concept explanations when possible;
- 7-8 short-answer questions;
- 3-4 analysis/comprehensive questions.

For a single chapter, keep the full-paper style but scale counts sensibly. A good default is:

- 单项选择: 20-30 points;
- 填空: about 10 points;
- 名词解释: 5 questions, about 20 points;
- 简答题: 7 questions, about 28 points;
- 分析综合: 3 questions, about 22 points.

Adjust only when source density or the user's request makes this inappropriate.

## Question Rules

For every question, show near the question number:

- **source label**: `章节作业原题`, `雨课堂原题`, `PPT原题`, `改编题`, or `预测题`;
- **importance**: one, two, or three stars; three stars are highest priority;
- **points**.

Use original source questions as the backbone when they are relevant and readable. Use prediction questions to cover missing exam-scope points, repeated PPT emphasis, formula applications, and likely transfer questions. Keep difficulty close to the folder's related exercises.

Cover all chapter points listed in `考试范围`. Then broaden to the chapter PPT's core concepts, formulas, mechanisms, and summary pages.

If a question benefits from a diagram, use one:

- Crop from source only when the original figure is necessary and readable.
- Prefer clean TikZ/self-drawn diagrams for predicted mechanism questions.
- Do not force diagrams into questions that do not need them.

## Student PDF Requirements

Start with a usage guide. For this user's 材科基 workflow, include the meaning:

- before using the document, first review the teacher's corresponding chapter questions and exercises;
- then complete this paper;
- for long-answer practice, it is acceptable to write only the answer logic, keywords, and structure first to save time;
- after completion, carefully correct mistakes and memorize all questions in this document;
- if there is extra energy, return to memorize the teacher's original questions.

Leave answer spaces sized to the expected writing volume:

- choices: answer line;
- fill-in: blanks;
- concept explanations: several ruled lines;
- short-answer and comprehensive questions: larger ruled areas.

Add a wrong-question review table near the end unless the user opts out.

## Answer PDF Requirements

For every question, include the original question text first, followed by detailed answer analysis. This is mandatory because the answer PDF must be usable for direct review without flipping back to the question paper.

For each item include:

- final answer;
- source出处, with file name and page/slide when available;
- tested knowledge point;
- explanation or method;
- scoring points/rubric matching the question's point value;
- common mistake or memory tip;
- mnemonic, analogy, or plain-language explanation when helpful.

Never make the answer PDF a bare list like `1.B 2.C`. Even objective questions need brief解析 and考点.

## LaTeX And Publication Quality

Build real LaTeX sources and compiled PDFs. Use `ctexart` and XeLaTeX for Chinese materials. The visual target is publication-quality teaching-aid style:

- restrained academic design, clear title block, headers/footers, and page numbers;
- consistent metadata tags and section hierarchy;
- print-safe colors and grayscale readability;
- no clipped text, overlapping content, broken tables, unresolved references, or obvious overfull boxes;
- text and formulas reconstructed as selectable LaTeX where feasible, not screenshots.

Use screenshots only for figures that are impractical to redraw.

## Output Placement

Honor the user's explicit output folder. If they name a final folder such as `期末复习模拟题单元卷`, put only the final PDFs from the locked deliverable list there (two PDFs under the default primary-workflow contract).

Keep all working artifacts outside the final folder, in the active task or project `work` directory:

- `.tex` sources;
- compile logs and auxiliaries;
- rendered pages/contact sheets;
- extracted text;
- cropped images and scratch files.

If no project folder is specified, follow the user's standing output-location preference before choosing another path.


## QA Ownership and Checklist

Run each check once on the final relevant revision. Reuse compile and render evidence produced by the selected document-production layer.

Before final delivery:

- total score and displayed point values match across both PDFs;
- question numbers match exactly between student and answer PDFs;
- source labels and importance stars appear on all questions;
- all `考试范围` points for the requested chapter are covered;
- answer PDF repeats each original question before the answer;
- answer explanations are detailed enough for review and memorization;
- LaTeX logs contain no severe errors, missing glyphs, unresolved references, or serious overfull boxes;
- rendered pages show no overlap, clipped text, or cramped answer areas;
- final folder contains only the requested final PDFs when the user asked for that constraint.

## Final Response

Link the final PDFs from the locked deliverable list. State the compilation and render QA actually performed. Mention any real limitations, such as unreadable source screenshots or excluded out-of-chapter files.
