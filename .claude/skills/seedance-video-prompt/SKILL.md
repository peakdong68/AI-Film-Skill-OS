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

## Compilation Principle

> Seedance 2.0 prompts are **image-reference-driven motion instructions**. They reference locked visual assets (storyboard images, character images, product images) and add temporal motion descriptions.

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

## Output Structure: Seedance 2.0 Video Prompt

### Complete Template

```
Seedance 2.0 Prompt:

Use @[storyboard image 1] as the authoritative shot blueprint. Do not render the storyboard itself. Ignore all borders, panel frames, text, labels, titles, color swatches, director bar graphics, and layout elements. Treat each panel as a continuous cinematic beat.
The entire video must play as one continuously developing master shot with no visible cuts; each panel is a sampled stage of the same uninterrupted camera movement, not separate shots.
Use a single virtual lens / same-lens continuous camera movement; scale changes come only from physical camera movement.
Use @[character image 1] as the authoritative character reference.

[Add multi-character or product references here if applicable]

Music: [music style, BPM, mood]
[Subject action description, expanded on a timeline, each segment corresponding to a storyboard panel]
[Negative constraint list]
```

## Detailed Specification

### 1. Image Reference Zone (@[ref] Syntax)

Every Seedance 2.0 prompt must begin with the image reference zone:

| Reference Type | Format | Description |
|----------|------|------|
| Storyboard | `@[storyboard image 1]` | Authoritative shot blueprint — used for action planning reference, do not render the storyboard itself |
| Character | `@[character image 1]` | Authoritative character reference — locks face, hair, body type, skin tone |
| Product | `@[product image 1]` | Locks color, pattern, silhouette, position |
| Background | `@[background image 1]` | Locks spatial structure, lighting, color tone, display arrangement |

**Reference rules:**
- Storyboard reference must declare: "Ignore all borders, panel frames, text, labels, titles, color swatches, director bar graphics, and layout elements"
- Character reference must declare: "Keep the same model's primary features"
- Product reference must declare lock parameters: "Strictly lock color, print pattern, print color, size, position, silhouette"

### 2. Continuous Camera Movement Zone

**Core principle: The entire video plays as one continuously developing master shot with no visible cuts.**

Each storyboard panel is a sampled stage of the same uninterrupted camera movement:
- Use a single virtual lens / same-lens continuous camera movement
- Scale changes come only from physical camera movement (push-in/pull-out/tracking)
- No jump cuts between panels — smooth motion transitions

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

### Example 2: E-Commerce Menswear Livestream

```
Seedance 2.0 Prompt:

Modern urban trendy menswear brand, high-quality e-commerce livestream environment. Scene is a real warm-toned walk-in closet and menswear showroom, highlighting young male fashion styling and lifestyle expression.

Use @[background image 1] as the fixed background reference, strictly maintaining spatial structure, lighting, color tone, and background display stability.
Use @[character image 1] as the authoritative character reference, keeping the same model's primary features, natural face. Replace the model's printed t-shirt with @[product image 1], strictly locking color, front print pattern, print color, size, position, loose dropped-shoulder silhouette.
Use @[storyboard image 1] as the authoritative video storyboard narrative blueprint, used for action planning reference, do not render the storyboard itself. Exclude all panel borders, text, labels, titles, and layout elements. Treat each storyboard panel as an independent sequential shot guide. Strictly follow panel order, camera angles, action flow, timing rhythm.

Music: lo-fi hip-hop / chill trap / fashion beat, BPM 90-110, no narration, no dialogue.

Model movement natural and fluid, fabric produces realistic wrinkles and slight swinging with movement. If a turn or back angle appears, the t-shirt back must be solid color with no pattern, no text, no logo.

No subtitles, no watermark, no brand logo, no back print, no back text, no print drift, no clothing deformation, no scene drift, no new characters.
```

## Validation Checklist

Before delivering the final Seedance 2.0 prompt, verify each item:

- [ ] Storyboard reference correct, declared "do not render the storyboard itself"
- [ ] Character reference correct, declared "keep the same model's primary features"
- [ ] Product reference correct (if applicable), locked color/pattern/silhouette/position
- [ ] Background reference correct (if applicable), locked spatial structure/lighting/color tone
- [ ] Continuous camera movement description covers all storyboard panels
- [ ] Each panel corresponds to one motion phase (1-N numbering clear)
- [ ] Declared "no visible cuts" and "same uninterrupted camera movement"
- [ ] Music style and BPM specified
- [ ] Fabric/hair dynamic description (if applicable)
- [ ] Back-side constraint declared (if applicable)
- [ ] Negative constraint list complete (no subtitles/watermark/logo/drift/deformation/new characters)
- [ ] Prompt can be directly pasted into Seedance 2.0 platform for use

## Common Scene Adaptations

### Fashion/Apparel Videos
- Must lock product color, print position, silhouette
- Fabric dynamics (wrinkles, swing) must be described
- Back-side constraint (solid color, no pattern, no text)
- Music: lo-fi hip-hop / chill trap, BPM 90-110

### Product Showcase Videos
- Product reference locks appearance
- Background reference locks environment
- Camera movement focused on push-in/orbit/detail
- No product appearance drift

### Drama Short Films
- Character reference locks identity
- Storyboard reference locks narrative rhythm
- Continuous camera movement throughout
- Emotional progression, not reset

### Multi-Character Scenes
- Each character has separate @[character N] reference
- Declare spatial relationships between characters remain stable
- No character identity swap or drift

## Integration

When invoked by `director-core`:
- Confirm STATE 5 is complete (storyboard images have been generated)
- Load all visual reference assets (storyboard images, character images, product images, background images)
- Compile Seedance 2.0 executable prompts
- Execute validation checklist
- Present for final user review
- Upon confirmation, mark STATE 6 complete
