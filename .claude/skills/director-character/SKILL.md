---
name: director-character
description: Design and lock character identity for AI film production — character identity definitions, visual identity parameters, behavior systems, emotion→action mappings, and multi-character relationship management. Based on Seedance 2.0 official guidelines, recommends separate headshot + full-body character reference approach (multi-view/three-view character sheets are PROHIBITED). Use for character design, character setup, character consistency, character sheet creation, or when director-core routes to STATE 3 (Character Lock). When AI-generated characters repeatedly change faces, outfits, or break style across shots, the identity lock system built by this skill is the core defense. Note: this skill produces character identity **definitions** (text-level design documents). To compile them into executable image generation prompts, use the character-image-prompt skill.
---

# Director Character — Character Consistency Engine

## Overview

Design character identity with sufficient precision that AI video generators can maintain consistency across shots. This skill produces a **Character Consistency Sheet** — a structured identity document that locks face, body type, clothing, behavior, and emotional expression, ensuring the character remains stable in every frame.

The most common failure in AI video production is character drift (face-swapping / outfit-changing / style-breaking). This skill is the first line of defense against it.

Can be used independently for character design, or called by `director-core` at STATE 3.

**Important:** This skill produces **character identity definitions** (text-level design documents). It does **not** produce executable image generation prompts. To compile identity definitions into platform-ready character sheet prompts (MJ/Flux/Jimeng/Kling), use the `character-image-prompt` skill.

## Load Resources

This skill includes bundled reference knowledge. Load when needed:
- For the complete visual identity parameter checklist and identity locking specifications, read `references/character-identity.md`
- For the micro-motion unit library, emotion-to-full-body-action mapping, and micro-expression system, read `references/motion-translation.md`

## Core Principle

> Character consistency in AI video is not a prompt-tuning problem — it is an identity specification problem.

The AI must receive the same identity parameters in every prompt. Minor differences in description cause cascading drift. This skill creates the master identity document that all prompts reference.

## Output Structure

### 1. Character Identity Core

```
Character: [Name]
- Narrative Role: [Protagonist / Antagonist / Supporting / Observer]
- Age Range: [e.g. 25-30]
- Gender Expression: [description]
- Emotional Identity: [core emotional state — calm, anxious, intense, vulnerable]
- Psychological Profile: [key traits, motivations, fears]
- Story Function: [what does this character accomplish in the narrative?]
- Character Arc: [from starting state A → to ending state B]
```

### 2. Visual Identity System

**Facial System:**
```
- Face Shape: [oval / round / angular / heart / square]
- Skin Tone: [specific descriptor with undertone reference]
- Eye Shape: [almond / round / hooded / monolid / deep-set]
- Eye Color: [specific color, NOT "beautiful eyes"]
- Eyebrows: [shape, thickness, arch]
- Nose: [shape, bridge, tip]
- Mouth: [shape, lip fullness]
- Jaw/Chin: [shape, definition]
- Distinguishing Features: [scars, moles, freckles, asymmetry]
- Facial Structure Notes: [overall impression, bone structure]
```

**Hair System:**
```
- Hairstyle: [specific cut name or description]
- Length: [measurement relative to facial features]
- Color: [specific shade, NOT "brown"]
- Texture: [straight / wavy / curly / coiled]
- Part Direction: [left / right / center / none]
- Dynamic Quality: [how it moves with the character]
```

**Body Type System:**
```
- Body Type: [lean / average / rounded / specific description]
- Height: [tall / medium / short — relative to environment reference]
- Build: [slim / athletic / soft / angular]
- Posture: [upright / hunched / tense / relaxed]
- Movement Signature: [how they walk, stand, fidget]
```

**Clothing System:**
```
- Signature Outfit: [complete description of primary clothing]
- Color Scheme: [2-4 colors that define the character's wardrobe]
- Fabric Language: [materials — leather, cotton, silk, technical fabric]
- Fit: [loose / fitted / drop-shoulder / structured]
- Accessories: [watch, glasses, jewelry, bag, weapon]
- Layering: [how pieces combine]
```

**Signature Props:**
```
- Prop 1: [description, which hand/side, when visible]
- Prop 2: [description, significance]
```

### 3. On-Camera Behavior System

**Eye Logic:**
```
- Default Gaze Direction: [direct / averted / scanning / distant]
- When Thinking: [up-right / down-left / etc.]
- When Lying: [behavioral cue]
- When Attracted: [gaze pattern]
- When Threatened: [eye movement]
```

