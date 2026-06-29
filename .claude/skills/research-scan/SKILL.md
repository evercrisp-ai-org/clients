---
name: research-scan
description: Weekly freshness pass that enriches the EXISTING annual content plan — it does NOT conduct new external research or acquire new material. For a given week, it refreshes that week's scheduled items so they stay relevant for the period they will publish in, using only material already in the repo. Use before generating a week's batch, or when the user asks to refresh / freshen / tune up the plan for a week.
---

# Research Scan — Weekly Plan Freshness Pass

Refresh the existing annual content plan for a given week so the scheduled items land correctly for the moment they publish. **This skill does NOT acquire new external material, run web searches, or fetch new facts.** It works entirely from what is already in the repo — the editorial plan, the quarterly plan, the content calendar's static cycles, the voice profile, and prior batches — and simply re-tunes the week's already-planned content for timeliness and relevance.

## Input

A week (e.g. `week-21`) or a date. If none is given, infer the week about to be produced (the next un-produced week after the most recent batch folder).

## What this skill does NOT do

- No web searches, no fetching, no new sources, no new facts.
- No new topics. It refreshes the items **already scheduled** in the plan; it does not invent additions.
- If a planned item depends on a figure that could be stale (a rate, limit, or legal reference), **flag it for manual verification before publish — do not go acquire it.**

## Load (existing material only)

- `brand/editorial-plan-2026.md` — the annual plan. Find this week's month and its scheduled items + relevance flags.
- `brand/quarterly-plan-Q*-2026.md` — the weekly slot detail (covers weeks 1-13).
- `brand/content-calendar.md` — Layer 1 static annual cycles, deadlines, and seasonal timing rules.
- `brand/voice-profile.md` and recent `outputs/drafts/content-batch-*` — to keep angles consistent and continue the sequential arc.

## The freshness pass (for THIS week's portion of the plan)

For each scheduled item in the week:

1. **Timing check** — does the angle still fit the week's actual publish dates and the calendar's static cycle? (A "before the June 15 estimated-tax deadline" item must publish in the window before it; a quarter-review item must fall after the quarter closes.) Adjust the framing, or move the item earlier/later within the plan, if the timing has drifted.
2. **Relevance refresh** — re-tune the working title, angle, and emphasis so they speak to what the surgeon is facing in that specific period (year-end vs. mid-year vs. tax season), using the calendar's seasonal context. Keep the topic; sharpen the moment.
3. **Continuity** — make sure the week's items still build on the prior week's batch and don't repeat a recently used angle.
4. **Flag, don't fetch** — if an item leans on a rate/limit/legal figure that could be stale, mark it "verify before publish" and name the figure. Do not research it here.

## Output

A **refreshed weekly content brief**: the (possibly adjusted) list of the week's scheduled items with refreshed titles, angles, and timing, plus any "verify before publish" flags. This brief is the handoff into `/generate-batch`. Propose any plan adjustments (reordering, retiming, reframing) as suggestions — update the plan docs only on the user's approval.
