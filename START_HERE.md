# Capable Wealth: Content Command Center

> This document is your single orientation point for the Capable Wealth content system. It tells you what every file does, where you are in the process, and gives you copy-paste-ready prompts to execute each session in a fresh Cursor Agent chat.

---

## A. File Map

### Brand Foundation (Single Source of Truth)

| File | Purpose | When to Reference |
|------|---------|-------------------|
| `brand/voice-profile.md` | **WHO**: Jared's voice, philosophy, writing style, structural patterns, rhetorical toolkit | Before creating any content. Rarely updated. |
| `brand/content-recipe.md` | **HOW**: Production workflow, building blocks, quality gates, audience translation, voice calibration, relevance filter | Before creating any content. Updated quarterly via Recursive Learning. |
| `brand/content-calendar.md` | **WHEN**: Annual cycles, research checkpoints, signal triggers, source library | For timing decisions and relevance validation. Updated monthly. |
| `brand/brand_config.json` | **LOOK + TONE**: Visual standards, colors, fonts, imagery rules, and calibrated brand voice attributes | For designed deliverables AND voice/language guidance. The `voice_and_tone` section defines the calibrated output voice for the surgeon audience. |
| `brand/performance-log-template.md` | **MEASURE**: Standardized format for logging real engagement metrics from platform analytics | Before running a Recursive Learning cycle (Session 5). Copy to `outputs/performance-logs/` and fill in with real data. |
| `brand/system-guide.md` | **GUIDE**: Client-facing walkthrough of the entire content system, document relationships, maintenance rhythm, and update procedures | Share with Jared as orientation. Reference when onboarding or when Jared asks how the system works. |

### Source Material

| File / Directory | Purpose | When to Reference |
|-----------------|---------|-------------------|
| `example-blog-posts/` | 126 original blog posts by Jared. The raw material the voice profile was built from. | When calibrating voice or resolving "would Jared say it this way?" questions. |
| `operating-framework/AI_Ready_Leader_FINAL.md` | Ben's book manuscript, the intellectual backbone and operating philosophy. | For strategic decisions, framework design, or when the content recipe references operating principles. |
| `examples/tax_strategies_report.json` | Sample report content showing how content feeds the PDF generation pipeline. | When creating lead magnets or reports. |
| `examples/sample_report_content.json` | Shorter 8-page sample report content. | Same as above. |

### Templates and Infrastructure

| File / Directory | Purpose |
|-----------------|---------|
| `templates/` | Page layout templates (JSON) for branded PDF reports. |
| `src/` | Python code: PDF generation (ReportLab-based) and content batch Excel export. |
| `brand/fonts/` | Playfair Display (headings) and Inter (body) font files. |

### Outputs

| Directory | Purpose |
|-----------|---------|
| `outputs/drafts/` | Work in progress: content batches, draft reports. |
| `outputs/final/` | Published, approved deliverables. |
| `outputs/performance-logs/` | Performance data logs with real engagement metrics from platform analytics. Populated before each Recursive Learning cycle. Template: `brand/performance-log-template.md`. |
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
  - [x] `brand/voice-profile.md`: Voice capture complete
  - [x] `brand/content-recipe.md`: Content recipe complete
  - [x] `brand/content-calendar.md`: Relevance calendar complete
  - [x] `START_HERE.md`: Command center complete
- [ ] **Session 2:** 12-month editorial plan populated (`brand/editorial-plan-2026.md`)
- [ ] **Session 3:** Current quarter drilled down to weekly content slots by channel
- [ ] **Session 4:** First batch of content generated (LinkedIn, YouTube, Facebook, blog)
- [ ] **Session 5:** Production rhythm established, first Recursive Learning cycle completed

---

## C. Session Prompts

Copy-paste the prompt for your next session into a fresh Cursor Agent chat. Each prompt is self-contained. It provides all the context needed through `@` file references.

---

### Session 2: Build the 12-Month Editorial Plan

**What this produces:** A 12-month editorial plan (March 2026 - February 2027) with monthly themes, 3-4 content ideas per month, and relevance flags.

**Copy-paste this prompt:**

