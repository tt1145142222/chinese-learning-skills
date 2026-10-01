# Learner Model

> Copy this file into a course project. Add only evidence-supported observations. A single correct response does not close a recurring issue.

## Mastery status

- `new`: newly identified; insufficient evidence to judge consistency.
- `developing`: some supported progress, but performance is not yet consistent.
- `unstable`: performance varies or a previously improving issue has recurred.
- `stable`: repeatedly demonstrated under appropriate conditions and supported by closure evidence.
- `reopen`: a previously stable issue has reappeared and requires renewed tracking.

`Mastery status` must contain exactly one of `new`, `developing`, `unstable`, `stable`, or `reopen`. It describes performance consistency, not whether an issue is currently open.

## Issue lifecycle

- `active`: correction, retest, or carry-forward action is still required.
- `monitoring`: improvement has supporting evidence, but closure evidence is not yet sufficient or durability still needs checking.
- `closed`: independent fresh evidence satisfies the closure rule; retain the row as historical evidence.

`Issue lifecycle` must contain exactly one of `active`, `monitoring`, or `closed`. Keep this axis separate from `Mastery status`: never place a lifecycle value in the mastery column or a mastery value in the lifecycle column. Update each axis from its own evidence. If a closed issue recurs, set `Mastery status` to `reopen` and `Issue lifecycle` to `active`.

## K/R/O/C/S classification

- **K — knowledge gap:** missing or inaccurate concept, fact, rule, or prerequisite knowledge.
- **R — retrieval instability:** knowledge may be present but cannot be recalled or applied reliably.
- **O — expression or organization incomplete:** explanation, representation, structure, or communication is incomplete.
- **C — calculation / derivation / operation / diagram-process error:** an error in a calculation, derivation, operation, or diagramming process.
- **S — reading / symbol / unit / direction / careless error:** a misread prompt, symbol, unit, direction, or attention-related mistake.

Record exactly one value in `Primary K/R/O/C/S` for each finding. Use the optional `Qualifier` for nuance, never for a second primary label. If evidence supports two distinct issues, record them in separate rows. Provide evidence rather than inferring a label from impression alone.

## Active and historical evidence

| Concept / skill | Mastery status | Issue lifecycle | Primary K/R/O/C/S | Qualifier (optional) | Latest evidence | Confidence | Recurrence count | Correction action | Retest date | Closure evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | new | active |  |  |  |  | 0 |  |  |  |

## Evidence notes

| Date | Concept / skill | Evidence source or location | Interpretation limits | Related iteration-log session |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
