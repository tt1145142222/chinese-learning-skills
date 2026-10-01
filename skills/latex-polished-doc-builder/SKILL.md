---
name: latex-polished-doc-builder
description: Reconstruct source materials as semantic, print-ready LaTeX and compiled PDF. Use when the user explicitly wants LaTeX source, semantic re-typesetting, or faithful reconstruction of formulas, tables, and mixed document content; do not use for simple PDF export or native DOCX/PPTX editing.
---

# LaTeX Polished Document Builder

## Core Contract

Produce a real `.tex` source file and a compiled PDF unless the user explicitly asks for PDF only. The result should be professionally typeset and printable, not a raw conversion.

Default to semantic reconstruction: extract the source content, then rebuild it as a real LaTeX document with appropriate fonts, hierarchy, spacing, tables, equations, and page furniture. Do not satisfy a conversion request by embedding every source page/slide as a screenshot or full-page PDF unless the user explicitly requests a facsimile, the source is inherently unrecognizable as text, or you clearly label it as a temporary fallback rather than the main conversion.

Accept source material from Word, PowerPoint, PDFs, screenshots, scans, phone photos, handwritten notes, text/Markdown, or mixed folders. Convert the material into the user's requested target document; if no target or style requirement is stated, default to a publication-ready teaching-aid/worksheet standard with clean hierarchy, readable math, printable spacing, and polished page furniture.

Preserve the original content and meaning exactly. Unless the user asks for rewriting, do not change factual claims, problem statements, answer choices, examples, formulas, numbers, units, citations, terminology, or logical order. When no special instruction is given, you may make aesthetic and layout refinements that do not alter meaning, such as improving spacing, heading hierarchy, table widths, page breaks, callout styling, font choices, line breaks, and printable answer-space layout.

**Deliverable contract:** when used as a layout/production companion, execute the output list already established by the user's request or by an explicitly selected primary skill. This includes the two-packet default of an explicitly selected practice skill such as `math-practice-generator` or `caikeji-mock-exam`; do not remove its answer booklet or ask for another confirmation. An explicit "questions only" or other narrower user request always overrides a skill default. An inferred helper skill cannot expand the authorized list.

When used independently for conversion, typesetting, or general document production, generate an answer booklet only when the user explicitly requests answers, solutions, an answer/analysis edition, or a deliverable specification that includes one. A request for questions, exercises, a worksheet, or a test alone does not authorize an additional answer booklet. Lock this output list before authoring and reuse it throughout production and delivery.

Answer-booklet self-containment is mandatory whenever an answer booklet is in the locked deliverable list. Every entry must contain, in this order: (1) the complete corresponding question, (2) a clearly labeled reference answer, and (3) an explanation or analysis showing the reasoning, distinctions, derivation, or basis for that answer. Preserve the original question number, score, stem, all subparts, givens, options, tables, figures, and other information needed to understand the answer. Do not deliver an answer-only document and do not replace the question with a bare label such as “Question 3” or “see the exercise booklet.” Add scoring rubrics and source notes when requested or useful, but never use them as substitutes for the required question, answer, or analysis.

Always honor the active thread or personalization instructions for output location. If the user or project specifies a folder, put final user-facing files there. If no output path is specified, follow the user's configured default output location before falling back to the current workspace `outputs/` directory. Keep scratch files under a non-delivered working directory.

For Chinese documents, default to `xelatex` with `ctex`. For mixed Chinese/English/math documents, prefer `latexmk -xelatex`. Use `pdflatex` only when the source is clearly Latin-only and the chosen template benefits from it.

If formulas are embedded as images, recognize and re-typeset them as LaTeX whenever reasonably possible. Do not silently leave formula screenshots in the final document unless the user asks to preserve the original image or the content is not reliably readable.

Use images selectively. Complex diagrams, photographs, dense scientific plots, hand-drawn figures, or visual compositions that would be slower or less accurate to redraw may be cropped from the source and inserted as high-quality figures. Crop only the needed object or figure region, keep it visually clean, add the surrounding text/caption in LaTeX when possible, and avoid full-page screenshots except for genuinely image-only source pages.

## Workflow

1. Inventory source files before authoring.
   - For DOCX: use the available document extraction/rendering capability first. Inspect `word/document.xml`, relationships, media, or Office math objects only when high-level extraction omits content or a specific OOXML/OLE problem must be resolved.
   - For PPT/PPTX: use the available presentation extraction/rendering capability first. Inspect slide XML, relationships, embedded media, or equation objects only when high-level extraction is incomplete or an object-level fault must be resolved. Use slide order as source order unless the user requests a different structure. Render slides only for visual inspection, OCR support, or object-level figure cropping; do not use rendered slides as the primary final content by default.
   - For PDF: use text extraction plus rendered page inspection; formulas may require visual transcription.
   - For images/scans/handwritten notes: create a numbered contact sheet or page renders before transcribing; preserve page order and flag uncertain handwriting, symbols, diagrams, or formula parts.
   - For mixed folders: group files by source type and infer document order from filenames, slide/page numbers, timestamps, or visible headings.

