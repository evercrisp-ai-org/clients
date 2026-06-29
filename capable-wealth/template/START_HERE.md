# Content Production Engine: Command Center

> This document is your single orientation point for the content production system. It tells you what every file does, where you are in the process, and gives you copy-paste-ready prompts to execute each session in a fresh Cursor Agent chat.

---

## A. File Map

### Brand Foundation (Single Source of Truth)

| File | Purpose | When to Reference |
|------|---------|-------------------|
| `brand/voice-profile.md` | **WHO**: Voice owner's philosophy, writing style, structural patterns, rhetorical toolkit | Before creating any content. Updated via Recursive Learning. |
| `brand/content-recipe.md` | **HOW**: Production workflow, building blocks, quality gates, audience translation, voice calibration | Before creating any content. Updated quarterly via Recursive Learning. |
| `brand/content-calendar.md` | **WHEN**: Annual cycles, research checkpoints, signal triggers, source library | For timing decisions and relevance validation. Updated monthly. |
| `brand/brand_config.json` | **LOOK + TONE**: Visual standards, colors, fonts, imagery rules, channel config, and calibrated brand voice attributes | For designed deliverables AND voice/language guidance. |
| `brand/experience-inventory.md` | **WHAT YOU CAN CLAIM**: Verified stories, professional facts, and experience boundaries | Before drafting any content with client stories or experience claims. |
| `brand/experience-interview-guide.md` | **DEEP DIVE**: Structured questions to populate the experience inventory | When onboarding or updating the experience inventory. |
| `brand/performance-log-template.md` | **MEASURE**: Standardized format for logging real engagement metrics | Before running a Recursive Learning cycle. Copy to `outputs/performance-logs/`. |
| `brand/system-guide.md` | **GUIDE**: Stakeholder-facing walkthrough of the entire content system | Share with voice owner as orientation. |

### Source Material

| File / Directory | Purpose | When to Reference |
|-----------------|---------|-------------------|
| `samples/` | Representative content pieces. The raw material the voice profile was built from. | When calibrating voice or resolving "would they say it this way?" questions. |

### Outputs

| Directory | Purpose |
|-----------|---------|
| `outputs/drafts/` | Work in progress: content batches, draft reports. |
| `outputs/final/` | Published, approved deliverables. |
| `outputs/performance-logs/` | Performance data logs with real engagement metrics. |
| `outputs/learning-reviews/` | Recursive Learning cycle outputs. |

### Planning Documents (Created in Sessions 2-3)

| File | Purpose | Created In |
|------|---------|------------|
| `brand/editorial-plan.md` | 12-month editorial plan with monthly themes and content ideas | Session 2 |
| `brand/quarterly-plan-Q[N].md` | Quarterly drill-down with weekly content slots by channel | Session 3 |

---

## B. Progress Checklist

Track your progress through the content system build-out:

- [ ] **Session 0:** Integration complete
  - [ ] Template copied and placeholders replaced
  - [ ] Recalibrating Interview completed
  - [ ] Brand & Voice Alignment Guide followed
  - [ ] Validation smoke test passed
- [ ] **Session 1:** Voice profile generated from samples
  - [ ] `brand/voice-profile.md` complete and reviewed by voice owner
  - [ ] AI-giveaway detection run; banned patterns documented
- [ ] **Session 2:** 12-month editorial plan populated (`brand/editorial-plan.md`)
- [ ] **Session 3:** Current quarter drilled down to weekly content slots by channel
- [ ] **Session 4:** First batch of content generated
- [ ] **Session 5:** First Recursive Learning cycle completed

---

## C. Session Prompts

Copy-paste the prompt for your next session into a fresh Cursor Agent chat. Each prompt is self-contained.

---

### Session 1: Generate Voice Profile from Samples

**What this produces:** A complete voice profile document (`brand/voice-profile.md`) distilled from your sample content.

**Prerequisites:** Sample content in `samples/` (10-30+ pieces), completed Recalibrating Interview, populated `brand/brand_config.json`.

**Copy-paste this prompt:**

