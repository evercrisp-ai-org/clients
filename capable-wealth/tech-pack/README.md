# Capable Wealth: Technical Pack

This folder is the technical documentation for the Capable Wealth content-generation harness. The repo itself **is** the tech pack; these docs describe how the system works, what it costs, where it can fail, and how its quality is enforced and measured.

The harness produces a full week of on-brand content (blog, podcast script, LinkedIn posts, Facebook posts, clips, optional video and carousel) for Jared Paul, CFP, serving orthopedic surgeons, and gates every piece against a large rulebook before it reaches human review.

## Contents

| Doc | What it covers | Status |
|---|---|---|
| [02-model-selected.md](02-model-selected.md) | Model choice (Claude Sonnet 4.6) and the full rationale | Complete |
| [03-tech-stack.md](03-tech-stack.md) | Every tool and library, by role, plus a recommendation on Google Sheets | Complete |
| [04-workflow-maps.md](04-workflow-maps.md) | Visual maps of the workflows as GitHub-rendered Mermaid flow + sequence diagrams | Complete |
| [05-time-study.md](05-time-study.md) | Stage-by-stage timing with HITL dependency callouts | **Pinned** (template ready, awaiting measured data) |
| [06-risk-assessment.md](06-risk-assessment.md) | Risk register with severity, mitigation, and residual risk | Complete |
| [07-guardrails.md](07-guardrails.md) | The always-on and gate-enforced guardrails | Complete |
| [08-evals.md](08-evals.md) | The evals (the quality gates), criteria, and how to run them as a regression set | Complete |

## How the pieces fit together

- The **model** (02) runs inside **Cowork** with the **tech stack** (03).
- The **workflow maps** (04) show how `generate-batch` orchestrates the gates.
- The **guardrails** (07) are the constraints; the **evals** (08) are how those constraints are checked; the **risk assessment** (06) is what they protect against.
- The **time study** (05) quantifies what a run costs in time.

## Open items

- **Time study (05):** awaiting measured run data from Jared/Dave.
- **Evals (08):** recommend building a small seeded "bad batch" so the gates have a permanent regression target.
- **Google Sheets (03):** decision deferred; add only if a stakeholder needs a browser-based shared tracker.
