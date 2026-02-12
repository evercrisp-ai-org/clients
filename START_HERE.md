# Capable Wealth — Content Command Center

> This document is your single orientation point for the Capable Wealth content system. It tells you what every file does, where you are in the process, and gives you copy-paste-ready prompts to execute each session in a fresh Cursor Agent chat.

---

## A. File Map

### Brand Foundation (Single Source of Truth)

| File | Purpose | When to Reference |
|------|---------|-------------------|
| `brand/voice-profile.md` | **WHO** — Jared's voice, philosophy, writing style, structural patterns, rhetorical toolkit | Before creating any content. Rarely updated. |
| `brand/content-recipe.md` | **HOW** — Production workflow, building blocks, quality gates, audience translation, voice calibration, relevance filter | Before creating any content. Updated quarterly via Recursive Learning. |
| `brand/content-calendar.md` | **WHEN** — Annual cycles, research checkpoints, signal triggers, source library | For timing decisions and relevance validation. Updated monthly. |
| `brand/brand_config.json` | **LOOK + TONE** — Visual standards, colors, fonts, imagery rules, and calibrated brand voice attributes | For designed deliverables AND voice/language guidance. The `voice_and_tone` section defines the calibrated output voice for the surgeon audience. |

### Source Material

| File / Directory | Purpose | When to Reference |
|-----------------|---------|-------------------|
| `example-blog-posts/` | 126 original blog posts by Jared. The raw material the voice profile was built from. | When calibrating voice or resolving "would Jared say it this way?" questions. |
| `operating-framework/AI_Ready_Leader_FINAL.md` | Ben's book manuscript — the intellectual backbone and operating philosophy. | For strategic decisions, framework design, or when the content recipe references operating principles. |
| `examples/tax_strategies_report.json` | Sample report content showing how content feeds the PDF generation pipeline. | When creating lead magnets or reports. |
| `examples/sample_report_content.json` | Shorter 8-page sample report content. | Same as above. |

### Templates and Infrastructure

| File / Directory | Purpose |
|-----------------|---------|
| `templates/` | Page layout templates (JSON) for branded PDF reports. |
| `src/` | Python PDF generation code (ReportLab-based). |
| `brand/fonts/` | Playfair Display (headings) and Inter (body) font files. |

### Outputs

| Directory | Purpose |
|-----------|---------|
| `outputs/drafts/` | Work in progress — content batches, draft reports. |
| `outputs/final/` | Published, approved deliverables. |
| `outputs/learning-reviews/` | Recursive Learning cycle outputs. (Created in Session 5.) |

### Planning Documents (Created in Sessions 2-3)

| File | Purpose | Created In |
|------|---------|------------|
| `brand/editorial-plan-2026.md` | 12-month editorial plan with monthly themes and content ideas | Session 2 |
| `brand/quarterly-plan-Q[N]-2026.md` | Quarterly drill-down with weekly content slots by channel | Session 3 |

---

## B. Progress Checklist

Track your progress through the content system build-out:

- [x] **Session 1:** Foundation documents built
  - [x] `brand/voice-profile.md` — Voice capture complete
  - [x] `brand/content-recipe.md` — Content recipe complete
  - [x] `brand/content-calendar.md` — Relevance calendar complete
  - [x] `START_HERE.md` — Command center complete
- [ ] **Session 2:** 12-month editorial plan populated (`brand/editorial-plan-2026.md`)
- [ ] **Session 3:** Current quarter drilled down to weekly content slots by channel
- [ ] **Session 4:** First batch of content generated (LinkedIn, YouTube, Facebook, blog)
- [ ] **Session 5:** Production rhythm established, first Recursive Learning cycle completed

---

## C. Session Prompts

Copy-paste the prompt for your next session into a fresh Cursor Agent chat. Each prompt is self-contained — it provides all the context needed through `@` file references.

---

### Session 2: Build the 12-Month Editorial Plan

**What this produces:** A 12-month editorial plan (March 2026 - February 2027) with monthly themes, 3-4 content ideas per month, and relevance flags.

