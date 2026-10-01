# 数理类练习题生成工作流参考

## 1. Source Triage Checklist

- Identify source types and likely authoritative files:
  - review slides, exercise-session slides, chapter summary slides
  - teacher-highlighted textbook pages
  - worked examples and in-class examples
  - past papers or homework banks
- Extract text where reliable, but render pages/slides when formulas or diagrams matter.
- Record a short source map: file name, chapter/topic, examples found, teacher emphasis, and usable question candidates.
- If source scope is broad, select by evidence density: marked examples > review slides > repeated lecture formulas > ordinary exercises.

## 2. Practice Blueprint

Before authoring, decide:

- Audience and goal: exam review, daily practice, remedial drill, challenge set, or diagnostic.
- Coverage: exact topic families and exclusions.
- Workload: target minutes and approximate point allocation.
- Output: default to two compiled LaTeX PDFs plus `.tex` sources. Use another format only when the user explicitly requests it.
- Score plan: assign every question a point value. If unspecified, use a 100-point exam-style total; make objective questions lighter and long-form problems heavier.
- Question mix:
  - objective questions for recognition, formulas, direction/sign, units, and quick setup
  - fill-in questions for standard calculations
  - long-form problems for complete method chains
- Source mix:
  - original source problems for high-signal teacher emphasis
  - adapted problems for controlled difficulty
  - prediction problems for exam-style transfer
- Importance:
  - `★★★`: core exam method, common source emphasis, high transfer value
  - `★★☆`: standard but narrower method
  - `★☆☆`: warm-up, recognition, or low-frequency variant

Default scoring guidance:

- Choice questions: 3-5 points each.
- Fill-in or short-answer questions: 5-8 points each.
- Long-form problems: 10-18 points each, depending on setup and calculation length.
- If a 100-point paper does not fit the requested time budget, use a smaller explicit total and show it in the title block.

## 3. Authoring Rules

- Write clean, unambiguous problem statements. Define regions, orientations, constants, and parameter ranges.
- Prefer values that produce exact answers and reveal the method.
- For multistep math problems, ensure the intended method is visible but not over-signposted unless the packet is remedial.
- Balance originality and source fidelity:
  - `课本原题` / `PPT原题`: use only when the exact original is short and central.
  - `改编题`: preserve method but change constants, region, or wording.
  - `预测题`: designed from the pattern, not copied.
- Solve each problem before finalizing the exercise document.

## 4. Answer-Key Pattern

For each question, use this structure:

1. **答案**: final result, preferably displayed as a formula.
2. **考点**: topic and tested subskill.
3. **方法与技巧**: one concise sentence about the strategic move.
4. **过程**: enough algebra/calculus steps to teach correction.
5. **采分点**: rubric items whose points add up to the question value. Include setup/modeling, formula choice, substitution/transformation, calculation, final answer, and units/sign/orientation where relevant.
6. **易错点**: one concrete risk such as sign, orientation, bounds, units, missing Jacobian, or formula conditions.

For objective questions, the scoring point can be short, such as `选对得满分；若要求写理由，方向/公式判断占 1 分`. For long-form problems, split scoring into 3-5 concrete items.

## 5. Wrong-Question Review Table

Add a printable 错题复盘表 near the end of the exercise document unless the user opts out.

Default columns:

- 题号
- 失分原因
- 正确方法/关键公式
- 重做结果
- 复习日期

Leave enough row height for handwriting. Include at least as many blank rows as there are questions, or 8-12 rows for shorter packets.

## 6. LaTeX/PDF Document QA

- Exercise document:
  - contains completion guide
  - every question has source and importance tag
  - every question has a point value
  - includes a wrong-question review table
  - answer space is sufficient for printing
  - formulas are native LaTeX math, not plain-text approximations
  - page count matches time budget
- Answer document:
  - every question has answer, knowledge point, method, process, scoring points, and mistake note
  - scoring points add up to the displayed question value
  - formulas are readable at print size
  - no scratch notes, TODOs, or placeholders remain
- Technical checks:
  - compile with XeLaTeX or LuaLaTeX at least twice when cross-references, page labels, or table of contents entries are used
  - inspect LaTeX logs for overfull/underfull boxes, missing glyphs, missing images, undefined references, and package errors
  - render representative PDF pages to PNG when possible, including the first page, a dense formula page, a table page, and the final page
  - check max formula/table/image width against the printable text block; split or resize content instead of allowing overflow
  - scan final `.tex` and PDF text for TODO markers, placeholder tokens, repeated question numbers, and mismatched point totals
  - disclose any skipped compile or render QA in the final response
