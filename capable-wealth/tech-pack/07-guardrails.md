# Guardrail Callouts

A guardrail is a constraint the harness enforces automatically so that bad output cannot pass through, regardless of the prompt. This system has two layers of guardrails: **always-on** (apply to every task, even a plain-English prompt that names no skill) and **gate-enforced** (run as explicit checks during `generate-batch` or on demand).

---

## Layer 1: Always-on guardrails

These live in the Cowork Project Instructions and the `.cursor/rules/*.mdc` files. They hold for every interaction in the workspace.

### G1. No em dashes
The `—` character is banned everywhere. Use commas, parentheses, periods, semicolons, colons. Enforced by a literal text scan during generation and by `voice-check`. **Hard fail.**

### G2. No pivot constructions
No "It's not X, it's Y," "Not X, but Y," "not because X, because Y," or "You don't have an X problem, you have a Y problem." Reframes must emerge in the flow of the argument. Enforced by literal `not ... but` / `not ... it's` scan and by `voice-check`. **Hard fail.**

### G3. Story integrity (the most important compliance guardrail)
The experience inventory is unpopulated, so **every client story defaults to `[ILLUSTRATIVE]`** with approved framing ("Consider a surgeon earning..."). Never imply a real advisory relationship ("I sat down with," "a client told me," "last Tuesday," real quotes or pseudonyms). Every story must be classified `[REAL-ANONYMIZED]` / `[ILLUSTRATIVE]` / `[GENERAL-PRINCIPLE]` and listed in Post Metadata. Enforced by `content-integrity.mdc` and `validate`. A fabricated real-client interaction is a **RED / Blocked** outcome.

### G4. Date honesty
Never reference a deadline, quarter-close, or event before it has occurred relative to the publish date. Quarter closes are hard stops (Q1 3/31, Q2 6/30, Q3 9/30, Q4 12/31). Deadline content publishes 2 to 4 weeks ahead. Week numbers are an internal sequential index, not ISO weeks. Enforced by `content-date-alignment.mdc` and `validate`. **Hard fail on any post-event framing used early.**

### G5. Audience lock
Every piece must be surgeon-specific (orthopedic surgeons, ages 45 to 65, $700K to $2M income). Use surgeon-level numbers and practice context. Never explain basics (do not define a 401(k)). Loss framing over gain framing. Diagnostician, not educator. Enforced by `voice-check` (Audience Specificity gate).

### G6. Brand palette and type lock
Visuals use only the six brand hex colors (#243A4B, #5F7483, #B08D57, #F6F7F5, #1E2428, #9AA3A8), Playfair Display + Inter, at a 60/30/10 ratio. No cartoons, clip art, generic stock, or clickbait. Enforced by `content-production-batch.mdc` and `image-brief`. **Any other color is a fail.**

### G7. Trust nothing a draft says about itself
Every quality check is re-derived from scratch. A draft's own `[x]` checklist marks are ignored, because drafts have shipped claiming false checks. Enforced by `validate`, `voice-check`, and `linkedin-check`, each of which re-checks independently.

### G8. Brand-doc change control
Brand source docs (voice profile, content recipe, content calendar, LinkedIn guidelines) change **only on Jared's explicit approval**. Edits are proposed as diffs and never applied silently. This is a human-approval guardrail, not an automatic one.

---

## Layer 2: Gate-enforced guardrails

These run as explicit checks. In `generate-batch` they run automatically and fixes are applied before finalizing; each can also be run standalone.

### G9. LinkedIn structural rules (`linkedin-check`)
17-item checklist derived from a 50-post, 3-month engagement analysis where 83% of impressions came from 5 posts. Non-negotiable items include: a dollar figure, percentage, or specific number in the first ~8 words; a trust-advisor gap in the first two sentences; loss framing not gain; a diagnostic-question close (no "DM me / book a call"); body of 180 to 230 words (hard cap 230); the exact hashtag set `#orthopedicsurgeon #orthopedicsurgery #physicianfinance`; no throat-clearing openers; no acronym in the opening sentence.

### G10. Voice fidelity (`voice-check`)
Three gates run on every piece: Voice Alignment (8 items), Audience Specificity (4 items), Pull Signal Design (4 items). Flags every off-voice line and proposes an in-voice rewrite. Catches G1 and G2 at the line level.

### G11. Production completeness and variety (`content-production-batch.mdc`)
Exactly 10 core pieces plus 2 to 5 clips per week, even on "channel-primary" weeks. Strict file-naming convention. Required file sections. Image-type variety (max 1 text-on-block per platform per week; minimum conceptual photos and infographics). Opening-line variation (banned templates capped at 1 per batch; no repeated rhetorical device on the same platform in a week). Excel summary must stay in sync with the markdown after any change.

### G12. Three-rule final gate (`validate`)
Content integrity + date alignment + relevance, returning Green / Yellow / Red per piece. A piece is Green only if Integrity is Clean AND Date is Pass AND Relevance is Green. Any Blocked or Fail is Red. Rate-sensitive figures that cannot be verified from the repo are marked Yellow, never Green.

---

## Guardrail summary table

| ID | Guardrail | Layer | Enforced by | Failure severity |
|---|---|---|---|---|
| G1 | No em dashes | Always-on | text scan + voice-check | Hard fail |
| G2 | No pivot constructions | Always-on | text scan + voice-check | Hard fail |
| G3 | Story integrity | Always-on | content-integrity.mdc + validate | RED / Blocked |
| G4 | Date honesty | Always-on | content-date-alignment.mdc + validate | Hard fail |
| G5 | Audience lock | Always-on | voice-check | Fail |
| G6 | Palette + type lock | Always-on | content-production-batch.mdc + image-brief | Fail |
| G7 | Trust nothing self-reported | Always-on | all gates | n/a (method) |
| G8 | Brand-doc change control | Always-on | human approval | Blocking |
| G9 | LinkedIn structural rules | Gate | linkedin-check | Needs-fixes |
| G10 | Voice fidelity | Gate | voice-check | Off-voice / rework |
| G11 | Production completeness + variety | Gate | content-production-batch.mdc | Fail |
| G12 | Three-rule final gate | Gate | validate | RED / YELLOW |