**Copy-paste this prompt:**

```
I need you to build a 12-month editorial plan for Capable Wealth, a financial advisory brand targeting orthopedic surgeons ages 45-65 approaching practice transition or retirement.

Read the following foundational documents first:

- @brand/content-calendar.md — This defines the static annual cycles, research checkpoints, and signal-driven triggers. Use Layer 1 (Static Annual Cycles) as the backbone for timing.
- @brand/content-recipe.md — This defines how content gets made. Pay special attention to Section 8 (Topic Mapping), Section 2 (Audience Translation Matrix), and Section 3 (Voice Calibration Guide).
- @brand/voice-profile.md — This captures Jared's voice and philosophy. Use the Core Philosophy and Rhetorical Toolkit sections to inform content angles.
- @brand/brand_config.json — For brand voice guidelines in the "voice_and_tone" section.

Now, research current conditions that affect content timing and relevance:
- 2026 federal tax brackets, rates, and standard deduction amounts
- 2026 retirement contribution limits (401k, IRA, HSA, cash balance plan, defined benefit)
- Current estate and gift tax exemption amounts and the status of the sunset provision
- Current Federal Reserve interest rate and forward guidance
- Any pending or recently passed legislation affecting physician taxes, retirement, or healthcare
- Current orthopedic practice economics (average compensation, valuation multiples, industry trends)

Using all of the above, create a 12-month editorial plan covering March 2026 through February 2027. For each month, provide:

1. **Monthly theme** — aligned to the static annual cycle from content-calendar.md
2. **3-4 content ideas** — each with:
   - Working title (in Jared's contrarian/curiosity-driven style)
   - Target angle (the specific insight or reframe)
   - Which of Jared's original themes it maps to (reference Topic Mapping in content-recipe.md)
   - Primary channel (blog, LinkedIn, YouTube, or Facebook)
3. **Relevance flags** — note months where dynamic research is especially critical (e.g., year-end tax window, estate sunset, Fed decisions)
4. **Surgeon context note** — 1-2 sentences on what's happening in the surgeon's world that month

Save the output as: brand/editorial-plan-2026.md

The plan should feel like a year's worth of content that a surgeon would look forward to reading — not a calendar of generic financial tips.
```

---

### Session 3: Quarterly and Weekly Drill-Down by Channel

**What this produces:** The next quarter broken into weekly content slots, each assigned to a specific channel (LinkedIn, YouTube, Facebook, blog) with rationale.

**Copy-paste this prompt:**

```
I need you to take the next quarter from the Capable Wealth editorial plan and drill it down into weekly content slots assigned to specific channels.

Read the following documents:

- @brand/editorial-plan-2026.md — The 12-month plan. Focus on the next quarter (the next 3 months from today's date).
- @brand/content-recipe.md — Pay special attention to Section 7 (Content Architecture Templates) for channel-specific formats, and Section 4 (Content as Building Blocks) for the production workflow.
- @brand/content-calendar.md — For timing precision. Check Layer 1 for upcoming deadlines and Layer 2 for any research checkpoint results.
- @brand/voice-profile.md — For voice reference on all content planning.

For each week in the quarter, assign:

1. **1 anchor piece** — Long-form blog post or article (800-1,200 words). Include:
   - Working title
   - Target angle and key argument
   - The math example to include (specific to surgeon-level numbers)
   - Structural approach (which of Jared's patterns to use)

2. **2-3 LinkedIn posts** — Derived from or complementing the anchor. Include:
   - Hook line (the first line that earns the "see more" click)
   - Core insight (1 sentence)
   - Relationship to the anchor piece

3. **1 YouTube concept** — Not a full script, but:
   - Topic and angle
   - The contrarian hook (first 15 seconds)
   - 3-5 key talking points
   - The philosophical close

4. **1-2 Facebook posts** — Adapted from LinkedIn or standalone. Include:
   - The core idea
   - Tone adjustment notes (more conversational than LinkedIn)

For each piece, include a brief **timing rationale** (why this week — tied to calendar events, deadlines, or signal-driven relevance).

Save the output as: brand/quarterly-plan-Q[N]-2026.md (use the actual quarter number).

The weekly plan should show clear content flow — each week's pieces should feel connected, not random. The anchor piece drives the week's theme, and social content amplifies and extends it.
```

