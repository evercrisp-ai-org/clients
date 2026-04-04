# Recalibrating Interview

> This is the first thing to run after integrating the Content Production Engine into a project. It captures all the context needed to configure the system for your organization. Work through each section with the voice owner or key stakeholder.

**How to use this document:**

- Work through each section in order. Short answers are fine. "Not yet" and "N/A" are valid.
- After completing the interview, use the answers to fill placeholders across the system (see `INTEGRATION_INSTRUCTIONS.md` Placeholder Checklist).
- Then follow `BRAND_VOICE_ALIGNMENT_GUIDE.md` to refine the voice profile, configure channels, and set up rules.

**This interview is distinct from the Experience Interview Guide** (`brand/experience-interview-guide.md`), which captures verifiable claims and client stories for content integrity. Run this interview first to establish the broad context, then use the experience interview guide for the deeper dive.

---

## Section 1: Organization Context

These answers fill `[ORG_NAME]` and `[TAGLINE]` across all system files, and establish the strategic foundation for content.

1. What is your organization's name?

2. What is your tagline or positioning statement? (If you don't have one, describe your brand's promise in one sentence.)

3. What does your organization do? (2-3 sentences.)

4. What is your organization's mission or purpose beyond revenue?

5. What are your primary goals for content? (Select all that apply and rank by priority.)
   - Lead generation / attracting new clients
   - Authority building / thought leadership
   - Client retention / deepening existing relationships
   - Community building
   - Education / public service
   - Brand awareness
   - Recruiting / employer brand
   - Other: ___

6. What would success look like for your content program in 12 months?

---

## Section 2: Voice Owner

These answers fill `[PERSON_NAME]` and `[SIGN_OFF_PHRASE]`, and form the foundation for the voice profile.

7. Who is the voice behind the content? (Name and role.)

8. **Voice configuration:** Which model best describes your content voice?
   - **Single voice owner:** All content sounds like one specific person.
   - **Institutional voice:** Content sounds like the organization (no single person).
   - **Multiple contributors:** Multiple people contribute, each with their own style.

9. If single voice owner: Describe this person's background in 3-5 sentences. What makes them credible? What is their personal story?

10. If institutional voice: Describe the brand's personality as if it were a person. What are 3-5 adjectives that capture how the brand "speaks"?

11. If multiple contributors: Who are the primary contributors? Is there a unified brand voice they all follow, or does each have their own style?

12. How does content sign off? (e.g., "Best, Jane" / "The [ORG_NAME] Team" / no sign-off / varies by channel.)

13. Where does the voice owner's authority come from? (Select all that apply.)
    - Professional credentials or designations
    - Years of industry experience
    - Personal story or journey
    - Published work or thought leadership
    - Academic background
    - Track record of results
    - Other: ___

---

## Section 3: Target Audience

These answers fill `[AUDIENCE]` and inform the Audience Translation Matrix in the content recipe.

14. Who is the content for? Describe your primary audience in 2-3 sentences. Include demographics, role/title, industry, and life stage if relevant.

15. What is the audience's approximate income or seniority level? (This determines the sophistication level of content.)

16. What are their top 3-5 concerns, problems, or goals that your content addresses?

17. How does this audience make decisions? (e.g., data-driven, peer-influenced, authority-trusting, research-heavy.)

18. What does this audience already know well? (Topics you should NOT over-explain.)

19. What does this audience need help understanding? (Topics where they need education or reframing.)

20. How much time does this audience have for content consumption? (e.g., time-scarce executives vs. deep-dive researchers.)

21. Where does this audience spend time online? (Which platforms, communities, forums, publications.)

22. Is there a secondary audience the content should also serve? If so, describe briefly.

---

## Section 4: Branding

These answers fill `[PRIMARY_HEX]`, `[SECONDARY_HEX]`, `[ACCENT_HEX]`, `[HEADING_FONT]`, `[BODY_FONT]`, and other visual configuration in `brand_config.json`.

