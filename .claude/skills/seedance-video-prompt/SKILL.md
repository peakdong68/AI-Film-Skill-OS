---
name: seedance-video-prompt
description: 'Compiles image, video, and audio multimodal references into executable video generation prompts for Seedance 2.0 / Kling platforms. Selects generation mode automatically based on available resources (3 task categories: multimodal reference, video edit, video extend; 7 sub-modes). Storyboard images are optional. This is the final L5 video generation layer compiler in the AI Film OS pipeline. Use for Seedance 2.0 prompts, video generation prompts, or when director-core routes to STATE 6. Trigger words: Seedance 2.0 prompt, video generation prompt, Seedance prompt, video generation prompt, I2V, first-last frame.'
---

# Seedance Video Prompt — L5 Video Generation Compiler

## Overview

The final compiler of **L5 — VIDEO GENERATION LAYER** in the AI Film OS pipeline. Receives multimodal references and compiles them into platform-executable video prompts for Seedance 2.0 / Kling.

**Key Distinction:**

- STATE 4 (`director-prompt-packager`): Text-level compiler. **Not a video platform prompt.**
- STATE 6 (`seedance-video-prompt`): Image-reference-level compiler → platform-executable prompts.

**Storyboard frame images are NOT mandatory** — only required in storyboard-driven mode.

## Load Resources

This skill has built-in reference knowledge. Load on demand. Read this file first; only load external references in these scenarios:

| When to Load                                    | Which File                                        | Content                                                                                                    |
| ----------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Need full mode templates & examples             | `references/seedance-methodology.md`              | Complete prompt examples for all 7 modes, troubleshooting table, camera movement guide, character contract |
| Need to verify platform hard constraints        | `../references/seedance-platform.md`              | Character/word limits, Part duration, `@[ref]` format spec                                                 |
| Need cinematography terminology                 | `../references/cinematography-quick-reference.md` | Shot size / movement / angle / composition / lighting bilingual quick reference                            |
| Encounter hollow adjectives needing replacement | `../references/anti-slop-lexicon.md`              | 13 slop words → production language mapping                                                                |
| Commercial/genre film needs special recipes     | `../references/seedance-genre-recipes.md`         | E-commerce / livestream / fashion / narrative genre templates                                              |

## Context Probe (Required for Standalone Use)

This skill can be used standalone or called by `director-core` STATE 6. After loading, first probe for available context:

**Step 1 — Check pipeline state:** Read `STATE.md` to determine if running within a director-core pipeline.

**Step 2 — Scan project files:** Probe the `outputs/` directory for upstream artifacts:

| If found...                                | Then infer...                                                                                      |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `State-4-prompt-package.md`                | A complete storyboard design plan exists — ready for prompt compilation                            |
| `character-sheets.md`                      | Character design prompts exist — suggest user generate character reference images before using I2V |
| `State-5-storyboard.md`                    | A storyboard master sheet plan exists — can reference as `@[Image3]`                               |
| `State-3-characters.md`                    | Character identity definitions exist — key locking parameters can be extracted                     |
| User-provided reference images/video/audio | Proceed directly to mode gating with user-supplied assets                                          |

**Step 3 — Aggregate available resources:** Combine pipeline state + project files + user input into a resource inventory. If upstream `character-sheets.md` exists but user hasn't mentioned character images, proactively ask whether to generate character reference images first.

**Step 4 — Fallback decision:** If none of the above exist (no `STATE.md`, no `outputs/`, no user reference assets), fall back to pure T2V mode using only the user's text description.

---

## Output Structure Template

**All prompts across all modes MUST follow this skeleton.** Mode-specific differences only affect which fields are required vs. optional.

### Standard Prompt Skeleton

```
[Material Declaration]        ← Required (when reference assets exist); omit for T2V
[Subject Definition]          ← Required (multi-character / reference images); may simplify for single subject
[Storyboard Blueprint Constraints] ← Required (I2V storyboard mode); omit for other modes
[Narrative Content]           ← Required: subject + scene + action sequence
[Camera & Movement]           ← Required: one primary camera movement
[Lighting & Color]            ← Optional: physical light sources, color temperature, atmosphere
[Audio]                       ← Optional: music (), SFX <>, dialogue {}
[Constraints]                 ← Required: preservation items + exclusion items
```

### Field Specification

