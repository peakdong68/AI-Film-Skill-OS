---
name: seedance-video-prompt
description: Compile storyboard images, character reference images, and product reference images into Seedance 2.0 / Runway / Sora / Kling video platform-executable prompts. This is the final L5 video generation layer compiler in the AI Film OS pipeline. Use for generating Seedance 2.0 prompts, video generation prompts, storyboard-to-video prompts, or when director-core routes to STATE 6 (Video Prompt Compilation). Use when the user has generated storyboard images and character reference images and needs them converted into executable prompts for video platforms like Seedance. Trigger words: Seedance 2.0 prompt, video generation prompt, storyboard to video, Seedance prompt, video generation prompt.
---

# Seedance Video Prompt — L5 Video Generation Compiler

## Overview

This is the final compiler of **L5 — VIDEO GENERATION LAYER** in the AI Film OS pipeline. It receives generated storyboard images, character reference images, product reference images, and background reference images, and compiles them into Seedance 2.0 / Runway / Sora / Kling video platform-executable prompts.

**Key distinctions:**
- `director-prompt-packager` (STATE 5): Text-level compiler → produces storyboard prompts for AI image generators
- `seedance-video-prompt` (STATE 6): Image-reference-level compiler → produces Seedance 2.0 executable prompts for video platforms

**Knowledge dependency:** This skill extracts Seedance 2.0 prompt methodology from `reference/seedance-20/` — including the Director Formula, @[ref] role mapping, compression rules, anti-slop, and I2V best practices.

## Platform Hard Constraints

### Prompt Length Limit

| Language | Limit | Rationale |
|------|------|------|
| **Chinese** | ≤ 500 characters | Excess text disperses focus; model may ignore details |
| **English** | ≤ 1000 words | Same as above |
| **Total characters** | ≤ 2000 characters | seedance-prompt platform budget |

**Violating these limits causes missing video elements, character drift, and incomplete actions.** Count and annotate word/character count after compilation.

### @[ref] Reference Format (Seedance 2.0 Standard)

All uploaded image/video/audio assets use the `@[descriptor]` format:

| Reference Example | Role |
|---------|------|
| `@[storyboard image 1]` | Storyboard blueprint — action planning reference |
| `@[character image 1]` | Character identity lock — face, hair, body type |
| `@[product image 1]` | Product lock — color, print, silhouette |
| `@[background image 1]` | Environment lock — space, lighting, color tone |

## Compilation Principle

> Seedance 2.0 prompts are **image-reference-driven motion instructions**. They reference locked visual assets (storyboard images, character images, product images) and add temporal motion descriptions. **Prompt only what the image cannot show** — motion, camera, light changes, time progression, sound.

Adopting the Director Formula from `reference/seedance-20/`:

```
Subject + Action + Scene + Camera + Lighting/Style + Audio + Constraints
```

The compiler translates three layers into a single Seedance 2.0 executable prompt:
1. **Visual Lock Layer** (what to reference) → @[storyboard] @[character] @[product] @[background]
2. **Motion Instruction Layer** (how to move) → continuous camera movement + character action + environmental dynamics
3. **Constraint Rule Layer** (what must not appear) → negative constraints + continuity preservation

## Input Requirements

Before compilation, verify these assets are ready:

- [ ] Storyboard frame images (from AI image generators like MJ/Flux/Jimeng) — each panel as a continuous cinematic beat
- [ ] Character reference images (from director-character or user-provided) — authoritative character identity lock
- [ ] (Optional) Product reference images — lock product color, pattern, silhouette
- [ ] (Optional) Background reference images — lock spatial structure, lighting, color tone
- [ ] Project metadata: total duration, aspect ratio, music style

If any critical asset is missing, prompt the user to generate the corresponding images first.

## Reference Role Mapping (from seedance-20 reference-workflow)

Before writing prompt prose, assign each uploaded asset a **single primary role**. Role mapping prevents accidental transfer of identity, logos, scene ownership, or incompatible camera and motion instructions.

| Asset | Recommended Roles | Avoid |
|------|---------|------|
| Image | identity, product, pose, costume, environment, first frame, last frame | asking it to define unseen motion |
| Video | motion, camera, pacing, blocking, timing, gesture rhythm | copying protected identity, logo, or scene ownership |
| Audio | rhythm, tempo, mood, ambience, delivery tone, music texture | assuming voice, song, or likeness authorization |

**Core rules:**
- Assign each reference asset one primary role; do not stack style descriptions on top
- State explicitly "what must be preserved" and "what must not transfer"
- When authorization is unclear, transfer broad motion, tempo, mood, or production function — not protected identity

**Role mapping declaration template:**

