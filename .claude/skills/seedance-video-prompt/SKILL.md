---
name: seedance-video-prompt
description: Compiles storyboard images, character reference images, and product reference images into executable video generation prompts for Seedance 2.0 / Kling platforms. This is the final L5 video generation layer compiler in the AI Film OS pipeline. Use for generating Seedance 2.0 prompts, video generation prompts, storyboard-to-video prompts, or when director-core routes to STATE 6 (video prompt compilation). Use when the user has already generated storyboard images and character reference images and needs them converted into executable prompts for Seedance and other video platforms. Trigger words: Seedance 2.0 prompt, video generation prompt, storyboard to video, Seedance prompt, video generation prompt.
---

# Seedance Video Prompt — L5 Video Generation Compiler

## Overview

This is the final compiler of **L5 — VIDEO GENERATION LAYER** in the AI Film OS pipeline. It receives generated storyboard images, character reference images, product reference images, and background reference images, and compiles them into executable video generation prompts for Seedance 2.0 / Kling platforms.

**Key Distinction:**

- `director-prompt-packager` (STATE 4): Text-level compiler → produces a film-level short film prompt package (storyboard design + camera language + sound design + Seedance decomposition plan). **Not a video platform prompt.**
- `seedance-video-prompt` (STATE 6): Image-reference-level compiler → produces Seedance 2.0 executable prompts for video platforms.

## Load Resources

This skill includes bundled reference knowledge. Load when needed:

- For Director Formula, @[ref] role mapping, I2V principles, compression rules, anti-slop lexicon, and mode gates — read `references/seedance-methodology.md`
- For Seedance platform constraints (word limits, @[ref] format, Part limits), read shared reference `../references/seedance-platform.md`
- For a more detailed anti-slop replacement table, read shared reference `../references/anti-slop-lexicon.md`
- For genre recipe families and prompt skeletons (product, drama, first/last frame, etc.), read `../references/seedance-genre-recipes.md`

---

## Platform Hard Constraints

### Prompt Word Count Limits

| Language             | Limit             | Rationale                                                        |
| -------------------- | ----------------- | ---------------------------------------------------------------- |
| **Chinese**          | ≤ 500 characters  | Excess characters scatter information; the model ignores details |
| **English**          | ≤ 1000 words      | Same as above                                                    |
| **Total characters** | ≤ 2000 characters | seedance-prompt platform budget                                  |

**Violating this constraint will cause missing video elements, character drift, and incomplete motion.** After compilation, count and annotate the character/word count.

### @[ref] Reference Format (Seedance 2.0 Standard)

All uploaded image/video/audio assets use the `@[description]` format:

| Reference Example       | Purpose                                          |
| ----------------------- | ------------------------------------------------ |
| `@[storyboard image 1]` | Storyboard blueprint — motion planning reference |
| `@[character image 1]`  | Character identity lock — face, hair, body type  |
| `@[product image 1]`    | Product lock — color, print, fit                 |
| `@[background image 1]` | Environment lock — space, light, color tone      |

## Compilation Principles

> Seedance 2.0 prompts are **image-reference-driven motion instructions**. They reference locked visual assets (storyboard images, character images, product images), adding temporal motion descriptions to them. **Only describe what the image cannot convey** — motion, camera, lighting changes, time progression, sound.

Seedance Director Formula:

```
Subject + Action + Scene + Camera + Lighting/Style + Audio + Constraints
```

The compiler translates three layers into a single Seedance 2.0 executable prompt:

1. **Visual Lock Layer** (what to reference) → @[storyboard image] @[character image] @[product image] @[background image]
2. **Motion Instruction Layer** (how it moves) → continuous camera movement + character action + environment dynamics
3. **Constraint Rule Layer** (what must not appear) → negative constraints + continuity preservation

## Input Requirements

Before compiling, verify these assets are ready:

