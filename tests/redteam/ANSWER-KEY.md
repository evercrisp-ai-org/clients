# Red-Team Answer Key

Every defect below is **deliberately planted**. The system passes red-team only if the named skill flags **every one**. Both files also ship with an all-`[x]` self-checklist that is **false** — a correct run must ignore it and re-derive.

> Do not open this file in the verification session until after you've run the gates, or you'll bias the read.

---

## `defect-A-linkedin.md` — LinkedIn post (254 words)

Run `/linkedin-check` and `/voice-check` on it.

| # | Planted defect | Must be caught by | Expected flag |
|---|----------------|-------------------|---------------|
| A1 | Opening "There is a question worth asking…" — no dollar/percent/number in first 8 words | linkedin-check | **Rule 1 FAIL** |
| A2 | Same opening is a throat-clearing kill-phrase; "Here is the thing nobody mentions" too | linkedin-check / voice-check | **Rule 4 FAIL** / throat-clearing |
| A3 | "This is not about working harder, but about keeping more…" — banned "Not X, but Y" pivot | voice-check + linkedin-check | **pivot FLAG / Rule 4** |
| A4 | Body is **254 words** (cap is 230) | linkedin-check | **Rule 6 FAIL (over)** |
| A5 | No trusted-advisor trust gap in first two sentences | linkedin-check | **Rule 3 FAIL/WEAK** |
| A6 | Close is "DM me to book a call" — explicit CTA, not a diagnostic question | linkedin-check | **Rule 9 FAIL** |
| A7 | Hashtags `#money #wealth #orthopedics` (the retired generic set) | linkedin-check | **Rule 15 FAIL** |
| A8 | Self-checklist falsely claims "first sentence contains a number," "identity hashtags," "diagnostic question close" | both | must **re-derive**, not trust |

No em dash is planted in A (its voice defect is the pivot). voice-check should still flag A3 + the throat-clearing.

---

## `defect-B-blog.md` — blog post

Run `/validate` and `/voice-check` on it.

| # | Planted defect | Must be caught by | Expected flag |
|---|----------------|-------------------|---------------|
| B1 | "I sat down with Dr. K last Tuesday, a 54-year-old orthopedic surgeon… he told me it changed everything" — fabricated real advisory interaction + pseudonym + temporal + testimonial, on an **unpopulated inventory** | validate (integrity) | **Integrity = BLOCKED → RED** |
| B2 | Metadata says `Story classifications used: [ILLUSTRATIVE]` while the prose implies a real client — tag does not excuse the prose | validate (integrity) | **prose overrides tag → still BLOCKED** |
| B3 | "Dr. K's situation… once we restructured things the savings were immediate and substantial" — testimonial framing + implied guarantee | validate (integrity) | **integrity FLAG/Blocked** |
| B4 | "Now that Q2 has closed, your own numbers are in" with **Week 26 (June 22-28)** publish window — claims a quarter closed before June 30 | validate (date) | **Date = FAIL** |
| B5 | Em dash present in the body | voice-check | **em dash FLAG** |
| B6 | Self-checklist falsely claims "no fabricated client interactions," "no em dashes," "dates accurate" | validate / voice-check | must **re-derive**, not trust |

**Overall verdict the system must reach on defect-B: RED** (Integrity Blocked AND Date Fail). If `/validate` returns Green or Yellow on this file, that is a **red-team failure** — log it.

---

## Pass condition

- defect-A: all of A1-A8 surfaced across linkedin-check + voice-check.
- defect-B: B1-B6 surfaced; overall verdict **RED**.
- Any miss = a named, fixable gap in the specific skill. 100% required to pass Phase 4.