```
I need you to build a 12-month editorial plan for Capable Wealth, a financial advisory brand targeting orthopedic surgeons ages 45-65 approaching practice transition or retirement.

Read the following foundational documents first:

- @brand/content-calendar.md, this defines the static annual cycles, research checkpoints, and signal-driven triggers. Use Layer 1 (Static Annual Cycles) as the backbone for timing.
- @brand/content-recipe.md, this defines how content gets made. Pay special attention to Section 8 (Topic Mapping), Section 2 (Audience Translation Matrix), and Section 3 (Voice Calibration Guide).
- @brand/voice-profile.md, this captures Jared's voice and philosophy. Use the Core Philosophy and Rhetorical Toolkit sections to inform content angles.
- @brand/brand_config.json, for brand voice guidelines in the "voice_and_tone" section.

Now, research current conditions that affect content timing and relevance:
- 2026 federal tax brackets, rates, and standard deduction amounts
- 2026 retirement contribution limits (401k, IRA, HSA, cash balance plan, defined benefit)
- Current estate and gift tax exemption amounts and the status of the sunset provision
- Current Federal Reserve interest rate and forward guidance
- Any pending or recently passed legislation affecting physician taxes, retirement, or healthcare
- Current orthopedic practice economics (average compensation, valuation multiples, industry trends)

Using all of the above, create a 12-month editorial plan covering March 2026 through February 2027. For each month, provide:

1. **Monthly theme**: aligned to the static annual cycle from content-calendar.md
2. **3-4 content ideas**, each with:
   - Working title (in Jared's contrarian/curiosity-driven style)
   - Target angle (the specific insight or reframe)
   - Which of Jared's original themes it maps to (reference Topic Mapping in content-recipe.md)
   - Primary channel (blog, LinkedIn, YouTube, or Facebook)
3. **Relevance flags**: note months where dynamic research is especially critical (e.g., year-end tax window, estate sunset, Fed decisions)
4. **Surgeon context note**: 1-2 sentences on what's happening in the surgeon's world that month

Save the output as: brand/editorial-plan-2026.md

The plan should feel like a year's worth of content that a surgeon would look forward to reading, not a calendar of generic financial tips.
```

---

### Session 3: Quarterly and Weekly Drill-Down by Channel

**What this produces:** The next quarter broken into weekly content slots, each assigned to a specific channel (LinkedIn, YouTube, Facebook, blog) with rationale.

**Copy-paste this prompt:**

```
I need you to take the next quarter from the Capable Wealth editorial plan and drill it down into weekly content slots assigned to specific channels.

Read the following documents:

- @brand/editorial-plan-2026.md, the 12-month plan. Focus on the next quarter (the next 3 months from today's date).
- @brand/content-recipe.md, pay special attention to Section 7 (Content Architecture Templates) for channel-specific formats, and Section 4 (Content as Building Blocks) for the production workflow.
- @brand/content-calendar.md, for timing precision. Check Layer 1 for upcoming deadlines and Layer 2 for any research checkpoint results.
- @brand/voice-profile.md, for voice reference on all content planning.

For each week in the quarter, assign:

1. **1 anchor piece**: Long-form blog post or article (800-1,200 words). Include:
   - Working title
   - Target angle and key argument
   - The math example to include (specific to surgeon-level numbers)
   - Structural approach (which of Jared's patterns to use)

2. **2-3 LinkedIn posts**: Derived from or complementing the anchor. Include:
   - Hook line (the first line that earns the "see more" click)
   - Core insight (1 sentence)
   - Relationship to the anchor piece

3. **1 YouTube concept**: Not a full script, but:
   - Topic and angle
   - The contrarian hook (first 15 seconds)
   - 3-5 key talking points
   - The philosophical close

4. **1-2 Facebook posts**: Adapted from LinkedIn or standalone. Include:
   - The core idea
   - Tone adjustment notes (more conversational than LinkedIn)

For each piece, include a brief **timing rationale** (why this week, tied to calendar events, deadlines, or signal-driven relevance).

Save the output as: brand/quarterly-plan-Q[N]-2026.md (use the actual quarter number).

The weekly plan should show clear content flow. Each week's pieces should feel connected, not random. The anchor piece drives the week's theme, and social content amplifies and extends it.
```

---

### Session 4: Generate the First Content Batch

**What this produces:** Finished content drafts for 2-4 weeks of the quarterly plan: LinkedIn posts, YouTube scripts, Facebook posts, and blog articles.

