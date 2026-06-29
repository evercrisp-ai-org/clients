# Evals

This documents the evaluations used to assess each workflow: what is checked, the pass/fail criteria, and how to run them as a regression set (for example after a model change or a rule edit).

A note on terminology: in this harness, the **quality gates are the evals**. Each gate is a deterministic, criteria-based assessment with an explicit verdict. Unlike a free-form review, every item has a defined pass condition, and the gates re-derive every check from scratch rather than trusting the draft's self-report. That makes them repeatable: the same draft against the same rules yields the same verdict.

---

## Eval suite overview

| Eval | Run by | Unit assessed | Verdict scale | Item count |
|---|---|---|---|---|
| E1. Content Integrity | validate | each piece | Clean / Flagged / Blocked | rule-set |
| E2. Date Alignment | validate | each piece | Pass / Fail | rule-set |
| E3. Relevance | validate | each piece | Green / Yellow / Red | rule-set |
| E4. LinkedIn structural | linkedin-check | each LinkedIn post | Pass / Needs-fixes (N) | 17 items |
| E5. Voice fidelity | voice-check | each piece | On-voice / Drift / Off-voice | 16 items (8+4+4) |
| E6. Image rotation + spec | image-brief | each visual asset | conforms / fails | 9-point + rotation |
| E7. Batch completeness | generate-batch | whole batch | complete / short | volume rules |
| E8. Literal AI-tell scan | generate-batch | each piece | clean / hit | 2 patterns |

---

## E1. Content Integrity eval (`validate`)
**Assesses:** whether any client story fabricates a real advisory relationship.
**Criteria (each must hold):**
- Every story is classified `[REAL-ANONYMIZED]` / `[ILLUSTRATIVE]` / `[GENERAL-PRINCIPLE]` and listed in Post Metadata.
- `[REAL-ANONYMIZED]` traces to a specific entry in `experience-inventory.md` Section 4 (currently unpopulated, so any such claim fails).
- `[ILLUSTRATIVE]` uses approved framing ("Consider a surgeon earning..."), not real-advisory language.
- Body prose (not just the tag) contains no fabricated interaction, real-person quote, or specific temporal reference.
**Verdict:** Clean (pass) / Flagged (soften) / Blocked (fail -> RED).

## E2. Date Alignment eval (`validate`)
**Assesses:** temporal honesty against the publish date.
**Criteria:** no quarter claimed closed before its close date; deadline references accurate for the publish week; no post-event framing before the event; relative date references ("this week / next week") correct for the publish window.
**Verdict:** Pass / Fail. Any violation is Fail -> RED.

## E3. Relevance eval (`validate`)
**Assesses:** currency and timeliness.
**Criteria:** all facts, figures, tax/contribution limits, and legal references current as of publish date; timing correct vs the annual calendar; no conflicting current event. Any rate/limit/legal fact not verifiable from the repo is marked Yellow, never Green.
**Verdict:** Green (publish) / Yellow (revise) / Red (hold).

> A piece is **GREEN overall** only if E1 Clean AND E2 Pass AND E3 Green. Any Blocked or Fail makes it RED. Otherwise YELLOW.

## E4. LinkedIn structural eval (`linkedin-check`)
**Assesses:** a LinkedIn text post against the 17-item, performance-tested rulebook (derived from a 50-post, 3-month analysis where 83% of impressions came from 5 posts).
**Headline criteria:** number in first ~8 words (non-negotiable); mental-math gap; trust-advisor gap in first two sentences; no throat-clearing; no pivot constructions; no acronym open; body 180 to 230 words (hard cap); one idea; loss frame; diagnostic-question close; correct hashtag set; no external links in body.
**Verdict:** Pass (ready) / Needs-fixes (N), with ranked fixes. Also classifies the opening rhetorical device.

## E5. Voice fidelity eval (`voice-check`)
**Assesses:** every piece against Jared's voice across three gates.
**Criteria:** Voice Alignment (8 items, including the hard fails for em dashes and pivots), Audience Specificity (4 items, surgeon-specific + surgeon-level numbers), Pull Signal Design (4 items, forward-able value + non-anxious close).
**Verdict:** On-voice / Minor drift (N fixes) / Off-voice (rework), with a quoted offending line and an in-voice rewrite for every miss.

## E6. Image rotation + spec eval (`image-brief`)
**Assesses:** each visual asset prompt.
**Criteria:** all 9 prompt points specified; exclusive brand palette + 60/30/10; correct platform dimensions; rotation rules satisfied (max 1 text-on-block per platform per week, color rotation Blue -> Charcoal -> Off-White, photo-subject uniqueness, infographic-layout uniqueness, cross-platform dedup of the same stat).
**Verdict:** conforms / fails per asset, with a rotation ledger for the batch.

## E7. Batch completeness eval (`generate-batch`)
**Assesses:** the whole batch on disk before reporting done.
**Criteria:** every week has blog + podcast + at least 2 clips + 3 LinkedIn + 5 Facebook, with correct file naming, even on "channel-primary" weeks; Excel summary regenerated and in sync.
**Verdict:** complete / short (produce missing pieces immediately).

## E8. Literal AI-tell scan (`generate-batch`)
**Assesses:** each finalized file with a literal text search, independent of any model judgment.
**Criteria:** zero occurrences of the em-dash character `—`; zero `not ... but` / `not ... it's` pivot constructions.
**Verdict:** clean / hit (any hit is a defect to fix before finalizing).

---

## Running the suite as a regression set

The eval suite is the regression test for the harness. Re-run it whenever something foundational changes.

**When to run:**
- After any **model change** (the primary trigger; see `02-model-selected.md` and risk R10).
- After editing any **brand doc or rule** (voice profile, content recipe, the `.cursor/rules/*.mdc`).
- After a **skill change**.

**How to run:**
1. Keep a small **fixed sample set** of representative drafts (a known-good batch and a known-bad batch with seeded violations: an em dash, a fabricated client line, a stale date reference, an over-length LinkedIn post).
2. Run `/validate`, `/voice-check`, `/linkedin-check`, and `/image-brief` against the sample set.
3. Confirm the known-good batch passes clean and the seeded violations are each caught with the correct verdict (the bad batch is the more important test, because it proves the gates still bite).
4. Record results in the log below.

**What "passing" means:** the gates catch every seeded violation in the bad batch and raise no false positives on the good batch. A model or rule change that lets a seeded violation through is a regression.

---

## Eval run log

| Date | Trigger (model change / rule edit / routine) | Good-batch result | Bad-batch: violations caught | Regressions | Notes |
|---|---|---|---|---|---|
| _pending_ | baseline on Sonnet 4.6 | | | | establish baseline |

> Recommended next step: build the small seeded "bad batch" sample once, so E1 to E8 have a permanent regression target. Until that exists, the evals run on live content only, which tests production but not the gates' own sensitivity.