**Emotion → Action Mapping:**
```
Sadness → shoulders drop, jaw lowers, breathing slows, gaze averts
Anger → jaw tightens, stillness, eyes narrow, breath controlled
Fear → micro-freeze, half-step back, rapid scanning, shallow breathing
Affection → hesitant approach, stolen glances, breathing shallows
Shock → complete stillness, eyes widen, mouth slightly open, no blinking
Joy → posture relaxes, smile reaches eyes, body language opens
```

**Movement Signature:**
```
- Walking Style: [stride length, speed, arm swing, weight distribution]
- Gesture Pattern: [gestural / restrained / exaggerated / nervous fidgeting]
- Stillness Behavior: [state when not actively moving]
- Signature Action: [define one distinctive movement]
```

### 4. Continuity Lock System

**Hard Locks (immutable):**
- [ ] Facial Identity — face shape, features, proportions
- [ ] Hair — length, style, color, texture
- [ ] Body Type — build, height proportions
- [ ] Clothing — signature outfit, color scheme
- [ ] Age — does not age or de-age across shots

**Soft Variations (allowed to change):**
- Facial lighting (different angles, different intensity)
- Emotional expression (within defined range)
- Camera angle (different views of the same face)
- Environmental effects (wind in hair, rain on face)

**Prohibited Changes:**
- Face-swapping / AI regenerating a different face
- Random outfit changes
- Age jumps between shots
- Style mutations (realistic → anime)
- Hair color or style change (unless story-driven and explicitly noted)

### 5. Character Reference Image Layout

**Seedance 2.0 critical restriction: Multi-view/three-view character sheets are PROHIBITED as video generation reference.** The model may recognize the same character from different angles as multiple distinct subjects, worsening ID drift and causing twin problems (two identical figures appearing in the same frame).

The correct character reference layout is **separate headshot + separate full-body image**, uploaded as two independent reference images:

```
Image1: Face Close-Up (Headshot)
  - Face only, minimize background interference
  - Expressionless preferred, minimize neck/shoulder area
  - Frontal, even lighting, neutral studio light
  - Purpose: lock facial identity (face shape, features, proportions)

Image2: Full-Body Shot
  - Show signature outfit complete fit, color scheme, body posture
  - Include signature props and accessories
  - Neutral studio light, clean background, frontal or 3/4 angle
  - Purpose: lock clothing, body type, overall styling

In Seedance prompts, reference as:
  `Subject1`'s facial features reference `Image1` (headshot), styling references `Image2` (full-body).

The more precise the reference needed, the earlier it should appear in the prompt.
```

To compile complete character identity definitions into platform-ready image generation prompts (MJ/Flux/Jimeng/Kling), route to the `character-image-prompt` skill, which follows the separate headshot + full-body layout specification.

### 6. Multi-Character System

For multi-character projects, add:

```
Character Relationship Map:
[A] ←→ [B]: [relationship type, power dynamic, emotional tone]
[B] ←→ [C]: [relationship type, power dynamic, emotional tone]

Visual Contrast Design:
- Character A vs B: [body type contrast, color contrast, shape language contrast]
- Shared Lighting Rules: [how they interact with the same light source]
- Interaction Rules: [physical distance norms, eye contact patterns, touch boundaries]
```

## Constraints

- Every character must have a complete visual identity system before entering storyboarding.
- Facial parameters must be specific enough that different prompt writers would produce the same description.
- Emotion→action mappings must cover the full emotional range the character experiences in the story.
- Hard locks must be explicitly referenced in every Seedance prompt containing that character.
- Multi-character scenes must define interaction rules to prevent AI confusion.
- **Multi-view/three-view character sheets are PROHIBITED as Seedance reference** — use separate headshot (face only) + full-body, uploaded separately, with headshot placed first in prompt.

## Downstream Pipeline

This skill produces **character identity definitions** (text-level design documents). After user confirmation:

1. Route to `character-image-prompt` → compile identity definitions into platform-ready image prompts (separate headshot + full-body, NOT multi-view sheets)
2. User generates character reference images (MJ/Flux/Jimeng/Kling)
3. Generated character reference images (ImageN: headshot + ImageN+1: full-body) serve as Seedance reference input, face reference placed first in prompt

## Integration

When called by `director-core`:
- Character Identity Core and Visual Identity System become the single source of truth for all downstream prompts
- After STATE 3 completion, route to `character-image-prompt` to compile image generation prompts (separate headshot + full-body format)
- Continuity Lock System hard locks must be embedded in every Seedance prompt via `seedance-video-prompt`
- Character identity definitions must be user-confirmed before entering image prompt generation
- **Seedance 2.0 constraint: use separate headshot (face close-up) + full-body; multi-view/three-view character sheets PROHIBITED**
