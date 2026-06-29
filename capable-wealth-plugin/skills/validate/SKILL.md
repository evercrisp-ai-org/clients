---
name: validate
description: Gate a Capable Wealth content draft (or a whole batch folder) through all three enforcement rules at once — content integrity, date alignment, and relevance — and return a per-piece verdict of Green / Yellow / Red plus the full Quality Checklist. Use when the user asks to validate, check, gate, QA, or review a draft / batch for compliance before publishing.
---

# Validate

Run a draft (or every `.md` draft in a batch folder) through the three Capable Wealth enforcement rules simultaneously and return a gated verdict. This is the final quality gate before content publishes.

## Input

A path to a draft file, a path to a `content-batch-*` folder (validate every piece), or pasted content. If given a folder, validate each file and produce a summary table at the end.

## Load first

- `.cursor/rules/content-integrity.mdc`
- `.cursor/rules/content-date-alignment.mdc`
- `brand/content-recipe.md` §5 (Research & Relevance Filter, the Green/Yellow/Red definitions) and §13 (Quality Checklist)
- `brand/content-calendar.md` Layer 1 (deadlines). For the week → date mapping, use the draft's own Post Metadata `Week:` field as the publish window of record (e.g. "Week 18 (June 22-28)"). The quarterly plans (`brand/quarterly-plan-Q*-2026.md`) only cover Weeks 1-13 (Mar-May); for later weeks the source is `brand/editorial-plan-2026.md`, organized by month. **Week numbers here are an internal sequential index, NOT ISO week numbers — never infer a date from a standard-calendar week number.**
- `brand/experience-inventory.md` (to trace `[REAL-ANONYMIZED]` claims; if unpopulated, any real-client framing is a fail)

**Trust nothing the draft asserts about itself.** Ignore the draft's embedded Quality Checklist `[x]` marks and re-derive every item independently. These self-checklists are frequently false (drafts have shipped claiming a clinical metaphor or an integrity pass the prose does not support).

## Three checks per piece

### 1. Content Integrity (→ Clean / Flagged / Blocked)
- Is every client story classified `[REAL-ANONYMIZED]`, `[ILLUSTRATIVE]`, or `[GENERAL-PRINCIPLE]`, and listed in Post Metadata?
- Do `[REAL-ANONYMIZED]` stories trace to a specific entry in experience-inventory §4? (Unpopulated inventory → must be `[ILLUSTRATIVE]`.)
- **Read the actual body prose against the banned-framing list — a correct `[ILLUSTRATIVE]` tag in metadata does NOT excuse real-relationship language in the text.** "I was talking through X with a surgeon," "I sat down with," "a client told me," a direct quote attributed to a real client, or a specific temporal reference ("last Tuesday") are violations regardless of the tag.
- Do `[ILLUSTRATIVE]` examples use approved framing ("Consider a surgeon earning…")?
- Any fabricated temporal references, relationship-duration claims, experience-pattern claims, implied guarantees, or testimonial framing? Quote the offending line.

**Flagged vs. Blocked:** Mark **Blocked** (→ RED) when the prose fabricates a real client interaction, names/quotes an implied real person, or makes an experience-pattern claim the unpopulated inventory cannot support. Mark **Flagged** (→ YELLOW) when framing merely needs softening but no fabricated relationship is asserted.

### 2. Date Alignment (pass / fail)
- Does any title/body claim a quarter has closed before its close date (Q1 3/31, Q2 6/30, Q3 9/30, Q4 12/31)?
- Are deadline references ("next week") accurate for the publish week? Any post-event framing used before the event? Any "this week"/"next week" that conflicts with the publish date?
- Cross-reference the piece's publish date from the quarterly plan.

### 3. Relevance (→ Green / Yellow / Red)
- Are all facts, figures, tax/contribution limits, and legal references current as of the publish date? **If a rate/limit/legal fact cannot be verified from the repo, mark Relevance=Yellow and flag the specific figure for manual verification before publish — never mark Green on an unverifiable rate-sensitive figure, even if the draft's own checklist says Green.**
- Is the timing right vs. the annual calendar (tax content 4-6 weeks pre-deadline, year-end content Sept-Oct, etc.)?
- Any conflicting current event that would make it tone-deaf?

## Output per piece

```
FILE: week-N-linkedin-1.md
Integrity:  Clean | Flagged | Blocked   — <one line; quote any offending text>
Date:       Pass | Fail                 — <one line>
Relevance:  Green | Yellow | Red        — <one line>
VERDICT:    GREEN (publish) | YELLOW (revise: <what>) | RED (hold: <why>)
```

Then render the full §13 Quality Checklist (Voice Alignment, Audience Specificity, Relevance Validation, Pull Signal Design, Visual Assets, Content Integrity, + Short-Form Clips for podcasts) with each item checked or flagged. For LinkedIn posts, additionally run the Section 6 checklist from `rules/linkedin-content-creation-guidelines.md` (the recipe §13 checklist does not contain it).

A piece is **GREEN** only if Integrity=Clean, Date=Pass, Relevance=Green. Any Blocked or Fail → RED. Otherwise YELLOW with the specific fix. For a folder, end with a summary table: file | verdict | top issue.

Do not edit the files — report only, unless the user explicitly asks you to fix.
