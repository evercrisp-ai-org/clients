---
name: generate-batch
description: Produce a full week's Capable Wealth content batch (blog, podcast script, 3 LinkedIn posts, 5 Facebook posts, 2-5 clips, optional LinkedIn native video + carousel) from the quarterly plan. Loads all brand context, enforces every production rule during drafting, runs the LinkedIn/image/validation gates, writes files with correct naming, exports the Excel summary, and posts a review summary to Slack. Use when the user asks to generate, draft, or produce a content batch / a week of content (e.g. "generate-batch week-21", "draft week 22").
---

# Generate Batch

You are producing one week of Capable Wealth content for Jared Paul, CFP — a financial advisor serving orthopedic surgeons (ages 45-65, $700K-$2M income) approaching practice transition or retirement. This is the engine skill. Everything you produce must sound like Jared and pass every brand rule.

## Input

The user gives you a week (e.g. `week-21`, `21`, or a date) or a range of weeks. Optionally a theme override. If no week is given, ask which week, or infer the next un-produced week from the most recent folder in `outputs/drafts/`.

**A batch may span multiple weeks** (the real batches do — e.g. weeks 18-20 live in one folder). If the user names a range, produce each week in turn while maintaining **ONE running ledger across the whole batch**. The ledger is what makes the cross-week rules enforceable; carry it through every drafting and image-brief step:
- (a) banned opening templates — max 1 use total across the entire batch
- (b) opening rhetorical devices — distinct per platform per week, AND the first-slot device must differ across consecutive weeks
- (c) text-on-block card background colors (rotate Blue → Charcoal → Off-White)
- (d) conceptual-photo subjects and person archetypes (no subject back-to-back across weeks; no archetype in >2 photos per batch)
- (e) infographic layouts

## Step 1 — Load context (always, before writing anything)

Read these in full. They are the single source of truth:

