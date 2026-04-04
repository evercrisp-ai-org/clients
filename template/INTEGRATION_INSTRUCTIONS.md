# Integration Instructions

This document explains how to integrate the Content Production Engine into your project. Choose the path that matches your situation, then follow the steps in order.

---

## Before You Start

You will need:

1. **This template folder** (the one containing this file).
2. **Sample content** -- 10-30+ pieces of existing content that represent the voice you want the system to capture (blog posts, social posts, emails, scripts, etc.).
3. **Brand information** -- colors, fonts, logo, and any existing brand guidelines.
4. **Access to the voice owner** (or key stakeholder) for the Recalibrating Interview.

---

## Path A: Integrate into an Existing Project

Use this when the project already has a repo, existing content, brand assets, or scripts.

### Step 1: Copy the template

Copy this entire template folder into your project. Choose one approach:

- **As a subfolder:** `your-project/content-production-engine/` (keeps the engine self-contained)
- **At project root:** Merge template files into your existing folder structure (use `docs/FILE_MAP.md` for guidance on where each file belongs)

### Step 2: Resolve conflicts

If your project already has files that overlap with the template:

| Template file | If you already have one | Resolution |
|---------------|------------------------|------------|
| `README.md` | Keep yours; add a section linking to the engine's README | Link |
| `brand/` folder | Copy template brand files alongside yours; merge later | Coexist |
| `.cursor/rules/` | Copy template rules into your existing rules folder | Add |
| `src/` | Copy template scripts alongside yours | Coexist |

### Step 3: Create output directories

If they don't already exist:

```
outputs/
  drafts/
  final/
  performance-logs/
  learning-reviews/
```

### Step 4: Add sample content

Place 10-30+ representative content pieces in the `samples/` folder. See `samples/README.md` for accepted formats and guidance.

### Step 5: Replace placeholders

Use the **Placeholder Checklist** below. Do a project-wide find-and-replace for each placeholder, or fill them in manually as you go through the Recalibrating Interview.

### Step 6: Run the Recalibrating Interview

Open `RECALIBRATING_INTERVIEW.md` and work through all 10 sections with the voice owner or key stakeholder. Use the answers to fill or refine `brand/brand_config.json`, `brand/voice-profile.md`, `brand/content-recipe.md`, and `brand/content-calendar.md`.

### Step 7: Generate the voice profile

Run **Session 1** from `START_HERE.md` to analyze your sample content and produce a complete voice profile.

### Step 8: Follow the Brand & Voice Alignment Guide

Open `BRAND_VOICE_ALIGNMENT_GUIDE.md` and work through: branding configuration, AI-giveaway detection, channel setup, compliance rules, and example transformations.

### Step 9: Run the validation smoke test

Run the **Validation Smoke Test** from `START_HERE.md` Section E to verify the system is correctly configured.

### Step 10: Update Cursor rule paths

If your drafts live somewhere other than `outputs/drafts/content-batch-*/**/*.md`, update the `globs` field in each `.cursor/rules/*.mdc` file to match your project's layout.

---

## Path B: Start a New Project from the Template

Use this when the project is brand new and the template is the starting point.

### Step 1: Create the project

Create a new repo or folder for the project.

### Step 2: Copy the template

Copy the **entire contents** of this template folder into the project root. Your project structure will look like:

```
your-project/
  README.md
  INTEGRATION_INSTRUCTIONS.md
  RECALIBRATING_INTERVIEW.md
  BRAND_VOICE_ALIGNMENT_GUIDE.md
  START_HERE.md
  brand/
  samples/
  outputs/
  .cursor/rules/
  src/
  docs/
```

### Step 3: Replace placeholders

Use the **Placeholder Checklist** below. You can do a project-wide find-and-replace now with temporary values, or fill them in during the Recalibrating Interview.

### Step 4: Add sample content

Place 10-30+ representative content pieces in the `samples/` folder. If you don't have samples yet, the Recalibrating Interview will help identify where to find them.

### Step 5: Run the Recalibrating Interview

Open `RECALIBRATING_INTERVIEW.md` and work through all 10 sections with the voice owner or key stakeholder.

### Step 6: Generate the voice profile

Run **Session 1** from `START_HERE.md` to produce the voice profile from your samples.

