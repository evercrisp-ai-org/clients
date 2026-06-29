# Token Use and Cost Estimate

This doc does two things:
1. Explains **how to capture the real token cost of any Cowork run** (the reproducible method).
2. Provides a **grounded estimate** for a full `generate-batch` run so there is a working number before the first measured run.

Pricing used throughout (Claude Sonnet 4.6): **$3.00 / 1M input tokens, $15.00 / 1M output tokens.** See `02-model-selected.md`.

---

## Part 1: How to get the real per-run cost on Cowork

Cowork does not always surface a token counter in the chat UI, so the cost of a single run is captured from the billing/usage layer, not from the conversation. There are three methods, in order of accuracy.

### Method A: Anthropic Console Usage dashboard (ground truth, recommended)
This is the authoritative number because it is what you are actually billed.

1. Run **one** workflow in isolation (for example a single `generate-batch week-NN`). Do not run anything else against the same org in that window.
2. Note the start and end timestamps of the run.
3. Open the Anthropic Console, go to **Usage** (`console.anthropic.com` -> Usage / Cost).
4. Filter to the date and, if available, the hour of the run, and to the **Sonnet 4.6** model.
5. Read the **input tokens** and **output tokens** consumed in that window.
6. Cost = (input_tokens / 1,000,000 x $3.00) + (output_tokens / 1,000,000 x $15.00).

Tip: the Usage page also breaks out **cache read** vs **cache write** tokens. Cache reads bill at ~10% of the input rate, so a run that re-uses the brand context prefix will show a large cache-read figure and a small fresh-input figure. Capture both; the blended cost is what matters.

### Method B: Token Counting API (exact input side, before running)
For the deterministic input side (the brand context that loads every run), you can measure exactly without spending generation tokens, using the `messages.count_tokens` endpoint.

- Concatenate the brand docs that a run loads (voice profile, content recipe, calendar, editorial plan, quarterly plan, brand config, LinkedIn guidelines, the `.cursor/rules/*.mdc` files, and the Cowork project instructions).
- Call `count_tokens` with `model: "claude-sonnet-4-6"` on that payload.
- This gives the fixed input-token floor for a run. Output tokens still have to be measured or estimated (Part 2).

### Method C: Decompose-and-sum (fast estimate, no console access)
When you cannot reach the Console, estimate from artifacts you already have:
- **Input** = brand context tokens (measure once with Method B, or use the ~62K figure below) x number of LLM calls that re-load it.
- **Output** = word count of the produced batch x 1.33 (words-to-tokens rule of thumb), plus a gate overhead.
This is what Part 2 does.

### Recording each run
Log every measured run in the table at the bottom of this doc so estimates converge on reality over time.

---

## Part 2: Grounded estimate for one `generate-batch` run

These figures are measured from this repo (brand-doc word counts and a real produced batch), then converted to tokens at **1 word ~= 1.33 tokens**.

### Input side
| Component | Measured | Tokens (approx) |
|---|---|---|
| Full brand context loaded per run | ~46,800 words | **~62,000** |
| Re-reads across drafting + gate steps (the context is referenced by multiple sub-steps: draft, linkedin-check, image-brief, validate, voice-check) | ~5x effective | see note |

**Note on the multiplier:** a batch is not one API call. The orchestrator drafts each asset and then runs several gates, and each step needs the relevant rules in context. Without caching, that is roughly 5x the 62K base = **~310K input tokens**. With prompt caching on the stable brand prefix (cache reads at ~10% of input price), the *billed* input collapses toward roughly **62K full-price + ~250K at cache-read rate**.

### Output side
| Component | Measured | Tokens (approx) |
|---|---|---|
| One full batch of drafts (blog, podcast script, 3 LinkedIn, 5 Facebook, clips, metadata) | 16 files, ~22,000 words | **~29,000** |
| Gate outputs (checklists, validation verdicts, image briefs, revision diffs) | additive | **~10,000 - 20,000** |
| **Total output** | | **~40,000 - 50,000** |

### Cost per batch run

**Without caching (upper bound):**
- Input: 310,000 / 1,000,000 x $3.00 = **$0.93**
- Output: 50,000 / 1,000,000 x $15.00 = **$0.75**
- **Total ~= $1.68 per batch**

**With prompt caching (realistic, repeated runs in a session):**
- Input: (62,000 x $3.00 + 250,000 x $0.30) / 1,000,000 = $0.186 + $0.075 = **$0.26**
- Output: 50,000 / 1,000,000 x $15.00 = **$0.75**
- **Total ~= $1.01 per batch**

### Interpretation
A full week's content batch costs on the order of **$1 to $2 in model usage**. Even at a high re-run rate (say 3 passes to get a batch fully through the gates), a single week stays in the **$3 to $6** range. Across a 52-week editorial year, model cost is on the order of **$150 to $300**, which is negligible relative to the value of the output. This is the core reason the Sonnet 4.6 default is correct: the task does not need a model 5x more expensive.

> These are estimates. Replace them with Method A measurements as soon as the first isolated run is logged below.

---

## Measured-run log (fill in from Console)

| Date | Workflow + scope | Input tokens | Cache-read tokens | Output tokens | Measured cost | Notes |
|---|---|---|---|---|---|---|
| _pending_ | generate-batch week-NN | | | | | first measured run |