```
@[product image 1] controls product identity — strictly lock color, print pattern, print color, size, position, silhouette.
@[character image 1] controls character identity — strictly preserve the same model's primary features, natural face.
@[storyboard image 1] controls action rhythm — used for action planning reference, do not render the storyboard itself.
@[background image 1] controls environment — strictly preserve spatial structure, lighting, color tone, and display arrangement.
@[audio 1] controls tempo and energy only — do not copy protected voice, song, or performer identity.
```

## Output Structure: Seedance 2.0 Video Prompt

### Complete Template

```
Seedance 2.0 Prompt:

Use @[storyboard image 1] as the authoritative shot blueprint. Do not render the storyboard itself. Ignore all borders, panel frames, text, labels, titles, color swatches, director bar graphics, and layout elements. Treat each panel as a continuous cinematic beat.
The entire video must play as one continuously developing master shot with no visible cuts; each panel is a sampled stage of the same uninterrupted camera movement, not separate shots.
Use a single virtual lens / same-lens continuous camera movement; scale changes come only from physical camera movement.
Use @[character image 1] as the authoritative character reference.

[Add role mapping declarations for multi-character or product references here if applicable]

Music: [music style, BPM, mood]

[Subject action description, expanded on a timeline, each paragraph corresponding to a storyboard panel, one action phase per panel]

[Negative constraint list]
```

### 1. Image Reference Zone (@[ref] Syntax)

Every Seedance 2.0 prompt must begin with the image reference zone:

| Reference Type | Format | Role Declaration (must include) |
|----------|------|---------|
| Storyboard | `@[storyboard image 1]` | "Used for action planning reference, do not render the storyboard itself. Ignore all borders, panel frames, text, labels, titles, color swatches, director bar graphics, and layout elements" |
| Character | `@[character image 1]` | "As authoritative character reference, strictly preserve the same model's primary features, natural face" |
| Product | `@[product image 1]` | "Strictly lock color, print pattern, print color, size, position, silhouette" |
| Background | `@[background image 1]` | "Strictly preserve spatial structure, lighting, color tone, and background display arrangement" |

### 2. Continuous Camera Movement Zone

**Core principle: The entire video plays as one continuously developing master shot with no visible cuts.**

Each storyboard panel is a sampled stage of the same uninterrupted camera movement:
- Use a single virtual lens / same-lens continuous camera movement
- Scale changes come only from physical camera movement (push-in/pull-out/tracking)
- No jump cuts between panels — smooth motion transitions
- **Use one primary camera movement** (from cinematography-shot-language: push-in / lateral track / orbit / crane / locked-off, etc.)

Motion description expands on a timeline, each panel corresponding to a natural language paragraph:

```
1. [Opening shot for panel 1 — establish space and initial state]
2. [Motion phase for panel 2 — character action or environmental change]
3. [Motion phase for panel 3 — continue progression]
...
N. [Closing shot for panel N — emotional landing point]
```

### 3. Music/Rhythm Zone

```
Music: [style description], BPM [range], [additional notes like no narration, no dialogue]
```

Common music style references:
- Fashion/apparel: lo-fi hip-hop / chill trap / fashion beat, BPM 90-110
- Drama/film: cinematic ambient / orchestral swell, BPM 60-80
- Action/fast-paced: electronic / drum & bass, BPM 120-140
- Warm/lifestyle: acoustic guitar / soft piano, BPM 70-90

### 4. Action Description Standards

- **One action phase per panel**, not independent shots
- Actions transition naturally through camera movement (push-in → tracking → orbit → pull-out)
- Fabric, hair, environmental elements produce realistic dynamics with movement
- If there is a turn or back angle, declare the back must have no pattern/text/logo
- **Describe observable physical actions** (from anti-slop: if a camera cannot detect it, rewrite it)

### 5. Negative Constraint Zone

Must include (adjusted per scene):

```
No subtitles, no watermark, no brand logo.
No face distortion, no identity drift, no character face swap.
No wardrobe deformation, no print drift, no product appearance inconsistency.
No scene drift, no spatial reset, no environment jump.
No new characters, no extra characters.
No unnatural motion, no CGI artifacting.
[Scene-specific constraints]
```

## I2V Core Rule (from seedance-20 i2v-guide)

**Prompt only what the image cannot show.** A still image already contains subject identity, product form, wardrobe, palette, composition, and background. Re-describing those static details often causes drift. Only add for the image: motion, camera, timing, lighting changes, sound, preservation constraints.

**Minimal I2V template:**
```
@[image 1] is the reference; preserve [identity/product/scene] exactly. Only [motion] changes. Camera: [one move]. Lighting: [source or transition]. Sound: [cue]. Constraint: [what must not change].
```