### Step 7: Follow the Brand & Voice Alignment Guide

Open `BRAND_VOICE_ALIGNMENT_GUIDE.md` to refine branding, detect AI giveaways, configure channels and compliance, and create example transformations.

### Step 8: Run the validation smoke test

Run the **Validation Smoke Test** from `START_HERE.md` Section E.

### Step 9: Proceed to content production

Follow `START_HERE.md` Sessions 2-4 to build your editorial plan, quarterly drill-down, and first content batch.

---

## Summary Table

| Step | Existing Project | New Project |
|------|-----------------|-------------|
| 1 | Copy template into project (subfolder or root) | Create project; copy template to root |
| 2 | Resolve file conflicts per table above | (No conflicts) |
| 3 | Create output directories if needed | (Already included) |
| 4 | Add sample content to `samples/` | Add sample content to `samples/` |
| 5 | Replace placeholders | Replace placeholders |
| 6 | Run Recalibrating Interview | Run Recalibrating Interview |
| 7 | Generate voice profile (Session 1) | Generate voice profile (Session 1) |
| 8 | Follow Alignment Guide | Follow Alignment Guide |
| 9 | Run validation smoke test | Run validation smoke test |
| 10 | Update Cursor rule paths if needed | Proceed to Session 2 |

---

## Placeholder Checklist

Replace every placeholder below across all files. The "Source" column tells you which section of the Recalibrating Interview provides the value.

| Placeholder | Description | Source | Files that use it |
|-------------|-------------|--------|-------------------|
| `[ORG_NAME]` | Your organization's name | Interview Section 1 | All files |
| `[PERSON_NAME]` | The voice owner's name | Interview Section 2 | voice-profile, content-recipe, integrity rule, START_HERE |
| `[AUDIENCE]` | Your target audience description | Interview Section 3 | content-recipe, voice-profile, brand_config, START_HERE, batch rule |
| `[SIGN_OFF_PHRASE]` | How content signs off (e.g., "Best, Jane") | Interview Section 2 | content-recipe, batch rule, START_HERE |
| `[TAGLINE]` | Your organization's tagline | Interview Section 1 | brand_config, README |
| `[PRIMARY_HEX]` | Primary brand color hex code | Interview Section 4 | brand_config |
| `[SECONDARY_HEX]` | Secondary brand color hex code | Interview Section 4 | brand_config |
| `[ACCENT_HEX]` | Accent brand color hex code | Interview Section 4 | brand_config |
| `[LIGHT_NEUTRAL_HEX]` | Light neutral color hex code | Interview Section 4 | brand_config |
| `[DARK_NEUTRAL_HEX]` | Dark neutral color hex code | Interview Section 4 | brand_config |
| `[MID_NEUTRAL_HEX]` | Mid-tone neutral color hex code | Interview Section 4 | brand_config |
| `[HEADING_FONT]` | Heading font family name | Interview Section 4 | brand_config |
| `[BODY_FONT]` | Body font family name | Interview Section 4 | brand_config |
| `[KEY_DEADLINE_1]` | First important deadline | Interview Section 8 | content-calendar, date-alignment rule |
| `[KEY_DEADLINE_2]` | Second important deadline | Interview Section 8 | content-calendar, date-alignment rule |
| `[AUDIENCE_METAPHORS]` | Audience-specific metaphors/bridges | Interview Section 9 | content-recipe, voice-profile |
| `[COMPLIANCE_RULE_1]` | First compliance rule | Interview Section 7 | content-recipe, integrity rule |
| `[COMPLIANCE_RULE_2]` | Second compliance rule | Interview Section 7 | content-recipe, integrity rule |
| `[REQUIRED_DISCLAIMERS]` | Required disclaimer language | Interview Section 7 | content-recipe, integrity rule |

---

## After Integration

Once all steps are complete, your day-to-day workflow lives in `START_HERE.md`. That document contains:

- **Session prompts** for editorial planning, quarterly drill-downs, content production, and recursive learning.
- **Ongoing production prompts** for writing individual posts, running voice checks, logging performance data, and running research scans.
- **A quick reference** for troubleshooting when content feels off.

You should not need to return to this integration document after initial setup.
