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

User has provided subject + action + scene + emotional direction. Confirm key params and output the brief — no additional questions needed.

## Creative Expansion (descriptive but no plot)

When the user provides descriptive detail (scene, style, tone, etc.) but lacks specific narrative action and shot rhythm, do NOT output structure directly. First offer 2-3 creative options:

```
Based on your material, here are a few creative directions:

Option A: [name] — [one-line description + suitable duration + pacing style]
Option B: [name] — [one-line description + suitable duration + pacing style]
Option C: [name] — [one-line description + suitable duration + pacing style]

Which direction do you prefer? Or do you have other ideas?
```

Options should cover different styles (pure showcase / micro-drama / lifestyle MV / documentary / abstract performance, etc.). After user confirms direction, collect production params and output brief.

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


## Save Output

After delivering the final output, prompt the user to save:

```
Save to outputs/director-interview-production-brief.md?
```

If the user confirms, write the output to the specified path.