```
I need you to generate a voice profile for [ORG_NAME] by analyzing sample content.

Read the following:
- All content files in @samples/ -- these are real pieces written by (or representing) [PERSON_NAME]. Analyze every one.
- @brand/brand_config.json -- the voice_and_tone section contains initial voice attributes from the Recalibrating Interview.
- @brand/voice-profile.md -- this is the template structure to fill in.

Analyze all the sample content and produce a complete voice profile following the template structure:

**Section 1: The Person Behind the Voice** (or "The Brand Voice" if institutional)
- Background: Who is this person? What is their story?
- Credibility model: Where does their authority come from?
- The role they play: How do they position themselves relative to the reader?

**Section 2: Core Philosophy / Belief System**
- Identify 3-8 foundational beliefs that run through the samples. These are not topics; they are the lens through which every topic is viewed.
- For each belief, provide a representative quote from the samples.

**Section 3: Voice Characteristics**
- Register: Where does the voice sit on the casual-to-formal spectrum?
- Tone: What emotional qualities define the voice? (warm, direct, cautionary, humorous, etc.)
- Vocabulary patterns: Words and phrases used frequently. Words and phrases never used.
- Emotional range: What different registers does the voice move through?

**Section 4: Structural DNA**
- Recurring post architecture: How do posts typically open, develop, and close?
- Formatting patterns: Paragraph length, header usage, list usage, emphasis patterns.
- Any signature elements (catchphrases, sign-offs, recurring frameworks).

**Section 5: Rhetorical Toolkit**
- Rhetorical questions, contrarian framing, metaphors, analogies, storytelling patterns, data/math as persuasion, named frameworks, emotional appeals.

**Section 6: Anti-Patterns (What the Voice Never Does)**
- Tone the voice avoids (preachy, salesy, academic, etc.)
- Structures the voice avoids
- Vocabulary the voice avoids
- Punctuation patterns (does the voice use em dashes? Exclamation points? Emoji?)

**Section 7: Voice Samples**
- 5-8 direct excerpts from the samples demonstrating key characteristics. Label each with the characteristic it demonstrates.

After generating the profile, run an AI-giveaway detection test:

1. Generate 3 short test paragraphs (2-3 sentences each) on different topics, written in the voice you just profiled.
2. Compare these test paragraphs against the real samples.
3. Note any patterns in the test paragraphs that do not appear in the real samples (punctuation choices, sentence structures, word choices, transition phrases, opening patterns).
4. Add these patterns to the Anti-Patterns section as "Never Use" rules.

Save the output as: brand/voice-profile.md
```

---

### Session 2: Build the Editorial Plan

**What this produces:** A 12-month editorial plan with monthly themes and content ideas.

**Copy-paste this prompt:**

```
I need you to build a 12-month editorial plan for [ORG_NAME], targeting [AUDIENCE].

Read the following foundational documents first:
- @brand/content-calendar.md -- defines the static annual cycles, research checkpoints, and signal-driven triggers. Use Layer 1 (Static Annual Cycles) as the backbone for timing.
- @brand/content-recipe.md -- defines how content gets made. Pay special attention to the Audience Translation Matrix, Voice Calibration Guide, and Topic Mapping.
- @brand/voice-profile.md -- captures the voice and philosophy. Use the Core Philosophy and Rhetorical Toolkit sections to inform content angles.
- @brand/brand_config.json -- for brand voice guidelines and channel configuration.

Now, research current conditions that affect content timing and relevance for [AUDIENCE]:
- Current industry trends, regulations, or legislative changes affecting [AUDIENCE]
- Economic conditions relevant to [AUDIENCE]
- Seasonal or cyclical factors in the industry
- Any upcoming events, deadlines, or milestones [AUDIENCE] cares about

Using all of the above, create a 12-month editorial plan. For each month, provide:

1. **Monthly theme**: aligned to the static annual cycle from content-calendar.md
2. **3-4 content ideas**, each with:
   - Working title (in the voice owner's style)
   - Target angle (the specific insight or reframe)
   - Which core theme it maps to (reference Topic Mapping in content-recipe.md)
   - Primary channel
3. **Relevance flags**: note months where dynamic research is especially critical
4. **Audience context note**: 1-2 sentences on what is happening in the audience's world that month

Save the output as: brand/editorial-plan.md

The plan should feel like a year of content that [AUDIENCE] would look forward to consuming, not a calendar of generic tips.
```

---

### Session 3: Quarterly and Weekly Drill-Down

**What this produces:** A quarterly plan with weekly content slots broken out by channel.

**Copy-paste this prompt:**

