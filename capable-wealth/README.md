# Capable Wealth | Content System & Cowork Harness

> The complete content operation for **Capable Wealth** (Jared Paul, CFP), a financial advisory brand serving orthopedic surgeons (ages 45-65, $700K-$2M income) approaching practice transition or retirement.
>
> This repo holds three things that work together: the **brand brain** (voice, recipe, calendar, rules), a **six-skill Claude Cowork harness** that drafts and quality-gates a full week of on-brand content, and a **Python rendering pipeline** for branded PDFs and social images, plus the acceptance test that proves the harness works.

---

## Table of Contents

- [Overview](#overview)
- [Repository structure](#repository-structure)
- [The Cowork harness: the seven skills](#the-cowork-harness-the-seven-skills)
- [How the skills work together](#how-the-skills-work-together)
- [The recursive learning loop](#the-recursive-learning-loop)
- [Setup & use](#setup--use)
- [Brand system (source of truth)](#brand-system-source-of-truth)
- [Testing the system](#testing-the-system)
- [The Python rendering pipeline](#the-python-rendering-pipeline)
- [The plugin / marketplace](#the-plugin--marketplace)
- [Diagrams & docs](#diagrams--docs)
- [Outputs](#outputs)

---

## Overview

The bottleneck this system solves: every content session used to require hours of research, brainstorm and brand, voice and rule consistency enforcement. The harness puts that knowledge inside Claude Cowork so you types one command and gets a full week of content drafted, with voice and compliance gated automatically, he reviews and approves rather than writing from scratch.

Three layers:

1. **Brand brain**: the voice profile, content recipe, calendar, editorial/quarterly plans, brand config, and enforcement rules. The single source of truth every skill reads.
2. **Cowork harness**: seven skills (`/research-scan`, `/generate-batch`, `/image-brief`, `/linkedin-check`, `/voice-check`, `/validate`, `/retro`) packaged as a Cowork plugin.
3. **Python pipeline**: JSON-templated rendering of branded PDFs (lead magnets, reports) and social images.

A fourth element ties them together: a **recursive learning loop** that logs Jared's revision requests and feeds them back into the brand brain (see below).

---

## Repository structure

```
capable_wealth/
├── README.md                       ← you are here (master overview)
├── START_HERE.md                   ← session-by-session content command center
├── COWORK_PROJECT_INSTRUCTIONS.md  ← paste into the Cowork Project's Instructions panel
│
├── brand/                          ← the brand brain (single source of truth)
│   ├── voice-profile.md            ← WHO Jared is (distilled from 126 blog posts)
│   ├── content-recipe.md           ← HOW content is made (workflow, 9-pt image std, quality checklist)
│   ├── content-calendar.md         ← WHEN (annual cycles, research checkpoints)
│   ├── editorial-plan-2026.md      ← 12-month plan (by month)
│   ├── quarterly-plan-Q2-2026.md   ← weekly slots (weeks 1-13)
│   ├── brand_config.json           ← palette, fonts, voice_and_tone
│   ├── experience-inventory.md     ← client-story sourcing (unpopulated → all ILLUSTRATIVE)
│   ├── experience-interview-guide.md  ← interview script to populate the inventory
│   ├── performance-log-template.md ← format for logging real engagement data
│   ├── corrections-log.md          ← behavioral log for the recursive learning loop
│   ├── system-guide.md             ← plain-English guide to the whole system
│   └── fonts/ · logos/ · graphics/ ← brand assets
│
├── rules/linkedin-content-creation-guidelines.md   ← the 17-rule LinkedIn rulebook
├── .cursor/rules/                  ← enforcement rules (integrity, date-alignment, production-batch)
│
├── .claude/skills/                 ← the seven skills (dev copies, for Claude Code)
├── capable-wealth-plugin/          ← the same skills packaged as a Cowork plugin
├── .claude-plugin/marketplace.json ← marketplace catalog so Cowork can install the plugin
├── automation/                     ← scheduled-pipeline config (Cowork Scheduled task)
│
├── src/                            ← Python rendering pipeline (PDF + image + Excel export)
├── pdf-page-templates/             ← JSON page templates the pipeline renders report PDFs from
├── examples/                       ← sample report content (JSON)
├── generate_tax_report.py          ← entry point: render the tax-strategies report
│
├── client-starter-kit/             ← self-contained boilerplate to launch a NEW client's system
│
├── tests/                          ← acceptance test, red-team defect kit, render test
│   ├── system-acceptance-test.md
│   ├── test_render.py
│   └── redteam/                    ← planted-defect files + answer key
│
├── tech-pack/                      ← technical documentation (model, stack, workflows, risks, evals, learning loop)
├── reference/                      ← brand-standard PDFs + the rendered lead-magnet report
├── diagrams/capable-wealth-sequence.excalidraw   ← UML sequence diagram of the workflow
├── docs/
│   ├── Capable-Wealth-Harness-Setup-Guide.docx   ← branded 2-page setup & use guide
│   └── python-template-system.md                 ← detailed pipeline docs (former root README)
│
├── outputs/drafts/                 ← generated content batches (by week)
├── operating-framework/            ← intellectual backbone (AI-Ready Leader manuscript)
└── social-media-audit/             ← AEO assessment
```

---

## The Cowork harness: the seven skills

Each skill is a markdown `SKILL.md` invoked by name in Cowork (e.g. `/generate-batch week-21`).

| Skill | What it does | When it runs |
|-------|--------------|--------------|
| `/research-scan` | Weekly **research + freshness pass**: researches the live web to verify the week's planned items are current (figures, limits, law changes, timely hooks), updates stale items, cites sources, flags rate-sensitive facts. | Weekly, before generating |
| `/generate-batch` | **The engine.** Produces the full week (blog, podcast, 3 LinkedIn, 5 Facebook, 2-5 clips, native video, carousel), enforcing every rule and running the gates as it writes. | Weekly |
| `/image-brief` | A production-ready **9-point AI image prompt** for every visual asset, with batch-wide rotation rules. | Auto inside `generate-batch`; or on demand |
| `/linkedin-check` | **17-item** performance checklist on each LinkedIn post (hook, length, loss frame, hashtags). | Auto inside `generate-batch`; or on demand |
| `/voice-check` | **Voice fidelity** across every produced piece, catches em dashes, formulaic pivots, off-voice lines. | Auto inside `generate-batch`; or on demand |
| `/validate` | **Compliance gate**: story integrity, date alignment, relevance → Green / Yellow / Red. | Auto inside `generate-batch`; or on demand |
| `/retro` | **Recursive learning pass.** Clusters the revision requests logged in `brand/corrections-log.md`; once a preference recurs 3+ times, proposes a brand-doc diff for Jared's approval. | Weekly, after content work |

---

## How the skills work together

```
EACH WEEK            THE ENGINE                       BEFORE PUBLISH
/research-scan  →    /generate-batch             →    /validate (fresh)
  refreshes the       ├─ /image-brief (every asset)   /voice-check
  week's planned      ├─ /linkedin-check (LinkedIn)   /linkedin-check
  items               ├─ /voice-check (all pieces)         │
                      └─ /validate (gates batch)           ▼
                              │                       Jared reviews & approves
                              ▼
                       drafts + Excel summary
```

`research-scan` keeps the plan timely → `generate-batch` produces the week and runs the gate skills inline → a **fresh, independent gate pass** re-checks before publishing → Jared approves. The full visual is in [`diagrams/capable-wealth-sequence.excalidraw`](diagrams/capable-wealth-sequence.excalidraw).

> **The one rule that matters:** always run the independent gate pass before publishing. `generate-batch` grades its own work, and self-checks miss things (em dashes, a fabricated client story, a stale figure). A fresh `/validate` + `/voice-check` pass catches what generation waves through. On-voice is not the same as publish-ready.

---

## The recursive learning loop

The harness improves itself over time. Because it runs in Cowork (no model fine-tuning), "learning" means the **brand docs get better**, so the same model produces better-aligned content with fewer corrections.

The signal is **Jared's revision requests in Cowork** ("too salesy, pull it back"). A standing rule logs each one to `brand/corrections-log.md` as it is applied. The weekly `/retro` skill clusters the log by rule-candidate and, once a preference recurs 3+ times, proposes a diff to the right brand doc. Jared approves; brand docs never change automatically.

```
Jared prompts a revision  →  assistant logs it to corrections-log.md
   →  weekly /retro clusters + counts  →  3+ recurrences = proposed brand-doc diff
   →  Jared approves  →  next batch reads the improved docs  →  fewer corrections
```

It cannot drift, because the signal is a human correcting the machine, not the machine grading itself. Full detail in [`tech-pack/09-learning-loop.md`](tech-pack/09-learning-loop.md).

---

## Setup & use

Step-by-step setup (clone, link the Cowork project, install the skills, paste the project instructions, enable web access) is in [`SETUP.md`](SETUP.md). A branded walkthrough is also in [`docs/Capable-Wealth-Harness-Setup-Guide.docx`](docs/Capable-Wealth-Harness-Setup-Guide.docx). In brief:

1. Open the Claude desktop app → **Cowork** mode.
2. Create a Project ("Capable Wealth Content System") and link it to this folder.
3. Paste [`COWORK_PROJECT_INSTRUCTIONS.md`](COWORK_PROJECT_INSTRUCTIONS.md) into the Project Instructions; turn Memory on.
4. Add the `brand/` + `rules/` source files as Project files.
5. Install the plugin from the marketplace (see [The plugin / marketplace](#the-plugin--marketplace)).
6. Each week: `/research-scan week N` → `/generate-batch week N` → independent re-grade in a fresh chat → fix & approve.

[`START_HERE.md`](START_HERE.md) is the deeper session-by-session command center.

---

## Brand system (source of truth)

The skills are prompt-native: they read the brand docs directly, so updating a brand doc updates every skill's behavior with no code change.

- **WHO**: [`brand/voice-profile.md`](brand/voice-profile.md): Jared's voice, distilled from 126 real blog posts. Hard rules: no em dashes, no "It's not X, it's Y" pivots.
- **HOW**: [`brand/content-recipe.md`](brand/content-recipe.md): the production workflow, the 9-point image standard, the standard draft format, and the quality checklist.
- **WHEN**: [`brand/content-calendar.md`](brand/content-calendar.md) + [`brand/editorial-plan-2026.md`](brand/editorial-plan-2026.md) + the quarterly plan.
- **LOOK + TONE**: [`brand/brand_config.json`](brand/brand_config.json): palette (`#243A4B`, `#5F7483`, `#B08D57`, `#F6F7F5`, `#1E2428`, `#9AA3A8`), fonts (Playfair Display + Inter), and `voice_and_tone.language_to_avoid`.
- **RULES**: [`rules/linkedin-content-creation-guidelines.md`](rules/linkedin-content-creation-guidelines.md) and the three `.cursor/rules/*.mdc` enforcement rules.
- **COMPLIANCE**: [`brand/experience-inventory.md`](brand/experience-inventory.md): currently unpopulated, so **every client example must be illustrative** ("Consider a surgeon earning…"), never an implied real relationship.

---

## Testing the system

[`tests/system-acceptance-test.md`](tests/system-acceptance-test.md) is a five-phase acceptance test built around a real scenario ("the mid-year push"): freshness → production → independent re-grade → **red-team** → business acceptance.

The red-team kit ([`tests/redteam/`](tests/redteam/)) contains deliberately broken drafts with an answer key, it proves the gates actually catch planted defects (em dashes, a fabricated client interaction, a premature quarter-close, an over-length LinkedIn post) and don't trust a draft's own checkmarks.

---

## The Python rendering pipeline

A JSON-templated engine that renders branded PDFs (lead magnets, multi-page reports) and social images. Full documentation: [`docs/python-template-system.md`](docs/python-template-system.md).

```bash
pip install -r requirements.txt
python generate_tax_report.py          # render the tax-strategies report
python src/export_content_batch.py outputs/drafts/content-batch-YYYY-MM-DD/   # Excel summary
```

---

## The plugin / marketplace

The seven skills are packaged as a Cowork plugin under [`capable-wealth-plugin/`](capable-wealth-plugin/), cataloged by [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json).

**Install in Cowork:** Personal plugins → Add marketplace → point at this repo → install `capable-wealth`. After any skill change, just **refresh** the plugin in Cowork, no re-zip, no re-upload.

---

## Diagrams & docs

- [`diagrams/capable-wealth-sequence.excalidraw`](diagrams/capable-wealth-sequence.excalidraw), UML sequence diagram of the full workflow (open at excalidraw.com → File → Open).
- [`docs/Capable-Wealth-Harness-Setup-Guide.docx`](docs/Capable-Wealth-Harness-Setup-Guide.docx), branded 2-page setup & use guide.
- [`docs/python-template-system.md`](docs/python-template-system.md), detailed pipeline reference.

---

## Outputs

Generated content batches live in [`outputs/drafts/`](outputs/drafts/), one folder per batch (e.g. `content-batch-2026-07-20/`), each with the week's markdown drafts plus an Excel summary. Approved, published deliverables go in `outputs/final/`.