---

### Session 4: Generate the First Content Batch

**What this produces:** Finished content drafts for 2-4 weeks of the quarterly plan — LinkedIn posts, YouTube scripts, Facebook posts, and blog articles.

**Copy-paste this prompt:**

```
I need you to generate the first batch of content from the Capable Wealth quarterly plan. We're going to produce the actual content for the next 2 weeks.

Read the following documents:

- @brand/quarterly-plan-Q[N]-2026.md — The weekly content plan. Focus on the next 2 weeks.
- @brand/voice-profile.md — This is your primary voice reference. Every piece must sound like Jared. Study the Voice Characteristics, Structural DNA, Rhetorical Toolkit, and Voice Samples sections carefully.
- @brand/content-recipe.md — Follow the Building Block workflow (Section 4): Research → Brief → Draft → Relevance Validation → Voice Validation. Use the Quality Checklist (Section 11) as the final gate for every piece.
- @brand/content-calendar.md — For relevance validation. Check all facts, figures, and legal references against current conditions.

For each piece in the 2-week window, produce:

**Blog posts (800-1,200 words each):**
- Follow Jared's 6-step structural DNA: hook → reframe → core teaching → math example → philosophical tie-back → sign-off
- Include specific surgeon-level numbers (not generic examples)
- Run through the Quality Checklist and note the result

**LinkedIn posts (150-300 words each):**
- First line must earn the "see more" click
- One core insight per post
- End with a question or clear takeaway
- Ready to copy-paste into LinkedIn

**YouTube scripts (talking points outline):**
- Hook (15-30 seconds)
- Context and stakes (30-60 seconds)
- 3-5 key points (60-90 seconds each)
- Philosophical close (30-60 seconds)
- Written as natural speech, not essay prose

**Facebook posts (100-200 words each):**
- More conversational than LinkedIn
- One idea, one takeaway
- Drive engagement through questions

After producing each piece, run it through the Quality Checklist from content-recipe.md Section 11. Flag any items that are Yellow (need revision) and fix them before finalizing.

Organize the output into a folder: outputs/drafts/content-batch-[YYYY-MM-DD]/ with individual files:
- week-1-blog-[slug].md
- week-1-linkedin-1.md, week-1-linkedin-2.md, etc.
- week-1-youtube-[slug].md
- week-1-facebook-1.md, week-1-facebook-2.md, etc.
- (repeat for week 2)

Every piece of content should pass two tests: (1) Does this sound like Jared? and (2) Could this only have been written for orthopedic surgeons?
```

---

### Session 5: Recursive Learning Cycle

**What this produces:** A "What We Learned" brief, recommended updates to master documents, and the next production queue.

**Copy-paste this prompt:**

```
It's time to run the first Recursive Learning cycle for Capable Wealth content production.

Read the following documents:

- @brand/content-recipe.md — Section 10 (The Recursive Learning Loop) defines the five-stage process: Observe → Detect → Interpret → Refactor → Reflect. Section 6 (Human Checkpoints) defines quality governance.
- @brand/editorial-plan-2026.md — The 12-month editorial plan for context.
- @brand/quarterly-plan-Q[N]-2026.md — The quarterly plan we've been executing.
- @brand/content-calendar.md — For any needed calendar updates.
- @brand/voice-profile.md — For any voice calibration refinements.

Also review any content that has been produced in outputs/drafts/ to understand what was created.

Execute the five-stage learning cycle:

**Stage 1: Observe**
- What content was produced? List each piece with its channel and topic.
- What performance data is available? (If no data yet, note what metrics should be tracked going forward.)
- What feedback was received? (If none, note what feedback channels to establish.)

**Stage 2: Detect**
- Identify patterns: Which topics felt strongest? Which formats worked best?
- Are there gaps in the content plan that became apparent during production?
- Did any pieces feel off-voice or off-audience during creation?

**Stage 3: Interpret**
- Why did certain pieces feel stronger than others?
- What does this suggest about what the audience wants?
- Were there production bottlenecks? (e.g., research took too long, voice validation caught many issues)

**Stage 4: Refactor**
- Recommend specific updates to:
  - Content Calendar (new timing insights, adjusted priorities)
  - Content Recipe (workflow improvements, template refinements)
  - Editorial Plan (topic additions, removals, or resequencing)
  - Voice Profile (calibration refinements, if any)
- Document each recommendation with rationale.

**Stage 5: Reflect**
- Write a "What We Learned" brief summarizing the cycle
- Identify 2-3 experiments to try in the next cycle
- Queue the next month's content production (what to produce next, in priority order)

Save the output as: outputs/learning-reviews/review-[YYYY-MM-DD].md

This is not a one-time exercise. It is a recurring rhythm. Each cycle makes the system better.
```