| Field                                | Required When                                          | Key Points                                                                                                                               |
| ------------------------------------ | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Material Declaration                 | `@[ImageN]` / `@[VideoN]` / `@[AudioN]` assets present | Declare each asset's role (identity / action / scene / rhythm)                                                                           |
| Subject Definition                   | Character reference images present                     | `` Define [2–3 static features] in @[ImageN] as `SubjectN` ``                                                                            |
| **Storyboard Blueprint Constraints** | **I2V storyboard mode**                                | **Must state: do NOT render the storyboard itself, ignore panel borders and text labels, strictly follow panel order and camera angles** |
| Narrative Content                    | Always                                                 | Describe shot-by-shot per storyboard panel order; each shot = one visible beat                                                           |
| Camera & Movement                    | Always                                                 | One primary movement with endpoint; no multi-movement stacking                                                                           |
| Lighting & Color                     | When specific light sources / color temperature exist  | Physical light source + direction + color temperature; no hollow adjectives                                                              |
| Audio                                | When music / SFX / dialogue present                    | Music with (), SFX with <>, dialogue with {}                                                                                             |
| Constraints                          | Always                                                 | `keep subtitle-free, no logos, no watermarks` as baseline; I2V adds `no facial deformation, no identity drift`                           |

### I2V Storyboard Blueprint Constraints (Hard Rule)

**When a prompt includes storyboard reference images (`@[ImageN]` as a storyboard blueprint), the following COMPLETE constraints MUST be used. Do NOT simplify to "reference the storyboard" as a single phrase:**

```
Use @[ImageN] storyboard as the video narrative blueprint — do NOT render the storyboard itself.
Ignore all panel borders, text labels, and layout elements.
Strictly follow panel order, camera angles, and action rhythm.
```

**Constraint Semantics:**

| Constraint                           | Meaning                                                          | Why It's Required                                                               |
| ------------------------------------ | ---------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| As narrative blueprint               | The storyboard defines the shot sequence and narrative structure | Tells the model the storyboard is "script," not "source material"               |
| Don't render the board itself        | Output is video, not a storyboard panel image                    | Prevents the model from treating the board as visual content to output directly |
| Ignore panel borders and text labels | Exclude storyboard UI elements                                   | Prevents rendering table lines, shot numbers, timecodes                         |
| Follow panel order                   | Generate in 01→02→03... sequence                                 | Ensures narrative causal chain is not scrambled by the model                    |
| Follow camera angles                 | Each panel's specified shot size/angle must correspond           | Ensures the director's shot design is faithfully executed                       |
| Follow action rhythm                 | Time allocation and action density between panels                | Ensures the emotion arc is not freely reinterpreted by the model                |

---

## Mode Gating

Seedance 2.0 defines **three core task types**. Each covers sub-modes selected by available resources.

| Task Type                | Sub-Modes                                        | Required Inputs                                          | Core Pattern                                                                      |
| ------------------------ | ------------------------------------------------ | -------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Multimodal Reference** | T2V / I2V minimal / I2V storyboard / R2V / FLF2V | At least one reference (image/video/audio), or text only | Extract elements from refs, generate a new video                                  |
| **Video Edit**           | V2V Edit                                         | `@[Video1]`                                              | Local/global modification of source video; **do NOT use "reference" prefix**      |
| **Video Extend**         | V2V Extend                                       | `@[Video1]`                                              | Temporal extension matching audio-visual style; **do NOT use "reference" prefix** |

### Mode Decision Tree

**Step 1 — Check route lock.** When called by `director-core` STATE 6, check upstream STATE 4's routing decision. If a route is already locked, use the corresponding mode directly — do not re-evaluate available assets.

| Route Lock                 | Forced Mode                  | Notes                                                                                                |
| -------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------- |
| Plan A (I2V storyboard)    | I2V (storyboard)             | Even if the user has not yet generated assets, produce `@[ImageN]` placeholder prompts in I2V format |
| Plan B (direct to STATE 6) | Evaluate by available assets | Follow Step 2 logic below                                                                            |

> **Key rule: Once Plan A is locked, STATE 6 MUST use I2V (storyboard) mode.**
> Assets may not be generated yet — in this case, use `@[ImageN]` placeholders and prepend a "Material Mapping (effective after upload)" note to the prompt.

**Step 2 — When no route lock exists, evaluate by available assets:**

