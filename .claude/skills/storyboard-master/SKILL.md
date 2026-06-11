---
name: storyboard-master
description: "Generate multi-shot storyboard master sheet / director treatment board prompts for AI image generators (Midjourney, Flux, Jimeng, Kling, GPT Image) — one planning board containing all shots. Use for storyboard master sheets, director treatment boards, full visual planning boards, pre-production blueprints, or combining shot grid + rhythm + camera + visual language into one board. Triggers: storyboard overview, 分镜总览图, 导演提案板, shot list board. Note: single-frame shots → `storyboard-prompt`; commerce boards → `storyboard-ecommerce`; I2V text planning → `storyboard-sketch`."
---

# Storyboard Master Sheet

## Overview

Generate a comprehensive Storyboard Master Sheet prompt — a single visual document that combines shot grid, rhythm timeline, camera movement diagram, and visual language design into one professional planning board. This is the format directors, agencies, and production teams use for pitches, treatments, and pre-production blueprints.

Use this skill for multi-shot master sheets. For single-frame storyboard prompts, use `storyboard-prompt`. For e-commerce/livestream storyboards with product/creator reference areas, use `storyboard-ecommerce`. For Seedance I2V planning, use `storyboard-sketch`.

## Load Resources

- For anti-slop lexicon replacement when writing prompts, read shared reference `../references/anti-slop-lexicon.md`.
- For bilingual cinematography quick reference tables, read `../references/cinematography-quick-reference.md`.

## Mode Gate

The master sheet has two output densities. Choose based on user intent:

| If the user says...                                                                                                                        | Output                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| "storyboard master sheet", "Master Sheet", "Director Treatment Board", "director treatment board", "full plan", "pre-production blueprint" | **Full Master Sheet** (4 sections, 6-24 shots)                 |
| "concise storyboard board", "storyboard panel board", "quick board", "concise version"                                                     | **Concise Director Board** (shot grid only + bottom 3 modules) |

Shot count is determined by the following priority:
1. **User explicitly specifies** → use directly
2. **Upstream pipeline artifacts exist** (e.g., scene breakdown from `director-story`, shot plan from `director-prompt-packager`, outputs from `director-core` states) → derive from existing shot/scene breakdowns
3. **No context available (fallback)** → default to 6 shots for concise, 12 shots for full

## Full Master Sheet Structure

The full master sheet has four mandatory sections. Write the prompt so the image generator produces all four in a single coherent layout.

### 4-Section Layout

```
┌─────────────────────────────────────────┐
│          Section 1: Shot Grid           │
│   (upper ~60% of the board)             │
│   Grid of numbered shot cards           │
├──────────────┬──────────────┬───────────┤
│ Section 2:   │ Section 3:   │Section 4: │
│ Rhythm       │ Camera       │ Visual    │
│ Timeline     │ Movement     │ Language  │
│ (lower left) │ (lower mid)  │ (lower rt)│
└──────────────┴──────────────┴───────────┘
```

### Section 1: Shot Grid (Shot Grid)

The primary section. Each shot card in the grid must contain:

```
┌──────────────────────────┐
│ #01 | WS | 00:00-00:02  │  ← gray header bar
│                          │
│    [Frame Preview]       │  ← visual preview of the shot
│                          │
│ Action: [one line]       │  ← subject action in the shot
│ Camera: [shot + move]    │  ← camera setup
│ Purpose: [story reason]  │  ← why this shot exists
└──────────────────────────┘
```

Shot card information format: `Shot # | Shot Size | Timecode`

Layout rules:

- Arrange shots in reading order (left→right, top→bottom)
- Use thin gray borders between cards
- Maintain equal card sizes across the grid
- White or light gray background for the board

### Section 2: Rhythm & Structure (Rhythm & Structure)

Display the narrative rhythm and editing structure:

- **Timeline bar**: Full video duration with shot markers (①②③...)
- **Rhythm curve**: Waveform showing intensity changes (calm → build → peak → release)
- **Phase labeling**: Name each narrative phase and which shots belong to it
- **Music/beat alignment**: Key beat points and corresponding shots

Rhythm phases should follow the narrative arc. Use one of these templates based on content type:

| Content Type         | Arc Pattern                                          |
| -------------------- | ---------------------------------------------------- |
| Film / Drama         | Establish → Develop → Conflict → Climax → Resolution |
| Advertising          | Hook → Showcase → Emphasize → Peak → Brand Close     |
| E-commerce           | Atmosphere → Display → Detail → Scene → CTA          |
| Documentary          | Background → Expand → Analyze → Reinforce → Conclude |
| Short Video / Social | Hook → Problem → Solution → Effect → CTA             |

Phase labeling format: `Phase 1: [name] (Shots XX-XX) — [what happens]`

Add a rhythm density line: `[calm] →→ [building] →→→ [peak] →→ [decelerating]`