- `brand/voice-profile.md` — WHO Jared is. Study Structural DNA (§4), Rhetorical Toolkit (§5), Anti-Patterns (§7). **Hard rules: no em dashes; never the "It's not X, it's Y" pivot.**
- `brand/content-recipe.md` — Content Architecture Templates (§7) for each format; the 9-point image standard (§10); Standard Draft File Format (§12); Quality Checklist (§13).
- `brand/quarterly-plan-Q2-2026.md` (or the current quarter's plan) — the authoritative week → topic → channel → date mapping. **This tells you the theme, the anchor angle, the math example, and the LinkedIn hooks for this week.** The quarterly plans only cover **Weeks 1-13 (Mar-May)**. For any later week, fall back to `brand/editorial-plan-2026.md` (organized by month — June = Month 4) for the theme, then derive the week's anchor angle from the prior week's batch to continue the sequential arc. If neither plan covers the week, ask the user before drafting.
- `brand/content-calendar.md` — Layer 1 for timing/deadline alignment.
- `brand/brand_config.json` — palette, fonts, and `voice_and_tone` (the banned-language list is nested at `voice_and_tone.language_to_avoid`).
- `rules/linkedin-content-creation-guidelines.md` — the full LinkedIn rulebook (Section 6 checklist is the gate).
- `brand/experience-inventory.md` — read it. **If unpopulated, every client story defaults to `[ILLUSTRATIVE]` with approved framing — no real-client implications.**

Also load the three enforcement rules so you apply them as you write, not after:
`.cursor/rules/content-production-batch.mdc`, `.cursor/rules/content-integrity.mdc`, `.cursor/rules/content-date-alignment.mdc`.

## Step 2 — Resolve the week to dates

Map the week number to its Monday-start date range and publication dates (from the quarterly plan, or the editorial plan for weeks >13). **Week numbers are an internal sequential index, NOT ISO week numbers.** Record the resolved range in each file's `Week:` metadata (e.g. "Week 18 (June 22-28)"). LinkedIn posts publish **Tuesday (hook) / Wednesday (story) / Thursday (mechanism)** only. Confirm no piece will reference an event, deadline, or quarter-close that hasn't occurred by its publish date (date-alignment rule).

## Step 3 — Produce exactly 10 core pieces + 2-5 clips, per week

Per `content-production-batch.mdc`:

| File | Format |
|---|---|
| `week-N-blog-{slug}.md` | 800-1,200 word anchor, six-step DNA, signs "Capably Yours, Jared" |
| `week-N-podcast-{slug}.md` | Solo video podcast script (15-25 min; audio must stand alone from the video) with COLD OPEN → CONTEXT → 3-5 MAIN SEGMENTS (mark `[CLIP-CANDIDATE]`) → TAKEAWAY → PHILOSOPHICAL CLOSE, plus a Clip Extraction Map |
| `week-N-clip-1..5.md` | 2-5 standalone clips derived from the podcast's clip map (only where a segment truly stands alone; never force the count) |
| `week-N-linkedin-1..3.md` | Tue/Wed/Thu, 180-230 words, one idea each |
| `week-N-linkedin-native-video.md` | ~60s native video brief from podcast material (recommended) |
| `week-N-linkedin-carousel.md` | Carousel outline for the mechanism post (optional) |
| `week-N-facebook-1..5.md` | 100-200 words, warmer/personal tone, no sign-off |

**Non-negotiable: every week gets all 10 core pieces + 2-5 clips, regardless of "primary channel."** A "primary channel" (or "LinkedIn-primary / blog-primary") designation in the plan or the research-scan brief sets *emphasis* only — which piece leads the week and gets the most promotion. It NEVER reduces the mandatory set. Even on a "LinkedIn-primary" week, you still produce the blog, the podcast, the 2-5 clips, and the 5 Facebook posts. The only piece whose count flexes is clips (2-5, by natural standalone value); blog, podcast, 3 LinkedIn, and 5 Facebook are always present.

Every file follows the Standard Draft File Format (recipe §12):

1. **Title** (H1)
2. **Post Metadata** — `Type`, `Week` (resolved date range), `Theme`, `Quarterly plan reference` (cite the source exactly, e.g. "editorial-plan-2026.md, Month 4 (June); extended as Week 18 after content-batch-YYYY-MM-DD Week 17"), `Strategic context`, and `Story classifications used`.
3. **Visual Assets** — 9-point brief(s), delegated to Step 5.
4. **Clip Extraction Map** — podcast files only.
5. **Content**.
6. **Quality Checklist** (recipe §13) — and the **conditional sections**: podcast files MUST include the Short-Form Clips checklist; LinkedIn text posts MUST include the LinkedIn-guidelines (Section 6) checklist block. Write the resolved **Relevance Score (Green/Yellow/Red)** into the Relevance Validation section of every file.

## Step 4 — Enforce these while drafting (not after)

- **LinkedIn:** every post obeys the 15 rules in `linkedin-content-creation-guidelines.md`. First 8 words contain a dollar/percent/number; mental-math gap; trusted-advisor trust gap in first 2 sentences; loss frame not gain frame; diagnostic-question close (no CTA); `#orthopedicsurgeon #orthopedicsurgery #physicianfinance`; no throat-clearing; no acronym opens.
- **Opening-line variation:** no rhetorical device repeats on the same platform in the same week; the first-slot device differs across consecutive weeks; banned templates ("Most X don't Y…", "Here's what nobody tells you…", "The math is simple:", "I talk to surgeons every…") max once per batch. Also vary sentence structure: don't open 3+ posts in the same week with sentences under 8 words; at least 2 posts per week should open with 15+ word sentences. Track all of this in the running ledger.
- **Image-type rotation:** max 1 text-on-block card per platform per week; ≥2 conceptual photos and ≥1 infographic per platform; rotate stat-card background colors and photo subjects across the batch (no repeats back-to-back). Do not hand-write the prompts here — Step 5 delegates them.
- **Integrity:** classify every story `[REAL-ANONYMIZED]` / `[ILLUSTRATIVE]` / `[GENERAL-PRINCIPLE]` and list them in Post Metadata. Inventory unpopulated → all `[ILLUSTRATIVE]`.
- **Voice:** no em dashes anywhere; no "not X, but Y" pivots; conversational-professional; diagnostician not educator.

## Step 5 — Run the gates (delegate to the other skills)

Apply these to the produced content before finalizing:
1. **image-brief** — generate the 9-point AI image prompt(s) for every asset, with batch-wide rotation awareness.
2. **linkedin-check** — run the 17-item checklist on each LinkedIn text post; fix any failure before finalizing.
3. **voice-check** — run on **EVERY produced piece**: the blog, the podcast, all 3 LinkedIn posts, all 5 Facebook posts, every clip, the native video, and the carousel. This is the brand-wide voice gate and it runs across all content exactly as `linkedin-check` runs across the LinkedIn posts. It must catch **em dashes** (`—`) and the **"not X, but Y" / "it's not X, it's Y"** pivots in any piece, plus the three voice gates. Fix every flagged line before finalizing.
4. **validate** — run content-integrity + date-alignment + relevance on every piece; only `Green` (or justified `Yellow`) proceeds. Record the result in each file's Quality Checklist.

**Check the literal text, not your memory.** Before finalizing each file, actually search its body for the em-dash character `—` and for `not … but` / `not … it's` pivots — any hit is a defect to fix, not to wave through. The Quality Checklist you write must reflect this real re-derivation: never mark "No em dashes: PASS" on a body that still contains one.

If you have the Agent tool available, you may fan these out in parallel (one agent per piece) for speed. Otherwise run them inline.

## Step 6 — Write, export, notify

1. Write all files to `outputs/drafts/content-batch-{YYYY-MM-DD}/`, dated to the **batch's first week's Monday**. All weeks in a multi-week batch go in the SAME folder — do not fragment weeks into separate folders.
2. **Completeness check (before reporting done):** for every week in the batch, confirm on disk that all mandatory files exist — `week-N-blog-*`, `week-N-podcast-*`, `week-N-clip-1..N` (≥2), `week-N-linkedin-1/2/3`, `week-N-facebook-1..5`. If any week is short (e.g. a podcast or clips missing because the week was treated as "channel-primary"), produce the missing pieces now. Report the per-week file counts so a shortfall is visible.
3. Regenerate the Excel summary: `python3 src/export_content_batch.py outputs/drafts/content-batch-{YYYY-MM-DD}/`. This produces `content-batch-summary-{YYYYMMDD}.xlsx` in that folder. It is the primary handoff artifact and must always match the markdown — re-run it after ANY later edit to any draft.
4. If the Slack connector is connected, post a summary to `#content-review`: week number, theme, file count by channel, any `Yellow` flags that need Jared's eye, and the folder path. If Slack is not connected, print the same summary in chat and note it wasn't posted.

## Output

End with a concise report: week, theme, files created (by channel), validation results (Green/Yellow/Red counts), any rule conflicts you had to resolve, and the next action for Jared (review in Slack / the folder). Do not dump full file contents into chat — they are on disk.