- [ ] Storyboard blueprint images (from AI image generators like MJ/Flux/Jimeng) — each panel as a continuous cinematic beat
- [ ] Character reference images (from director-character or user-provided) — authoritative character identity lock
- [ ] (Optional) Product reference images — lock product color, pattern, fit
- [ ] (Optional) Background reference images — lock spatial structure, light, color tone
- [ ] Project metadata: total duration, aspect ratio, music style

If any critical asset is missing, prompt the user to generate the corresponding image using an AI image generator first.

## Reference Role Mapping

Before writing prompts, assign a **unique primary role** to each uploaded asset. Role mapping prevents accidental cross-contamination between identity, logo, scene ownership, and camera instructions.

| Asset | Recommended Role                                                       | Avoid                                           |
| ----- | ---------------------------------------------------------------------- | ----------------------------------------------- |
| Image | identity, product, pose, costume, environment, first frame, last frame | Asking it to define unseen motion               |
| Video | motion, camera, pacing, blocking, timing, gesture rhythm               | Copying protected identity, logo, or scenes     |
| Audio | rhythm, tempo, mood, ambience, delivery tone, music texture            | Assuming voice/song/portrait rights are cleared |

**Core Rules:**

- Each referenced asset gets one primary role; do not layer additional style descriptions on top
- Explicitly declare "what must be preserved" and "what must not transfer"
- If authorization is unclear, only transfer generalized motion/rhythm/mood/production function, not protected identity

**Role Mapping Declaration Template:**

```
@[product image 1] controls product identity — strictly lock color, print pattern, print color, size, position, fit.
@[character image 1] controls character identity — strictly preserve the same model's core features, natural face.
@[storyboard image 1] controls action pacing — used as motion planning reference, do not render the storyboard itself.
@[background image 1] controls environment — strictly preserve spatial structure, lighting, color tone, and display stability.
@[audio 1] controls rhythm and energy only — do not copy protected sounds, songs, or performer identity.
```

## Output Structure: Seedance 2.0 Video Prompt

### Complete Template

```
Seedance 2.0 Prompt:

Use @[storyboard image 1] as the authoritative shot blueprint. Do not render the storyboard itself. Ignore all borders, panel frames, text, labels, titles, color swatches, director bar graphics, and layout elements. Treat each panel as a continuous cinematic beat.
The entire video must play as one continuously developing master shot with no visible cuts; each panel is a sampled stage of the same uninterrupted camera movement, not a separate shot.
Use one virtual lens / same lens continuous camera movement; scale changes come only from physical camera movement.
Use @[character image 1] as the authoritative character reference.

[If multi-character or product references exist, add role mapping declarations here]

Music: [music style, BPM, mood]

[Subject action description, unfolding along the timeline, each paragraph corresponds to one storyboard panel, each panel one action stage]

[Negative constraint list]
```

### 1. Image Reference Section (@[ref] Syntax)

Every Seedance 2.0 prompt must begin with an image reference section:

| Reference Type | Format                  | Role Declaration (must include)                                                                                                                                                              |
| -------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Storyboard     | `@[storyboard image 1]` | "Used as motion planning reference, do not render the storyboard itself. Ignore all borders, panel frames, text, labels, titles, color swatches, director bar graphics, and layout elements" |
| Character      | `@[character image 1]`  | "As the authoritative character reference, strictly preserve the same model's core features, natural face"                                                                                   |
| Product        | `@[product image 1]`    | "Strictly lock color, print pattern, print color, size, position, fit"                                                                                                                       |
| Background     | `@[background image 1]` | "Strictly preserve spatial structure, lighting, color tone, and background display stability"                                                                                                |

### 2. Continuous Camera Movement Section

**Core principle: The entire video plays as one continuously developing master shot with no visible cuts.**

Each storyboard panel is a sampled stage of the same uninterrupted camera movement:

- Use one virtual lens / same lens continuous camera movement
- Scale changes come only from physical camera movement (push-in / pull-out / tracking)
- No jump cuts between panels — motion transitions smoothly
- **Use one primary camera movement** (from cinematography-shot-language: push-in / lateral track / orbit / crane / locked-off, etc.)

