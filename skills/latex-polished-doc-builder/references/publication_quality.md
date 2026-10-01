# Publication Quality Reference

Read this reference when building a polished LaTeX/PDF document from source material.

## Design Targets

- Make the first page immediately identify the document: title, subtitle/version, scope, time/score/metadata when relevant.
- Use restrained professional styling. Prefer typography, spacing, rules, and subtle tint fills over decorative graphics.
- Keep page geometry printable. Use A4 for Chinese teaching materials unless the user or source implies Letter.
- Use page headers/footers with short title, section marker if useful, and page numbering.
- Avoid one-page landing-page aesthetics. The document should start as a usable artifact.

## Content Fidelity

- Preserve original meaning, factual content, numeric values, units, formulas, answer choices, examples, citations, and logical order unless the user explicitly asks for rewriting or restructuring.
- Allow non-semantic polish by default: spacing, margins, line breaks, heading hierarchy, table column widths, box/rule styling, page breaks, font pairing, and answer-space layout.
- Do not paraphrase problem text, simplify arguments, merge or split content semantically, change notation, reorder questions, or infer missing content just to make the document look cleaner.
- For OCR or handwriting uncertainty, keep a scratch note and surface unresolved ambiguity instead of silently changing the source.

## Semantic Recomposition

- Rebuild documents as real LaTeX text, math, tables, and structured blocks by default; do not use full-page screenshots or full-page PDF embedding as the main conversion strategy.
- Reorganize visual hierarchy for readability while preserving source order and substantive wording: title levels, body text, examples, notes, exercises, captions, and answer areas may be visually rebalanced but not rewritten.
- For slide decks, convert slide content into a coherent handout or teaching packet unless the user explicitly asks for a slide facsimile.
- Use cropped source images only for complex diagrams, photos, dense plots, hand drawings, or visual objects that cannot be faithfully and efficiently redrawn in LaTeX.
- When inserting a cropped figure, crop tightly, keep resolution high, and typeset surrounding captions, labels, and explanatory text in LaTeX whenever possible.

## Common Archetypes

- Teaching packet / worksheet: title block, completion guide, section bands, problem cards, answer blanks, worked-space lines, wrong-question review table.
- Report / brief: title block, executive summary, clear heading ladder, tables for comparable data, footnotes or references if needed.
- Paper / academic note: title, author/date if provided, abstract if present, numbered sections, theorem/proof/example environments when useful.
- Form / checklist: obvious fields, row height that supports handwriting, grouped sections, restrained grid lines.
- Handbook / guide: compact navigation, repeated subsection style, examples and callouts.

## Typography

- Chinese: `ctexart` or `ctexbook` with `xelatex`; use SimSun or Source Han Serif-like body text and Microsoft YaHei/SimHei-like headings when available.
- English: Times-like body text and Arial/Helvetica-like sans headings are safe defaults.
- Math: use AMS packages and real math operators. Do not type formulas as plain text.
- Do not use fonts below readable print size unless table density absolutely requires it.

## LaTeX Structure

Recommended packages for most polished documents:

```tex
\documentclass[UTF8,zihao=-4,fontset=windows]{ctexart}
\usepackage[a4paper,top=22mm,bottom=22mm,left=21mm,right=21mm,headheight=15pt]{geometry}
\usepackage[table]{xcolor}
\usepackage{amsmath,amssymb,mathtools,bm}
\usepackage{tabularx,booktabs,array}
\usepackage{enumitem,fancyhdr,lastpage,tcolorbox,needspace}
\tcbuselibrary{breakable,skins}
```

Use macros for repeated objects:

- `problem` boxes for exercises.
- `infobox` for guides or notes.
- `\answerblank`, `\resultblank`, or ruled-line macros for printable answer space.
- `tabularx` column types for flexible tables.

## Formula Transcription

- Convert integral bounds, radicals, vectors, matrices, differential symbols, and domains into LaTeX.
- Include Jacobian factors explicitly when the original formula includes transformed coordinates.
- Use `\iint`, `\iiint`, `\,dA`, `\,dV`, `\,dx`, `\,dy`, `\bm{F}` where appropriate.
- Split long expressions with `aligned`, `gathered`, or `multline`; avoid overfull formulas.

## Tables And Forms

- Use `booktabs` for reading tables and full ruled grids for handwriting forms.
- Size columns by content, not equally by default.
- Give handwriting rows enough height, normally 8-12 mm for short entries.
- Repeat table headers manually if a table spans pages and the toolchain does not do it automatically.

## Page Break QA

Before delivery, inspect rendered pages for:

- Problem title separated from the problem body.
- Answer line orphaned on a new page.
- Section heading left alone at the bottom of a page.
- Table title split from its table.
- Large blank pages caused by over-aggressive `\clearpage`.
- Overfull formulas extending past the margin.

Use `\Needspace`, local `\clearpage`, shorter answer-line counts, or smaller but readable spacing to fix these.
