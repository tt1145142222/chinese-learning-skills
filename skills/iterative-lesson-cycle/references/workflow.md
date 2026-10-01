# Teaching-cycle workflow

Use this workflow for any course. Keep the course profile, learner model, iteration log, submitted work, and generated artifacts in the active course project.

## Project structure and output location

Follow an existing course-project structure when one is present. Otherwise create this structure in the active project:

```text
迭代上课/
├── 课程档案.md
├── 学情总表.md
├── 迭代日志.md
└── 课次/
    └── YYYY-MM-DD-主题/
```

Choose output locations in this order: an explicit user destination, then the active course project, then the environment's default deliverable location. Project state and learner data must stay in the active course project and must never be written to the global skill folder.

## State axes and session phase

Track two independent learner-model axes for every finding:

- `Mastery status` is exactly one of `new`, `developing`, `unstable`, `stable`, or `reopen`; it describes performance consistency.
- `Issue lifecycle` is exactly one of `active`, `monitoring`, or `closed`; it describes whether correction, monitoring, or closure action remains.

Never mix values from these axes in one column or infer one automatically from the other. Update `Mastery status` from performance consistency and `Issue lifecycle` from correction, monitoring, and closure evidence. When a closed issue recurs, use mastery `reopen` and lifecycle `active`.

`Session phase` is a third, separate axis. Its value must be exactly one of `planned`, `in progress`, `awaiting practice`, `awaiting correction`, or `cycle complete`. Never combine a phase with explanatory text. Store details such as active carry-forward or a deadline checkpoint in `Phase note`.

## Cycle and scheduling rule

Follow this complete cycle:

```text
course profile -> pre-class guide -> actual class evidence -> student practice
-> check-in analysis -> correction/retest evidence review
-> learner-model and iteration-log update -> next lesson
```

When a schedule changes, move or shorten work only after preserving a complete `class -> practice -> correction` loop. Do not stack multiple unfinished cycles into one day. Record the changed date, what was deferred, and the next evidence-collection point.

## 1. New-course initialization

**Inputs:** authoritative course sources, confirmed assessment rules and schedule, approved teaching plan, available learner history, and project location.

**Actions:** create or verify the course profile; record source versions, assessment constraints, course outcomes, available class cadence, and learner baseline. Create or verify a learner model and iteration log. Separate confirmed facts from assumptions and mark unavailable information as missing.

**State updates:** course profile becomes the current source map; learner model records baseline strengths, weaknesses, confidence, evidence dates, and the two state axes separately; iteration log records the first cycle with session phase `planned`.

**Complete when:** the project has enough confirmed scope and baseline evidence to plan one lesson without inventing rules or learner facts.

## 2. Pre-class preparation

**Inputs:** course profile, confirmed plan, authoritative sources, unresolved learner-model items, prior corrections, and session time.

**Actions:** choose an achievable lesson focus; prepare the instructor lecture guide; include diagnostic prompts that can produce observable evidence; define what class artifact or observation will confirm actual coverage and performance.

**State updates:** iteration log records planned objectives, planned evidence, and the link to the instructor guide. Do not overwrite prior evidence with the plan.

**Complete when:** the guide is instructor-ready, timing fits the session, and post-class reconciliation can distinguish planned from actual coverage.

## 3. Post-class reconciliation

**Inputs:** accessible recording, final slides, teaching notes, attendance or participation observations, and the pre-class guide.

**Actions:** inspect only accessible evidence; identify actual coverage, changes from plan, observed performance, unanswered questions, and evidence gaps. Generate the next-day student exercise from actual coverage, with recall, light transfer, and historical repair sized to the evidence.

**State updates:** iteration log records actual coverage and evidence status; learner model receives provisional observations only when attributable to the learner. Missing or unreadable artifacts remain marked missing.

**Complete when:** the practice matches what actually occurred, not merely what was planned, and its check-in method can collect diagnostic evidence.

## 4. Next-day practice

