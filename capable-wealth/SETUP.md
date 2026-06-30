# Setup: Running the Capable Wealth harness in Cowork

This guide stands the content harness up in Claude Cowork from a clean start. It takes about 15 minutes. By the end you can type `/generate-batch week-NN` and get a full, on-brand, gated week of content.

> The harness is the `capable-wealth/` folder: brand docs, enforcement rules, the seven skills, the Python rendering pipeline, and the outputs. The skills read the brand docs by relative path, so the Cowork project must be linked to this folder for anything to resolve.

---

## Step 1: Get the files onto your machine

The repo is private under the `evercrisp-ai-org` org. Clone it (you must be a member of the org and signed in):

```bash
# Easiest, uses the GitHub CLI auth you already have:
gh repo clone evercrisp-ai-org/clients

# Or with plain git (will prompt for credentials / a token):
git clone https://github.com/evercrisp-ai-org/clients.git
```

The harness lives in the `clients/capable-wealth/` subfolder. That subfolder is what you link to Cowork.

(No terminal? On GitHub: open the repo, click **Code → Download ZIP**, unzip, and use `clients/capable-wealth/`.)

---

## Step 2: Create the Cowork project and link the folder

1. In Cowork, create a **new Project** (e.g. "Capable Wealth Content System").
2. Link / add the **`capable-wealth/` folder** as the project's working folder, so `brand/`, `rules/`, `src/`, and `outputs/` resolve by relative path. The skills carry the instructions; the linked folder carries the brand data and outputs.

---

## Step 3: Make the seven skills available

The skills are packaged as the `capable-wealth` plugin (`capable-wealth-plugin/`, cataloged by `.claude-plugin/marketplace.json`). Add the plugin so the skills appear, then confirm by typing `/` in the composer and checking you see:

`/generate-batch` · `/validate` · `/linkedin-check` · `/image-brief` · `/voice-check` · `/research-scan` · `/retro`

(The same skills are mirrored in `.claude/skills/` as dev copies for Claude Code; the plugin is the source of truth.)

---

## Step 4: Paste the Project Instructions

Copy everything in the fenced block below into the Project's **Instructions** panel. This sets the always-on guardrails so on-brand, compliant behavior holds for every task, even a plain-English prompt that names no skill. (This is the contents of `COWORK_PROJECT_INSTRUCTIONS.md`, the canonical source; if that file changes, re-paste.)

