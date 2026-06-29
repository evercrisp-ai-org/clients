# Model Selected

**Selected model:** Claude Sonnet 4.6
**Where it is set:** the Claude Cowork model selector (shown as "Sonnet 4.6" in the composer)
**Context window:** 1,000,000 tokens

## Decision

Every workflow in this harness runs on **Claude Sonnet 4.6**, selected in Cowork. This is the standing default for all content generation, gating, and validation work unless a specific run is explicitly switched to a larger model.

## Context: this runs in Claude Cowork, not the cloud API

This system runs inside **Claude Cowork on a Claude Max plan**, not against the metered cloud API. That matters for how the model decision is framed: there is **no per-token bill**. You pay a flat subscription, and the practical constraint is the **usage window** (how much work fits before hitting your plan's rolling limit), not a dollar-per-million-tokens rate. So the rationale below is about capability fit and usage-window efficiency, not API pricing.

## Why Sonnet 4.6 is the optimal choice here

The decision is not "use the biggest model available." It is "use the model whose capability clears the hardest task in the workload, while consuming the least of the usage window." For this harness, that is Sonnet 4.6.

### 1. The work is constraint-following, not frontier reasoning
The hard part of this workload is not open-ended reasoning. It is **faithful adherence to a large, fixed rulebook**: the voice profile, the content recipe, the LinkedIn 17-item checklist, the no-em-dash rule, the loss-framing mandate, the `[ILLUSTRATIVE]` story-integrity rule, the date-alignment logic, and the brand color rotation. Sonnet 4.6 follows long, detailed instruction sets reliably and is strong at structured, rule-bound generation. The task rewards consistency and instruction adherence over raw inventiveness, which is exactly Sonnet's strength band.

### 2. The 1M-token context window holds the full brand corpus
A single batch run loads the entire brand context (voice profile, content recipe, calendar, editorial plan, quarterly plan, brand config, LinkedIn guidelines, and the enforcement rules), which is on the order of 62K tokens of source material before any drafting begins. Sonnet 4.6 carries a **1M-token context window**, so the complete source-of-truth set fits with very large headroom. There is no need to chunk, summarize, or selectively drop brand docs, which is precisely the failure mode that produces off-voice or non-compliant content. The model can hold every rule in working context for every asset it drafts.

### 3. Efficient on the Claude Max usage window
Because there is no per-token bill, the meaningful efficiency question is how much of the **usage window** each run consumes, which determines how many batches you can run before hitting your plan's limit. A lighter model consumes the window more slowly, so you get more runs per window. Sonnet 4.6 is substantially lighter on the window than the Opus tier while fully clearing this task, so choosing it directly increases how many content batches you can produce in a given period. See `05-time-study.md` for the throughput method.

### 4. Latency suits a human-in-the-loop workflow
The pipeline pauses for human review after each run (Jared approves before scheduling; Jared approves any brand-doc change). A faster model shortens each draft-review-revise cycle, which matters more here than the last few percent of quality a larger model might add on a task the smaller model already handles well.

### 5. The large fixed context is handled inside the Cowork session
Every run re-loads the same large, stable brand context. Cowork manages that context within the session for you; there is nothing to configure or optimize by hand. Sonnet 4.6 carries this fixed rulebook on every run without it becoming a bottleneck, which keeps the workflow simple and the behavior consistent run to run.

## When to escalate (and to what)

Sonnet 4.6 is the default, not a hard floor. For a specific run, switch the **Cowork model selector to a larger model (for example Claude Opus)** only when a task genuinely exceeds constraint-following and enters frontier reasoning, such as:

- Designing a brand-new content framework or editorial strategy from scratch.
- Resolving a subtle, multi-document contradiction across the brand corpus.
- A piece that has failed the same gate repeatedly and needs a qualitatively different drafting approach.

Escalation is a per-run decision a person makes in the model selector, not an automatic behavior of the harness. For the standing weekly production workload, Sonnet 4.6 is the optimal choice.

## Notes

- Set the model by selecting **Sonnet 4.6** in the Cowork model selector. The same model runs every skill in the harness.
- If the model is ever changed, re-run the eval suite (`08-evals.md`) as a regression check, since tone and instruction-following can shift between models.