**Copy-paste this prompt:**

```
I need you to generate the first batch of content from the Capable Wealth quarterly plan. We're going to produce the actual content for the next 2 weeks.

Read the following documents:

- @brand/quarterly-plan-Q[N]-2026.md, the weekly content plan. Focus on the next 2 weeks.
- @brand/voice-profile.md, this is your primary voice reference. Every piece must sound like Jared. Study the Voice Characteristics, Structural DNA, Rhetorical Toolkit, and Voice Samples sections carefully.
- @brand/content-recipe.md, follow the Building Block workflow (Section 4): Research, Brief, Draft, Relevance Validation, Voice Validation. Use the Quality Checklist (Section 13) as the final gate for every piece. Study Section 10 (Visual Asset Guidelines) and Section 12 (Standard Draft File Format) carefully.
- @brand/content-calendar.md, for relevance validation. Check all facts, figures, and legal references against current conditions.
- @brand/brand_config.json, for exact brand colors, fonts, and imagery rules. Reference the hex codes and social_image_specs when writing image prompts.

CRITICAL: Every draft file must follow the Standard Draft File Format (content-recipe.md Section 12):
1. Post Metadata (type, week, theme, quarterly plan reference, strategic context)
2. Visual Assets (full image briefs with AI prompts following the 9-point standard)
3. Content (the post itself)
4. Quality Checklist (Section 13 results)

For each piece in the 2-week window, produce:

**Blog posts (800-1,200 words each):**
- Follow Jared's 6-step structural DNA: hook → reframe → core teaching → math example → philosophical tie-back → sign-off
- Include specific surgeon-level numbers (not generic examples)
- Include Visual Asset Briefs: one hero image plus 1-3 in-body images as needed (infographics, data visualizations, stat highlights)
- Every AI image prompt must follow the full 9-point standard (Section 10) with exact canvas dimensions, hex codes, font specs, layout positions, mood, and audience context

**LinkedIn posts (150-300 words each):**
- First line must earn the "see more" click
- One core insight per post
- End with a question or clear takeaway
- Ready to copy-paste into LinkedIn
- Include one Visual Asset Brief with a production-ready AI image prompt (9-point standard)

**YouTube scripts (talking points outline):**
- Hook (15-30 seconds)
- Context and stakes (30-60 seconds)
- 3-5 key points (60-90 seconds each)
- Philosophical close (30-60 seconds)
- Written as natural speech, not essay prose
- Include a Thumbnail Brief with a production-ready AI image prompt (9-point standard, 1280x720, text overlay max 5 words)

**Facebook posts (100-200 words each):**
- More conversational than LinkedIn
- One idea, one takeaway
- Drive engagement through questions
- Include one Visual Asset Brief with a production-ready AI image prompt (9-point standard)

After producing each piece, run it through the Quality Checklist from content-recipe.md Section 13, including the Visual Assets checklist. Flag any items that are Yellow (need revision) and fix them before finalizing.

Organize the output into a folder: outputs/drafts/content-batch-[YYYY-MM-DD]/ with individual files:
- week-1-blog-[slug].md
- week-1-linkedin-1.md, week-1-linkedin-2.md, etc.
- week-1-youtube-[slug].md
- week-1-facebook-1.md, week-1-facebook-2.md, etc.
- (repeat for week 2)

Every piece of content should pass three tests: (1) Does this sound like Jared? (2) Could this only have been written for orthopedic surgeons? (3) Is the AI image prompt detailed enough to produce a brand-consistent visual in any generator?

After generating all content files, export the batch to an Excel summary spreadsheet:

python3 src/export_content_batch.py outputs/drafts/content-batch-[YYYY-MM-DD]/

This creates content-batch-summary-[YYYYMMDD].xlsx in the batch folder with one sheet per platform (Blog, LinkedIn, Facebook, YouTube). Each row contains the full content in a single cell for easy copy/paste, plus metadata, visual asset briefs, and source file references. The spreadsheet is formatted with branded headers, week separators, and frozen panes for quick navigation.
```

---

### Session 5: Recursive Learning Cycle

**What this produces:** A "What We Learned" brief, recommended updates to master documents, and the next production queue.