```
I need you to drill down the current quarter of the editorial plan into weekly content slots by channel for [ORG_NAME].

Read:
- @brand/editorial-plan.md -- the 12-month plan. Focus on the current quarter.
- @brand/content-recipe.md -- for production standards, channel specifications, and building blocks.
- @brand/content-calendar.md -- for timing alignment and relevance triggers.
- @brand/voice-profile.md -- for voice and angle guidance.
- @brand/brand_config.json -- for channel configuration (which channels, how many posts per week).

For each week in the quarter, produce:

1. **Week number and date range**
2. **Weekly theme** (derived from the monthly theme)
3. **Content slots by channel**, each with:
   - Working title
   - Content angle / brief (2-3 sentences)
   - Which building blocks apply (reference content-recipe.md Section 4)
   - Any relevance dependencies (facts to verify, deadlines to check)
4. **Derivative content map** (if applicable): which anchor pieces generate which derivative posts on other channels

The plan should ensure:
- Every week has content on every active channel (per brand_config.json channel_config)
- Anchor content (blog/podcast) is produced first; derivative posts flow from it
- No two consecutive weeks feel repetitive in theme or angle
- Relevance-sensitive content is timed correctly (content-calendar.md alignment)

Save the output as: brand/quarterly-plan-Q[N].md
```

---

### Session 4: Produce a Content Batch

**What this produces:** A batch of content drafts for a specified number of weeks, following the Standard Draft File Format.

**Copy-paste this prompt:**

```
I need you to produce a content batch for [ORG_NAME] covering [WEEK RANGE] of the quarterly plan.

Read the following documents:
- @brand/quarterly-plan-Q[N].md -- the specific weeks and content slots to produce.
- @brand/voice-profile.md -- the definitive voice reference. Every piece must sound like [PERSON_NAME].
- @brand/content-recipe.md -- for production standards, building blocks, visual asset guidelines (Section 10), draft file format (Section 12), and quality checklist (Section 13).
- @brand/brand_config.json -- for exact brand colors, fonts, imagery rules, and channel specifications.
- @brand/experience-inventory.md -- for content integrity: what can be claimed as real vs illustrative.
- @brand/content-calendar.md -- for relevance validation and timing alignment.

For each content slot in the specified weeks, produce a complete draft file following the Standard Draft File Format (content-recipe.md Section 12):

1. **Post Metadata**: type, week, theme, quarterly plan reference, strategic context, story classifications used
2. **Visual Assets**: image type, rationale, production-ready AI image prompt (9-point standard from Section 10), text overlay, platform/dimensions
3. **Clip Extraction Map** (podcast/video scripts only): 2-5 clip candidates with hook, insight, platform tags, duration
4. **Full content draft**: written in the voice owner's voice per voice-profile.md and content-recipe.md
5. **Quality Checklist**: all items from Section 13 evaluated

Production rules:
- Every piece must pass all Quality Checklist items
- All client stories must be classified per the Content Integrity Filter
- All facts and figures must be current as of publication date
- AI image prompts must be fully self-contained and production-ready
- Content must be appropriately timed (content-date-alignment rule)

Save each piece as a separate file:
outputs/drafts/content-batch-[YYYY-MM-DD]/week-N-channel-N.md

Use the file naming convention from content-recipe.md.
```

---

### Session 5: Recursive Learning Cycle

**What this produces:** A "What We Learned" brief, recommended updates to master documents, and the next production queue.

**Prerequisites:** A completed performance data log in `outputs/performance-logs/`.

**Copy-paste this prompt:**

```
It is time to run a Recursive Learning cycle for [ORG_NAME] content production.

Read the following documents:
- @brand/content-recipe.md Section 11 (The Recursive Learning Loop) -- defines the five-stage process.
- @outputs/performance-logs/log-[YYYY-MM-DD].md -- the performance data log for this cycle. This contains the real engagement metrics that drive the analysis.
- @brand/editorial-plan.md -- the 12-month editorial plan for context.
- @brand/quarterly-plan-Q[N].md -- the quarterly plan we have been executing.
- @brand/content-calendar.md -- for any needed calendar updates.
- @brand/voice-profile.md -- for any voice calibration refinements.

Also review the content in outputs/drafts/ to understand what was created.

Execute the five-stage learning cycle:

**Stage 1: Observe**
- What content was produced? List each piece with its channel, topic, and publish date.
- Review the performance data log: key engagement numbers, top and bottom performers.
- Qualitative feedback: what did people say in comments, replies, and DMs?
- Audience demographics: are we reaching [AUDIENCE], or is a different audience engaging?

**Stage 2: Detect**
- Patterns: which topics outperformed? Which underperformed?
- Channel comparison: which platform produced the strongest results?
- Timing patterns: day of week, proximity to deadlines, seasonal effects?
- Format patterns: which content types drove the most engagement?

**Stage 3: Interpret**
- Root causes: why did certain pieces outperform or underperform?
- Audience insights: what does the data say the audience actually wants?
- Production observations: were there bottlenecks or workflow issues?
- Disconnects: where did expectations diverge from reality?

**Stage 4: Refactor**
- Recommend specific updates to: Content Calendar, Content Recipe, Editorial Plan, Voice Profile, Channel Strategy.
- Each recommendation must be tied to specific data points from the performance log.

**Stage 5: Reflect**
- Write a "What We Learned" brief.
- Identify 2-3 experiments for the next cycle.
- Note data gaps and tracking improvements needed.
- Queue the next production cycle.

Save the output as: outputs/learning-reviews/review-[YYYY-MM-DD].md
```