```
Video source to modify? → Video Edit (use @[Video1] directly, no "reference" prefix)
Video to continue? → Video Extend (use @[Video1] directly, no "reference" prefix)
Reference images available? → I2V (storyboard) — primary recommendation
Single reference image only? → I2V (minimal) — simpler fallback
First + last frame? → FLF2V
Multiple different ref types? → R2V
Text description only? → T2V
```

> **For I2V, I2V (storyboard) is the primary recommendation.** It provides the best multi-shot control through storyboard blueprint images. I2V (minimal) is available as a simpler option for single-reference-image use cases. Always present both options to the user with their tradeoffs.

### Placeholder Material Declaration (When I2V Materials Not Yet Generated)

When I2V mode is used but assets are not yet generated, the prompt MUST be prepended with a material mapping declaration:

```
Material Mapping (effective after corresponding assets are uploaded):
| Upload # | Asset | Source |
| ---------| ----- | ------ |
| `@[Image1]` | [Character A] Character Sheet | character-sheets.md |
| `@[Image2]` | [Character B] Character Sheet | character-sheets.md |
| `@[Image3]` | Storyboard Master Sheet | State-5-storyboard.md |
```

> This table lets the user know exactly which assets to upload and in what order.

> Detailed templates and examples: see `references/seedance-methodology.md`

## Director Formula

```
Precise Subject + Action Detail + Scene Environment + Lighting/Color + Camera Movement + Visual Style + Quality + Constraints
```

| Slot        | Purpose                                                      | Example                                                                               |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| Subject     | The anchor the model tracks; define first                    | `` Define the woman in @[Image1] wearing a red dress and straw hat as `Subject1` ``   |
| Action      | Visible change with body-part detail + degree quantification | `slowly raises hand, gently nods, using the momentum of the turn to swing the arm up` |
| Scene       | Only what is not already in references                       | `quiet rain-lit kitchen counter, shallow depth of field`                              |
| Camera      | One primary movement with endpoint                           | `medium shot steady follow, slow push-in to close-up`                                 |
| Light/Style | Physical light + visual tone                                 | `warm amber daylight through window, cool blue rim, cinematic documentary style`      |
| Quality     | Clarity, detail, texture                                     | `high definition, rich detail, cinematic quality, natural color`                      |
| Audio       | SFX/dialogue/music                                           | `(upbeat rock plays in background) <dog barking in distance>`                         |
| Constraints | Preservation and exclusions                                  | `keep subtitle-free, no logos, no watermarks`                                         |

## Reference Format

Seedance 2.0 uses `@[ImageN]` / `@[VideoN]` / `@[AudioN]` format for uploaded assets. Upload in order, reference by sequence number.

| Asset Type | Format                  | Purpose                                                               |
| ---------- | ----------------------- | --------------------------------------------------------------------- |
| Image      | `@[Image1]` `@[Image2]` | Character anchoring, scene setting, product locking, first/last frame |
| Video      | `@[Video1]`             | Camera reference, motion reference, VFX reference, edit/extend source |
| Audio      | `@[Audio1]`             | Rhythm/atmosphere, voice timbre reference                             |

### Subject Definition Rules

Explicitly define subjects in reference assets for unique identifiability.

**Core principle: the reference image itself IS the identity definition — do not enumerate static appearance details already contained in the reference image.** Reiterating facial structure, hairstyle, body type, etc. that are already locked in the image causes the model to reinterpret rather than directly reference the image. Subject definitions need only 1-2 distinctive appearance identifiers; the rest is carried by the reference image.

**When reference images exist (I2V / R2V / FLF2V):**

| Scenario                     | Format                                                                             | Example                                                                                 |
| ---------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Basic definition**         | `` Define [1-2 distinctive identifiers] in @[Image1] as `Subject1` ``              | `` Define the male model in @[Image1] as `Model` ``                                     |
| **Short binding**            | `` `Subject1`@[Image1] ``                                                          | `` `Model`@[Image1] ``                                                                  |
| **Multi-asset same subject** | `` Define [identifier] in @[Image1] and [identifier] in @[Image2] as `SubjectN` `` | `` Define the character's face in @[Image1] and outfit in @[Image2] as `Protagonist` `` |
| **Face close-up separation** | `` `Subject1`'s face references @[Image1], outfit references @[Image2] ``          | Separate headshot + full-body references for enhanced facial extraction weight          |

**When no reference images exist (T2V):** detailed subject appearance description is required in the prompt (face + hairstyle + body type + wardrobe).

