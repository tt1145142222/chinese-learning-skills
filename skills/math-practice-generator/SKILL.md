---
name: math-practice-generator
description: Generate or substantially revise quantitative practice sets, exams, and worked answer keys from course materials or a defined topic scope. Use when the requested outcome includes authoring, adapting, organizing, or solving exercises; do not use for pure LaTeX/PDF conversion or formatting of already-final content.
---

# 数理类题目生成

## Core Workflow

Use this skill to turn a folder of 数理类教材、课件、例题、习题 or exam materials into the authorized practice deliverables.

**Deliverable contract:** lock the output list before authoring from the user's request and any explicitly selected primary skill. When the user explicitly selects this skill as the primary practice workflow, its default is one exercise packet plus one separate answer/analysis packet; do not ask for an extra confirmation of that default. An explicit "questions only" or other narrower output request overrides it. When this skill is only an inferred helper, follow the already authorized output list instead of adding an answer booklet. Pass this same list to LaTeX and other companion skills; answer-side requirements below apply whenever an answer packet is included.

1. **Inventory sources first.** List available PDFs, PPT/PPTX, DOCX, images, and exercise files. Prefer `rg --files`; use PowerPoint COM, PDF text extraction, rendering, or screenshots when formulas are embedded as images/OLE objects.
2. **Infer the exam scope from evidence.** Prioritize teacher-marked textbook pages, lecture examples, review slides, exercise-session slides, and repeated formulas/methods. If the user gives a scope, use it as the boundary and use sources only to tune difficulty and style.
3. **Create a blueprint before authoring.** Decide covered topic types, question count, estimated completion time, source mix, difficulty/importance mix, and output format. Keep the packet focused; avoid trying to cover an entire course unless the user asks.
4. **Write and solve every problem before building documents.** Verify all answers independently. For generated prediction questions, choose numbers/regions/parameters that lead to clean exam-style results.
5. **Generate the locked deliverable set.** Under this explicitly selected primary workflow, default to a student-facing exercise PDF and a separate teacher-facing answer/analysis PDF, compiled from LaTeX. Follow any narrower user request or upstream output list. Keep `.tex` sources as working files unless the locked deliverable list explicitly includes them. Include a wrong-question review table in the exercise PDF unless the user opts out.
6. **Render and QA the PDFs.** This primary Skill owns question correctness, coverage, scoring, and exercise/answer correspondence. The selected document-production layer owns one compile/layout QA pass; reuse that evidence here instead of repeating it. If LaTeX compilation is unavailable, create the `.tex` working source and state clearly that PDF compilation was not run.

## Required Output Standards

- Default final format is polished PDF, not DOCX. Only create DOCX/Word output when the user explicitly requests it or when the source workflow requires an intermediate editable copy.
- Put a short **completion guide** at the start of the exercise document: what to do first, time allocation, what to review before big questions, how to correct mistakes, and what to revisit after grading.
- Include mixed question types unless the user specifies otherwise: choice, fill-in/short answer, and long-form problems.
- Keep workload aligned with the user's time budget. For a 2-hour practice set, usually use about 10-14 questions with 3-5 substantial problems.
- Assign a point value to every question. If the user does not specify a total score, default to a 100-point paper for exam-style packets; otherwise choose a clear total that matches the requested workload.
- Label each question with:
  - Source: `课本原题`, `PPT原题`, `讲义/习题原题`, `改编题`, or `预测题`
  - Importance: `★☆☆`, `★★☆`, or `★★★`
- Show point value in the same metadata area as source and importance, for example `【PPT原题｜★★★｜10分】`.
- Leave enough writing space in the exercise document for printing.
- Add a **错题复盘表** near the end of the exercise document. Default columns: `题号`, `失分原因`, `正确方法/关键公式`, `重做结果`, `复习日期`.
- In the answer document, do not give bare answers. For every question include:
  - final answer
  - tested knowledge point
  - method/strategy
  - key calculation steps
  - scoring points/rubric keyed to the question's point value
  - technique or common mistake

## LaTeX PDF Production Standards

- Treat LaTeX PDF as the primary publication format. Prefer `ctexart` or an equivalent CJK-capable class, compile with XeLaTeX or LuaLaTeX, and use A4 print margins suitable for handouts.
- Use `assets/publishing-practice-template.tex` as the default starting point unless the user supplies a house style. Read `references/latex-pdf.md` before final document construction.
- Produce 教辅-quality pages: balanced title block, compact instructions, consistent question metadata tags, readable hierarchy, professional headers/footers, stable page numbering, and enough whitespace for handwritten answers.
- Keep the visual style academic and restrained: no decorative clutter, no low-contrast text, no oversized marketing-style headings, no single-color monotony. Accent colors should guide structure without hurting grayscale printability.
- Use proper LaTeX math for every formula that needs textbook appearance: fractions, radicals, vectors, matrices, summations, limits, integrals, units, cases, aligned derivations, and upper/lower bounds.
- Split long formulas with `aligned`, `split`, `multline`, or manual line breaks. Never squeeze formulas below readable print size or let them run into margins.
- For diagrams, use TikZ/PGFPlots when the geometry is simple and deterministic; otherwise use high-resolution images with clear labels and print-safe contrast.
- Keep exercise and answer PDFs visually related but distinct. The exercise PDF should prioritize answer space; the answer PDF should prioritize worked reasoning, boxed final answers, and scoring rubrics.

## Source Handling

- For PPT/PPTX, inspect both text and rendered slide images; formulas are often not recoverable from text extraction alone.
- For PDFs, check text extraction, outlines/table of contents, annotations/highlights, and rendered pages around likely chapters.
- For textbooks, avoid copying large copyrighted passages. Use source labels and direct original questions only sparingly; prefer short original examples, adapted variants, and prediction questions based on the same methods.
- When the source language, notation, or coordinate conventions differ from the target student packet, normalize notation consistently and mention any convention in the answer key.

## When More Detail Is Needed

Read `references/workflow.md` only for a full document-generation task, a large source folder, a non-calculus subject needing its routing details, or a requested reusable/three-day/full-coverage plan. The LaTeX reference is already routed above and should not be read a second time when unchanged.
