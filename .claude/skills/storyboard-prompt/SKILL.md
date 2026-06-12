---
name: storyboard-prompt
description: 'Generate single-frame storyboard image prompts for AI image generators (Midjourney, Flux, Jimeng, Kling, GPT Image) using an 8-element framework (Scene/Subject/Action/Camera/Composition/Lighting/Mood/Story Purpose). Use for single-frame composition design, keyframe visualization, shot atmosphere exploration, single-frame storyboard validation, or when translating narrative beats into executable image prompts. Note: for multi-shot overview boards use `storyboard-master`; for e-commerce boards use `storyboard-ecommerce`; for I2V frame planning use `storyboard-sketch`.'
---

# Storyboard Prompt — Single-Frame Image Prompts

## Overview

Transform a single narrative beat into a paste-ready storyboard image prompt for AI image generators (MJ/Flux/Jimeng/Kling/GPT Image). Unlike master sheets, this skill focuses on **one frame at a time** — each shot as a standalone image, used to validate composition, lighting, and mood direction, or to confirm visual language frame by frame before entering video generation.

This skill is for single-frame storyboard images. For multi-shot overview boards use `storyboard-master`. For e-commerce boards with product/creator zones use `storyboard-ecommerce`. For Seedance I2V text planning use `storyboard-sketch`.

## Load Resources

- For bilingual cinematography quick reference (shot sizes, movements, angles, composition, lighting), read `../references/cinematography-quick-reference.md`
- For anti-slop word replacement, read shared reference `../references/anti-slop-lexicon.md`

## Context Detection (mandatory when used standalone)

Probe available context on load to determine material sources:

**1. Check pipeline state:** Read `STATE.md`; if present, obtain character material slot mappings from the `Material Slots` block.

**2. Scan project files:** Check for the following files:

| If discovered...                    | Then...                                                         |
| ----------------------------------- | --------------------------------------------------------------- |
| `outputs/character-sheets.md`       | Extract character names and sheet sources, map to `@[imageN]` slots |
| `outputs/State-4-prompt-package.md` | Extract shot size, action, camera, lighting plan for current shot |
| `outputs/State-3-characters.md`     | Extract character lock parameters (face, body type, wardrobe)   |
| `outputs/State-2-visual.md`         | Extract lighting and color schemes                              |
| `outputs/State-1-story-emotion.md`  | Extract emotion value for the current scene                     |

**3. Auto-complete slots:** If character sheets or Material Slot Registry are detected, automatically establish character anchor mappings and reference `@[imageN]` in prompts.

**4. No context:** Rely entirely on direct user description, organize using the 8-element framework.

---

## Mode Gate

> **This skill does NOT auto-select.** Only execute when explicitly routed by `director-core` STATE 5 or when the user explicitly requests single-frame storyboard prompts.

| User says...                                                                     | Action                                         |
| -------------------------------------------------------------------------------- | ---------------------------------------------- |
| "how to shoot this shot", "write a storyboard frame", "single frame composition" | Use 8-element framework for single-frame prompt |
| "make a master sheet", "full planning board", "multi-shot grid"                  | Route to `storyboard-master`                   |
| "e-commerce storyboard", "fashion director board"                                | Route to `storyboard-ecommerce`                |
| "I2V frame planning", "storyboard sketch"                                        | Route to `storyboard-sketch`                   |

---

## 8-Element Framework

Every single-frame storyboard prompt must cover the following 8 elements. This is the complete mapping from narrative beat to executable image generation prompt:

| # | Element | Description |
|---|---------|-------------|
| 1 | **Scene** | Time, place, environment context — the space the viewer sees |
| 2 | **Subject** | The core object in frame — character, product, or key element. When reference images exist, use `@[imageN]` reference — do not enumerate appearance |
| 3 | **Action** | What the subject is doing — specific, observable physical action, not abstract emotion |
| 4 | **Camera** | Shot size + angle + movement — one primary camera move |
| 5 | **Composition** | Framing rule — rule of thirds / centered / negative space / frame-in-frame |
| 6 | **Lighting** | Key light direction+quality + fill + color temperature + atmosphere |
| 7 | **Mood** | Visual emotion conveyed by the frame — expressed through shootable light/color |
| 8 | **Story Purpose** | Why this shot exists — establish/reveal/advance/escalate/contrast/resolve |

