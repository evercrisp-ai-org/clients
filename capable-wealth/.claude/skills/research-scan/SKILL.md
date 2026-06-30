---
name: research-scan
description: Weekly research and freshness pass for Capable Wealth. Takes the week's planned content items and researches the live web (and any source necessary) to confirm every fact, figure, rate, date, and angle is current, timely, and relevant for the publish window. Updates anything stale, cites sources, and flags rate/limit/legal facts for human confirmation. Use before generating a week's batch, or when the user asks to refresh, freshen, fact-check, or update the plan for a week.
---

# Research Scan: Weekly Research and Freshness Pass

Make the week's planned content fresh, timely, and relevant before it is generated. This skill takes the items already scheduled in the plan for a given week and researches the current real world to confirm nothing is outdated: tax figures and contribution limits for the publish year, recent law or IRS changes, market and economic context, seasonal timing, and any current event that changes how an orthopedic surgeon would read the piece. It updates stale items, records its sources, and flags anything that still needs human confirmation.

**This skill IS allowed to search the web and fetch sources.** It requires the Cowork project to have web access / search enabled. If web access is unavailable, fall back to the repo-only freshness pass and say clearly in the output that figures could not be verified live.

## Input

A week (e.g. `week-21`) or a date. If none is given, infer the next un-produced week (after the most recent batch folder).

## Load first (the plan being refreshed)

- `brand/editorial-plan-2026.md`, `brand/quarterly-plan-Q*-2026.md`, `brand/content-calendar.md` — the week's scheduled items, deadlines, and static seasonal cycles.
- `brand/voice-profile.md` and recent `outputs/drafts/content-batch-*` — to keep angles consistent and continue the sequential arc.

## The research pass (for THIS week's items)

For each scheduled item:

1. **Currency check (web).** Verify every fact, figure, tax rate, contribution/income limit, and legal reference is correct **as of the publish year and date**. Look specifically for anything that changed since the plan was written: new IRS/SSA limits, law or regulation changes, shifted deadlines.
2. **Timeliness and context (web).** Surface current events, market conditions, or news relevant to orthopedic surgeons approaching practice transition or retirement that would sharpen, or date, the angle. Is the moment still right? Is there a fresher hook?
3. **Relevance and continuity.** Re-tune the title, angle, and emphasis to the moment it publishes; confirm it builds on prior weeks and does not repeat a recently used angle.
4. **Update and cite.** Update the item with the current figure or angle, and record the source for every fetched fact: publisher, URL, and date accessed.
5. **New opportunity (recommend, do not replace).** If research surfaces a timely topic that strongly warrants a new or reordered piece, flag it as a recommendation for Jared's approval. Do not silently swap the plan.

## Sourcing and compliance rules (this is content for a CFP, so be strict)

- Prefer **primary, authoritative sources** (IRS, SSA, Treasury, official publications) over secondary blogs or aggregators.
- **Cite source and date** for every figure or claim you add or change.
- **Rate-sensitive and legal facts:** even after researching them, still **flag them "confirm before publish"** with the source attached. Web data can be stale or wrong, and a CFP's content has to be right. `validate` re-checks these too; this is belt and suspenders, by design.
- **Never fabricate** a figure or a source. If you cannot verify something, or sources conflict, say so and flag it rather than guessing.
- **Stay anchored to the plan.** New topics are proposals, not auto-changes. Plan-doc edits happen only on Jared's approval.

## Output

A refreshed weekly brief, ready to hand to `/generate-batch`:

- The (possibly adjusted) list of the week's items with updated titles, angles, and figures.
- A **Sources** list: each fetched figure or claim mapped to its source and date.
- **"Confirm before publish"** flags for every rate-sensitive or legal fact.
- Any **new-opportunity recommendations**, clearly marked as proposals.

Propose any plan-doc changes (reordering, retiming, reframing, new topics) as suggestions; apply them only on the user's approval.