Motion description unfolds along the timeline, each panel corresponding to a natural language paragraph:

```
1. [Opening shot corresponding to panel 1 — establish space and initial state]
2. [Motion stage corresponding to panel 2 — character action or environment change]
3. [Motion stage corresponding to panel 3 — continuing progression]
...
N. [Closing shot corresponding to panel N — emotional landing point]
```

### 3. Music / Rhythm Section

```
Music: [style description], BPM [range], [additional notes such as no narration, no speaking]
```

Common music style references:

- Fashion/Apparel: lo-fi hip-hop / chill trap / fashion beat, BPM 90-110
- Drama/Film: cinematic ambient / orchestral swell, BPM 60-80
- Action/Fast-paced: electronic / drum & bass, BPM 120-140
- Warm/Lifestyle: acoustic guitar / soft piano, BPM 70-90

### 4. Motion Description Specifications

- **One action stage per panel**, not independent shots
- Natural transitions between actions via camera movement (push-in → tracking → orbit → pull-out)
- Fabric, hair, environment elements produce realistic dynamics with motion
- If there is a turn or back angle, declare that the back must be plain / no text / no logo
- **Describe observable physical actions** (from anti-slop: if a camera cannot detect it, rewrite)

### 5. Negative Constraints Section

Must-include negative constraints (adjust per scene):

```
No subtitles, no watermarks, no brand logos.
No facial distortion, no identity drift, no character face swaps.
No clothing distortion, no print drift, no product appearance inconsistency.
No scene drift, no spatial reset, no environment jumps.
No new characters appearing, no extra figures.
No unnatural motion, no CGI artifacts.
[Scene-specific constraints]
```

## I2V Core Principles

**Only describe what the image cannot convey.** A static image already contains subject identity, product form, clothing, color palette, composition, background. Re-describing these static details typically causes drift. Only add to the image: motion, camera, time progression, lighting changes, sound, preservation constraints.

**Minimal I2V Template:**

```
@[image 1] as reference, strictly preserve [identity/product/scene]. Only [motion] changes. Camera: [one movement]. Light: [source or transition]. Sound: [cue]. Constraints: [what must not change].
```

**Common I2V Failure Fixes:**

| Failure             | Fix                                                                   |
| ------------------- | --------------------------------------------------------------------- |
| Identity drift      | Reduce new visual descriptions, strengthen preservation constraints   |
| Camera jumps        | Use one camera movement, note start and end frames                    |
| Product deformation | Declare preserved, static identity, no shape change                   |
| Static image        | Add one physical action and one temporal cue                          |
| Background change   | Preserve environment layout, only animate lighting/weather/atmosphere |
| Hand deformation    | Simplify hand motion or exclude hands from the main action            |

## Mode Gates

| Mode    | Compilation Priority                    | Common Error                                                               | Fix                                                            |
| ------- | --------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **T2V** | Build complete shot with compact layers | Too many events in one segment                                             | Keep one visible beat + one end point                          |
| **I2V** | Preserve visible identity; add motion   | Re-describing image until product or face drifts                           | Write `strictly preserve @[image 1]`; only add dynamic changes |
| **R2V** | Assign independent roles to each asset  | One asset asked to simultaneously control identity, pose, scene, and style | Split roles or prioritize the most important role              |

## Compression Rules

When prompts are too long, trim in this order:

1. **Delete**: repeated style adjectives, generic quality words, background details already visible in references, secondary camera movements, secondary actions, speculative emotion labels
2. **Keep**: reference tags and their roles, subject/product identity, one action verb + visible endpoint, one camera movement, physical light source or atmosphere, sound cue, safety/IP/continuity constraints

**Compressed Template (Chinese I2V):**

```
@[image 1] as reference, strictly preserve [subject] unchanged; only add [action/light/camera]. Sound: [cue]. Constraints: [what must not change].
```

