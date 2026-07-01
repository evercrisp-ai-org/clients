---
name: voice-check
description: Audit a Capable Wealth draft against Jared's voice profile — the Voice Alignment, Audience Specificity, and Pull Signal Design gates — flagging the exact lines that miss and suggesting rewrites in his voice. Use when the user asks whether something sounds like Jared, to voice-check / tone-check a draft, or to catch voice drift.
---

# Voice Check

Audit a draft for voice fidelity to Jared Paul. He is the "knowledgeable friend," not a guru — conversational-professional, warm, gently contrarian, positioned alongside the reader. Catch drift at the line level before it becomes a pattern.

## Input

A path to a draft or pasted content. Audit the Content section. Infer the content type from the Post Metadata `Type:` field to apply the correct sign-off rule; if pasted text has no type, ask or state the assumption.

**voice-check does NOT verify whether a client story is real.** A line can be perfectly on-voice and still be a fabricated client interaction. If the draft opens with "a surgeon I talked with," "I sat down with," or a quoted real client, note **"integrity review required — run `validate`"** even when the voice passes. On-voice is not publish-clear.

## Load first

`brand/voice-profile.md` (Voice Characteristics §3, Structural DNA §4, Rhetorical Toolkit §5, Anti-Patterns §7, Voice Samples §8), `brand/content-recipe.md` §13 (the three checklists below) and §9 (Language Guide), and `brand_config.json` → `voice_and_tone.language_to_avoid` (nested key, not top-level) for the full banned list: em dashes, the pivot constructions, "secrets/hacks/shortcuts," "crush/dominate," fear-based urgency, "guaranteed/no-brainer."

## Three gates

### Voice Alignment (8 items)
- [ ] Opens with a story, conversation, or specific scenario (not a definition or statistic)
- [ ] Contains at least one contrarian reframe or myth-bust — woven into the argument, not delivered as a blunt pivot
- [ ] Direct "you" address throughout (reader is "you", never an abstract "people")
- [ ] Reads like a conversation with a trusted advisor, not a brochure or sales pitch
- [ ] Avoids all banned language (brand_config `voice_and_tone.language_to_avoid`); no fear/urgency tactics, no get-rich-quick framing
- [ ] Ends with a clear takeaway and the right sign-off (blog/email: "Capably Yours, Jared"; LinkedIn/Facebook: no sign-off)
- [ ] Tone matches profile: warm, encouraging, gently contrarian, lightly humorous where it fits
- [ ] **No em dashes anywhere. No "It's not X, it's Y" / "You don't have an X problem, you have a Y problem" pivot constructions.** These are hard fails — em dashes and the pivot are AI tells that break voice instantly.

### Audience Specificity (4 items)
- [ ] Could only have been written for orthopedic surgeons (not generic financial advice)
- [ ] Includes a concrete number at surgeon-level income ($700K-$2M)
- [ ] References practice-specific context where appropriate (valuations, transitions, compensation structures, reimbursement)
- [ ] Respects the reader's intelligence and time — no explaining what a 401(k) is

### Pull Signal Design (4 items)
- [ ] Provides genuine value a surgeon would forward to a colleague
- [ ] Ties tactical advice back to a bigger principle (control, purpose, legacy, "life beyond the OR")
- [ ] Includes a natural next step, not a hard sell
- [ ] Reader finishes feeling more informed and in control, not more anxious

## Output

Per-item ✓/✗ across all three gates. For every ✗, **quote the offending line** and give a one-line rewrite in Jared's voice.

Scan specifically for:
- **Em dashes (run this scan first, every time)** — search the literal text for `—` (em dash, U+2014), and also for `–` (en dash, U+2013) and `―` (horizontal bar), which are the same defect. Any hit is a hard fail. This is the most common AI tell in this content; never report a piece as on-voice without having actually run this character search.
- **The banned pivot, every surface form** — "It's not X, it's Y"; "You don't have an X problem, you have a Y problem"; "Not X, but Y"; "not because X, because Y"; and the quoted question form 'not "[A]," but "[B]."' Search for `not ... but` and `not ... it's` across the whole text. (A real draft slipped a `not "can I push this out," but "what does the year look like"` pivot past an earlier check — catch this class.)
- **Throat-clearing kill-phrases** — "There is a question worth asking," "Let me put that in perspective," "Here's why that matters," "Most people don't realize."
- **Brochure tone** — feature-listing with no antagonist or scenario ("A cash balance plan can shelter $150K-$350K").
- Academic/textbook phrasing, anything preachy or guru-like.

Re-derive every item independently; ignore the draft's own `[x]` self-checklist. End with a 1-line verdict: **On-voice** / **Minor drift (N fixes)** / **Off-voice (rework)**. Report only — offer to apply rewrites if the user wants.
