---
name: storyboard-prompt
description: Generate professional storyboard frame prompts for AI image generators (Midjourney, Flux, Jimeng, Kling, GPT Image, Runway, Veo). Use when the user asks for storyboard prompts, shot planning prompts, 分镜提示词, storyboard frame generation, film pre-visualization prompts, animation storyboard, commercial storyboard, single-frame storyboard, or needs to write structured prompts that produce cinema-grade storyboard panel images. Also use when the user gives a vague scene idea and wants it turned into a professional storyboard shot description.
---

# Storyboard Prompt

## Overview

Turn a scene idea, subject, or action into a professionally structured prompt that AI image generators can convert into cinema-grade storyboard frame images. This skill enforces an 8-element shot description framework derived from film industry pre-production standards, ensuring every prompt produces a readable, technically accurate storyboard panel regardless of the image generator used.

Use this skill for single-frame storyboard prompts. For multi-shot master sheets, use `storyboard-master`. For e-commerce/livestream storyboards, use `storyboard-ecommerce`. For Seedance I2V planning prompts, use `storyboard-sketch`.

## Load Resources

- For anti-slop lexicon replacement when writing prompts, read shared reference `../references/anti-slop-lexicon.md`.
- For bilingual cinematography quick reference tables, read `../references/cinematography-quick-reference.md`.

## Input Gate

Before generating a prompt, check that the user has provided enough material to fill the 8-element framework. Treat the input as sufficient when it includes at least:

- A scene idea, subject, or theme.
- A desired visual style or use context (film/ad/animation/CG).

If sufficient, proceed and fill gaps with reasonable defaults, marked clearly.

If insufficient, infer from context then confirm:

```markdown
Let me first confirm the direction for this storyboard shot:

- Scene/Theme: [inferred]
- Subject/Character: [inferred]
- Action: [inferred]
- Target style: Cinematic storyboard / B&W line art / Animation previs / Ad pitch
- Target tool: Midjourney / Flux / Jimeng / Kling / GPT Image

Does this look right? Adjust one line and I will generate the prompt.
```

If the user says "just generate", proceed with assumptions and mark them.

## The 8-Element Framework

Every storyboard prompt must address these eight dimensions. The model cannot invent missing critical information — if the user hasn't provided it, make a justified assumption and note it.

| #   | Element       | Chinese       | What it answers                                     |
| --- | ------------- | ------------- | --------------------------------------------------- |
| 1   | Scene         | Scene         | Where and when does this take place?                |
| 2   | Subject       | Subject       | Who or what is the focus? Appearance? Wardrobe?     |
| 3   | Action        | Action        | What is the subject doing? State, direction?        |
| 4   | Camera        | Camera        | Shot size, angle, movement?                         |
| 5   | Composition   | Composition   | How is the frame arranged? Subject position?        |
| 6   | Lighting      | Lighting      | Key light, fill, color temp, quality?               |
| 7   | Mood          | Mood          | What emotional atmosphere?                          |
| 8   | Story Purpose | Story Purpose | Why does this shot exist? What does it communicate? |

This framework applies whether the user needs a film noir detective scene, an animation fantasy shot, or a luxury product commercial. The elements stay the same; only the values change.

## Output Format

Write the prompt in two layers. First, show the structured breakdown so the user can verify every element. Then, provide the compressed prompt ready for pasting into an image generator.

```markdown
## Shot Breakdown

**Scene:** [time · location · environment details]
**Subject:** [character/object · appearance · wardrobe · state]
**Action:** [what the subject is doing · movement direction · state]
**Camera:** [shot size] · [angle] · [movement]
**Composition:** [framing approach · subject position · depth layers]
**Lighting:** [key light direction/quality] · [fill] · [color temp] · [atmosphere]
**Mood:** [2-3 emotional keywords]
**Story Purpose:** [narrative function — establish/reveal/emphasize/transition]

## Prompt

[Compressed prompt in 40-100 words, English or Chinese depending on user preference. End with style keywords.]
```

### Prompt Compression Rules

The compressed prompt should flow naturally as one paragraph. Order elements by visual priority: Scene → Subject → Action → Camera → Composition → Lighting → Mood, then append style keywords. Do not use bullet points or labels in the compressed prompt — it must read as a single descriptive passage that image generators parse well.

### Style Keywords

Always append these to the compressed prompt. Choose the set that matches the user's intent:

**Film storyboard:**