```markdown
# Capable Wealth: Cowork Project Instructions

## What this project is

This workspace produces content for **Capable Wealth**, Jared Paul, CFP, a financial advisor serving **orthopedic surgeons aged 45-65, $700K-$2M income**, approaching practice transition or retirement. Audience is sophisticated, time-scarce, and values clinical precision. Never explain the basics (don't define a 401(k)); discuss cash balance plans, QBI, S-corp structure, installment sales.

## Source of truth (read before producing content)

Always read the relevant brand docs first; never produce content from memory:
- `brand/voice-profile.md`: WHO Jared is.
- `brand/content-recipe.md`: HOW content is made (templates §7, image standard §10, draft format §12, quality checklist §13).
- `brand/content-calendar.md` + `brand/editorial-plan-2026.md` + `brand/quarterly-plan-Q*-2026.md`: WHEN / what's planned.
- `brand/brand_config.json`: palette, fonts, `voice_and_tone.language_to_avoid`.
- `rules/linkedin-content-creation-guidelines.md` and `.cursor/rules/*.mdc`: the enforcement rules.
- `brand/experience-inventory.md`: client-story sourcing (currently unpopulated).

If a brand doc contradicts these instructions or your assumptions, **the brand doc wins.**

## Non-negotiable guardrails (apply to everything)

- **No em dashes.** Use commas, parentheses, periods, semicolons, colons. This is a hard rule.
- **No "It's not X, it's Y" / "Not X, but Y" / "not because X, because Y" pivots.** Let reframes emerge in the flow of the argument; state the cause directly.
- **Story integrity.** The experience inventory is unpopulated, so every client story defaults to **`[ILLUSTRATIVE]`** with approved framing ("Consider a surgeon earning…"). Never imply a real advisory relationship ("I sat down with," "a client told me," "last Tuesday," real quotes/pseudonyms). Classify every story and list it in Post Metadata.
- **Surgeon-specific, always.** Every piece could only have been written for orthopedic surgeons; use surgeon-level numbers and practice context.
- **Loss framing over gain framing** (what's leaking, not what you could shelter). Diagnostician, not educator.
- **Voice:** warm, conversational-professional, gently contrarian, the knowledgeable friend a few steps ahead. Blog/email sign off "Capably Yours, Jared"; LinkedIn/Facebook have no sign-off.
- **Visuals** use only the brand palette (#243A4B, #5F7483, #B08D57, #F6F7F5, #1E2428, #9AA3A8), Playfair Display + Inter, 60/30/10 ratio. No cartoons, clip art, generic stock, or clickbait.
- **Dates are honest.** Never reference a deadline, quarter-close, or event before it has occurred relative to the publish date. Week numbers are an internal sequential index, not ISO weeks.
- **Trust nothing a draft says about itself.** Re-derive every quality check; ignore a draft's own `[x]` checklist.
- **Log revision requests (the learning loop).** Whenever Jared asks to revise, retone, cut, restructure, or rephrase an already-generated piece, append a structured entry to `brand/corrections-log.md` (date, piece, verbatim request, category, rule-candidate, scope) **before** applying the change, and briefly note that you logged it as a preference candidate. This feeds the weekly `/retro` pass. Never change brand docs from these logs directly; only `/retro` proposes brand-doc diffs, and only Jared approves them.

## The skills (from the capable-wealth plugin)

Invoke by name, or describe the task and let Claude pick:
- `/generate-batch`: a full week (or range) of content. The engine; runs the gates automatically.
- `/validate`: gate any draft/folder → Green/Yellow/Red.
- `/linkedin-check`: the 17-item LinkedIn checklist on a post.
- `/image-brief`: 9-point image prompts with rotation rules.
- `/voice-check`: voice fidelity audit.
- `/research-scan`: weekly research and freshness pass. Researches the live web to confirm the week's planned items are current, timely, and relevant (tax figures, limits, law changes, current events), updates anything stale, cites sources, and flags rate-sensitive facts for confirmation. Run it before `/generate-batch` for the week.
- `/retro`: weekly recursive-learning pass. Reads the revision requests logged in `brand/corrections-log.md`, and once a preference recurs 3 or more times, proposes a brand-doc diff for your approval. Run it weekly, after a week of content work, before the next batch.

## Output conventions

- Drafts go in `outputs/drafts/content-batch-{YYYY-MM-DD}/`; finals in `outputs/final/`.
- After any change to a batch folder, regenerate the Excel summary: `python3 src/export_content_batch.py outputs/drafts/content-batch-{YYYY-MM-DD}/`.
- Brand source docs (`voice-profile.md`, `content-recipe.md`, `content-calendar.md`, LinkedIn guidelines) change **only on Jared's explicit approval**, propose edits as diffs, never apply silently.
```

---

## Step 5: Enable capabilities

- **Web access / search (required for `/research-scan`).** `/research-scan` researches the live web to verify figures, limits, law changes, and timing. Turn on web access for the project. Without it, `/research-scan` falls back to a repo-only pass and says so.
- **Slack (optional).** If connected, `/generate-batch` posts a review summary to `#content-review` at the end of a run. If not connected, it prints the summary in chat instead.
- **Python (optional, local).** The PDF/Excel pipeline (`src/`, `generate_tax_report.py`) runs locally. Install deps with `pip install -r requirements.txt` if you render reports or regenerate the Excel batch summary.

---

## Step 6: Verify

Type `/` and confirm the seven skills appear. Then sanity-check that the brand docs resolve: ask the project to read `brand/voice-profile.md` and summarize Jared's voice in one line. If it can read it, the folder link is correct.

---

## Step 7: First run

```
/research-scan week-21      ← verify + freshen the week's planned items (web)
/generate-batch week-21     ← produce the full week; gates run inline
```

Review the drafts in `outputs/drafts/`, confirm any "confirm before publish" figure flags, approve. Weekly, after content work, run `/retro` to fold your revision requests back into the brand docs.

---

## The two things that stay human (do not skip)

1. **Verify flagged figures.** `/research-scan` and `/validate` flag rate-sensitive facts; a person confirms them before publishing.
2. **Approve before publishing.** Drafts land in `outputs/drafts/`, never published automatically. Review and approve first.

---

## Reusing this for another client

The `client-starter-kit/` folder is a self-contained boilerplate: copy it out, follow its `INTEGRATION_INSTRUCTIONS.md`, and populate the blank brand docs to stand up the same harness for a different advisor.
