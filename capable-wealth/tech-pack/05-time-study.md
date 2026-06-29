# Time Study

> **Status: PINNED / pending data.** The timings below are to be measured by running the workflow end to end and recording the wall-clock at each stage. Jared/Dave will run the study and provide the numbers; this doc will then be populated. The structure, stage list, and HITL-dependency callouts are ready to fill.

## Method

For each workflow run, record the wall-clock time at the **start** and **finish** of each stage. Critically, separate **machine time** (the model drafting/gating) from **human-in-the-loop (HITL) wait time** (a person reviewing or approving), because HITL time is a dependency, not a cost of the system, and it dominates total elapsed time.

- **Machine time** = time the harness is actively working.
- **HITL wait** = elapsed time the run is blocked waiting on a human decision.
- **Total elapsed** = machine time + HITL wait.

## generate-batch: stage timing template

| # | Stage | Start | Finish | Machine time | HITL dependency? | Notes |
|---|---|---|---|---|---|---|
| 1 | Load brand context (read source-of-truth docs) | | | | No | |
| 2 | research-scan freshness pass for the week | | | | No | |
| 3 | Draft blog | | | | No | |
| 4 | Draft podcast script | | | | No | |
| 5 | Draft 3 LinkedIn posts | | | | No | |
| 6 | Draft 5 Facebook posts | | | | No | |
| 7 | Draft clips + optional video/carousel | | | | No | |
| 8 | Gate: linkedin-check on each LinkedIn post | | | | No | |
| 9 | Gate: image-brief for each visual asset | | | | No | |
| 10 | Gate: validate (integrity / date / relevance) | | | | No | |
| 11 | Gate: voice-check | | | | No | |
| 12 | Export Excel batch summary | | | | No | |
| 13 | Post review summary to Slack | | | | No | |
| 14 | **HITL: human reviews batch before publish** | | | n/a | **YES (blocking)** | run is blocked until a person approves |
| 15 | **HITL: Jared approves any brand-doc change** | | | n/a | **YES (blocking, conditional)** | only if a run proposes brand-doc edits; brand docs change only on Jared's explicit approval |

**Totals:** machine time = ___ ; HITL wait = ___ ; total elapsed = ___ .

## HITL dependency callouts (the blocking points)

These are the points where the workflow **cannot proceed without a human**, regardless of how fast the machine is:

1. **Pre-publish review (stage 14).** Every batch stops for human review before anything is published. This is by design (story integrity, compliance, voice). It is the single largest source of total-elapsed-time variance.
2. **Brand-doc approval (stage 15).** Brand source docs (voice profile, content recipe, content calendar, LinkedIn guidelines) change only on Jared's explicit approval. Edits are proposed as diffs and never applied silently. If a run surfaces a needed brand-doc change, it blocks on Jared.

> When the measured numbers come in, replace the blank cells, compute the three totals, and note the ratio of machine time to HITL wait. That ratio is the headline of this study.
