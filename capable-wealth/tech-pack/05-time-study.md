# Time Study and Throughput

This documents how long a run takes and how to reason about throughput, given that the harness runs **inside Claude Cowork, not a metered cloud API**.

## Monitoring note (important)

The workflows run inside Claude Cowork on **Claude Sonnet 4.6** (confirmed in the model selector), not against a cloud API with a billing dashboard. That has one direct consequence:

- **Token usage cannot be directly monitored.** There is no per-run token meter or billing line to read. The only things you can observe are the **outputs** (the files produced, the run summary, the elapsed time).
- **So monitoring focuses on outputs**, not tokens: did the batch produce the full file set, did it finish cleanly, did any piece get a Yellow/Red flag, and how long did it take.
- **The practical capacity question is "how many batches can I run in a usage window before hitting my limit,"** which is answered empirically by running batches and watching the usage window, not by reading a token dashboard.

Token *volume* can still be **estimated** from the observable outputs (see the throughput section below), but it is an estimate used for planning, not a measured cost.

---

## Generation time

`generate-batch` is the most generation-heavy skill in the system. It produces the most content of any skill (a full week: blog, podcast script, 3 LinkedIn posts, 5 Facebook posts, clips, plus the optional native video and carousel), and it runs every quality gate during the run, so it takes the longest.

**Measured baseline: a single week takes roughly 15 to 20 minutes to produce.**

Multi-week batches scale roughly linearly. Using the conservative (upper-bound) figure for planning:

| Batch scope | Realistic range | Conservative planning figure |
|---|---|---|
| 1 week | 15 to 20 min | **20 min** |
| 2 weeks | 30 to 40 min | **40 min** |
| 3 weeks | 45 to 60 min | **60 min** |
| 4 weeks | 60 to 80 min | **80 min** |

Plan with the conservative figure. Actual time varies with the number of pieces flagged for revision and the depth of the gate passes.

The other skills (`validate`, `voice-check`, `linkedin-check`, `image-brief`, `research-scan`) are far lighter and run in well under a couple of minutes each on a single piece, because they assess existing content rather than generate a full week.

---

## Stages within a generate-batch run

The 15 to 20 minutes per week is spread across these stages (all machine time; no blocking human pause occurs during the run):

| Stage | What happens |
|---|---|
| 1. Load context | Read the relevant skill, link all required skills, load brand docs and rules |
| 2. Resolve week to dates | Map week number to dates; date-alignment check |
| 3. Draft core pieces | Blog, podcast, 3 LinkedIn, 5 Facebook, clips |
| 4. Run gates | image-brief, linkedin-check, **voice-check on every piece**, validate |
| 5. Apply fixes | Resolve flagged items, literal em-dash and pivot scan |
| 6. Write + export | Write files, completeness check, regenerate Excel summary |
| 7. Summarize | Post the run summary (file count by channel, any Yellow flags) |

## Human-in-the-loop dependency (after the run)

The run itself does not pause. The human dependency happens **after** the machine finishes:

- **Read-through before scheduling.** Jared reviews the completed batch before anything is scheduled. The run summary surfaces whether any piece carries a Yellow flag needing his eye (a clean run reports "No Yellow flags requiring Jared's review. Ready for his read-through before scheduling").
- This review time is human-paced and separate from the 15 to 20 minute machine time. Total elapsed = machine time + Jared's read-through.

---

## Throughput: estimating batches per session

Since tokens are not metered, throughput is estimated from observable outputs and then confirmed empirically against the Claude Max usage window.

### Token volume per batch (estimate, not a bill)

Estimated from the actual artifacts in this repo (1 word is about 1.33 tokens):

- **Input side (inferred):** each run loads the skill, links all required skills, and processes the brand context and rules (including the voice-check pass). The loaded context is roughly **70K tokens** (about 47K words of brand docs plus about 5K words of skill files). Because the model re-reads and reasons over this context across many turns during a 15 to 20 minute run, the **cumulative** input processed across the run is a multiple of that, not a single 70K read.
- **Output side (observed):** one week of final content measures about **13K to 22K words** (Week 25, for example, is 15 files and about 12.8K words), which is roughly **17K to 29K output tokens** for the deliverables, plus the gate outputs, the run summary, and the model's working reasoning.

Both the inferred input and the observed output count toward the usage that draws down a Claude Max session. Adding them gives a per-batch volume figure you can use for planning.

### Why the reliable number is empirical, not a division

Claude Max usage is governed by a **rolling usage window** (a multiple of Pro usage, refreshing on a schedule), not by a published fixed token allowance per session. Anthropic does not publish an exact "X tokens per session" number, and effective capacity shifts with model and message size. So dividing a published allowance by the per-batch estimate would be guessing.

The dependable method:

1. Start a fresh usage window.
2. Run batches back to back, logging each one in the table below.
3. Record the batch at which you hit the usage limit. **That count is your real batches-per-window number.**
4. Repeat once or twice to confirm it is stable.

The token estimate above tells you the *relative weight* of a batch (a 4-week batch draws down roughly 4x a 1-week batch), so once you know how many 1-week batches fit in a window, you can predict multi-week capacity.

### Throughput log (fill in empirically)

| Date | Window start | Batches completed before limit | Batch scope each | Notes |
|---|---|---|---|---|
| _pending_ | | | | first capacity test |

---

## Summary

- A week of content takes **15 to 20 minutes** of machine time; plan multi-week batches at the conservative figures above.
- It runs in Cowork, not a cloud API, so **tokens are not monitorable**; monitor **outputs** and **batches per usage window** instead.
- Token volume can be **estimated** from outputs for planning, but **batches-per-window is measured empirically** because Claude Max uses a rolling usage window, not a fixed published token allowance.