**Common I2V failure fixes:**

| Failure | Fix |
|------|------|
| Identity drift | Reduce new visual description; strengthen preservation constraints |
| Camera jump | Use one camera move with start and endpoint |
| Product warps | Declare preserved, static identity, no shape change |
| Still output | Add one physical action and one time cue |
| Background changes | Preserve environment layout; animate only light, weather, or atmosphere |
| Hand deformation | Simplify hand motion or keep hands outside main action |

## Mode Gate (from seedance-20 seedance-prompt)

| Mode | Compilation Priority | Common Mistake | Fix |
|------|---------|---------|------|
| **T2V** | Build the whole shot in compact layers | Too many events in one clip | Keep one visible beat and one endpoint |
| **I2V** | Preserve visible identity; add motion | Re-describing the image until product or face drifts | Write "strictly preserve @[image 1]"; add only dynamic changes |
| **R2V** | Assign separate roles to each asset | One reference asked to control identity, pose, scene, and style | Split roles or prioritize the most important role |

## Compression Rules (from seedance-20 seedance-prompt-short)

When the prompt is too long, cut in this order:

1. **Delete**: duplicate style adjectives, generic quality words, background details already visible in references, secondary camera moves, secondary actions, speculative emotional labels
2. **Preserve**: reference tags and their roles, subject/product identity, one action verb + visible endpoint, one camera move, physical light source or atmosphere, sound cue, safety/IP/continuity constraints

**Compressed template (Chinese I2V):**
```
@[image 1] is reference, strictly preserve [subject] unchanged; only add [motion/light/camera]. Sound: [cue]. Constraint: [what must not change].
```

## Anti-Slop (from seedance-20 anti-slop-lexicon)

Replace empty evaluation language with observable production language:

| Empty Word | Replace With |
|------|-----|
| cinematic | shot scale + camera movement + lighting + grade |
| epic | physical scale + stakes + lens distance |
| beautiful | color + texture + composition + material + light behavior |
| stunning | visible contrast + reveal + movement + detail |
| dynamic | specific movement + speed + endpoint |
| dramatic | blocking + shadow + silence + camera pressure |
| ultra-realistic | material behavior + skin texture + lens artifacts + natural motion |

**Rule: if a camera, microphone, light meter, or stopwatch cannot detect it — rewrite it.**

## Full Examples

### Example 1: Fantasy Short Film

```
Seedance 2.0 Prompt:

Use @[storyboard ref] as the authoritative shot blueprint. Do not render the storyboard itself. Ignore all borders, panel frames, text, labels, titles, color swatches, director bar graphics, and layout elements. Treat each panel as a continuous cinematic beat.
The entire video must play as one continuously developing master shot with no visible cuts; each panel is a sampled stage of the same uninterrupted camera movement, not separate shots.
Use a single virtual lens / same-lens continuous camera movement; scale changes come only from physical camera movement.
Use @[character ref] as the authoritative C1 character reference.

Create a cinematic 16:9 video showing C1 falling through a nightmare temporal void that collapses into a moonlit gothic castle bedroom, where she wakes up and says "FATHER".

Final style: stylized fantasy, faithful to the referenced sculptural anime-fantasy character, matte graphite-inspired surfaces, cold silver-blue moonlight, deep soft volumetric shadows, thin time-fragment effects, collapsing dream debris, elegant high-end cinematic camera movement.

1. Begin with an endless black space, no floor, sky, or horizon, C1 falling at frame center, very long white hair streaming upward, one hand reaching out for stability, as the camera falls with her.
2. Camera begins a smooth falling orbit, shattered clocks, floating doors, ancient castle fragments, moonlit forest branches, ruined city pieces, battlefield debris, and forgotten faces rushing past at different depths.
3. A stone step or ledge briefly appears below C1; she reaches for it but it dissolves before contact, the camera falling past her on the same downward path.
4. Different eras collide around her, castle arches, battlefield banners, city ruins, and clock faces spinning faster, distorting the frame like runaway time travel.
5. Recognizable bedroom elements flash through the nightmare: a bed frame, a curtain, a tall gothic window, a stone wall, and a nightstand appear and vanish while C1 continues falling.
6. The falling axis narrows toward a partially formed bed below; nightmare debris funnels inward, windows, curtains, crystal chandelier, and stone walls trying to lock into place.
7. C1 slams into the bed, not into darkness or stone, all void fragments, time shards, and castle architecture collapsing into the mattress point on contact.
8. Reality silently snaps into form: the castle bedroom fully materializes around the bed, moonlight streams through the tall gothic window, stone walls and furniture becoming solid, nightmare residue gradually dissipating.
9. Without cutting, C1 jolts upright in bed, rapid breathing, eyes wide with fear, scanning the room to test if she is awake, then quietly says "FATHER".
10. Camera continues its residual momentum, slowly pulling back on the same axis, revealing the vast moonlit castle room, ancient stone architecture, lonely furniture, and C1 looking small in the bed under the cold light.
```

