# Content Production Engine

A document-led content production system that captures a brand's voice, enforces content integrity, produces multi-channel content at scale, and learns from performance data over time.

## What This Is

This framework provides everything needed to run a professional content operation:

- **Voice capture and enforcement:** Distill a person's (or brand's) authentic voice from sample content and enforce it across every piece produced.
- **Multi-channel content production:** Blog posts, social media, podcasts/video, email, with configurable channels and volumes.
- **Content integrity:** Story classification, compliance guardrails, and fact-checking gates that prevent fabricated claims.
- **Quality assurance:** Automated Cursor rules and checklists that validate voice, relevance, integrity, and visual assets.
- **Recursive learning:** A performance-data-driven loop that makes each content cycle better than the last.
- **AI-giveaway prevention:** Built-in detection and enforcement of patterns that reveal AI-generated text.

The system is designed to work with AI-assisted content production (e.g., Cursor with Claude) while maintaining human oversight at critical checkpoints.

## Start Here

**Read [INTEGRATION_INSTRUCTIONS.md](INTEGRATION_INSTRUCTIONS.md) first.** It walks you through:

1. How to integrate this into an **existing project** or use it to start a **new project**.
2. How to run the **Recalibrating Interview** to capture your organization's context.
3. How to generate your **voice profile** from sample content.
4. How to configure **channels, compliance, and rules**.
5. How to validate the configuration before producing content.

## File Overview

| File | Purpose |
|------|---------|
| `INTEGRATION_INSTRUCTIONS.md` | Step-by-step setup for existing or new projects |
| `RECALIBRATING_INTERVIEW.md` | Structured questionnaire to capture org context (run first) |
| `BRAND_VOICE_ALIGNMENT_GUIDE.md` | How to build voice profile, detect AI giveaways, configure rules |
| `START_HERE.md` | Operational command center with session prompts and production workflows |
| `brand/` | Brand foundation documents (voice profile, content recipe, config, etc.) |
| `samples/` | Place your sample content here (10-30+ pieces) |
| `outputs/` | Where produced content, performance logs, and learning reviews go |
| `.cursor/rules/` | Automated quality gates for Cursor IDE |
| `src/` | Optional Python scripts (Excel export, config loader) |
| `docs/FILE_MAP.md` | Detailed file map, placeholder checklist, schema documentation |

## How It Works

```
Recalibrating Interview
        |
        v
Voice Profile Generation (from samples)
        |
        v
Editorial Plan (12-month themes)
        |
        v
Quarterly Drill-Down (weekly content slots)
        |
        v
Content Batch Production (drafts with quality gates)
        |
        v
Publish + Collect Performance Data
        |
        v
Recursive Learning (improve the system from real data)
        |
        +-------> feeds back into Voice Profile, Content Recipe, Calendar
```

## Requirements

- **Cursor IDE** (recommended) for AI-assisted content production and automated rule enforcement.
- **Python 3.8+** (optional) if using the Excel export script.
- **Sample content:** 10-30+ pieces that represent the desired voice.

## The System Works Without Code

The core content production system is entirely document-based. The session prompts in `START_HERE.md`, the brand documents in `brand/`, and the quality rules in `.cursor/rules/` function independently of any scripts. The Python tooling in `src/` is optional and provides Excel export for content batch summaries.
