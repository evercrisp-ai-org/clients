# Weekly pipeline instruction (for the scheduled job)

This is the instruction the scheduled job runs unattended. It is written to be fully self-determining: do not ask clarifying questions, resolve every decision from the repo and these rules, and if something is genuinely ambiguous, make the conservative choice and note it in the run summary rather than stopping.

---

You are running the automated weekly content pipeline for Capable Wealth. Follow the project's always-on guardrails (see `COWORK_PROJECT_INSTRUCTIONS.md`) for everything you produce.

## Step 1: Determine the target week

- The target is the **next un-produced upcoming week** so that its content is ready to publish the following week.
- Infer it from the most recent `outputs/drafts/content-batch-*` folder: the target week is the next sequential week after the latest produced one.
- If that inference is ambiguous, choose the earliest upcoming week that has no draft folder, and state the week number and date range you chose in the run summary.
- Produce **one week** unless this instruction has been edited to specify a multi-week range.

## Step 2: Refresh the plan

Run `research-scan` for the target week. This refreshes that week's already-scheduled items for timeliness using only material already in the repo. It does not fetch new external sources. Carry any "verify before publish" flags it raises into the final summary.

## Step 3: Generate the batch

Run `generate-batch` for the target week. This produces the full mandatory set (blog, podcast script, 3 LinkedIn posts, 5 Facebook posts, 2 to 5 clips, plus the optional native video and carousel) and runs the gates (image-brief, linkedin-check, voice-check, validate) during the run. Apply all production rules and the running ledger.

## Step 4: Verify completeness and integrity

- Confirm on disk that every mandatory file exists for the target week with correct naming. If any are missing, produce them now.
- Run the literal scans: zero em-dash characters, zero "not ... but" / "not ... it's" pivot constructions in any file.
- Confirm every story is classified and listed in Post Metadata.

## Step 5: Export and summarize

- Regenerate the Excel summary: `python3 src/export_content_batch.py outputs/drafts/content-batch-{YYYY-MM-DD}/`.
- Post the run summary to Slack `#content-review` (or print it if Slack is unavailable): target week and date range, theme, file count by channel, validation results (Green / Yellow / Red counts), any "verify before publish" figure flags, and the folder path.

## Step 6: Stop. Do not publish.

- Leave all output in `outputs/drafts/`. Do **not** move anything to `outputs/final/`, do not schedule, and do not publish.
- The run ends here. Jared reviews and approves before anything is scheduled.

## Hard rules for the unattended run

- Never invent or "freshen" a rate, contribution limit, or legal figure. Flag it for human verification instead.
- Never imply a real client relationship; all stories default to `[ILLUSTRATIVE]` with approved framing.
- Never reference a deadline, quarter-close, or event before it has occurred relative to the publish date.
- If you cannot complete a step, write what failed and why in the run summary so a human can pick it up. Do not silently skip it.
