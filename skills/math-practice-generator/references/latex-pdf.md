# LaTeX/PDF 教辅制作参考

Use this reference whenever the final output is a `.tex` source or PDF.

## Production Flow

1. Build the content blueprint first: topic coverage, question count, score distribution, source mix, difficulty mix, and expected page count.
2. Draft all problems and solve them before typesetting. Keep the exercise and answer documents synchronized by question number, point value, source, and importance.
3. Start from `assets/publishing-practice-template.tex` unless the user supplies a template. Create separate exercise and answer `.tex` files from the same style system.
4. In LaTeX source, use the template's `\ImportanceLow`, `\ImportanceMedium`, and `\ImportanceHigh` macros for importance tags instead of raw Unicode star glyphs when possible.
5. Compile with XeLaTeX or LuaLaTeX. For Chinese documents, prefer `ctexart` and avoid CJK hacks that require fragile manual font setup.
6. Render and inspect representative pages. Fix overfull boxes, bad page breaks, cramped answer space, and unreadable formulas before delivery.

## Page Design Rules

- Use A4 paper. Keep margins near 18-22 mm unless the user needs binding space.
- Keep title blocks compact: document title, course/topic, suggested time, total score, and version/date if useful.
- Use subtle accents for structure, but ensure the PDF remains legible when printed in grayscale.
- Use boxes only for repeated semantic units: completion guide, question metadata, final answers, rubrics, and wrong-question review. Do not put every paragraph inside a decorative box.
- Keep exercise pages open and writable. Long-form problems should have explicit blank space or ruled answer areas.
- Keep answer pages denser. Use short headings, aligned derivations, boxed final results, and point-by-point rubrics.
- Avoid orphaned headings and split tables. Use `needspace`, manual page breaks, or shorter blocks where needed.

## Formula Rules

- Use display math for central equations and derivations.
- Use `aligned`, `split`, `cases`, `bmatrix`, and `pmatrix` for multi-line reasoning.
- Use `\mathrm{d}`, `\sin`, `\ln`, `\lim`, `\sum`, `\int`, `\vec{}`, `\boldsymbol{}`, and `\left...\right` consistently.
- Use `siunitx` for units when the subject needs units.
- For long equations, split the expression rather than shrinking the font.
- When converting from Word/PPT screenshots, reconstruct formulas manually in LaTeX instead of embedding low-resolution formula images.

## Recommended File Set

- `student.tex`: student-facing exercise packet.
- `solutions.tex`: teacher-facing answer and analysis packet.
- `assets/`: diagrams or images used by the `.tex` files.
- `student.pdf` and `solutions.pdf`: final deliverables.

## Compile Commands

Prefer:

```powershell
xelatex -interaction=nonstopmode -halt-on-error student.tex
xelatex -interaction=nonstopmode -halt-on-error solutions.tex
```

Run a second pass when cross-references, page references, table of contents entries, or labels are used.

If `xelatex` is unavailable but `lualatex` is available, use `lualatex`. If no LaTeX engine is available, still produce complete `.tex` files and report that PDF compilation was not run.

## QA Checklist

- Both PDFs compile without errors.
- LaTeX logs have no unresolved references, missing glyphs, missing images, or serious overfull boxes.
- The first page looks publication-ready: compact title, clear metadata, no excessive whitespace, no crowding.
- A dense formula page has readable display math and no margin overflow.
- Tables do not exceed the text width.
- Student PDF has enough handwriting space for every non-objective question.
- Solution PDF includes final answer, tested knowledge, method, key steps, scoring rubric, and common mistake for every question.
- Question numbers, point values, and total score match across student and solution PDFs.
- Wrong-question review table is present unless explicitly omitted.
- No TODO markers, placeholder labels, repeated numbers, or source-analysis scratch notes remain.