**Before running this prompt:** You must first fill in a performance data log with real metrics from your platform analytics. Copy `brand/performance-log-template.md` to `outputs/performance-logs/log-[YYYY-MM-DD].md` and populate it with actual data from LinkedIn Analytics, YouTube Studio, Facebook Insights, and your website analytics. The learning cycle cannot produce meaningful insights without real performance data. See the "Log Performance Data" prompt in Section D if you need guidance on filling in the log.

**Copy-paste this prompt:**

```
It's time to run a Recursive Learning cycle for Capable Wealth content production.

Read the following documents:

- @brand/content-recipe.md, Section 11 (The Recursive Learning Loop) defines the five-stage process and its prerequisite: real performance data. Section 6 (Human Checkpoints) defines quality governance.
- @outputs/performance-logs/log-[YYYY-MM-DD].md, the performance data log for this cycle. This contains the real engagement metrics, audience data, and qualitative feedback that drives the entire analysis. (Replace [YYYY-MM-DD] with the actual log file date.)
- @brand/editorial-plan-2026.md, the 12-month editorial plan for context.
- @brand/quarterly-plan-Q[N]-2026.md, the quarterly plan we've been executing.
- @brand/content-calendar.md, for any needed calendar updates.
- @brand/voice-profile.md, for any voice calibration refinements.

Also review any content that has been produced in outputs/drafts/ to understand what was created.

Execute the five-stage learning cycle:

**Stage 1: Observe**
- What content was produced? List each piece with its channel, topic, and publish date.
- Review the performance data log: What are the key engagement numbers for each piece? Which pieces got the most impressions, engagement, shares, and saves?
- What qualitative feedback was received? What did people actually say in comments, replies, and DMs?
- What do the audience demographics tell us? Are we reaching orthopedic surgeons 45-65, or is a different audience engaging?

**Stage 2: Detect**
- Identify patterns in the data: Which topics outperformed? Which underperformed? What do the top performers have in common?
- Which channels produced the strongest results? Is one platform clearly outperforming the others?
- Are there timing patterns (day of week, proximity to financial deadlines)?
- Are there gaps in the content plan that became apparent from audience response?
- Did any pieces get unexpected results (positive or negative) that warrant investigation?

**Stage 3: Interpret**
- Why did certain pieces outperform? Was it the topic, the timing, the angle, the headline, the format, or external factors?
- Why did certain pieces underperform? Was it the wrong audience, wrong channel, wrong moment, or wrong execution?
- What does the data suggest about what the audience actually wants (not what we assumed they want)?
- Were there production bottlenecks? (e.g., research took too long, voice validation caught many issues)
- Are there disconnects between what we expected to work and what actually did?

**Stage 4: Refactor**
- Recommend specific updates to:
  - Content Calendar (new timing insights, adjusted priorities based on data)
  - Content Recipe (workflow improvements, template refinements)
  - Editorial Plan (topic additions, removals, or resequencing based on audience response)
  - Voice Profile (calibration refinements based on which tones resonated most)
  - Channel strategy (double down on what's working, adjust or drop what isn't)
- Document each recommendation with rationale tied to specific data points from the performance log.

**Stage 5: Reflect**
- Write a "What We Learned" brief summarizing the cycle
- Identify 2-3 experiments to try in the next cycle (each grounded in a data observation)
- Note what data was most useful and what gaps remain in the performance tracking
- Queue the next month's content production (what to produce next, in priority order, informed by what the data says the audience wants)

Save the output as: outputs/learning-reviews/review-[YYYY-MM-DD].md

This is not a one-time exercise. It is a recurring rhythm. Each cycle makes the system better, but only if it is fed real data from real audience behavior.
```

---

## D. Ongoing Production Prompts

These are shorter, tactical prompts for day-to-day content work. Copy-paste into a Cursor Agent chat whenever you need to produce a specific piece.

---

### Write a LinkedIn Post