## Anti-Slop Lexicon

Replace hollow evaluation words with observable production language:

| Hollow Word     | Replace With                                                                |
| --------------- | --------------------------------------------------------------------------- |
| cinematic       | shot size + camera movement + lighting + color grading                      |
| epic            | physical scale + stakes + lens distance                                     |
| beautiful       | color + texture + composition + material + light behavior                   |
| stunning        | visible contrast + reveal + motion + detail                                 |
| dynamic         | specific motion + speed + endpoint                                          |
| dramatic        | blocking + shadow + silence + camera pressure                               |
| ultra-realistic | material performance + skin texture + lens characteristics + natural motion |

**Rule: If a camera, microphone, light meter, or stopwatch cannot detect it — rewrite.**

## Complete Examples

### Example 1: Fantasy Short Film

```
Seedance 2.0 Prompt:

Use @[storyboard ref] as the authoritative shot blueprint. Do not render the storyboard itself. Ignore all borders, panel frames, text, labels, titles, color swatches, director bar graphics, and layout elements. Treat each panel as a continuous cinematic beat.
The entire video must play as one continuously developing master shot with no visible cuts; each panel is a sampled stage of the same uninterrupted camera movement, not a separate shot.
Use one virtual lens / same lens continuous camera movement; scale changes come only from physical camera movement.
Use @[character ref] as the authoritative C1 character reference.

Create a cinematic 16:9 video showing C1 falling through a nightmare space-time void that collapses into a moonlit gothic castle bedroom, where she wakes up and says "FATHER".

Final style: stylized fantasy, faithful to the referenced sculptural anime-fantasy character, matte graphite-inspired surfaces, cold silver-blue moonlight, deep soft volumetric shadows, thin temporal fragmentation effects, collapsing dream debris, elegant high-end cinematic camera movement.

1. Begin in endless black space with no floor, sky, or horizon. C1 falls in the center of frame, very long white hair drifting upward, one hand reaching out for stability, while the camera falls with her.
2. The camera begins a smooth falling orbit. Broken clocks, floating doors, ancient castle fragments, moonlit forest branches, ruined cities, battlefield debris, and forgotten faces rush past at varying depths.
3. A stone step or ledge momentarily appears beneath C1; she reaches for it, but it dissolves before contact. The camera drops from beneath her along the same downward path.
4. Different eras collide around her — castle arches, battlefield banners, city ruins, and clock faces spiral faster, distorting the frame like runaway time travel.
5. Recognizable bedroom elements flash through the nightmare: a bed frame, a curtain, a tall gothic window, a stone wall, and a nightstand appear and vanish while C1 continues falling.
6. The falling axis narrows toward a partially formed bed below; nightmare fragments funnel inward — windows, curtains, a crystal chandelier, and stone walls attempt to lock into place.
7. C1 crashes violently into the bed, not into darkness or stone. All void fragments, time shards, and castle architecture collapse into the mattress point on contact.
8. Reality silently snaps into form: the castle bedroom fully materializes around the bed. Moonlight pours through the tall gothic window, stone walls and furniture become solid, nightmare residue gradually fades.
9. Without a cut, C1 sits up sharply in bed, breathing rapidly, eyes wide with fear, scanning the room to test if she is awake, then says softly: "FATHER".
10. The camera continues its remaining momentum, slowly pulling back on the same axis, revealing the vast moonlit castle room — ancient stone architecture, solitary furniture, and C1 appearing small in the bed under cold light.
```

### Example 2: E-commerce Menswear (Role Mapping + I2V Compressed Version)