23. What are your brand colors? Provide hex codes if available.
    - Primary color: ___
    - Secondary color: ___
    - Accent color: ___
    - Light neutral (backgrounds): ___
    - Dark neutral (text): ___
    - Mid-tone neutral (captions, dividers): ___

24. What fonts does your brand use?
    - Heading font: ___
    - Body font: ___
    - (Provide font files if available; place in `brand/fonts/`.)

25. Do you have an existing brand book, style guide, or visual identity document? If yes, where is it? (Place a copy in `brand/references/` or link to it.)

26. What is the visual tone of your brand? (Select the closest.)
    - Calm, understated, professional
    - Bold, energetic, modern
    - Warm, approachable, friendly
    - Luxurious, refined, premium
    - Clean, minimal, technical
    - Other: ___

27. What types of imagery are appropriate for your brand? (e.g., professional photography, illustrations, data visualizations, conceptual scenes.)

28. What types of imagery should your brand never use? (e.g., stock photo cliches, cartoons, flashy graphics, specific demographics to avoid.)

---

## Section 5: Channels

These answers populate `brand_config.json` `channel_config` and determine the content batch structure.

29. Which channels will you produce content for? For each, note the target frequency.

| Channel | Active? | Posts per week | Notes |
|---------|---------|---------------|-------|
| Blog / Website | | | |
| LinkedIn | | | |
| Facebook | | | |
| YouTube (long-form) | | | |
| YouTube Shorts | | | |
| Instagram (feed) | | | |
| Instagram Reels | | | |
| Twitter / X | | | |
| TikTok | | | |
| Email newsletter | | | |
| Podcast (audio) | | | |
| Other: ___ | | | |

30. Does the tone or style change between channels? If so, describe the differences. (e.g., "LinkedIn is more professional; Facebook is warmer and personal; Twitter is punchier.")

31. Do you repurpose content across channels? (e.g., blog post becomes LinkedIn posts, podcast becomes short-form clips.) If so, describe the repurposing flow.

32. Are there any channels where content must go through an additional review or approval before publishing?

---

## Section 6: Content Objectives and Criteria

These answers shape the content recipe's value flow, quality checklist, and production standards.

33. What does "good" content look like for your organization? Describe the qualities of a piece you would be proud to publish.

34. What does "bad" content look like? Describe the qualities of a piece you would reject.

35. What is your target volume? (e.g., "12 pieces per week" / "3 blog posts per month" / "daily social posts".)

36. What topics are on-limits for your content? (The core subject areas you want to own.)

37. What topics are off-limits? (Subjects you should never cover, or areas where you lack authority.)

38. Are there any specific content formats you want to prioritize? (e.g., "We want more video" / "Data-heavy infographics perform best for us" / "Story-driven posts.")

39. Is there an existing content library or archive of past content? If yes, where is it?

---

## Section 7: Compliance and Regulatory Constraints

These answers populate the compliance section of the content recipe and the content integrity rule.

40. Does your industry have specific regulatory requirements for content? If so, describe them.

    Examples by industry:
    - Financial services: no guarantees, no testimonials, forward-looking disclaimers
    - Healthcare: medical disclaimer requirements, HIPAA considerations
    - Legal: privilege caveats, jurisdiction disclaimers
    - Real estate: fair housing language requirements
    - Education: accreditation disclosures

41. Are there any required disclaimers or disclosures that must appear on content? If so, provide the exact language.

42. Is there an internal review or compliance approval process? If so, who is involved and what do they check?

43. Are there any claims you cannot make in content? (e.g., specific outcome promises, comparative claims, endorsements.)

44. Are there any external regulations, professional codes, or industry standards that govern what you can publish?

---

## Section 8: Key Dates and Cycles

These answers populate `brand/content-calendar.md` and the date-alignment Cursor rule.

