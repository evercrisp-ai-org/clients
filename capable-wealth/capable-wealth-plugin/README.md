# Capable Wealth Plugin (for Claude Cowork)

A content-production harness for Jared Paul, CFP — financial content for orthopedic surgeons. Seven skills that load the brand context, enforce every production rule, gate quality, and produce on-voice content. No connectors — skills only.

## The seven skills

| Skill | What it does | Who triggers it |
|-------|--------------|-----------------|
| `/generate-batch` | Produces a full week (or multi-week range) of content from the plan; enforces every rule while drafting; runs the gates; writes files; exports the Excel summary. | Jared (weekly) |
| `/validate` | 3-rule gate (integrity + date alignment + relevance) → Green/Yellow/Red per piece + the §13 checklist. | auto inside generate-batch; or on demand |
| `/linkedin-check` | 17-item LinkedIn performance checklist; pass/fail, fixes, word count, opening device. | auto inside generate-batch; or on demand |
| `/image-brief` | 9-point AI image prompts with dimensions, palette, and batch rotation rules. | auto inside generate-batch; or on demand |
| `/voice-check` | Voice fidelity audit (Voice Alignment / Audience Specificity / Pull Signal). | on demand |
| `/research-scan` | Weekly freshness pass over the EXISTING plan — refreshes that week's scheduled items for timeliness. No new external research. | before generating a week's batch |
| `/retro` | Recursive learning pass — clusters the revision requests logged in `brand/corrections-log.md`; once a preference recurs 3+ times, proposes a brand-doc diff for Jared's approval. The only skill that improves the source-of-truth itself. | weekly, after content work |

## The recursive learning loop

A standing rule (in the Project Instructions) logs every revision Jared prompts to `brand/corrections-log.md` as it is applied. The weekly `/retro` skill clusters those corrections and, once a preference recurs 3+ times, proposes an improvement to the brand docs the other six skills read. Jared approves; brand docs never change automatically. Over time the system needs fewer corrections of the same kind.

## Requirement: link the Project to the `capable_wealth` folder

The skills read the brand source of truth by relative path (`brand/voice-profile.md`, `rules/linkedin-content-creation-guidelines.md`, `.cursor/rules/*.mdc`, `brand/brand_config.json`, `src/export_content_batch.py`, `outputs/`). For those paths to resolve, the Cowork **Project must be linked to the `capable_wealth` folder** (or any folder that contains `brand/`, `rules/`, `src/`, `outputs/`). The plugin carries the *instructions*; the linked folder carries the *brand data and outputs*.

## Install in Cowork

1. In Claude Cowork (desktop app, Cowork mode), open the plugins area.
2. Install this plugin from its local folder path, or add the repo as a plugin marketplace and install `capable-wealth`.
3. Confirm the skills appear (type `/` to see `/generate-batch`, `/validate`, etc.).

## Maintenance

Skills are plain `SKILL.md` markdown. Edit any skill in `skills/<name>/SKILL.md`. The skills intentionally do **not** duplicate the brand docs — they read them live, so updating a brand doc in the linked folder updates every skill's behavior with no plugin change.