### Example 2: E-Commerce Menswear (Role Mapping + I2V Compressed)

```
Seedance 2.0 Prompt:

@[background image 1] controls environment — strictly preserve spatial structure, lighting, warm wood tones, and display arrangement.
@[character image 1] controls character identity — strictly preserve the same young male model's primary features, natural face.
@[product image 1] controls product identity — strictly lock t-shirt color, front print pattern, print color, size, position, loose dropped-shoulder silhouette.
@[storyboard image 1] controls action rhythm — used for action planning reference, do not render the storyboard itself. Ignore all borders, panel frames, text, labels, layout elements. Treat each panel as a continuous cinematic beat, strictly follow panel order and timing rhythm.

Music: lo-fi hip-hop / chill trap, BPM 90-110, no narration, no dialogue.

The entire video plays as a continuous master shot with no visible cuts. Model movement natural and fluid, fabric produces realistic wrinkles and slight swinging with movement. If a turn or back angle appears, the t-shirt back must be solid color with no pattern, no text, no logo.

No subtitles, no watermark, no brand logo, no back print, no back text, no print drift, no clothing deformation, no scene drift, no new characters.

Character count: ~420 chars ✅
```

### Example 3: Chinese I2V Minimal Compression (Jimeng/Kling Standard)

```
@[image 1] is product reference, strictly preserve logo, label, bottle shape, and color unchanged.
Camera slowly pushes in to label close-up; warm left light sweeps across the glass, water droplets slide down the bottle.
Background remains dark and still. Sound: soft room tone, single crisp glass chime at the end.
Character count: ~220 chars ✅
```

## Validation Checklist

Before delivering the final Seedance 2.0 prompt, verify each item:

- [ ] Storyboard reference correct, declared "do not render the storyboard itself"
- [ ] Character reference correct, declared role mapping ("controls character identity / strictly preserve")
- [ ] Product reference correct (if applicable), declared product mapping role and lock parameters
- [ ] Background reference correct (if applicable), declared environment mapping role
- [ ] Each @[ref] assigned a single primary role, no stacked style descriptions
- [ ] Continuous camera movement description covers all storyboard panels
- [ ] Each panel corresponds to one motion phase (1-N numbering clear)
- [ ] Uses one primary camera movement, not stacked multiples
- [ ] Declared "no visible cuts" and "same uninterrupted camera movement"
- [ ] Music style and BPM specified
- [ ] Fabric/hair dynamic description (if applicable)
- [ ] Back-side constraint declared (if applicable)
- [ ] Negative constraint list complete
- [ ] **Character count compliant: ZH ≤ 500 chars / EN ≤ 1000 words (count annotated)**
- [ ] **Anti-slop check: no empty evaluation words (cinematic/epic/beautiful, etc. without physical referents)**
- [ ] Prompt can be directly pasted into Seedance 2.0 platform for use

## Common Scene Adaptations

### Fashion/Apparel Videos
- Must use role mapping declaration: `@[product image 1]` locks color/print/silhouette
- Fabric dynamics (wrinkles, swing) must be described
- Back-side constraint (solid color, no pattern, no text)
- Music: lo-fi hip-hop / chill trap, BPM 90-110
- **Compactness: prefer Chinese compression, within 500 characters**

### Product Showcase Videos
- Product reference locks appearance; background reference locks environment
- Camera movement focused on push-in/orbit/detail, **one primary movement**
- No product appearance drift
- **Key rule: move light/particles/camera around the product — do not transform the product itself**

### Drama Short Films
- Character reference locks identity; storyboard reference locks narrative rhythm
- Continuous camera movement throughout
- Emotional progression, not reset
- **One clip = one beat = one emotional turn**

### Multi-Character Scenes
- Each character has separate `@[character N]` reference + role mapping declaration
- Declare spatial relationships between characters remain stable
- No character identity swap or drift

## Integration

When invoked by `director-core`:
- Confirm STATE 5 is complete (storyboard images have been generated)
- Load all visual reference assets (storyboard images, character images, product images, background images)
- Assign @[ref] role mapping for each asset
- Compile Seedance 2.0 executable prompts
- **Count and annotate character/word count** (ZH ≤ 500 chars)
- Execute validation checklist (including role mapping check + character count check + anti-slop check)
- Present for final user review
- Upon confirmation, mark STATE 6 complete