45. What is your fiscal year? (e.g., calendar year Jan-Dec, or a different cycle.)

46. List the key deadlines, dates, or events that your content should align to. For each, note the date and why it matters.

| Date / Period | Event or Deadline | Content Implication |
|---------------|-------------------|---------------------|
| | | |
| | | |
| | | |
| | | |

47. Are there seasonal cycles that affect your audience? (e.g., "Q4 is budget season" / "Summer is slow" / "Conference season is March-May".)

48. Are there recurring industry events, conferences, or publications that your content should reference or align with?

49. How far in advance should content reference upcoming deadlines? (e.g., "4-6 weeks before" / "the week of".)

---

## Section 9: Language Rules and AI-Giveaway Detection

These answers populate `voice-profile.md` (anti-patterns), `content-recipe.md` (language lists), and `brand_config.json` (`voice_and_tone`).

50. Are there specific words or phrases your organization always uses? (Branded terms, preferred vocabulary, signature phrases.)

51. Are there specific words or phrases your organization never uses? (And why.)

52. Are there industry terms that your audience expects to see? (Terminology that signals credibility.)

53. Are there industry terms your audience dislikes or that feel too jargon-heavy?

54. What is your organization's stance on punctuation and formatting?
    - Em dashes: use them / avoid them / no preference
    - Oxford comma: use it / avoid it / no preference
    - Exclamation points: use sparingly / use freely / avoid entirely
    - Emoji: use them / avoid them / context-dependent
    - Capitalization style: title case / sentence case / no preference

55. **AI-giveaway detection:** Review the following common AI-generated patterns. Mark any that should be banned for your voice:
    - [ ] Em dashes (the long dash: --)
    - [ ] "It's not X. It's Y." pivot construction
    - [ ] Overuse of "delve," "landscape," "navigate," "crucial," "realm," "foster," "robust"
    - [ ] Excessive hedging ("It's important to note that...")
    - [ ] Formulaic list introductions ("Here are X things you need to know about...")
    - [ ] Overuse of "in today's [adjective] [noun]" openings
    - [ ] "Let's dive in" / "Let's break it down" / "Let's unpack this"
    - [ ] Excessive use of "leverage," "utilize," "facilitate"
    - [ ] Others you've noticed: ___

56. Are there any phrases, constructions, or patterns you've noticed in AI-generated text that feel wrong for your brand? Describe them.

57. What is the "golden rule" for your content voice? Complete this sentence: "If it sounds like ___, rewrite it. If it sounds like ___, it's correct."

---

## Section 10: Sample Content

These answers confirm the `samples/` folder is ready for voice-profile generation (Session 1).

58. Do you have existing content that represents the voice you want the system to capture? If yes, how many pieces and where are they?

59. Place 10-30+ representative pieces in the `samples/` folder (see `samples/README.md` for accepted formats). Confirm when complete:
    - [ ] Samples placed in `samples/`
    - [ ] Number of samples: ___

60. If you don't have existing samples: who will create them, and by when?

61. Are there any samples that should be treated as "gold standard" (the absolute best representation of the voice)? If so, mark them or list them here.

62. Are there any samples that represent the voice at its worst (drafts that went wrong, content that doesn't sound right)? These are useful as negative examples during voice-profile generation.

---

## After the Interview

1. Use the answers above to replace placeholders across all system files (see `INTEGRATION_INSTRUCTIONS.md` Placeholder Checklist).
2. Run **Session 1** from `START_HERE.md` to generate the voice profile from your samples.
3. Follow **BRAND_VOICE_ALIGNMENT_GUIDE.md** to refine branding, rules, channels, and compliance.
4. Run the **Validation Smoke Test** from `START_HERE.md` Section E.
5. When ready, run **Session 2** from `START_HERE.md` to build your editorial plan.

For verifiable claims, client stories, and experience documentation, proceed to `brand/experience-interview-guide.md` after the alignment guide is complete.
