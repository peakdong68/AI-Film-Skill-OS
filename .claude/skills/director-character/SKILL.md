---
name: director-character
description: Design and lock character identity for AI film production — character sheets, visual identity parameters, behavior systems, emotion-to-motion mapping, and multi-character relationship management. Use when the user needs character design, character design, character consistency, character consistency, character sheet creation, or when director-core routes to STATE 3 (Character Lock). Also use when AI-generated characters keep changing faces or outfits across shots — this skill builds the identity lock that prevents character drift. Note: this skill produces character identity DEFINITIONS (text-level design docs). For compiling these into executable image generation prompts, use the character-image-prompt skill.
---

# Director Character — Character Consistency Engine

## Overview

Design character identity with enough specificity that AI video generators can maintain it across shots. This skill produces a Character Consistency Sheet — a structured identity document that locks face, body, wardrobe, behavior, and emotional expression so the character remains stable through every frame of the film.

The most common failure in AI video production is character drift (face swaps, outfit changes, style breaks). This skill is the primary defense against it.

Works independently for character design or is invoked by `director-core` at STATE 3.

**Important:** This skill produces **character identity definitions** (text-level design documents). It does NOT produce executable image generation prompts. For compiling these definitions into platform-ready character sheet image prompts (MJ/Flux/Jimeng/Kling), use the `character-image-prompt` skill.


## Loaded Resources

This skill ships with reference knowledge files. Load them when:
- For the complete visual identity parameter checklist and identity lock specifications, read `references/character-identity.md`
- For the micro-motion unit library, emotion-to-full-body mapping, and micro-expression system, read `references/motion-translation.md`
## The Core Principle

> Character consistency in AI video is not a prompt-tuning problem — it's an identity-specification problem.

The AI must receive identical identity parameters in every prompt. Slight variations in description cause cascading drift. This skill creates the master identity document that all prompts reference.

## Output Structure

### 1. Character Identity Core (Character Identity Core)

```
CHARACTER: [name]
- Narrative role: [protagonist / antagonist / supporting / observer]
- Age range: [e.g., 25-30]
- Gender expression: [description]
- Emotional identity: [core emotional state — calm, anxious, fierce, vulnerable]
- Psychological profile: [key traits, motivations, fears]
- Story function: [what does this character accomplish in the narrative?]
- Character arc: [from state A at start → to state B at end]
```

### 2. Visual Identity System (Visual Identity System)

**Face System (Face):**
```
- Face shape: [oval / round / angular / heart / square]
- Skin tone: [specific descriptor with undertone reference]
- Eye shape: [almond / round / hooded / monolid / deep-set]
- Eye color: [specific, no "beautiful eyes"]
- Eyebrows: [shape, thickness, arch]
- Nose: [shape, bridge, tip]
- Mouth: [shape, lip fullness]
- Jaw/chin: [shape, definition]
- Distinguishing features: [scars, moles, freckles, asymmetry]
- Facial structure notes: [overall impression, bone structure]
```

**Hair System (Hair):**
```
- Style: [specific cut name or description]
- Length: [measured relative to facial features]
- Color: [specific shade, not "brown"]
- Texture: [straight / wavy / curly / coiled]
- Part direction: [left / right / center / none]
- Movement quality: [how it moves with the character]
```

**Body System (Body):**
```
- Body type: [ectomorph / mesomorph / endomorph / specific description]
- Height: [tall / average / short — relative to environment cues]
- Build: [lean / athletic / soft / angular]
- Posture: [upright / slouched / coiled / relaxed]
- Movement signature: [how they walk, stand, fidget]
```

**Wardrobe System (Wardrobe):**
```
- Signature outfit: [complete description of primary costume]
- Color palette: [2-4 colors that define the character's wardrobe]
- Fabric language: [materials — leather, cotton, silk, tech fabric]
- Fit: [loose / tailored / oversized / structured]
- Accessories: [watch, glasses, jewelry, bag, weapon]
- Layering: [how pieces combine]
```

**Signature Props (Signature Props):**
```
- Prop 1: [description, which hand/side, when visible]
- Prop 2: [description, significance]
```

### 3. Cinematic Behavior System (Cinematic Behavior System)

