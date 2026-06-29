---
name: image-brief
description: Generate production-ready 9-point AI image prompts for Capable Wealth content — correct platform dimensions, exclusive brand palette, and the mandatory image-type/color/subject rotation rules applied across a week or batch. Use when the user asks for an image brief, image prompt, or visual asset for a piece, or it is invoked inside generate-batch to brief every asset.
---

# Image Brief

Produce self-contained AI image prompts a person can paste into any generator (Midjourney, Ideogram, DALL-E) and get a brand-consistent result. The credibility test governs everything: *"Would an orthopedic surgeon earning $800K+ take this seriously?"*

## Input

A content piece (path or description) + its channel, OR a batch folder (brief every asset with rotation awareness). If briefing for a single piece outside a batch, ask which platform if it's ambiguous.

## Load first

`brand/content-recipe.md` §10 (Visual Asset Guidelines, the 9-Point Standard, and Example Prompts A-E), `.cursor/rules/content-production-batch.mdc` (Image Type Variety + Image Prompt Variation), and `brand/brand_config.json` (palette, fonts, `social_image_specs`).

## Palette (exclusive — no other colors)

Deep Muted Blue `#243A4B` · Blue Slate `#5F7483` · Antique Gold `#B08D57` · Off-White `#F6F7F5` · Charcoal `#1E2428` · Warm Gray `#9AA3A8`. Ratio 60/30/10 (blue / neutrals / gold). Fonts: Playfair Display (headlines), Inter (body).

## Dimensions

LinkedIn 1200×627 or 1080×1080 · Facebook 1200×630 · Blog hero 1200×628 · Blog in-body 1200×628 · YouTube thumbnail 1280×720 · Podcast cover 1400×1400 · Shorts/Reels cover 1080×1920 (keep text in center 4:5 safe zone).

## Every prompt must specify all 9 points

1. **Canvas** — exact px + orientation. 2. **Background** — treatment with hex. 3. **Layout/composition** — where each element sits (quadrants, thirds, px margins, alignment). 4. **Typography** — exact text in quotes, font family, weight, ~pt size, hex, alignment, vertical position. 5. **Graphic elements** — dividers/accent lines/logo with hex, thickness, position, scale. 6. **Photographic direction** (if a photo) — subject, environment, lighting, angle, depth of field, color grading shifted toward brand palette. 7. **Brand constraints** — full palette + 60/30/10 + exclusion list (no cartoons, clip art, generic stock, clickbait, flashy/sensational, busy compositions). 8. **Mood** — 2-3 descriptors. 9. **Audience context** — "Professional financial advisory aesthetic for orthopedic surgeons ages 45-65."

A vague prompt ("minimalist navy quote card") is a failure. Two people generating from your prompt should get visually similar results. Mirror the specificity of Example Prompts A-E in recipe §10.

## Rotation rules (mandatory — track across the whole week/batch)

- **Max 1 text-on-block card** (stat/quote) per platform per week. The other assets are conceptual photo / infographic / data viz.
- **≥2 conceptual photographs and ≥1 infographic** per platform per week. This is a *count* minimum; the "max 1 per subject across platforms" rule below is a *subject-uniqueness* cap. Satisfy both: never fewer than 2 photos per platform per week, and never the same subject twice in a week — give each photo a distinct subject from the rotation table.
- **Text-on-block background colors rotate** across the batch: 1st Deep Muted Blue, 2nd Charcoal, 3rd Off-White, then repeat. Rotate layout too (centered stack / asymmetric anchor / split comparison / full-bleed number / stacked contrast). **Hard cap: centered stack on at most half of the text-on-block cards in a batch.**
- **Conceptual photos rotate subject** (office/desk · corridor/path · outdoor · people-in-conversation · object close-up · domestic · architectural) — max 1 per subject per week across platforms, no repeat back-to-back across weeks. Vary person age/gender; don't reuse one archetype in >2 photos per batch; state "no people" explicitly when none.
- **Infographics rotate layout** (timeline / checklist / comparison columns / step flow / single-stat callout / before-after) — no two the same week.
- **Clip covers** vary background color and text hierarchy across the week's clips. **Deep Muted Blue on at most 2 clip covers** per week; covers are 1080×1920 with all critical content in the center 4:5 safe zone (top/bottom 10% is obscured by platform UI).
- **Cross-platform dedup:** the same stat on multiple platforms must get different visual treatments — never the same card at three dimensions.

## Output

For each asset: image type · one-line rationale · the full 9-point prompt · text overlay spec (or "None") · platform + dimensions — matching the Visual Assets block of the Standard Draft File Format (recipe §12). When briefing a batch, start with a short rotation ledger (which card colors, photo subjects, and infographic layouts you assigned to each slot) so the set is provably distinct, then list the prompts.