```
Seedance 2.0 Prompt:

@[background image 1] controls environment — strictly preserve spatial structure, lighting, warm wood tones, and display stability.
@[character image 1] controls character identity — strictly preserve the same young male model's core features, natural face.
@[product image 1] controls product identity — strictly lock T-shirt color, front print pattern, print color, size, position, relaxed drop-shoulder fit.
@[storyboard image 1] controls action pacing — used as motion planning reference, do not render the storyboard itself. Ignore all borders, panel frames, text, labels, layout elements. Treat each panel as a continuous cinematic beat, strictly follow panel order and timing rhythm.

Music: lo-fi hip-hop / chill trap, BPM 90-110, no narration, no speaking.

The entire video plays as one continuous master shot with no visible cuts. Model's movements are natural and fluid, fabric produces realistic folds and subtle sway with motion. If a turn or back angle occurs, the T-shirt back must be solid color with no print, no text, no logo.

No subtitles, no watermarks, no brand logos, no back prints, no back text, no print drift, no clothing distortion, no scene drift, no new characters.

Word count: 380 characters ✅
```

### Example 3: Chinese I2V Minimal Compression (Jimeng/Kling Standard)

```
@[image 1] as product reference, strictly preserve logo, label, bottle shape, and color unchanged.
Camera slowly pushes in to label close-up; warm light from the left sweeps across the glass, water droplets slide down the bottle.
Background remains dark and still. Sound: subtle ambient noise, one crisp glass sound at the end.
Character count: 96 characters ✅
```

## Validation Checklist

Before delivering the final Seedance 2.0 prompt, verify item by item:

- [ ] Storyboard image reference is correct, with "do not render the storyboard itself" declared
- [ ] Character image reference is correct, with role mapping role declared ("controls character identity / strictly preserves")
- [ ] Product image reference is correct (if applicable), with product mapping role and lock parameters declared
- [ ] Background image reference is correct (if applicable), with environment mapping role declared
- [ ] Each @[ref] is assigned a unique primary role, no layered style descriptions
- [ ] Continuous camera movement description covers all storyboard panels
- [ ] Each panel corresponds to one motion stage (1-N numbering clear)
- [ ] One primary camera movement is used, not stacked multiples
- [ ] "No visible cuts" and "same uninterrupted camera movement" are declared
- [ ] Music style and BPM are specified
- [ ] Fabric/hair dynamics described (if applicable)
- [ ] Back constraint declared (if applicable)
- [ ] Negative constraint list is complete
- [ ] **Word count compliant: Chinese ≤ 500 characters / English ≤ 1000 words (count annotated)**
- [ ] **Anti-slop check: no hollow evaluation words (cinematic/epic/beautiful, etc., with no physical referent)**
- [ ] Prompt can be directly pasted into the Seedance 2.0 platform for use

## Common Scenario Adaptations

### Fashion / Apparel Videos

- Must use role mapping declaration: `@[product image 1]` locks color/print/fit
- Fabric dynamics (folds, sway) must be described
- Back constraint (solid color, no print, no text)
- Music: lo-fi hip-hop / chill trap, BPM 90-110
- **Compactness: prioritize Chinese compression, within 500 characters**

### Product Showcase Videos

- Product image reference locks appearance, background image reference locks environment
- Camera movement prioritizes push-in / orbit / detail, **one primary movement**
- No product appearance drift
- **Key principle: let light/particles/camera move around the product, not deform the product itself**

### Narrative Short Films

- Character image reference locks identity, storyboard image reference locks narrative pacing
- Continuous camera movementthroughout the film
- Emotion evolves, never resets
- **One segment = one beat = one emotional turn**

### Multi-Character Scenes

- Each character gets a separate `@[character image N]` reference + role mapping declaration
- Declare that spatial relationships between characters remain unchanged
- No character identity swapping or drift

## Integration

When called by `director-core`:

- Confirm STATE 5 is complete (storyboard blueprint images have been generated)
- Load all visual reference assets (storyboard images, character images, product images, background images)
- Assign @[ref] role mapping for each asset
- Compile Seedance 2.0 executable prompts
- **Count and annotate character/word count** (Chinese ≤ 500 characters)
- Execute validation checklist (including role mapping check + word count check + anti-slop check)
- Present for final user review
- Upon confirmation, mark STATE 6 complete