---

## D. Ongoing Production Prompts

These are shorter, tactical prompts for day-to-day content work.

---

### Write a Social Post

```
Write a [CHANNEL] post for [ORG_NAME] targeting [AUDIENCE].

Read @brand/voice-profile.md and @brand/content-recipe.md (Voice Calibration, Content Architecture, Language Guide, Visual Assets, Draft Format, Quality Checklist).
Also read @brand/brand_config.json for brand colors, fonts, imagery rules, and channel specs.

Topic: [INSERT TOPIC]
Angle: [INSERT SPECIFIC ANGLE OR CONTRARIAN REFRAME]

Output in Standard Draft File Format:
1. Post Metadata
2. Visual Assets (one primary image with production-ready AI prompt per 9-point standard)
3. Content
4. Quality Checklist

Requirements:
- 100-300 words (adjust per channel norms)
- First line must earn attention (bold statement, question, or contrarian hook)
- One core insight, clearly stated
- Include at least one specific number relevant to [AUDIENCE]
- End with a question or clear takeaway
- No hard CTA; the value is the CTA
- Tone per voice-profile.md and channel-specific notes in brand_config.json
```

---

### Write a Blog Post

```
Write a blog post for [ORG_NAME] targeting [AUDIENCE].

Read @brand/voice-profile.md (all sections) and @brand/content-recipe.md (Voice Calibration, Content Architecture, Language Guide, Visual Assets, Draft Format, Quality Checklist).
Also check @brand/content-calendar.md to ensure relevance and timing.
Also read @brand/brand_config.json for brand colors, fonts, and imagery rules.
Also read @brand/experience-inventory.md for content integrity boundaries.

Topic: [INSERT TOPIC]
Angle: [INSERT SPECIFIC ANGLE]

Output in Standard Draft File Format:
1. Post Metadata (including story classifications)
2. Visual Assets (hero image + 1-3 in-body images, all with 9-point AI prompts)
3. Content
4. Quality Checklist

Requirements:
- 800-1,200 words
- Follow the structural DNA from voice-profile.md
- All facts and figures must be current
- All stories classified per Content Integrity Filter
- Close with [SIGN_OFF_PHRASE]
```

---

### Write a Podcast / Video Script

```
Write a podcast/video script for [ORG_NAME] targeting [AUDIENCE].

Read @brand/voice-profile.md and @brand/content-recipe.md (Content Architecture, Language Guide, Visual Assets, Draft Format, Quality Checklist).
Also read @brand/brand_config.json for brand colors and channel specs.

Topic: [INSERT TOPIC]
Angle: [INSERT SPECIFIC ANGLE]

Output in Standard Draft File Format:
1. Post Metadata
2. Visual Assets (thumbnail with 9-point AI prompt)
3. Clip Extraction Map (2-5 standalone clip candidates with hook, insight, platform tags, duration)
4. Content (talking points format, not word-for-word teleprompter script)
5. Quality Checklist

Structure:
- COLD OPEN (30-60s): Hook that pulls the listener in immediately
- CONTEXT (60-90s): Why this matters to [AUDIENCE] specifically
- KEY POINTS (3-5 points): Structured teaching
- CLOSE (30-60s): Philosophical tie-back + invitation to engage

Requirements:
- Max 25 minutes total
- Language should be natural speech, not essay prose read aloud
- Include specific numbers relevant to [AUDIENCE]
```

---

### Run a Relevance Check

```
I need you to validate a piece of content for relevance and timeliness.

Read @brand/content-recipe.md Section 5 (Research and Relevance Filter) and @brand/content-calendar.md.

Here is the content to validate:
[PASTE DRAFT CONTENT HERE]

Check:
1. Static Calendar Alignment: Is this correctly timed relative to annual cycles?
2. Dynamic Fact Validation: Are all facts, figures, and references current as of today?
3. Signal-Driven Relevance: Is there anything happening right now that this content should acknowledge or that conflicts with it?

Produce a Relevance Score:
- Green: Timely, current, no conflicts. Publish.
- Yellow: Needs specific updates. List what needs to change.
- Red: Stale, conflicting, or poorly timed. Hold and explain why.
```

---

### Run a Voice Check