```
professional storyboard panel, film storyboard frame, director treatment, cinematic composition, pre-production visualization, black and white storyboard sketch, clean pencil drawing, highly detailed, production-ready storyboard
```

**Animation storyboard:**

```
animation storyboard, pre-production planning board, clean pencil sketch, animation keyframe planning, animatic reference frame, production storyboard panel
```

**Commercial storyboard:**

```
commercial storyboard, advertising shot planning, director treatment frame, high-end product storyboard, professional production board, clean composition, white background
```

**Color/finished style (when user explicitly wants color):**

```
professional storyboard panel, cinematic composition, color storyboard, production design, film pre-visualization, highly detailed
```

## Domain Templates

### Film / Drama Template

Use when the user describes a narrative scene with characters, tension, or emotional arc.

```
Scene: [time of day] · [location] · [weather/atmosphere]
Subject: [character name/type] · [age] · [appearance] · [wardrobe]
Action: [physical action with direction and state]
Camera: [shot size from WS to ECU] · [angle low/high/eye] · [static/push/track]
Composition: [rule of thirds / centered / leading lines] · [foreground/midground/background layers]
Lighting: [key source] · [quality soft/hard] · [color temp warm/cool] · [special: rim/volumetric/practical]
Mood: [2-3 words: tense/suspenseful/melancholic/hopeful/epic]
Story Purpose: [establish location / introduce character / build tension / reveal clue / transition]
```

### Animation Template

Use when the user describes animated or fantasy content.

```
Scene: [fantasy/real-world location] · [time/magical atmosphere]
Subject: [character type] · [age] · [design features] · [costume]
Action: [dynamic or emotional action with flow direction]
Camera: [shot size] · [three-quarter view / profile / bird's eye] · [dynamic movement]
Composition: [rule of thirds / dynamic perspective] · [depth layers]
Lighting: [soft/diffuse magical light] · [warm/cool/fantasy glow] · [atmosphere]
Mood: [wonder / adventure / fantasy / dreamlike / epic]
Story Purpose: [introduce world / show character emotion / reveal destination / emphasize scale]
```

### Advertising / Product Template

Use for product commercials, luxury goods, brand films.

```
Scene: [clean studio / lifestyle environment / abstract backdrop]
Subject: [product name/type] · [key visual features] · [material/texture]
Action: [slow reveal / rotation / interaction with light or environment]
Camera: [CU / ECU for product detail] · [eye level / top-down] · [slow push-in / orbit / static]
Composition: [centered / negative space] · [product as hero, minimal distraction]
Lighting: [rim light for edge definition] · [soft fill] · [dramatic / elegant / high key]
Mood: [luxury / elegant / premium / minimal / aspirational]
Story Purpose: [hero product / emphasize craftsmanship / lifestyle association / brand closer]
```

### Universal Template (when domain is unclear)

The most general template — use when the user's domain doesn't fit the above, or as default.

```
Scene: [time · location · environment]

Subject: [character / object · appearance · state]

Action: [what is happening · movement direction]

Camera: [shot size · angle · movement]

Composition: [framing · subject placement · depth]

Lighting: [key · fill · color temp · special qualities]

Mood: [emotional keywords]

Story Purpose: [why this shot matters]

Style: [professional storyboard panel, cinematic composition, clean pencil sketch, highly detailed, production-ready storyboard]
```

## Scene Generator

When the user provides only a theme (e.g., "futuristic cyberpunk city" or "detective in heavy rain") without complete scene details, first generate a scene breakdown, then build the prompt from it.

Template:

```markdown
Based on the theme "[user's theme]", let me first develop a scene plan:

**Scene Description:** [2-3 sentences establishing time, place, atmosphere]
**Subject Description:** [1-2 sentences on the main subject]
**Action Description:** [1 sentence on the key action]
**Camera Suggestion:** [shot size + angle]
**Lighting Suggestion:** [key light + atmosphere]
**Mood Suggestion:** [2-3 mood words]
**Storyboard Focus:** [what this shot should emphasize]

Once you confirm this direction, I will generate the full prompt.
```

## Quality Bar

- Every prompt must address all 8 elements. If the user hasn't provided one, make a note of the assumption.
- The compressed prompt should be usable as-is in any major image generator without modification.
- Style keywords must not include unsafe studio/franchise/celebrity names — use descriptive equivalents.
- If the user asks for Chinese output, write the breakdown in Chinese but keep style keywords in English (they perform better in image generators).
- A reader unfamiliar with the project should understand the full scene from just the compressed prompt.
