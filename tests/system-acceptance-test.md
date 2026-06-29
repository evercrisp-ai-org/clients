# Capable Wealth — System Acceptance Test

> Purpose: verify the whole harness end to end — that it produces correct, on-brand, compliant, useful content **at volume**, and that the gates actually **catch defects**. A "did it run" demo is not this. Passing this test is the green light for Jared to rely on the system.

## How to read this

The test has five phases. The first three run the system on a real scenario. **Phase 4 is the one that actually proves quality** — it feeds the gates known-bad content and checks they catch every planted defect. Phase 5 is the human "would I publish this" call.

Run it inside the **Capable Wealth Content System** project in Cowork. Use **two separate sessions**:
- **Production session** — Phases 1-2.
- **Verification session (fresh chat)** — Phases 3-4. Fresh matters: the verifier must not "remember" writing the content, or it will rubber-stamp its own work.

---

## The scenario — "The Mid-Year Push"

It's late June 2026. Q2 closes June 30, the June 15 estimated-tax deadline just passed, and orthopedic productivity/RVU benchmarks have shifted in a way that's moving practice valuations (the topic Jared already started in week 21). Jared wants to ride the half-year window: produce the next **three weeks of content (weeks 22-24)** in one batch, hand it to his VA to schedule, and walk into H2 ahead.

The constraints that make this a real test:
- He's an RIA with an **unpopulated experience inventory** — every client example must be `[ILLUSTRATIVE]`, zero implied real relationships. One compliance slip is a real problem.
- Three weeks at once means the **cross-week rotation and opening-line variation** rules get stressed.
- Weeks 22-24 are **past week 13**, so the system must fall back to the editorial plan (by month) and continue the arc from week 21.

This mirrors exactly how a solo advisor actually batches content: a few weeks at a time, around a topical hook, needing compliance + voice consistency without re-reading 40 pages of brand docs each time.

---

## Phase 1 — Plan freshness (`research-scan`)

**Run:**
```
/research-scan weeks 22-24
```