```
I need you to evaluate a piece of content against the voice profile.

Read @brand/voice-profile.md (all sections) and @brand/content-recipe.md Voice Calibration Guide.

Here is the content to evaluate:
[PASTE DRAFT CONTENT HERE]

Evaluate:
1. Does it open with a story, conversation, or specific scenario?
2. Does the tone match the voice profile (register, warmth, directness)?
3. Does it use the voice owner's vocabulary patterns and avoid banned vocabulary?
4. Does it follow the structural DNA?
5. Are there any anti-patterns present?
6. Does it match the audience calibration (keeps, elevates, retires, adds)?
7. Is it free of AI-giveaway patterns (em dashes, formulaic pivots, banned words)?

For each item, score Pass/Fail and provide specific feedback. If any fail, suggest concrete revisions.
```

---

### Log Performance Data

```
I need to log performance data for recently published [ORG_NAME] content.

Read @brand/performance-log-template.md for the standardized format.

Review period: [INSERT START DATE] to [INSERT END DATE]
Content batch: [e.g., content-batch-YYYY-MM-DD]

I have pulled the following data from my platform analytics:
[PASTE YOUR RAW ANALYTICS DATA HERE]

Using the template, produce a completed performance log:
1. Per-piece data (engagement metrics, platform-specific metrics, qualitative feedback)
2. Batch Summary (top performers, underperformers, audience growth, channel comparison)
3. Open Questions (patterns or anomalies worth investigating)

Save as: outputs/performance-logs/log-[YYYY-MM-DD].md
```

---

### Run a Monthly Research Scan

```
I need you to run the monthly research scan for [ORG_NAME] content.

Read @brand/content-calendar.md Layer 2 (Dynamic Research Checkpoints) for the scan checklist and output format.

Today's date: [INSERT DATE]

Run through the monthly scan checklist:
- Industry developments affecting [AUDIENCE]
- Regulatory or legislative changes
- Economic conditions relevant to [AUDIENCE]
- Market events or trends
- Industry news, publications, or conference announcements

Produce the scan in the output format from content-calendar.md:
- What Changed (with sources)
- Content Impact (existing content affected + recommended action)
- Recommended Actions

If any findings warrant urgent content, flag that explicitly.

Append the output to the Update Log section of brand/content-calendar.md.
```

---

## E. Validation Smoke Test

Run this after completing integration and voice-profile generation to verify the system is correctly configured.

```
I need you to run a configuration validation test for the [ORG_NAME] content production system.

Read:
- @brand/voice-profile.md
- @brand/brand_config.json
- @brand/content-recipe.md
- @brand/experience-inventory.md

Generate a single test LinkedIn post (or the primary social channel from brand_config.json channel_config) on a topic relevant to [AUDIENCE].

After generating the post, validate:

1. **Organization name:** Does the post reference [ORG_NAME] correctly (not any placeholder or other org)?
2. **Voice:** Does the post match the voice profile's tone, register, and vocabulary?
3. **Sign-off:** Is [SIGN_OFF_PHRASE] used correctly (or omitted correctly for social)?
4. **Audience:** Is the content clearly written for [AUDIENCE] (not a generic audience)?
5. **Banned language:** Does the post avoid all items in brand_config.json voice_and_tone.language_to_avoid?
6. **AI giveaways:** Is it free of em dashes, formulaic pivots, and all patterns in the anti-patterns list?
7. **Visual asset:** Does the AI image prompt use the correct brand colors (check hex codes against brand_config)?
8. **Content integrity:** Is a story classification present if any example or scenario is used?
9. **Quality checklist:** Does the post pass all applicable items from content-recipe.md Section 13?

Report: PASS or FAIL for each item. If any fail, state which file needs to be corrected and what the fix is.
```

---

## F. Quick Reference

### Content Production Shortcut

For any piece of content, the minimum viable workflow is:

1. Check `brand/content-calendar.md`: Is this the right time?
2. Reference `brand/voice-profile.md`: Does this sound right?
3. Follow `brand/content-recipe.md`: Does this meet the quality gates?
4. Publish.

### When Something Feels Off

- **Content doesn't sound right?** Re-read voice-profile.md Sections 3, 5, and 6.
- **Not sure if the topic fits the audience?** Check content-recipe.md Audience Translation Matrix and Topic Mapping.
- **Facts might be stale?** Run a Relevance Check (prompt above).
- **Not sure what to write next?** Check the editorial plan and quarterly plan, or run a Monthly Research Scan.
- **AI output has a "tell"?** Run the AI-giveaway detection process from BRAND_VOICE_ALIGNMENT_GUIDE.md Section 3.
