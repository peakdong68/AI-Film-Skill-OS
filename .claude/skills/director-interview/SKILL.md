---
name: director-interview
description: "Creative intake interview — transforms vague ideas or descriptive-but-no-plot inputs into executable production briefs. Three-path gating: creative-complete fast track, descriptive-but-no-plot option expansion (2-3 creative directions), vague creative interview. Outputs a confirmed production brief. Called by director-core STATE 0 and director-story for standalone use."
---

# Director Interview — Creative Intake Interview

## Overview

Unified intake interview logic. Based on the creative clarity of user input, selects the best path to transform input into an executable production brief. Called by `director-core` (STATE 0) and `director-story` (standalone).

## Three-Path Gating

| Input Quality | Criteria | Path | Output |
|---|---|---|---|
| Creative complete | Has subject + action + scene + emotional direction, ready to proceed | **Fast track** | Confirmed production brief |
| Descriptive but no plot | Has scene/style/tone but lacks specific narrative action and shot rhythm (not limited to brand/commerce — includes theme/atmosphere, nature/landscape, abstract concepts, etc.) | **Creative expansion** | 2-3 options → user selects → brief |
| Vague creative | Only keywords / broad concepts / no specific scene or action | **Creative interview** | 3 questions → answers → brief |

## Fast Track

User has provided subject + action + scene + emotional direction. Confirm key params and output the brief:

- **Duration, aspect ratio, style, platform** — confirm each one
- **Reference materials** — actively ask: "Do you have any reference images (characters, scenes, products), video clips, or audio you can provide?" This is mandatory regardless of how complete the input is.

  **Response handling rules:**
  | User says | Immediate action | Brief format |
  |-----------|-----------------|-------------|
  | "Yes, I have images/references" (including "I have character images", "I have scene photos", etc.) | **Register Material Slot immediately, mark `✅ Ready`**. Use sensible naming (e.g. `@[image1]` Boy reference, `@[image2]` Little yellow dog reference). **NEVER ask the user to re-upload.** | `@[imageN] [character/scene] reference — ✅ Ready` |
  | "No" | Record as `none` in brief; STATE 3 follows Path B (director-character) | `none` |
  | Skip / no answer | Record as `not provided` in brief; STATE 3 follows Path B (director-character) | `not provided` |

  **Core principle: user says yes = slot ready. Registration takes effect immediately — no re-upload proof required.**

- **Output brief** — the `Available references` field uses `@[imageN]` slot format

After confirmation, output the brief — no additional questions needed.

## Creative Expansion (descriptive but no plot)

When the user provides descriptive detail (scene, style, tone, etc.) but lacks specific narrative action and shot rhythm, do NOT output structure directly. First offer 2-3 creative options:

```
Based on your material, here are a few creative directions:

Option A: [name] — [one-line description + suitable duration + pacing style]
Option B: [name] — [one-line description + suitable duration + pacing style]
Option C: [name] — [one-line description + suitable duration + pacing style]

Which direction do you prefer? Or do you have other ideas?
```

Options should cover different styles (pure showcase / micro-drama / lifestyle MV / documentary / abstract performance, etc.). After user confirms direction, collect production params (duration, aspect ratio, style, platform, reference materials) and output brief. **Reference materials** is mandatory — proactively ask if they have reference images, video, or audio for characters/scenes/products.

User response handling follows the same rules as **Fast Track** (immediately register Material Slot, mark `✅ Ready`, never ask for re-upload).

## Creative Interview (vague input)

At most 3 high-impact questions. Only ask what is missing:

1. **Subject + change**: "Who is the main subject? What are they doing? What changes by the end?"
2. **Feeling + genre**: "What should it feel like? Product showcase, dramatic tension, comedy, realism, animation, or atmosphere?"
3. **Reference materials**: "Any reference images/videos/audio? Or a film style in mind?"

Build a creative brief from answers, then collect production params.

## Output: Production Brief

Regardless of path, output a unified production brief:

```
## Production Brief

- Project: [confirmed creative description]
- Creative direction: [selected option or naturally formed direction]
- Genre path: [product showcase / micro-drama / lifestyle MV / documentary / narrative short / ...]
- Target duration: [15s / 30s / 60s / custom]
- Visual style: [cinematic / commercial / documentary / anime / sci-fi / etc.]
- Delivery platform: [Seedance / Kling]
- Aspect ratio: [16:9 / 9:16 / 1:1]
- Available references: [character images / scene images / video clips / audio clips / none]
```

## Principles

- Don't ask for information already provided
- Don't output structure — this phase produces a brief, not a script or storyboard
- When user says "just do it" — fill reasonable defaults with annotations