**Pass criteria** (check each):
- [ ] It refreshes the **existing** scheduled items for weeks 22-24 — it does **not** invent new topics or claim it searched the web.
- [ ] It pulls the theme from the **editorial plan** (weeks >13 aren't in the quarterly plan) and continues the arc from week 21.
- [ ] Timing is re-tuned for the **late-June / H2** moment (e.g. mid-year review framing, not April tax-season framing).
- [ ] Any rate/limit/legal figure it relies on is **flagged "verify before publish,"** not asserted as freshly researched.
- [ ] Output is a usable weekly brief that hands into `generate-batch`.

---

## Phase 2 — Production (`generate-batch`, multi-week)

**Run:**
```
/generate-batch weeks 22-24
```

**Pass criteria — volume & structure** (per week, ×3):
- [ ] Exactly **10 core pieces** + 2-5 clips: 1 blog, 1 podcast, 3 LinkedIn, 5 Facebook, clips, + native-video and (optional) carousel.
- [ ] **File naming** correct: `week-N-{type}-{slug}.md`.
- [ ] Every file uses the **Standard Draft File Format**: Title → Post Metadata (incl. `Story classifications used`) → Visual Assets (9-point brief) → [Clip Map for podcast] → Content → Quality Checklist.
- [ ] Podcast files include the **Short-Form Clips** checklist; LinkedIn files include the **Section 6** checklist.
- [ ] All three weeks land in **one folder**, dated to the batch's first Monday; **Excel summary** regenerated.

**Pass criteria — cross-week rules (the hard part):**
- [ ] No banned opening template used more than once across the whole batch.
- [ ] First-slot opening device differs across consecutive weeks.
- [ ] Text-on-block card background colors rotate; **no two share a color** in the batch.
- [ ] Conceptual-photo subjects don't repeat back-to-back across weeks; no archetype in >2 photos.
- [ ] **Max 1 text-on-block card per platform per week.**

**Pass criteria — gates ran inline:**
- [ ] The run reports gate results (Green/Clean) and lists any violations it **caught and fixed** during the pass (em dashes, pivots, etc.). A run that reports zero issues across 30+ pieces is itself suspicious — spot-check.

---

## Phase 3 — Independent re-grade (FRESH session)

The point: does the system catch its *own* misses when it isn't the author? Open a **new chat** and run the gates on the Phase-2 output.

**Run:**
```
/validate outputs/drafts/content-batch-<date>/
```
```
/voice-check outputs/drafts/content-batch-<date>/week-22-blog-<slug>.md
```
```
/linkedin-check outputs/drafts/content-batch-<date>/week-22-linkedin-1.md
```
(repeat linkedin-check for linkedin-2 and -3)

**Pass criteria:**
- [ ] `validate` returns a per-piece Green/Yellow/Red verdict + the §13 checklist, and **re-derives** rather than trusting each draft's own `[x]` marks.
- [ ] Any piece the verifier marks **Yellow/Red is a real finding** — investigate it. (Generation shipping something the fresh verifier flags is exactly the kind of gap this test exists to surface.)
- [ ] `voice-check` confirms no em dashes, no pivots, correct sign-off, surgeon-specificity.
- [ ] `linkedin-check` confirms each LI post: number in first 8 words, 180-230 words, loss frame, diagnostic-question close, identity hashtags.

> Record any disagreement between what generation said and what the fresh verifier says. Zero disagreements is a good sign; disagreements are findings, not failures of the test.

---

## Phase 4 — Red-team: do the gates catch planted defects? (the real quality test)

Happy-path content tells you little. This phase feeds the gates content with **known, deliberate violations** and checks every one is caught. The defect files and the answer key are in `tests/redteam/`.

**Run, in the fresh session:**
```
/linkedin-check tests/redteam/defect-A-linkedin.md
```
```
/validate tests/redteam/defect-B-blog.md
```
```
/voice-check tests/redteam/defect-A-linkedin.md
```
```
/voice-check tests/redteam/defect-B-blog.md
```

Then open `tests/redteam/ANSWER-KEY.md` and confirm **every** planted defect was caught.

**Pass criteria — this is a hard gate:**
- [ ] **100% of planted defects caught.** Every item in the answer key is flagged by the skill that should flag it.
- [ ] In particular: the **fabricated real-client interaction** in defect-B is marked **Integrity = Blocked → RED** (not waved through because the metadata says `[ILLUSTRATIVE]`).
- [ ] The **"now that Q2 has closed"** line in defect-B, with a pre-June-30 publish date, is marked **Date = Fail**.
- [ ] The over-230-word LinkedIn post with no opening number and generic hashtags fails the right `linkedin-check` rules.
- [ ] Em dashes and the "Not X, but Y" pivot are caught by `voice-check`.

If any planted defect slips through, **the system fails red-team** — log which skill missed it; that's a concrete fix, not a vibe.

---

## Phase 5 — Business acceptance (would Jared publish this?)

Pure human judgment on the Phase-2 output. Read the week-22 blog and the three LinkedIn posts as if you were a surgeon.

- [ ] **Voice:** sounds like Jared (warm, diagnostician, contrarian), not generic AI finance content.
- [ ] **Audience:** could only have been written for orthopedic surgeons; numbers at $700K-$2M scale.
- [ ] **Value:** a surgeon would forward it to a colleague; leaves them informed, not anxious.
- [ ] **Accuracy:** no figure you'd be embarrassed to publish; "verify before publish" flags are honored.
- [ ] **Ship test:** you'd let this go out under Jared's name with light edits, not a rewrite.

---

## Scorecard

| Phase | What it proves | Result |
|-------|----------------|--------|
| 1 — Freshness | Plan refresh works without inventing research | ☐ Pass ☐ Fail |
| 2 — Production | Correct, compliant batch at volume + cross-week rules | ☐ Pass ☐ Fail |
| 3 — Independent re-grade | Gates catch their own work's misses | ☐ Pass ☐ Fail |
| 4 — Red-team | **Gates catch 100% of planted defects** | ☐ Pass ☐ Fail |
| 5 — Business acceptance | Jared would actually publish it | ☐ Pass ☐ Fail |

**Overall pass = all five phases pass, with Phase 4 at 100%.** Anything less is a documented gap with a named owner (which skill, which rule).

---

## Sign-off

- Tested by: ______________  Date: __________
- Batch under test: `outputs/drafts/content-batch-__________/`
- Findings / gaps: ______________
- Verdict: ☐ Ship  ☐ Fix and re-test