**Inputs:** reconciled class evidence, current learner model, unresolved issues, and available learner time.

**Actions:** issue the student exercise as a physically separate artifact from any shareable answer key and internal analysis. State time guidance and the required check-in format. Collect the learner response, work process if available, and confidence markers without supplying answers or internal workflow text to the learner.

**State updates:** store each submission with date, task version, and learner identity. Record non-submission, partial submission, or inaccessible material as evidence status rather than as mastery.

**Complete when:** a check-in response is received or the absence is explicitly logged with a next collection action.

## 5. Check-in analysis

**Inputs:** original learner response and process, confidence markers, relevant class evidence, and prior learner-model items.

**Actions:** analyze evidence before impressions; assign exactly one primary K, R, O, C, or S label to each material finding, with an optional qualifier for nuance; set priority; prescribe a concrete correction and a fresh retest. Record a supported learner-model update and carry-forward decision, but do not treat issuing the correction or retest as evidence that it succeeded.

**State updates:** add evidence-linked findings and the required corrections to the internal analysis and iteration log; update `Mastery status` and `Issue lifecycle` separately and only with supported conclusions; add unresolved high-impact items to the next-lesson focus list. Set the session phase to exactly `awaiting correction` when correction or retest evidence is still required, and put any qualifier in `Phase note`.

**Analysis phase complete when:** every material finding has an evidence reference, exactly one primary label, a priority, a correction action, a retest condition, a supported learner-model update, and a carry-forward decision. Completing this analysis phase does not complete the teaching cycle.

## 6. Correction and retest

**Inputs:** the internal check-in analysis, the learner's original correction or fresh retest response and process, confidence markers, and the active learner-model and iteration-log entries.

**Actions:** collect original correction work or fresh retest evidence and judge it under the evidence and closure rules. Update recurrence, confidence, and closure evidence. Separately update `Mastery status` using only `new/developing/unstable/stable/reopen` and `Issue lifecycle` using only `active/monitoring/closed`. If the required correction or retest evidence is completely missing, keep issue lifecycle `active` and session phase exactly `awaiting correction`. A schedule deferral belongs only in `Phase note` and the carry-forward action; it is not evidence and never permits `cycle complete`. If submitted evidence is incomplete, review and record what it supports, but keep lifecycle `active` and session phase `awaiting correction` whenever the prescribed correction or retest action remains incomplete.

**State updates:** link the reviewed evidence in the iteration log; update both learner-model axes and the carry-forward list. Keep lifecycle `active` when action is required, move it to `monitoring` when improvement needs durability evidence, and use `closed` only when independent fresh evidence satisfies the closure rule. Independently record the supported mastery value. Set session phase to exactly `cycle complete` only after the required correction or retest evidence has been submitted and reviewed, the prescribed correction or retest action has been completed, and all required state and log updates are written. Record unresolved or monitored carry-forward in `Phase note`. Merely issuing, rescheduling, or deferring a retest is insufficient.

**Complete when:** the required correction or retest evidence has been submitted and reviewed, the prescribed action is complete, and the project state updates are written. Cycle completion does not itself close an issue; an issue may keep lifecycle `active` after a completed but unsuccessful retest and carry forward. `stable` is a mastery value, not an issue-lifecycle closure value.

## 7. Stage simulation

**Inputs:** confirmed assessment scope and rules, cumulative learner evidence, unresolved high-impact issues, and the available timed conditions.

**Actions:** confirm scope before authoring; create the timed mixed-format student test, shareable answer key, and internal performance analysis as three physically separate files; administer or provide the test under stated conditions; analyze performance using the same evidence rules; produce a finite, ranked repair list rather than broad re-teaching.

**State updates:** log tested scope, conditions, outcomes, and repair items. Preserve unresolved items in the learner model for the next cycle.

**Complete when:** the simulation reflects confirmed conditions, results are evidence-linked, and the repair list has a bounded number of actionable items.
