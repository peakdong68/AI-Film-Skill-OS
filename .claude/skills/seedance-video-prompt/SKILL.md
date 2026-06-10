---
name: seedance-video-prompt
description: Compiles image, video, and audio multimodal references into executable video generation prompts for Seedance 2.0 / Kling platforms. Selects generation mode automatically based on available resources (3 task categories: multimodal reference, video edit, video extend; 7 sub-modes). Storyboard images are optional. This is the final L5 video generation layer compiler in the AI Film OS pipeline. Use for Seedance 2.0 prompts, video generation prompts, or when director-core routes to STATE 6. Trigger words: Seedance 2.0 prompt, video generation prompt, Seedance prompt, video generation prompt, I2V, first-last frame.
---

# Seedance Video Prompt — L5 Video Generation Compiler

## Overview

The final compiler of **L5 — VIDEO GENERATION LAYER** in the AI Film OS pipeline. Receives multimodal references and compiles them into platform-executable video prompts for Seedance 2.0 / Kling.

**Key Distinction:**
- STATE 4 (`director-prompt-packager`): Text-level compiler. **Not a video platform prompt.**
- STATE 6 (`seedance-video-prompt`): Image-reference-level compiler → platform-executable prompts.

**Storyboard frame images are NOT mandatory** — only required in storyboard-driven mode.

## Mode Gate

Seedance 2.0 defines **three core task types**. Each covers sub-modes selected by available resources.

| Task Type | Sub-Modes | Required Inputs | Core Pattern |
|---|---|---|---|
| **Multimodal Reference** | T2V / I2V minimal / I2V storyboard / R2V / FLF2V | At least one reference (image/video/audio), or text only | Extract elements from refs, generate a new video |
| **Video Edit** | V2V Edit | `` `Video1` `` | Local/global modification of source video; **do NOT use "reference" prefix** |
| **Video Extend** | V2V Extend | `` `Video1` `` | Temporal extension matching audio-visual style; **do NOT use "reference" prefix** |

### Mode Decision Tree

```
Video source to modify? → Video Edit (use `Video1` directly, no "reference" prefix)
Video to continue? → Video Extend (use `Video1` directly, no "reference" prefix)
Storyboard images? → I2V storyboard
First + last frame? → FLF2V
Multiple different ref types? → R2V
Single reference image? → I2V minimal
Text description only? → T2V
```

> Detailed templates and examples: see `references/seedance-methodology.md`

## Director Formula

```
Precise Subject + Action Detail + Scene Environment + Lighting/Color + Camera Movement + Visual Style + Quality + Constraints
```

| Slot | Purpose | Example |
|---|---|---|
| Subject | The anchor the model tracks; define first | `` Define the woman in `Image1` wearing a red dress and straw hat as `Subject1` `` |
| Action | Visible change with body-part detail + degree quantification | `slowly raises hand, gently nods, using the momentum of the turn to swing the arm up` |
| Scene | Only what is not already in references | `quiet rain-lit kitchen counter, shallow depth of field` |
| Camera | One primary movement with endpoint | `medium shot steady follow, slow push-in to close-up` |
| Light/Style | Physical light + visual tone | `warm amber daylight through window, cool blue rim, cinematic documentary style` |
| Quality | Clarity, detail, texture | `high definition, rich detail, cinematic quality, natural color` |
| Audio | SFX/dialogue/music | `(upbeat rock plays in background) <dog barking in distance>` |
| Constraints | Preservation and exclusions | `keep subtitle-free, no logos, no watermarks` |

## Reference Format

Seedance 2.0 uses `` `ImageN` `` / `` `VideoN` `` / `` `AudioN` `` format for uploaded assets. Upload in order, reference by sequence number.

| Asset Type | Format | Purpose |
|---|---|---|
| Image | `` `Image1` `` `` `Image2` `` | Character anchoring, scene setting, product locking, first/last frame |
| Video | `` `Video1` `` | Camera reference, motion reference, VFX reference, edit/extend source |
| Audio | `` `Audio1` `` | Rhythm/atmosphere, voice timbre reference |

### Subject Definition Rules

Explicitly define subjects in reference assets with 2-3 clear, stable static features (clothing, hairstyle, appearance category) for unique identifiability.

**Basic definition:** `` Define [feature1], [feature2] in `Image1` as `Subject1` ``
**Short binding:** `` `Subject1`@`Image1` `` / `` John@Image1 ``
**Multi-asset same subject:** `` Define [...] in `Image1` and [...] in `Image2` as `SubjectN` ``
**Face close-up separation:** `` `Subject1`'s facial features reference `Image1` (headshot), styling references `Image2` (full-body) ``
(Optional — recommended when high identity consistency is required; helps Seedance extract facial features with higher weight)

> **Recommendation**: For best identity consistency, use separate face close-up (headshot) + full-body reference images. Place face reference earliest in the prompt for higher weight.

### Edit/Extend: No "Reference" Prefix

Edit and extend tasks **must NOT use the "reference" prefix**. Use `` `VideoN` `` directly to avoid misclassification as a reference task.

- ✅ `` Edit `Video1`, change [original feature] to [new feature] ``
- ✅ `` Extend `Video1` forward, generating... ``
- ❌ `` Reference `Video1`, edit... ``

## Action Description Rules

