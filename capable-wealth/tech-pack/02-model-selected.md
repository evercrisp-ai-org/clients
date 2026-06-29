# Model Selected

**Selected model:** Claude Sonnet 4.6
**Model ID (API string):** `claude-sonnet-4-6`
**Context window:** 1,000,000 tokens
**Pricing:** $3.00 per 1M input tokens, $15.00 per 1M output tokens

## Decision

Every workflow in this harness runs on **Claude Sonnet 4.6**. This is the standing default for all content generation, gating, and validation tasks unless a specific run is explicitly escalated.

## Why Sonnet 4.6 is the optimal choice here

The model decision is not "use the biggest model available." It is "use the model whose capability ceiling clears the hardest task in the workload, at the lowest cost and latency that still clears it." For this harness, that model is Sonnet 4.6, for the following reasons.

### 1. The work is constraint-following, not frontier reasoning
The hard part of this workload is not open-ended reasoning. It is **faithful adherence to a large, fixed rulebook**: the voice profile, the content recipe, the LinkedIn 17-item checklist, the no-em-dash rule, the loss-framing mandate, the `[ILLUSTRATIVE]` story-integrity rule, the date-alignment logic, and the brand color rotation. Sonnet 4.6 follows long, detailed instruction sets reliably and is specifically strong at structured, rule-bound generation. The task rewards consistency and instruction adherence over raw inventiveness, and that is exactly Sonnet's strength band.

### 2. The 1M-token context window covers the full brand corpus
A single batch run loads the entire brand context (voice profile, content recipe, calendar, editorial plan, quarterly plan, brand config, LinkedIn guidelines, and the enforcement rules), which totals roughly 62K input tokens before any drafting begins. Sonnet 4.6 carries a **1M-token context window**, so the complete source-of-truth set fits with very large headroom. There is no need to chunk, summarize, or selectively drop brand docs, which is precisely the failure mode that produces off-voice or non-compliant content. The model can hold every rule in working context for every asset it drafts.

### 3. Cost efficiency at production cadence
Content is produced on a weekly batch cadence (blog, podcast script, 3 LinkedIn posts, 5 Facebook posts, clips, optional video and carousel), and each batch re-loads the brand context and runs multiple quality gates. At $3.00 / $15.00 per million tokens, Sonnet 4.6 sits at roughly one-fifth the input cost and one-fifth the output cost of the Opus tier. Across a full editorial year of weekly batches plus re-runs and gate passes, that ratio is the difference between a trivial and a meaningful operating cost, with no quality loss on this task type. See `01-token-cost-estimate.md` for the per-run math.

### 4. Latency suits a human-in-the-loop workflow
The pipeline pauses for human review at defined points (Jared approves brand-doc changes; drafts are reviewed before publishing). A faster model tightens each draft-review-revise cycle, which matters more here than shaving the last few percent of quality that a larger model might add on a task the smaller model already handles well.

### 5. Prompt caching amplifies the cost advantage
The ~62K-token brand context is a stable prefix that is identical across runs within a session. Sonnet 4.6 supports prompt caching, so that prefix can be served from cache at roughly one-tenth the input price on repeated runs. The economics of re-loading a large, fixed rulebook on every call are therefore strongly in Sonnet's favor.

## When to escalate (and to what)

Sonnet 4.6 is the default, not a hard floor. Escalate a specific run to a larger model (for example `claude-opus-4-8`) only when a task genuinely exceeds constraint-following and enters frontier reasoning, such as:

- Designing a brand-new content framework or editorial strategy from scratch.
- Resolving a subtle, multi-document contradiction across the brand corpus.
- A piece that has failed the same gate repeatedly and needs a qualitatively different drafting approach.

Escalation is a per-run decision made by a human, not an automatic behavior of the harness. For the standing weekly production workload, Sonnet 4.6 is the optimal model.

## Notes

- Use the exact model string `claude-sonnet-4-6`. Do not append a date suffix.
- Pricing and context window are current as of the cached model reference used to author this doc (2026). Verify against the live Anthropic pricing page before quoting figures externally.
