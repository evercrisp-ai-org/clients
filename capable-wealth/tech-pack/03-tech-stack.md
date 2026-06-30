# Tech Stack

The full set of tools, services, and libraries this harness depends on, grouped by role.

## Core runtime

| Layer | Tool | Role |
|---|---|---|
| **Agent runtime** | **Claude Cowork** | The environment the workflows run in. Hosts the conversation, loads the project context, executes the skills, and runs the agentic loop that drafts and gates content. |
| **Model** | **Claude Sonnet 4.6** (selected in the Cowork model picker) | The single model behind every workflow. See `02-model-selected.md`. |
| **Skill layer** | **`capable-wealth` plugin** (v1.2.0) | Packages the 7 skills (`generate-batch`, `validate`, `linkedin-check`, `image-brief`, `voice-check`, `research-scan`, `retro`) that load brand context, enforce rules, gate quality, and learn from corrections. |
| **Always-on guardrails** | **Cowork Project Instructions** + **`.cursor/rules/*.mdc`** | Keep the workspace on-voice and compliant even for plain-English prompts that do not name a skill. |

## Version control and delivery

| Tool | Role |
|---|---|
| **GitHub** (`evercrisp-ai-org/clients`) | Source of truth and delivery surface for the whole project, including brand docs, rules, skills, produced content, and this tech pack. Private repo under the org, content lives under `capable-wealth/`. |
| **Git** | Local version history; batches are committed as they are produced. |

## Python document-generation toolchain

Used by `src/` for rendering the branded PDF/report and the Excel batch summary. From `requirements.txt`:

| Library | Role |
|---|---|
| **Jinja2** | Template engine for variable substitution in the report templates. |
| **WeasyPrint** | HTML/CSS to PDF conversion (the branded report output). |
| **Pillow** | Image manipulation and generation. |
| **PyMuPDF** | PDF manipulation. |
| **reportlab** | Alternative PDF generation path. |
| **matplotlib + numpy + seaborn** | Chart and data-visualization generation. |
| **openpyxl** | Generates the `.xlsx` batch summary (`src/export_content_batch.py`). |
| **pydantic** | Schema validation for the JSON config files. |
| **click + rich** | CLI interface and rich terminal output. |
| **python-dotenv** | Environment configuration. |
| **watchdog** | File watching during development. |
| **pytest + black** | Testing and code formatting (dev only). |

## Outputs and integrations

| Surface | Role | Status |
|---|---|---|
| **Excel (.xlsx)** | Per-batch summary workbook, regenerated after any batch change via `python3 src/export_content_batch.py <batch-folder>`. | Active |
| **Web search / fetch** | `research-scan` uses live web access to verify the week's planned items against current facts (figures, limits, law changes, timely hooks) and cite sources. Must be enabled in the Cowork project. | Active (required for research-scan) |
| **Slack** | `generate-batch` posts a review summary to Slack at the end of a run, so a human can review before publishing. | Active |
| **Branded PDF report** | The client-facing report rendered from the template system. | Active |

## On Google Sheets: recommendation

**Short answer: optional, and not required for the pipeline to work. Add it only if non-technical stakeholders need a live, shared, web tracker.**

Reasoning:
- The pipeline already produces a structured **`.xlsx` batch summary** (via `openpyxl`) and the editorial plan / content calendar already live as version-controlled markdown in the repo. Those cover the "what was produced and what is planned" tracking need for anyone comfortable in GitHub or Excel.
- Google Sheets adds value in exactly one scenario: **stakeholders who live in Google Workspace and want to view or edit a shared, always-current tracker in the browser** without touching GitHub or downloading an Excel file. If that describes the team, it is worth adding.
- If you do add it, the clean way is as a **downstream sync target**, not a new source of truth: keep the repo and the `.xlsx` as canonical, and push a copy of the batch summary into a Sheet (manually at first, or later via the Google Sheets API as a small export step alongside `export_content_batch.py`). The repo stays the source of truth; the Sheet is a read-friendly mirror.

**Recommendation:** do not add it now. Revisit if a stakeholder explicitly asks for a browser-based shared tracker. If yes, add it as a one-way mirror of the existing `.xlsx`, not as a parallel source of truth.
