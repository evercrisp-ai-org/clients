---
name: linkedin-check
description: Run a Capable Wealth LinkedIn post through the 17-item performance-tested checklist (Rules 1-18, cadence rules excluded; Section 6 of the LinkedIn guidelines) and return pass/fail per item, line-level fixes, word count, and the opening rhetorical-device classification. Use when the user asks to check, score, or QA a LinkedIn post, or it is invoked inside generate-batch for each LinkedIn draft.
---

# LinkedIn Check

Gate a single LinkedIn post against the performance-tested rulebook. These rules come from a 50-post, 3-month engagement analysis (Jan-Apr 2026) where 83% of impressions came from 5 posts — the difference was structural, not topical. Enforce them strictly.

## Input

A path to a `week-N-linkedin-*.md` draft, or pasted post text.

**Format branch:** If the file is `*-linkedin-carousel.md` or `*-linkedin-native-video.md`, this is NOT a text post — skip Rules 1, 2, and 6 (word cap), check slide/clip structure instead, and label the output "non-text format — text-post rules N/A." The 17-item check below applies only to the three `week-N-linkedin-1/2/3.md` text posts.

**Word-count method:** The post body is the prose between the final `---` separator and the hashtag line. Exclude the H1 title, any duplicated title line, metadata, the visual brief, hashtags, and the Quality Checklist. If no body is clearly delimited (e.g. pasted text), state your assumed span before counting.

**Trust nothing the draft asserts about itself.** Ignore the draft's embedded Quality Checklist `[x]` marks and re-derive every item — these self-checks have shipped false (e.g. claiming a clinical metaphor the prose lacks).

## Load first

`rules/linkedin-content-creation-guidelines.md` (especially Section 6, the production checklist) and `brand_config.json` → `voice_and_tone.language_to_avoid` (nested key, not top-level).

## Run every item (Section 6)

**Pre-write / theme**
1. Theme passes the "silent loss" test — framable as money the surgeon is losing without knowing it (Rule 13).
2. No recap/summary/meta post (Rule 11).

**Hook (Rules 1-5)**
3. First sentence contains a dollar figure, percentage, or specific number in the first ~8 words (Rule 1). **Non-negotiable — if it fails, this is the #1 fix.**
4. Opening creates a mental-math gap: big number in → smaller number out → reader calculates (Rule 2).
5. A trusted advisor (CPA, financial advisor, practice manager) is challenged or a trust gap is implied in the first two sentences (Rule 3). **Rubric (this is the most consequential and most subjective item): PASS = an advisor is named or implied to have missed something within the first two sentences. WEAK (flag, don't fail) = advisor named but framed as a neutral habit, not a miss. FAIL = no advisor or trust gap at all.**
6. No throat-clearing in the first three lines — kill "There is a question worth asking", "Let me put that in perspective", "Here's why that matters", "Most people don't realize" (Rule 4).
7. No "Not X, but Y" / "Not because X, because Y" pivot anywhere (Rule 4 / brand voice).
8. No acronym in the opening sentence — lead with pocket impact, then name the policy (Rule 5).

**Structure (Rules 6-9)**
9. Body is **180-230 words** (hard cap 230). Report the exact count (Rule 6).
10. Exactly one idea: one number, one story, one takeaway (Rule 7).
11. Primary frame is loss/cost, not gain/benefit (Rule 8).
12. Closes with a diagnostic question the reader can only answer by auditing themselves — no "DM me / book a call / link in comments" (Rule 9).

**Voice (Rules 16-18)**
13. Diagnostician, not educator (Rule 16).
14. Clinical metaphor where it lands naturally — tax return as diagnostic report, structure as treatment plan, etc. (Rule 17). **If the post is at/under ~200 words and a metaphor would only pad it, mark N/A, not ✗. Never fail a post solely for lacking a metaphor.**
15. Specific story details (income, age, scenario) over "most surgeons" generalizations (Rule 18).

**Tags / format**
16. Uses `#orthopedicsurgeon #orthopedicsurgery #physicianfinance` — not the generic `#money #wealth #orthopedics` (Rule 15).
17. No external links in the post body; native video uploaded natively, not as a YouTube link (Rule 12).

## Output

```
WORD COUNT: N words   (target 180-230 — PASS/OVER/UNDER)
OPENING DEVICE: <Provocative stat | Direct question | Scenario | Contrarian assertion | Anecdote lead | Simple declarative | If/when conditional>

RULE CHECK
✓ Rule 1  Number in first 8 words
✗ Rule 3  Trust gap — <quote the opening; explain what's missing>
... (all items)

VERDICT: PASS (ready) | NEEDS FIXES (N)
TOP FIXES (ranked):
1. <specific rewrite suggestion with example>
```

When invoked from generate-batch, also return the opening device so the batch can track within-week variation (no two LinkedIn posts the same week share a device). If pasted standalone, offer to apply the fixes if the user wants.