---

## D. Ongoing Production Prompts

These are shorter, tactical prompts for day-to-day content work. Copy-paste into a Cursor Agent chat whenever you need to produce a specific piece.

---

### Write a LinkedIn Post

```
Write a LinkedIn post for Capable Wealth targeting orthopedic surgeons.

Read @brand/voice-profile.md and @brand/content-recipe.md (Sections 3, 7, 9, 11) for voice and format guidance.

Topic: [INSERT TOPIC]
Angle: [INSERT SPECIFIC ANGLE OR CONTRARIAN REFRAME]

Requirements:
- 150-300 words
- First line must earn the "see more" click (bold statement, question, or contrarian hook)
- One core insight, clearly stated
- Include at least one specific number relevant to surgeon-level income
- End with a question to the reader or a clear takeaway
- No hard CTA — the value is the CTA
- Must pass the Quality Checklist in content-recipe.md Section 11
- Tone: warm, direct, confident — like a trusted advisor sharing an insight over coffee
```

---

### Write a Blog Post

```
Write a blog post for Capable Wealth targeting orthopedic surgeons.

Read @brand/voice-profile.md (all sections — this is your voice bible) and @brand/content-recipe.md (Sections 3, 7, 8, 9, 11).
Also check @brand/content-calendar.md to ensure relevance and timing alignment.

Topic: [INSERT TOPIC]
Angle: [INSERT SPECIFIC ANGLE OR CONTRARIAN REFRAME]

Requirements:
- 800-1,200 words
- Follow Jared's 6-step structural DNA:
  1. Personal anecdote or scenario hook (1-2 paragraphs)
  2. Reframe/myth-bust conventional wisdom
  3. Core teaching with bold subheadings, numbered steps, or frameworks
  4. Concrete math example with surgeon-level numbers
  5. Philosophical tie-back to control, purpose, or legacy
  6. Close with "Capably Yours" sign-off
- All facts and figures must be current (verify against content-calendar.md)
- Must pass the Quality Checklist in content-recipe.md Section 11
- The final test: does this sound like Jared, and could it only have been written for orthopedic surgeons?
```

---

### Write a YouTube Script

```
Write a YouTube talking points script for Capable Wealth targeting orthopedic surgeons.

Read @brand/voice-profile.md and @brand/content-recipe.md (Sections 3, 7, 9).

Topic: [INSERT TOPIC]
Angle: [INSERT SPECIFIC ANGLE]

Requirements:
- Talking points outline format (not a word-for-word teleprompter script)
- Hook (15-30 seconds): Contrarian question or surprising stat
- Context (30-60 seconds): Why this matters to orthopedic surgeons specifically
- Key Points (3-5 points, 60-90 seconds each): Structured teaching, each point self-contained
- Close (30-60 seconds): Philosophical tie-back + invitation to engage
- Tone: conversational, as if talking to one surgeon across a desk
- Include specific numbers (surgeon-level income, tax impact, practice valuation)
- Language should be natural speech — not essay prose read aloud
```

---

### Write a Facebook Post

