# Risk Assessment

This assesses what can go wrong in an automated content pipeline that produces financial-advisory content for a regulated profession, and what the harness does (or should do) about each risk. Risks are rated by **likelihood** and **impact**, with the residual risk after the guardrail in place.

Severity key: **Critical** = compliance / reputational exposure; **High** = off-brand or wrong content reaching publish; **Medium** = quality drift; **Low** = operational friction.

---

## R1. Fabricated client relationships (compliance / reputational)
**Severity: Critical.** The single highest-stakes risk. A financial advisor implying a real client interaction that did not happen ("I sat down with a surgeon last Tuesday") is a compliance and reputational problem, not just a voice issue.
- **Likelihood without guardrail:** High. LLMs naturally write vivid, specific, real-sounding anecdotes.
- **Mitigation:** Guardrail G3 (story integrity). Experience inventory is unpopulated, so all stories default to `[ILLUSTRATIVE]` with approved framing. `content-integrity.mdc` + `validate` read the actual body prose against a banned-framing list and mark fabricated interactions **Blocked / RED**. Story classification is mandatory in Post Metadata.
- **Residual risk:** Low, but never zero. The validate gate reads body prose, not just the metadata tag, which closes the "correct tag, wrong prose" hole. Human review before publish is the backstop.

## R2. Unverified financial figures (compliance / accuracy)
**Severity: Critical.** Tax limits, contribution caps, rates, and legal references change year to year. Publishing a stale or wrong figure to a sophisticated audience is both an accuracy failure and a credibility hit.
- **Likelihood without guardrail:** High. The model may assert a confident but outdated number.
- **Mitigation:** Guardrail G12 (validate Relevance check). Any rate / limit / legal fact that cannot be verified from the repo is marked **Yellow** and flagged for manual verification, never Green. `research-scan` explicitly flags stale-figure dependencies ("verify before publish") rather than inventing current values.
- **Residual risk:** Medium. The system flags but cannot itself verify external current figures. This depends on the human verifying flagged numbers before publish. **This is the most important manual step in the pipeline.**

## R3. Date / timing errors (accuracy)
**Severity: High.** Referencing a quarter-close, deadline, or event before it has occurred relative to the publish date (for example "now that April 15 has passed" published in March).
- **Likelihood without guardrail:** Medium-High, especially with batches produced weeks ahead of publish and an internal week-numbering scheme that is not ISO weeks.
- **Mitigation:** Guardrail G4 (`content-date-alignment.mdc` + validate). Hard quarter-close stops, 2 to 4 week deadline lead-time rule, and explicit checks that relative date references match the publish window.
- **Residual risk:** Low.

## R4. Voice drift / AI tells (brand)
**Severity: High.** Em dashes, "not X but Y" pivots, throat-clearing, brochure tone, and generic phrasing erode the distinct voice that makes the content credible to surgeons.
- **Likelihood without guardrail:** High. These are default LLM habits.
- **Mitigation:** Guardrails G1, G2, G10. Literal character/phrase scans for `—` and pivot constructions, plus the three-gate `voice-check` on every piece with line-level rewrites.
- **Residual risk:** Low-Medium. Subtler drift (slightly off cadence, a metaphor that does not land) can survive automated checks; human review catches the rest.

## R5. Self-reported false quality (process integrity)
**Severity: High.** A draft that ships with its own Quality Checklist marked all-green while actually failing checks. This has happened.
- **Likelihood without guardrail:** Medium.
- **Mitigation:** Guardrail G7. Every gate re-derives every check independently and explicitly ignores the draft's own `[x]` marks.
- **Residual risk:** Low.

## R6. Incomplete batches (operational / quality)
**Severity: Medium.** A week produced short (missing clips, missing podcast) because it was treated as "channel-primary," leaving gaps in the publishing calendar.
- **Likelihood without guardrail:** Medium.
- **Mitigation:** Guardrail G11. Mandatory volume (10 core + 2 to 5 clips) regardless of channel emphasis, plus a completeness check on disk before the run reports done.
- **Residual risk:** Low.

## R7. Visual off-brand output (brand)
**Severity: Medium.** Off-palette colors, repeated image types, clickbait or stock-photo aesthetics, or the same stat card reused across platforms.
- **Likelihood without guardrail:** Medium.
- **Mitigation:** Guardrail G6 + G11. `image-brief` enforces the exclusive palette, 60/30/10 ratio, the 9-point prompt standard, and rotation rules (color, subject, layout, cross-platform dedup).
- **Residual risk:** Medium. Image generation happens in an external tool (Midjourney / Ideogram / DALL-E) outside the harness, so the brief constrains the prompt but not the final pixels. Human review of generated images is required.

## R8. Excel / markdown desync (operational)
**Severity: Low.** The `.xlsx` summary (the handoff artifact) drifting out of sync with the markdown drafts.
- **Likelihood without guardrail:** Medium if done manually.
- **Mitigation:** Guardrail G11 requires regenerating the Excel via `export_content_batch.py` after any batch change.
- **Residual risk:** Low, contingent on the regeneration step actually being run.

## R9. No blocking pre-publish gate inside the run (process)
**Severity: Medium.** `generate-batch` writes everything to disk and does not halt for approval mid-run. If the async human review is skipped, unreviewed content could be published.
- **Likelihood:** Low-Medium, depends on team discipline.
- **Mitigation:** The Slack summary to `#content-review` and the explicit "next action for Jared" in the final report make review the expected next step. Drafts land in `outputs/drafts/`, not `outputs/final/`, so the drafts/final split is itself a guardrail against accidental publish.
- **Residual risk:** Medium. This is a process dependency, not a hard technical lock. Worth considering whether a publish step should require an explicit human sign-off.

## R10. Model change shifts behavior (operational)
**Severity: Low-Medium.** Switching the Cowork model selector to a different model could change tone, instruction-following, or how much of the usage window a run consumes.
- **Mitigation:** The model is kept on Claude Sonnet 4.6 in Cowork (see `02-model-selected.md`), and the eval set (`08-evals.md`) provides a regression baseline to re-run after any model change.
- **Residual risk:** Low, as long as the eval set is run on any model change.

---

## Risk register summary

| ID | Risk | Severity | Primary mitigation | Residual |
|---|---|---|---|---|
| R1 | Fabricated client relationships | Critical | G3 story integrity + validate | Low |
| R2 | Unverified financial figures | Critical | G12 relevance flagging + manual verify | Medium |
| R3 | Date / timing errors | High | G4 date alignment | Low |
| R4 | Voice drift / AI tells | High | G1, G2, G10 | Low-Medium |
| R5 | Self-reported false quality | High | G7 re-derive everything | Low |
| R6 | Incomplete batches | Medium | G11 volume + completeness check | Low |
| R7 | Visual off-brand output | Medium | G6, G11 + human image review | Medium |
| R8 | Excel / markdown desync | Low | G11 regeneration step | Low |
| R9 | No blocking pre-publish gate | Medium | drafts/final split + Slack review | Medium |
| R10 | Model / provider change | Low-Medium | pinned model + eval regression | Low |

## The two risks that depend on humans, not the harness
1. **R2 (verify flagged figures).** The system flags rate-sensitive numbers; a person must verify them before publish.
2. **R9 (review before publish).** The system produces and summarizes; a person must review before anything moves from `drafts/` to publish.

Everything else is enforced automatically. These two are the deliberate human-in-the-loop dependencies and should be treated as required steps, not optional ones.
