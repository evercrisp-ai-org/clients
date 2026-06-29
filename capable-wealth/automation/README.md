# Automation: scheduled weekly content pipeline

This folder holds the configuration for running the content pipeline on a schedule, so a week's drafts are generated automatically and waiting for Jared's review.

## What it does

On a cron schedule, a Claude agent runs the **weekly pipeline** end to end:

1. `research-scan` to refresh the upcoming week's plan for timeliness.
2. `generate-batch` to produce the full week of content (which internally runs the image-brief, linkedin-check, voice-check, and validate gates).
3. Writes drafts to `outputs/drafts/content-batch-{YYYY-MM-DD}/`, regenerates the Excel summary, and posts the run summary to Slack `#content-review`.

The exact instruction the scheduled job runs is in [`weekly-pipeline.md`](weekly-pipeline.md). That file is written to be **fully self-determining**: an unattended run cannot answer clarifying questions, so the prompt resolves the target week, scope, and completeness on its own.

## Schedule

**4:00 AM Wednesday, local time.**

Cron expression: `0 4 * * 3`  (minute 0, hour 4, any day-of-month, any month, day-of-week 3 = Wednesday)

See [`crontab.example`](crontab.example).

### Why Wednesday 4 AM

The job generates **the upcoming week's** content. Running it early Wednesday means:

- The drafts are ready by Wednesday morning.
- Jared has Wednesday through Friday to do his read-through and approve (the pipeline flags any Yellow items needing his eye; a clean run reports "No Yellow flags requiring Jared's review. Ready for his read-through before scheduling").
- Everything is approved and ready to publish the **following week**, where LinkedIn posts go out Tuesday / Wednesday / Thursday. That gives a comfortable approval buffer of about five days before the first publish.

> Set the timezone on whatever runs the cron. `0 4 * * 3` fires at 4 AM in the scheduler's local timezone. On macOS launchd or a server, confirm the TZ so it does not fire at 4 AM UTC by accident.

## Human-in-the-loop: this automates generation, not publishing

The scheduled job **generates drafts only.** It does not publish, schedule, or send anything. The two human dependencies stay in place:

- **Approval (R9):** drafts land in `outputs/drafts/`, never `outputs/final/`. Jared reviews and approves before anything is scheduled.
- **Figure verification (R2):** any rate-sensitive figure the pipeline flags "verify before publish" must be checked by a person before publishing.

Automation removes the manual labor of *generating* the week. It deliberately does not remove the approval gate. See `../tech-pack/06-risk-assessment.md`.

## Runtime

The schedule is expressed as code in this repo: a standard cron definition (`0 4 * * 3`) in [`crontab.example`](crontab.example), paired with the instruction in [`weekly-pipeline.md`](weekly-pipeline.md). You attach that schedule to whatever execution environment you run it in.

One thing to keep in mind: Claude Cowork is an interactive surface, so a plain unix cron line cannot drive a Cowork chat session by itself. The committed schedule needs an executor that can run a Claude session unattended. Common ways, all using the same `0 4 * * 3` schedule and the same `weekly-pipeline.md` instruction:

- **Claude Code headless CLI** on an always-on machine: OS cron / launchd runs `claude -p "$(cat automation/weekly-pipeline.md)"` from the repo root (this is what `crontab.example` shows).
- **A Claude-native scheduled agent / routine** that runs the pipeline prompt on the cron, if your plan supports scheduled agents.
- **GitHub Actions** (`schedule:` workflow) that checks out the repo and invokes Claude Code in CI, if you prefer it to run off your machine.

The schedule, the pipeline instruction, and the HITL rules are identical across all three; only the executor differs.

## Setup

1. Pick an executor (see above).
2. Point it at [`weekly-pipeline.md`](weekly-pipeline.md) as the instruction to run, from the repo root, on the `0 4 * * 3` schedule in the correct timezone.
3. Ensure it can read this repo (brand docs and skills) and write to `outputs/drafts/`, and reach Slack for the summary.
4. Do a **manual dry run** of `weekly-pipeline.md` first and confirm the output before enabling the schedule.
5. After enabling, monitor the first few automated runs against the outputs (file completeness, Yellow flags, elapsed time).

## Monitoring

Because this runs in Cowork (not a metered API), monitor the **outputs**, not tokens: did the batch produce the full file set, did it finish without Red flags, and did it land in the drafts folder with a regenerated Excel summary. See `../tech-pack/05-time-study.md`.