**Anti-patterns (forbidden when reference images exist):**

- ❌ `` Define the Asian male model with angular face structure, Korean-style slightly wavy short dark hair, lean athletic build, white printed crew neck t-shirt in @[Image1] as `Model` `` — over-describes details already locked in the reference image
- ✅ `` Define the male model in @[Image1] as `Model` `` — identity binding only, no re-description

### Edit/Extend: No "Reference" Prefix

Edit and extend tasks **must NOT use the "reference" prefix**. Use `@[Video1]` directly to avoid misclassification as a reference task.

- ✅ `Edit @[Video1], change [original feature] to [new feature]`
- ✅ `Extend @[Video1] forward, generating...`
- ❌ `Reference @[Video1], edit...`

## Action Description Rules

**1. Body-part detail + degree quantification**: Specify hand, leg, head, shoulder movements with amplitude, speed, force. Ex: `slowly raises hand, quickly turns head, pushes off the ground hard, lowers head slightly`.

**2. Prefer low-slow-continuous micro-motions**: Use slow, gentle, continuous subtle movements. Avoid sprinting, leaping, violent tumbling, large dynamic actions. Ex: `walks slowly, gently raises hand, lowers head slightly, sits down smoothly`.

**3. Add motion transition bridging**: State inertia and continuity between actions. Ex: `using the turn's momentum to swing the arm up, naturally transitioning from stillness to raising a hand`.

**4. Emotional externalization**: Express emotion through physical body details instead of abstract words.

| Abstract Emotion | Externalize as Action & Detail                                                                      |
| ---------------- | --------------------------------------------------------------------------------------------------- |
| Sadness          | head lowered, shoulders trembling slightly, eyes reddening, fingers unconsciously gripping clothing |
| Joy              | corners of mouth rising uncontrollably, brows relaxed, footsteps lightened                          |
| Anxiety          | frequently checking watch, fingers tapping desk, rapid breathing, gaze darting                      |
| Anger            | fists clenched, jawline tight, chest heaving heavily, eyes sharp as blades                          |
| Relief           | long exhale, tense shoulders fully relaxing, a faint long-lost smile appearing                      |

## Special Characters

| Purpose   | Symbol | Example                                                            |
| --------- | ------ | ------------------------------------------------------------------ |
| Music     | `()`   | `(upbeat rock plays in background)`                                |
| SFX       | `<>`   | `<dog barking in distance>`                                        |
| Dialogue  | `{}`   | `{Hello, world}`. For non-English: `says in Japanese {こんにちは}` |
| Subtitles | `【】` | `【Chapter One: Departure】`                                       |

## Platform Hard Constraints

See `../references/seedance-platform.md`. Key: ≤ 500 Chinese chars / ≤ 1000 English words per prompt (counted independently), each Part ≤ 15s, Part 2+ references previous Part's output for continuity.

## Per-Mode Prompt Specifications

The following are prompt skeletons and key constraints for each mode. For full templates, troubleshooting, and scene adaptation, see `references/seedance-methodology.md`.

### I2V Precise Retention (minimal — single reference image)

```
@[Image1] as reference; strictly preserve [identity/product/scene].
Only [motion] changes. Camera: [one movement]. Light: [source or transition].
Sound: [cue]. Constraints: [what must not change].
```

Use when: Only a single character/product image, no storyboard blueprint. Focus: lock static features, describe motion only.

### I2V Storyboard-Driven (storyboard — multi-shot blueprint)

```
Use @[ImageN] storyboard as the video narrative blueprint — do NOT render the storyboard itself.
Ignore all panel borders, text labels, and layout elements.
Strictly follow panel order, camera angles, and action rhythm.

Define [features] in @[Image1] as `Subject1`.
Define [features] in @[Image2] as `Subject2`.

Shot 1 (Panel 01 — [narrative purpose]): [scene], [subject action]. [shot size], [camera movement].
Shot 2 (Panel 02 — [narrative purpose]): [scene], [subject action]. [shot size], [camera movement].
...

[Lighting / Color]
([music description]) <[SFX]> {[dialogue]}

Constraints: keep subtitle-free, no logos, no watermarks. No facial deformation, no identity drift.
```

Use when: Storyboard blueprint image + character reference images available. Focus: per-panel shot mapping + full storyboard blueprint constraints.

### R2V Multi-Reference Character Mapping