```
Write a LinkedIn post for Capable Wealth targeting orthopedic surgeons.

Read @brand/voice-profile.md and @brand/content-recipe.md (Sections 3, 7, 9, 10, 12, 13) for voice, format, visual asset, and file format guidance.
Also read @brand/brand_config.json for exact brand colors, fonts, and imagery rules.

Topic: [INSERT TOPIC]
Angle: [INSERT SPECIFIC ANGLE OR CONTRARIAN REFRAME]

Output the file in the Standard Draft File Format (content-recipe.md Section 12):

1. Post Metadata: type, week, theme, quarterly plan reference, strategic context
2. Visual Assets: one primary image brief with a production-ready AI image prompt following the 9-point standard (content-recipe.md Section 10). The prompt must be fully self-contained with exact canvas dimensions, background hex codes, layout/composition positions, typography specs (font, weight, size, color hex, position), graphic elements, brand constraints with all hex codes, mood descriptors, and audience context. See the example prompts in Section 10.
3. Content: the LinkedIn post itself
4. Quality Checklist: Section 13 results including the Visual Assets checklist

Content requirements:
- 150-300 words
- First line must earn the "see more" click (bold statement, question, or contrarian hook)
- One core insight, clearly stated
- Include at least one specific number relevant to surgeon-level income
- End with a question to the reader or a clear takeaway
- No hard CTA; the value is the CTA
- Tone: warm, direct, confident, like a trusted advisor sharing an insight over coffee
```

---

### Write a Blog Post

```
Write a blog post for Capable Wealth targeting orthopedic surgeons.

Read @brand/voice-profile.md (all sections, this is your voice bible) and @brand/content-recipe.md (Sections 3, 7, 8, 9, 10, 12, 13).
Also check @brand/content-calendar.md to ensure relevance and timing alignment.
Also read @brand/brand_config.json for exact brand colors, fonts, and imagery rules.

Topic: [INSERT TOPIC]
Angle: [INSERT SPECIFIC ANGLE OR CONTRARIAN REFRAME]

Output the file in the Standard Draft File Format (content-recipe.md Section 12):

1. Post Metadata: type, week, theme, quarterly plan reference, strategic context
2. Visual Assets: one hero image brief plus 1-3 in-body image briefs as needed (infographics for frameworks, data visualizations for math examples, stat highlights for key numbers). Every AI image prompt must follow the 9-point standard (Section 10) and be fully self-contained with exact canvas dimensions, background hex codes, layout positions, typography specs, brand constraints, mood, and audience context. See the example prompts in Section 10.
3. Content: the blog post itself
4. Quality Checklist: Section 13 results including the Visual Assets checklist

Content requirements:
- 800-1,200 words
- Follow Jared's 6-step structural DNA:
  1. Personal anecdote or scenario hook (1-2 paragraphs)
  2. Reframe/myth-bust conventional wisdom
  3. Core teaching with bold subheadings, numbered steps, or frameworks
  4. Concrete math example with surgeon-level numbers
  5. Philosophical tie-back to control, purpose, or legacy
  6. Close with "Capably Yours" sign-off
- All facts and figures must be current (verify against content-calendar.md)
- The final test: does this sound like Jared, could it only have been written for orthopedic surgeons, and are the image prompts detailed enough to produce brand-consistent visuals?
```

---

### Write a YouTube Script

```
Write a YouTube talking points script for Capable Wealth targeting orthopedic surgeons.

Read @brand/voice-profile.md and @brand/content-recipe.md (Sections 3, 7, 9, 10, 12, 13).
Also read @brand/brand_config.json for exact brand colors, fonts, and imagery rules.

Topic: [INSERT TOPIC]
Angle: [INSERT SPECIFIC ANGLE]

Output the file in the Standard Draft File Format (content-recipe.md Section 12):

1. Post Metadata: type, week, theme, quarterly plan reference, strategic context
2. Visual Assets: one thumbnail brief with a production-ready AI image prompt following the 9-point standard (Section 10). Thumbnail is 1280x720. Text overlay must be 5 words maximum. The prompt must be fully self-contained with exact canvas dimensions, background hex codes, layout positions, typography specs, brand constraints, mood, and audience context.
3. Content: the YouTube script itself
4. Quality Checklist: Section 13 results including the Visual Assets checklist

Content requirements:
- Talking points outline format (not a word-for-word teleprompter script)
- Hook (15-30 seconds): Contrarian question or surprising stat
- Context (30-60 seconds): Why this matters to orthopedic surgeons specifically
- Key Points (3-5 points, 60-90 seconds each): Structured teaching, each point self-contained
- Close (30-60 seconds): Philosophical tie-back + invitation to engage
- Tone: conversational, as if talking to one surgeon across a desk
- Include specific numbers (surgeon-level income, tax impact, practice valuation)
- Language should be natural speech, not essay prose read aloud
```