## Output Format

Present structured analysis first, then compressed image generation prompt:

```markdown
## Frame: [Shot Number] — [Beat Name]

### 8-Element Analysis

| Element | Content |
|---------|---------|
| Scene | [Time · Place · Environment] |
| Subject | [Subject description. When reference images exist: reference @[imageN], do not enumerate appearance] |
| Action | [Specific observable physical action] |
| Camera | [Shot size] + [Angle] + [Movement] |
| Composition | [Framing approach] |
| Lighting | [Key light + Fill + Color temp + Atmosphere] |
| Mood | [Visual mood keywords] |
| Story Purpose | [Narrative function] |

### Compressed Prompt

[A complete image generation prompt. Contains scene, subject, action, composition, lighting, and style keywords. Ready to paste into MJ/Flux/Jimeng/Kling.]
```

## Compressed Prompt Rules

- **Subject reference first**: When upstream material slots are defined, use `@[imageN]` to reference subject identity — do not enumerate face, hairstyle, body type details. The reference image already locks visual identity.
- **Concrete action**: No abstract emotion words ("he is sad" → "head lowered, shoulders slightly dropped, gaze shifts to the ground")
- **Explicit camera**: Each prompt includes one primary shot size and one movement
- **Executable lighting**: Describe physical light source + direction + quality — no empty adjectives
- **Uniform style keywords**: End with quality and style keywords (e.g. "cinematic realism, high detail, 50mm lens feel")

### Example

User request: First shot of "a courier discovers a ticking package in a rainy alley."

```markdown
## Frame: 01 — Entering the Alley

### 8-Element Analysis

| Element | Content |
|---------|---------|
| Scene | Midnight · Narrow back alley · Heavy rain |
| Subject | Courier in red jacket, holding a small black package. Reference character slot with @[image1] when available |
| Action | Enters from screen left, right hand holding package, cautious stride |
| Camera | Wide shot + Eye level + Lateral track |
| Composition | Alley wall leading lines, subject at left third |
| Lighting | Streetlamp top light as key, blue ambient fill, high contrast, cold tone |
| Mood | Tense · Wet · Isolated |
| Story Purpose | Establish scene space and character entry state |

### Compressed Prompt

```
Narrow brick back alley at midnight in heavy rain, a courier in a red jacket enters from screen left, right hand holding a small black package, cautious stride. Streetlamp top light casts hard light from above, blue cold ambient light fills the alley. Wet brick walls reflect faint light, ground puddles mirror silhouettes. Wide shot, eye level, lateral tracking. Leading line composition, subject at left third. High contrast, cinematic realism, 50mm lens feel, high detail texture.
```
```

## Quality Bar

- All 8 elements must be fully covered — none may be omitted.
- The Compressed Prompt must be self-contained — ready to paste into an image generator with no additional context needed.
- Mood is expressed through lighting/color/composition, not abstract adjectives.
- Camera decisions must have narrative justification — "why this shot size/angle/movement at this moment."
- **When reference images exist, do not enumerate subject appearance details (face, hairstyle, body type, wardrobe) in the Subject element or Compressed Prompt.** When upstream Material Slot Registry has registered `@[imageN]` character slots, use `@[imageN]` references for subject identity — do not re-describe visual parameters already locked in the reference image.
- The Compressed Prompt must end with negative constraint keywords (e.g. "no watermark, no logo, no text").

## Save Output

After delivering the final output, prompt the user to save with a date-prefixed and topic-named filename:

```
Save to outputs/YYYY-MM-DD-[topic]/frame-prompts.md?
Example: outputs/2026-06-10-cyberpunk-short/frame-prompts.md
```

After user confirmation, write the output to the specified path.

## Pipeline Integration

When called by `director-core` STATE 5:

1. Obtain character/product slot mappings from Material Slot Registry
2. Extract the current shot's storyboard design from `State-4-prompt-package.md`
3. Compile single-frame prompt using the 8-element framework
4. Submit for user confirmation, then output the paste-ready Compressed Prompt