```
Define [features] in @[Image1] as `Subject1`.
Use @[Video1] to control camera rhythm only — do NOT copy performers, rooms, brands, or clothing.
Use @[Audio1] to control rhythm and energy only.

`Subject1` [action], [scene]. Camera: [movement]. Sound: [SFX].
Constraints: [what must not change].
```

Use when: Multiple different reference types mixed. Focus: assign each asset a single role; declare "non-transferable items."

### FLF2V First/Last Frame

```
Use @[Image1] as first frame. Use @[Image2] as last frame.
Maintain the same subject facial structure, hairstyle, clothing, and scene layout.
Generate a continuous transition from [start state] to [end state].
Action: [one physical motion path]. Camera: [locked medium shot or one slow push-in].
Light: [source and continuity]. Sound: [ambient]. Constraints: [what must not change].
```

### T2V Text-to-Video

```
[Subject] in [scene] [action]. Camera: [one primary movement].
Light: [source and quality]. Style: [tone]. Constraints: [exclusion items].
```

### V2V Edit

```
Edit @[Video1], change [original feature] to [new feature].
Elements not mentioned remain unchanged by default.
Constraints: keep subtitle-free, no logos, no watermarks.
```

### V2V Extend

```
Extend @[Video1] forward, [subject] continues [action].
Audio-visual style, subject, and narrative remain consistent.
Constraints: keep subtitle-free, no logos, no watermarks.
```

> Detailed troubleshooting (identity drift / shot jumps / product deformation / frozen frames), camera movement selection guide, character contract, and scene adaptation (fashion / product / narrative short film / multi-character) — see `references/seedance-methodology.md`

## Visible Beat Principle

**Put only one visible beat per clip.** Beat types: reveal, arrival, decision, transformation, contact, pursuit, disappearance. One beat = one action verb + visible endpoint. Do not pack multiple event turns into one segment.

## I2V Core Principles

**Only describe what the image cannot convey.** A static image already contains subject identity, product form, composition. Re-describing static details causes drift. Add only: motion, camera, lighting changes, sound, preservation constraints.

| Good Addition       | Example                                                   |
| ------------------- | --------------------------------------------------------- |
| Micro-expression    | `subject blinks once, gaze drops slightly`                |
| Product light sweep | `a thin highlight sweeps across the label`                |
| Weather/atmosphere  | `rain streaks behind, dust catches in the doorway beam`   |
| Camera movement     | `slow push-in from current composition to tighter detail` |

## Anti-Slop

Replace hollow evaluation words with capturable production language. Core: cinematic → shot size+camera+lighting; epic → physical scale+lens distance; beautiful → color+texture+light behavior.

> Full lexicon (13 hollow words → production language) in `../references/anti-slop-lexicon.md`

**Rule: If a camera, microphone, light meter, or stopwatch cannot detect it — rewrite.**

## Validation Checklist

- [ ] Mode declared and matches available inputs
- [ ] References use `` `@[Image1]` `` / `` `@[Video1]` `` / `` `@[Audio1]` `` format
- [ ] Subjects explicitly defined (`` Define [features] in `@[Image1]` as `Subject1` ``)
- [ ] Edit/extend mode: no "reference" prefix, uses `` `@[Video1]` `` directly
- [ ] Actions include body-part detail + degree quantification, prefer low-slow-continuous
- [ ] Emotions expressed through physical details, no abstract emotion words
- [ ] SFX/dialogue/music use correct special characters (`()<>{}`)
- [ ] One shot specifies only one camera movement
- [ ] Word count compliant: Chinese ≤ 500 chars (annotated)
- [ ] Anti-slop check passed
- [ ] Constraints complete: `keep subtitle-free, no logos, no watermarks`

## Integration with director-core

When called at STATE 6:

1. Check route lock from upstream STATE 4 decision; if Plan A is locked, force I2V (storyboard) mode
2. If no route lock, check available inputs; do NOT assume storyboard images exist
3. Select mode via decision tree
4. Define subjects: explicitly label people/products in reference images as subject tags
5. Compile executable prompts per selected mode
6. Count words, run validation checklist
7. Present for user review; mark STATE 6 complete upon confirmation

## Save Output

After delivering the final output, prompt the user to save with a dated, topic-specific filename:

```
Save to outputs/F-[N]-[topic]-seedance-prompt.md?
Example: outputs/F-1-cyberpunk-short-seedance-prompt.md
```

If the user confirms, write the output to the specified path.
