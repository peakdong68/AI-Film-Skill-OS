---
name: director-emotion
description: Design the emotional architecture of an AI film — emotion curves, narrative rhythm, intensity scoring, and emotion-to-shot mapping. Use when the user needs emotional design, 情绪曲线, narrative pacing, rhythm design, emotional arc planning, or when director-core routes to STATE 1 (Emotion Design). Also use when the story feels flat, the user wants to control audience emotional experience, or needs to map abstract feelings to concrete visual decisions.
---

# Director Emotion — Narrative Emotion Engine

## Overview

Design the emotional journey that drives audience experience through the film. This skill takes a narrative structure (from `director-story`) and overlays an emotional timeline: where tension builds, where it releases, how each scene feels, and how those feelings map to camera and visual decisions. The output is the emotional blueprint that guides cinematography, lighting, and rhythm choices.

Works independently for emotional design or is invoked by `director-core` at STATE 1.

## Input Gate

Requires at minimum:
- A narrative structure or scene list (from `director-story` or user-provided)
- A genre or emotional tone reference

If insufficient, ask: "这个故事的总体情绪基调是什么？比如悬疑、浪漫、压抑、史诗？"

## Output Structure

### 1. Emotional Arc Map (情绪曲线)

Define the full emotional journey:

```
[Calm / Stable]
    ↓
[Building Tension / Curiosity]
    ↓
[Escalation / Conflict]
    ↓
[Peak / Crisis / Climax]
    ↓
[Release / Resolution / New State]
```

For each phase, assign:
- **Phase name**: e.g. "Unease", "Discovery", "Confrontation", "Collapse", "Acceptance"
- **Emotional keywords**: 2-3 words capturing the dominant feeling
- **Intensity level**: 1-10
- **Duration**: percentage of total runtime
- **Which scenes belong here**: map to the scene list

### 2. Emotional Beats (情绪节拍)

Identify the key turning points where emotion shifts:

```
Beat 1: [event] → emotion shifts from [A] to [B]
Beat 2: [event] → emotion shifts from [B] to [C]
Beat 3: [event] → emotion shifts from [C] to [D]
...
```

Each beat is a moment where the audience's emotional state changes. These are the anchor points for camera decisions — the most important shots in the film.

### 3. Intensity Timeline (情绪强度分布)

Map intensity (1-10) across the full duration:

```
0% ────── 25% ────── 50% ────── 75% ────── 100%
 3         5          8          9          4
[intro]  [build]   [climax]  [peak]    [release]
```

### 4. Character Emotion Drift (角色情绪变化)

For each major character, define their individual emotional trajectory:

```
Character [A]:
- Scene 1: [emotional state] → intensity [N]
- Scene 2: [emotional state] → intensity [N]
- ...
- Arc: [from X to Y across the story]
```

This is critical for character consistency — the character's emotional state must evolve, not reset.

### 5. Emotion-to-Visual Mapping (情绪→视觉映射)

Define how each primary emotion translates into visual decisions:

| Emotion | Camera | Lighting | Color | Pace |
|---------|--------|----------|-------|------|
| Tension | handheld / tight framing | flicker / high contrast | cold / desaturated | accelerating |
| Romance | slow orbit / close-up | warm soft light | gold / amber | slow, breathing |
| Fear | close-up / Dutch angle | low key / shadows | blue-green / dark | erratic |
| Sadness | wide / static / negative space | soft diffused | blue-gray | very slow |
| Power | low angle / symmetrical | dramatic rim | high contrast | controlled, steady |
| Mystery | partial framing / silhouettes | backlight / practical | muted / shadowed | deliberate pause |

Use this as the bridge between `director-emotion` and `director-camera` / `director-light`.

### 6. Rhythm Structure (节奏结构)

Define the editing rhythm across the film:

```
[Slow] → [Building] → [Fast] → [Faster] → [Abrupt stop] → [Slow release]
```

Map rhythm density (cuts per time segment) and identify where silence or stillness should dominate.

## Constraints

- Every scene must be assigned an emotional value — no emotionally neutral scenes.
- Emotion must change across the duration — static emotion is boring.
- Character emotion drift must be consistent with the narrative — no unmotivated emotional shifts.
- The emotion-to-visual mapping must be handed to `director-camera` and `director-light` as input.

## Integration with director-core

When invoked by `director-core`:
- Load the narrative structure from `director-story`
- Produce the full Emotional Blueprint  
- Present for user confirmation
- Feed the emotion-to-visual mapping into STATE 2 (Visual Design)