```
Write a Facebook post for Capable Wealth targeting orthopedic surgeons.

Read @brand/voice-profile.md and @brand/content-recipe.md (Sections 3, 7, 9).

Topic: [INSERT TOPIC]

Requirements:
- 100-200 words
- More conversational and personal than LinkedIn
- One idea, one takeaway
- Can include a question to drive comments
- Warm, approachable tone — Jared at his most human
```

---

### Run a Relevance Check

```
I need you to validate a piece of content for relevance and timeliness.

Read @brand/content-recipe.md Section 5 (The Research and Relevance Filter) and @brand/content-calendar.md.

Here is the content to validate:
[PASTE DRAFT CONTENT HERE]

Check the following:
1. Static Calendar Alignment — Is this correctly timed relative to annual cycles?
2. Dynamic Fact Validation — Are all facts, figures, tax rates, contribution limits, and legal references current as of today?
3. Signal-Driven Relevance — Is there anything happening right now (legislation, market events, industry news) that this content should acknowledge or that conflicts with it?

Produce a Relevance Score:
- Green: Timely, current, no conflicts — publish
- Yellow: Needs specific updates — list what needs to change
- Red: Stale, conflicting, or poorly timed — hold and explain why

For any Yellow or Red items, provide specific corrections or recommendations.
```

---

### Run a Voice Check

```
I need you to evaluate a piece of content against Jared's voice profile.

Read @brand/voice-profile.md (all sections) and @brand/content-recipe.md Section 3 (Voice Calibration Guide).

Here is the content to evaluate:
[PASTE DRAFT CONTENT HERE]

Evaluate against the following:
1. Does it open with a story, conversation, or specific scenario?
2. Does it contain a contrarian reframe or myth-bust?
3. Is the tone warm, encouraging, and conversational (not academic, preachy, or salesy)?
4. Does it use direct "you" address?
5. Does it include a concrete math example?
6. Does it tie tactical advice to a bigger life principle?
7. Are there any anti-patterns present (Section 7 of voice-profile.md)?
8. Does it match the voice calibration for surgeons (keep/elevate/retire/add from content-recipe.md)?

For each item, score Pass/Fail and provide specific feedback. If any items fail, suggest concrete revisions.
```

---

### Run a Monthly Research Scan

```
I need you to run the monthly research scan for Capable Wealth.

Read @brand/content-calendar.md Layer 2 (Dynamic Research Checkpoints) for the scan checklist and output format.

Today's date: [INSERT DATE]

Run through the monthly scan checklist:
- Federal Reserve decisions (rate changes, forward guidance)
- Major market movements
- New legislation affecting taxes, retirement, healthcare, or estate planning
- IRS guidance, rulings, or notices for high-income taxpayers
- CMS updates affecting physician reimbursement
- Orthopedic industry news

Produce the scan in the exact output format specified in content-calendar.md:
- What Changed (with sources)
- Content Impact (existing content affected + recommended action)
- Recommended Actions

If any findings warrant an Event-Triggered Scan, flag that explicitly.

Save the output as an update appended to the Update Log section at the bottom of brand/content-calendar.md.
```

---

## E. Quick Reference

### Content Production Shortcut

For any piece of content, the minimum viable workflow is:

1. Check `brand/content-calendar.md` — Is this the right time?
2. Reference `brand/voice-profile.md` — Does this sound like Jared?
3. Follow `brand/content-recipe.md` — Does this meet the quality gates?
4. Publish.

### When Something Feels Off

- **Content doesn't sound right?** → Re-read voice-profile.md Sections 3, 5, and 7.
- **Not sure if the topic fits the audience?** → Check content-recipe.md Section 2 (Audience Translation) and Section 8 (Topic Mapping).
- **Facts might be stale?** → Run a Relevance Check (prompt above).
- **Not sure what to write next?** → Check the editorial plan and quarterly plan, or run a Monthly Research Scan to find signal-driven opportunities.
- **Want to understand the deeper philosophy?** → Read `operating-framework/AI_Ready_Leader_FINAL.md`.
