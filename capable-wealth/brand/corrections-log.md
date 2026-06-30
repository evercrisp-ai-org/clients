# Corrections Log

This is the behavioral log for the recursive learning loop. It records the **revision requests Jared makes in Cowork** so the system can learn his preferences over time.

## How it works

- **Capture:** Whenever Jared asks to revise, retone, cut, restructure, or rephrase an already-generated piece, the assistant appends one entry here **before applying the change**, and briefly notes that it logged the request. This is an always-on rule (see `COWORK_PROJECT_INSTRUCTIONS.md`).
- **Synthesize:** The weekly `/retro` skill reads this log, clusters entries by rule-candidate, and once a preference recurs **3 or more times**, proposes a diff to the relevant brand doc.
- **Apply:** Jared approves the proposed diff. Brand docs are never changed from this log automatically (guardrail G8). Only `/retro` proposes, only Jared approves.

This log is the source signal. It is append-only. Do not delete entries; `/retro` needs the history to count recurrences. When a pattern has been promoted into a brand doc, `/retro` marks it `[PROMOTED]` rather than removing it.

## Entry format

```
## YYYY-MM-DD
- Piece: <which piece, e.g. week-25 linkedin-2 (draft)>
- Request (verbatim): "<exactly what Jared asked for>"
- Category: <hook | structure | voice/tone | word-choice | length | story-framing | visual | other>
- Rule candidate: <the generalizable preference this implies, in one line>
- Scope: generalizable | one-off
```

- **Category** lets `/retro` group similar requests.
- **Rule candidate** is the underlying preference, phrased as a reusable rule. Recurrence is counted by rule-candidate, not by verbatim text ("lead with a number" and "don't open with a question" are the same candidate).
- **Scope** separates a generalizable preference (eligible to become a brand-doc rule) from a one-off content request (logged for the record, never promoted).

## Status markers (added by /retro)

- `[WATCHING]` — seen 1 to 2 times; not yet proposed.
- `[CONFIRMED]` — seen 3+ times; `/retro` has proposed a brand-doc diff.
- `[PROMOTED]` — Jared approved the diff; the rule now lives in a brand doc. Keep the entries for history.

---

## Log

> Seed example below shows the format. Real entries are appended by the assistant during sessions. Delete the example once real entries exist if you prefer, but it is harmless to leave.

## 2026-06-30 (example)
- Piece: week-25 linkedin-2 (draft)
- Request (verbatim): "make the opener lead with the dollar figure, not the question"
- Category: hook
- Rule candidate: prefer number-led openers over question-led openers
- Scope: generalizable