### Section 3: Camera Movement Diagram (Camera Movement Diagram)

A top-down spatial diagram showing camera positions and movements:

- **Camera positions**: Numbered circles (①②③...) at their spatial locations
- **Movement trajectories**: Dashed arrows connecting positions, showing path
- **Movement type labels**: Static / Push-in / Pull-out / Pan / Tilt / Dolly / Crane / Orbit / Handheld / Steadicam / Tracking
- **Subject position**: A simple marker showing where the subject is relative to cameras

Present this as a description the image generator can render: "Top-down floor plan with numbered camera positions connected by dashed trajectory arrows..."

### Section 4: Visual Language (Visual Language)

Design specifications that apply across all shots:

- **Lighting Design**: Key light, fill light, rim light, color temperature, atmosphere
- **Color Palette**: Dominant colors, contrast level, saturation
- **Composition Rules**: Primary and secondary composition techniques
- **Mood Keywords**: 5-8 emotional/atmospheric descriptors
- **Art Direction Notes**: Key visual references, texture, production design intent

Format as a clean specification block:

```
LIGHTING: [key direction + quality] / [fill] / [color temp]
COLOR: [palette description] / [contrast level]
COMPOSITION: [technique 1] + [technique 2]
MOOD: [keyword 1] · [keyword 2] · [keyword 3] · [keyword 4] · [keyword 5]
ART DIRECTION: [1-2 lines of design guidance]
```

## Concise Director Board (Concise Version)

When the user wants the shorter format, reduce to:

```
┌─────────────────────────────────┐
│    Shot Grid (3 rows × 4-5 cols)│
│    12-15 shot cards             │
├─────────────────────────────────┤
│ Rhythm │ Camera  │ Lighting     │
│ Struct │ Movement│ & Mood       │
└─────────────────────────────────┘
```

Shot cards in concise mode: `#01 | LS Wide Shot | 0:00-0:02` as header, preview image, and one line of director-style description (≤15 characters in Chinese).

Bottom modules are simplified but must still include:

- Rhythm structure: time segments with beat points
- Camera movement: trajectory arrows with shot numbers
- Lighting & atmosphere: key light sources + mood keywords

## Output Format

For both modes, present the structured plan first for user review, then the compressed prompt for the image generator.

```markdown
## Master Sheet Plan

### Project Info

- Project: [name/theme]
- Style: [director treatment board / clean infographic / production document]
- Aspect ratio: [16:9 recommended]
- Total shots: [N]

### Section 1: Shot Grid

| #   | Size | Timecode | Preview | Action | Camera | Purpose |
| --- | ---- | -------- | ------- | ------ | ------ | ------- |
| 01  | ...  | ...      | ...     | ...    | ...    | ...     |
| 02  | ...  | ...      | ...     | ...    | ...    | ...     |

...

### Section 2: Rhythm & Structure

Arc: [phase 1 → phase 2 → phase 3 → phase 4 → phase 5]
[Phase breakdown with shot allocations]
Rhythm density: [curve description]
Music beats: [key points]

### Section 3: Camera Movement

Top-down: [shot numbers and positions]
Trajectories: [movement types per transition]

### Section 4: Visual Language

LIGHTING: [...]
COLOR: [...]
COMPOSITION: [...]
MOOD: [...]
ART DIRECTION: [...]

## Compressed Master Sheet Prompt

[One complete prompt for the image generator covering all 4 sections. 80-200 words. Include board-level style keywords.]
```

## Style Keywords for Master Sheet

Always append this keyword block to Master Sheet prompts (selecting the appropriate subset):

```
Storyboard master sheet, director treatment board, creative production blueprint, shot list layout, camera movement diagram, editing rhythm timeline, visual language board, film production planning document, professional storyboard presentation, information-rich infographic, cinematographic production guide, high-end editorial layout, clean grid system, architectural information graphics, ultra detailed, production ready
```

For concise boards, reduce to:

```
Director storyboard sheet, shot list board, camera movement diagram, rhythm structure, professional production board, clean infographic layout, white background, thin grid borders, ultra detailed
```

## Quality Bar

- All four sections (or three for concise mode) must be present in both the plan and the prompt.
- The narrative arc must match the content type — don't use a film arc for an e-commerce video.
- Shot cards must include: number, shot size, timecode, preview description, action, camera, and purpose.
- Camera movement diagram must include numbered positions and trajectory arrows.
- Style keywords must emphasize "board" and "sheet" concepts — this prevents the image generator from producing a finished film frame instead of a planning document.
- If the user specifies Chinese output, all descriptive text in the plan stays in Chinese; keep style keywords in English for better image generator performance.


## Save Output

After delivering the final output, prompt the user to save:

outputs/storyboard-master-storyboard-master.mdoutputs/storyboard-master-storyboard-master-example.md

If the user confirms, write the output to the specified path.
