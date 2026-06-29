# Capable Wealth — Content Harness (Claude Code Skills)

This folder contains the skill harness for Jared's content operation. Each subfolder is one skill (`SKILL.md`), invokable in Claude Code by name (e.g. `validate`, `linkedin-check`, `generate-batch week-21`).

Skills are **project-scoped**: they live in the repo, so anyone who opens this project in Claude Code gets them, and they version with the codebase.

---

## The seven skills

| Skill | Role | Trigger |
|-------|------|---------|
| `generate-batch` | **The engine.** Produces a full week (or multi-week range) of content from the plan, enforces every production rule while drafting, runs the gates, writes files, exports the Excel summary, posts a Slack review summary. | Jared, weekly |
| `validate` | 3-rule gate: content integrity + date alignment + relevance → Green/Yellow/Red per piece, plus the §13 Quality Checklist. | Auto inside `generate-batch`; or on demand |
| `linkedin-check` | 17-item performance-tested LinkedIn checklist (Rules 1-18, cadence excluded). Pass/fail per item, fixes, word count, opening device. | Auto inside `generate-batch` (×3); or on demand |
| `image-brief` | 9-point production-ready AI image prompts with platform dimensions, exclusive palette, and batch-wide rotation rules. | Auto inside `generate-batch` (every asset); or on demand |
| `voice-check` | Voice fidelity audit — Voice Alignment, Audience Specificity, Pull Signal Design. Flags lines, suggests rewrites. | On demand |
| `research-scan` | Weekly freshness pass over the EXISTING plan — refreshes that week's scheduled items for timeliness. No new external research. | Before generating a week's batch |

> Note: this `.claude/skills/` copy is a dev mirror for Claude Code. The Cowork deliverable is the **`capable-wealth-plugin/`** (skills only, no connectors). The two are kept in sync; the plugin is the source of truth.

---

## How they connect

```
EACH WEEK            WEEKLY ENGINE                    ON DEMAND
research-scan   →    generate-batch              →    validate
  refreshes that      ├─ image-brief (every asset)   linkedin-check
  week's planned      ├─ linkedin-check (×3)         image-brief
  items for           └─ validate (gates batch)      voice-check
  timeliness                  │
                              ▼
                       Jared reviews & approves
```

`research-scan` refreshes the week's portion of the existing plan for timeliness → `generate-batch` produces the week and runs the gate skills inside the batch → Jared reviews and approves. No external research, no connectors.

---

## What each skill reads (source of truth)

The skills are prompt-native: they read the brand docs directly rather than duplicating them, so updating a brand doc updates every skill.

- `brand/voice-profile.md`, `brand/content-recipe.md`, `brand/content-calendar.md`, `brand/editorial-plan-2026.md`, `brand/quarterly-plan-Q*-2026.md`
- `brand/brand_config.json` (palette, fonts, `voice_and_tone.language_to_avoid`)
- `rules/linkedin-content-creation-guidelines.md`
- `.cursor/rules/content-production-batch.mdc`, `content-integrity.mdc`, `content-date-alignment.mdc`
- `brand/experience-inventory.md` (unpopulated → all stories default to `[ILLUSTRATIVE]`)

---

## Build + test history

Built from the brand docs, then tested and optimized by four parallel review agents grounded in the real repo:

1. **Reference audit** — every file path, section reference, and the Excel invocation verified to resolve.
2. **Gate eval on live content** — ran `validate`/`linkedin-check`/`voice-check` against real week-18 drafts. Caught a fabricated client interaction the draft self-certified as clean, and a banned "Not X, but Y" pivot.
3. **Adversarial producer review** — `generate-batch`/`image-brief` checked against every non-negotiable in the production rule. Surfaced that batches are multi-week and the quarterly plan only covers weeks 1-13.
4. **Research/learning review** — checked against the calendar formats and the recipe's 5-stage loop.

Key optimizations applied: multi-week batching with a cross-batch rotation ledger; editorial-plan fallback for weeks >13; gate skills now ignore drafts' self-certified checklists and re-derive; Flagged-vs-Blocked integrity tie-breaker; unverifiable rate facts → Yellow not Green; corrected the nested `voice_and_tone.language_to_avoid` config path.

---

## Phase 1 status

- [x] Seven skills built, tested, optimized
- [ ] Authenticate connectors: Slack, Dropbox, Gmail
- [ ] Wire the Slack approval step into `generate-batch` output
- [ ] Live end-to-end test on an upcoming week

Deferred to later phases: renderer/research/analytics MCP servers, HubSpot, Squarespace API, analytics automation.