2. Extract content and build a conversion map.
   - Lock the deliverable set under the Deliverable contract above. Reuse an authorized primary-workflow list without reopening confirmation; independent typesetting does not add an answer booklet unless the user requested one.
   - Preserve section order, headings, metadata, tables, figure positions, answer blanks, and forms.
   - Build a conversion map that classifies each source item as real LaTeX text, LaTeX math, reconstructed table, cropped figure/image, or unresolved/uncertain content.
   - For slides, do not mechanically clone the slide layout unless requested; transform slide bullets, board-work, speaker notes, and diagrams into a coherent printable handout, worksheet, report, or teaching packet.
   - For slide decks and PDFs, reflow text into readable paragraphs, lists, examples, exercises, theorem-style blocks, or topic sections while preserving the original order and substantive wording.
   - Convert formulas to LaTeX display or inline math.
   - For tables, rebuild semantic tables with `tabularx`, `booktabs`, or explicit ruled grids; do not paste table screenshots.
   - Mark uncertain OCR or unreadable items in scratch notes and resolve before final delivery when possible.
   - Treat OCR cleanup as fidelity work, not rewriting: correct obvious recognition errors, but mark uncertain words, symbols, and formulas instead of guessing silently.

3. Design the document before writing the final `.tex`.
   - Read `references/publication_quality.md` only for a new or materially revised multi-page design, or when the user requests publication-quality visual polish. Reuse it when already read and unchanged in the same task.
   - Choose the document archetype: teaching packet, report, paper, form, proposal, handbook, or worksheet.
   - Define page size, margins, typefaces, heading hierarchy, table style, callout style, page headers/footers, and answer-space policy.
   - Choose fonts and layout roles from the source intent rather than copying source fonts mechanically: titles should read as titles, body text as body text, examples/exercises as structured blocks, and notes as secondary material.
   - Apply only non-semantic polish when the user gives no style details; improve presentation without changing wording, answer logic, data, formula meaning, or source intent.

4. Author LaTeX with stable, maintainable structure.
   - Use semantic macros for repeated blocks such as problems, notes, metadata tags, answer blanks, rubric rows, or form fields.
   - When an answer booklet is in the locked deliverable list, use one shared question source, macro, or structured data record so the question wording and numbering remain identical in the exercise and answer files. Structure every answer-booklet entry as: complete question first, then the reference answer, then the explanation/analysis. Add a scoring rubric and source note afterward when applicable.
   - Use extracted source text as selectable LaTeX text; use images only for complex visual objects or source regions that cannot be faithfully reconstructed.
   - Use real LaTeX math for formulas and operators.
   - Avoid oversized decorative design; use restrained color, spacing, and hierarchy to make the document feel publishable.
   - For long formulas, split lines with `aligned`, `multline`, or smaller scoped environments rather than squeezing.

5. Compile and iterate.
   - Run `latexmk -xelatex -interaction=nonstopmode -halt-on-error <file>.tex`.
   - Run `scripts/scan_tex_log.py <file>.log` and fix severe issues: LaTeX errors, missing characters, overfull boxes, unresolved references, or broken citations.
   - Recompile after each coherent batch of layout changes, and once for the final candidate. Content-only edits that cannot affect layout may be batched before recompilation.

6. Render and visually QA the final PDF.
   - Run `scripts/render_pdf_contact_sheet.py <pdf> --output-dir <qa-dir>` when Poppler/Pillow are available.
   - Inspect the contact sheet and, when needed, individual rendered pages.
   - Confirm no clipped text, overlapping elements, missing glyphs, broken tables, orphaned answer lines, or awkward page splits.
   - For every answer booklet in the locked deliverable list, verify one-to-one completeness: each entry contains the full matching question, a reference answer, and an explanation/analysis; the question number and score agree with the exercise booklet; all subparts and required figures/tables are present; and no answer appears without its question.
   - Compare the final PDF against the source map and spot-check representative pages/slides to ensure no substantive text, formula, number, option, table entry, or figure was omitted or altered.

7. Deliver.
   - Copy final `.pdf` and `.tex` to the configured final output directory.
   - Deliver exactly the locked output list. Include an answer booklet authorized by an explicitly selected primary practice workflow, but do not add one as a bonus or inferred companion to independent typesetting.
   - In the final response, link only final deliverables unless the user asks for QA intermediates.
   - State any real limitations, such as unreadable formulas, unresolved OCR, skipped visual QA, or places where cropped source images were used because faithful LaTeX reconstruction was not practical.

## Resource Usage

- `references/publication_quality.md`: read only for a new or materially revised nontrivial style, especially explicit "美观", "出版级", or multi-page design work. Do not reread it when unchanged in the same task.
- `scripts/scan_tex_log.py`: run after LaTeX compilation to catch severe log issues.
- `scripts/render_pdf_contact_sheet.py`: render final PDF pages and build a review sheet for visual QA.

## Output Naming

Prefer names based on the source title plus a clear suffix, for example:

- `<原文件名>_LaTeX出版版.tex`
- `<原文件名>_LaTeX出版版.pdf`

Use a different suffix when the user requests a specific version, such as `题目版`, `答案解析版`, `讲义版`, `打印版`, or `正式版`.