---

### Write a Facebook Post

```
Write a Facebook post for Capable Wealth targeting orthopedic surgeons.

Read @brand/voice-profile.md and @brand/content-recipe.md (Sections 3, 7, 9, 10, 12, 13).
Also read @brand/brand_config.json for exact brand colors, fonts, and imagery rules.

Topic: [INSERT TOPIC]

Output the file in the Standard Draft File Format (content-recipe.md Section 12):

1. Post Metadata: type, week, theme, quarterly plan reference, strategic context
2. Visual Assets: one primary image brief with a production-ready AI image prompt following the 9-point standard (Section 10). Quote cards and conceptual photographs work well for Facebook. The prompt must be fully self-contained with exact canvas dimensions, background hex codes, layout positions, typography specs, brand constraints, mood, and audience context.
3. Content: the Facebook post itself
4. Quality Checklist: Section 13 results including the Visual Assets checklist

Content requirements:
- 100-200 words
- More conversational and personal than LinkedIn
- One idea, one takeaway
- Can include a question to drive comments
- Warm, approachable tone, Jared at his most human
```

---

### Run a Relevance Check

```
I need you to validate a piece of content for relevance and timeliness.

Read @brand/content-recipe.md Section 5 (The Research and Relevance Filter) and @brand/content-calendar.md.

Here is the content to validate:
[PASTE DRAFT CONTENT HERE]

Check the following:
1. Static Calendar Alignment: Is this correctly timed relative to annual cycles?
2. Dynamic Fact Validation: Are all facts, figures, tax rates, contribution limits, and legal references current as of today?
3. Signal-Driven Relevance: Is there anything happening right now (legislation, market events, industry news) that this content should acknowledge or that conflicts with it?

Produce a Relevance Score:
- Green: Timely, current, no conflicts. Publish.
- Yellow: Needs specific updates. List what needs to change.
- Red: Stale, conflicting, or poorly timed. Hold and explain why.

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

### Log Performance Data

```
I need to log performance data for recently published Capable Wealth content.

Read @brand/performance-log-template.md for the standardized format.

Review period: [INSERT START DATE] to [INSERT END DATE]
Content batch: [e.g., content-batch-2026-02-12, Weeks 1-2]

I have pulled the following data from my platform analytics. Help me organize it into the performance log format and identify any immediate observations.

[PASTE YOUR RAW ANALYTICS DATA HERE. This can be screenshots described in text, copy-pasted analytics tables, or simply the numbers you've noted down. Include whatever you have from LinkedIn Analytics, YouTube Studio, Facebook Insights, and/or your website analytics for each published piece.]

Using the template, produce a completed performance log:

1. Fill in the per-piece data for each published piece (engagement metrics, platform-specific metrics, qualitative feedback)
2. Complete the Batch Summary section (top performers, underperformers, audience growth, demographic observations, channel comparison)
3. In the "Open Questions" section, flag any patterns or anomalies worth investigating in the next Recursive Learning cycle

Save the output as: outputs/performance-logs/log-[YYYY-MM-DD].md

This log will be used as input for the Recursive Learning cycle (Session 5). The more complete and accurate the data, the more useful the learning cycle will be.
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

1. Check `brand/content-calendar.md`: Is this the right time?
2. Reference `brand/voice-profile.md`: Does this sound like Jared?
3. Follow `brand/content-recipe.md`: Does this meet the quality gates?
4. Publish.

### When Something Feels Off

- **Content doesn't sound right?** → Re-read voice-profile.md Sections 3, 5, and 7.
- **Not sure if the topic fits the audience?** → Check content-recipe.md Section 2 (Audience Translation) and Section 8 (Topic Mapping).
- **Facts might be stale?** → Run a Relevance Check (prompt above).
- **Not sure what to write next?** → Check the editorial plan and quarterly plan, or run a Monthly Research Scan to find signal-driven opportunities.
- **Want to understand the deeper philosophy?** → Read `operating-framework/AI_Ready_Leader_FINAL.md`.