**Eye Direction Logic (Eye Direction Logic):**
```
- Default gaze: [direct / averted / scanning / distant]
- When thinking: [up-right / down-left / etc.]
- When lying: [behavioral tell]
- When attracted: [glance pattern]
- When threatened: [eye movement]
```

**Emotion-to-Motion Mapping (Emotion-to-Motion Mapping):**
```
Sadness → shoulders drop, chin lowers, breathing slows, eyes avoid contact
Anger → jaw tightens, stillness, narrowed eyes, controlled breathing
Fear → micro-freeze, slight step back, rapid eye movement, shallow breath
Affection → hesitant approach, stolen glances, breathing becomes shallow
Shock → complete stillness, eyes widen, mouth slightly open, no blink
Joy → relaxed posture, genuine smile reaching eyes, open body language
```

**Movement Signature (Movement Signature):**
```
- Walking style: [stride length, pace, arm swing, weight distribution]
- Gesture pattern: [hand talker / reserved / expansive / nervous ticks]
- Stillness behavior: [what they do when not actively moving]
- Signature action: [one unique movement that defines them]
```

### 4. Continuity Lock System (Continuity Lock System)

**Hard Locks (Immutable):**
- [ ] Face identity — face shape, features, proportions
- [ ] Hair — style, length, color, texture
- [ ] Body type — build, height proportion
- [ ] Wardrobe — signature outfit, color palette
- [ ] Age — no aging or de-aging between shots

**Soft Variations (Allowed Variations):**
- Lighting on face (different angles, intensities)
- Emotional expression (within the defined range)
- Camera angle (different perspectives of the same face)
- Environmental effects (wind in hair, rain on face)

**Forbidden Changes (Forbidden Changes):**
- Face swap / AI regenerated face
- Random wardrobe changes
- Age jumps between shots
- Style shift (photorealistic → anime)
- Hair color or style change (unless story-motivated and explicitly noted)

### 5. Character Sheet Image Layout Reference (Character Sheet Image Layout Reference)

This section provides a **view coverage template** — it defines what visual angles and states the character sheet should cover. It is NOT an executable image generation prompt.

To compile the full character identity definition into platform-ready image generation prompts (MJ/Flux/Jimeng/Kling), route to the `character-image-prompt` skill, which follows the multi-view character design board specification.

View coverage requirements:
```
Character sheet layout: full body front view, side profile, 3/4 view, back view
Face detail: close-up front, neutral expression
Expression range: neutral, [emotion 1], [emotion 2], [emotion 3]
Wardrobe: [signature outfit] shown in full
Lighting: neutral studio light, clean background
Style: cinematic realism, consistent across all views
Negative: no text, no watermark, no face distortion, no identity variance between views
```

### 6. Multi-Character System (Multi-Character System)

For projects with multiple characters, add:

```
Character Relationship Map:
[A] ←→ [B]: [relationship type, power dynamic, emotional tone]
[B] ←→ [C]: [relationship type, power dynamic, emotional tone]

Visual Contrast Design:
- Character A vs B: [size contrast, color contrast, shape language contrast]
- Shared lighting rules: [how they interact with the same light source]
- Interaction rules: [physical distance norms, eye contact patterns, touch boundaries]
```

## Constraints

- Every character must have a complete Visual Identity System before entering storyboard.
- Face parameters must be specific enough that two different prompt writers would produce the same description.
- Emotion-to-motion mapping must cover the full emotional range the character experiences in the story.
- Hard locks must be explicitly referenced in every Seedance prompt that features the character.
- Multi-character scenes must define interaction rules to prevent AI confusion.

## Downstream Pipeline

This skill produces a **character identity definition** (text-level design doc). After user confirmation:

1. Route to `character-image-prompt` → compiles identity into platform-ready image generation prompts
2. User generates character reference images (MJ/Flux/Jimeng/Kling)
3. Generated character images are used as `@[character ref]` in `seedance-video-prompt` (STATE 6)

## Integration

When invoked by `director-core`:
- The Character Identity Core and Visual Identity System become the single source of truth for all downstream prompts
- After STATE 3 completion, route to `character-image-prompt` to compile into image generation prompts
- The Continuity Lock System's Hard Locks must be embedded in every Seedance prompt via `seedance-video-prompt`
- Character identity definition must be confirmed by the user before proceeding to image prompt generation