**1. Body-part detail + degree quantification**: Specify hand, leg, head, shoulder movements with amplitude, speed, force. Ex: `slowly raises hand, quickly turns head, pushes off the ground hard, lowers head slightly`.

**2. Prefer low-slow-continuous micro-motions**: Use slow, gentle, continuous subtle movements. Avoid sprinting, leaping, violent tumbling, large dynamic actions. Ex: `walks slowly, gently raises hand, lowers head slightly, sits down smoothly`.

**3. Add motion transition bridging**: State inertia and continuity between actions. Ex: `using the turn's momentum to swing the arm up, naturally transitioning from stillness to raising a hand`.

**4. Emotional externalization**: Express emotion through physical body details instead of abstract words.

| Abstract Emotion | Externalize as Action & Detail |
|---|---|
| Sadness | head lowered, shoulders trembling slightly, eyes reddening, fingers unconsciously gripping clothing |
| Joy | corners of mouth rising uncontrollably, brows relaxed, footsteps lightened |
| Anxiety | frequently checking watch, fingers tapping desk, rapid breathing, gaze darting |
| Anger | fists clenched, jawline tight, chest heaving heavily, eyes sharp as blades |
| Relief | long exhale, tense shoulders fully relaxing, a faint long-lost smile appearing |

## Special Characters

| Purpose | Symbol | Example |
|---|---|---|
| Music | `()` | `(upbeat rock plays in background)` |
| SFX | `<>` | `<dog barking in distance>` |
| Dialogue | `{}` | `{Hello, world}`. For non-English: `says in Japanese {こんにちは}` |
| Subtitles | `【】` | `【Chapter One: Departure】` |

## Platform Hard Constraints

Each Seedance 2.0 prompt corresponds to one Part (≤ 15s), counted independently.

| Language | Limit (per prompt) |
|---|---|
| **Chinese** | ≤ 500 characters |
| **English** | ≤ 1000 words |
| **Total characters** | ≤ 2000 characters |

Multi-Part projects: write one prompt per Part. Part 2+ must reference the previous Part's output for continuity (`` Extend `Video1` backward, preserving... ``).

## Core Templates

### Multimodal Reference — I2V Preservation

```
`Image1` as reference; strictly preserve [identity/product/scene].
Only [motion] changes. Camera: [one movement]. Light: [source or transition].
Sound: [cue]. Constraints: [what must not change].
```

### Multimodal Reference — Multi-Character R2V

```
Define [feature1] in `Image1` as `Subject1`, define [feature2] in `Image2` as `Subject2`.
`Subject1` [action]; `Subject2` [action]. Scene: [environment].
Camera: [movement]. Style: [tone]. Constraints: keep subtitle-free, no logos.
```

### Video Edit — V2V Edit

```
Edit `Video1`, change [original feature] to [new feature].
Elements not mentioned remain unchanged by default.
```

### Video Extend — V2V Extend

```
Extend `Video1` forward, [subject] continues [action].
Audio-visual style, subject, and narrative remain consistent.
```

> Complete templates and scene adaptations: see `references/seedance-methodology.md`

## Visible Beat Principle

**Put only one visible beat per clip.** Beat types: reveal, arrival, decision, transformation, contact, pursuit, disappearance. One beat = one action verb + visible endpoint. Do not pack multiple event turns into one segment.

## I2V Core Principles

**Only describe what the image cannot convey.** A static image already contains subject identity, product form, composition. Re-describing static details causes drift. Add only: motion, camera, lighting changes, sound, preservation constraints.

| Good Addition | Example |
|---|---|
| Micro-expression | `subject blinks once, gaze drops slightly` |
| Product light sweep | `a thin highlight sweeps across the label` |
| Weather/atmosphere | `rain streaks behind, dust catches in the doorway beam` |
| Camera movement | `slow push-in from current composition to tighter detail` |

## Anti-Slop

Replace hollow evaluation words with capturable production language.

| Hollow Word | Replace With |
|---|---|
| cinematic | shot size + camera movement + lighting + color grading |
| epic | physical scale + lens distance |
| beautiful | color + texture + composition + light behavior |
| dynamic | specific motion + speed + endpoint |
| dramatic | blocking + shadow + silence + camera pressure |

**Rule: If a camera, microphone, light meter, or stopwatch cannot detect it — rewrite.**

## Validation Checklist

- [ ] Mode declared and matches available inputs
- [ ] References use `` `ImageN` `` / `` `VideoN` `` / `` `AudioN` `` format
- [ ] Subjects explicitly defined (`` Define [features] in `ImageN` as `SubjectN` ``)
- [ ] Edit/extend mode: no "reference" prefix, uses `` `VideoN` `` directly
- [ ] Actions include body-part detail + degree quantification, prefer low-slow-continuous
- [ ] Emotions expressed through physical details, no abstract emotion words
- [ ] SFX/dialogue/music use correct special characters (`()<>{}`)
- [ ] One shot specifies only one camera movement
- [ ] Word count compliant: Chinese ≤ 500 chars (annotated)
- [ ] Anti-slop check passed
- [ ] Constraints complete: `keep subtitle-free, no logos, no watermarks`

## Integration with director-core

When called at STATE 6:

1. Check available inputs; do NOT assume storyboard images exist
2. Select mode via decision tree
3. Define subjects: explicitly label people/products in reference images as subject tags
4. Compile executable prompts per selected mode
5. Count words, run validation checklist
6. Present for user review; mark STATE 6 complete upon confirmation
