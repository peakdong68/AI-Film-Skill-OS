---
name: director-core
description: "Master controller for the AI film production pipeline — manages the production state machine, enforces phase locks, maintains checkpoints, and routes tasks to director sub-skills in the correct order. Use this skill when users want to produce a complete AI film/video from a creative idea or script. Trigger scenarios: making an AI film, generating a video from a creative idea, directing a Seedance project, AI filmmaking, AI video production, AI director workflow, film production pipeline, or any multi-stage video creation request. Also triggers on any video/film production request, including e-commerce livestreams, product showcase videos, fashion videos, brand videos, product videos, fashion films, and commercial videos."
---

# Director Core — Production State Machine

## Overview

The master controller for the AI Film OS pipeline. Ensures every AI film/video project flows through a proven, phase-gated production sequence — from initial creative idea to final Seedance-ready video prompts. The state machine prevents the most common failure mode in AI video production: jumping to prompt generation before the story, visual language, and character identity are locked in.

This skill does not generate creative content itself. It routes tasks to the appropriate sub-skill at each stage and validates outputs before advancing.

## Load Resources

This skill ships with reference knowledge files. Load them when:

- For detailed state flow rules and multi-Part structure specifications, read `references/production-state-machine.md`

## Production Pipeline

```
STATE 0 → Input Collection
STATE 1 → Story & Emotion Design
STATE 2 → Visual Design (Camera + Lighting)
STATE 3 → Character Lock
STATE 4 → Prompt Packaging (Film-Level Short Film Prompt Package)
STATE 5 → Storyboard Blueprint Generation (Image Level)
STATE 6 → Seedance Video Prompts (multi-mode, image reference level)
STATE 7 → Final Validation
STATE 8 → Export Ready
```

Each state produces validated deliverables before the next state is unlocked. Skipping states is strictly prohibited.

**Key distinction between STATE 4 and STATE 5/6:**

- STATE 4 (`director-prompt-packager`): Compiles a **text-level** film-level short film prompt package — integrating story, visual design, and character identity into structured storyboard design, camera language, sound design, and Seedance decomposition plan. The output is a complete director's vision document, which serves as the design foundation for STATE 5 storyboard blueprint generation after user confirmation. **Never outputs video platform prompts.**
- STATE 6 (`seedance-video-prompt`): Compiles **image-reference-level** video prompts for Seedance 2.0 / Kling. Supports 7 modes (T2V / I2V / R2V / FLF2V / V2V / ...). **Storyboard images optional** — only required for I2V storyboard mode. Output: platform-executable video generation prompts.

**The STATE 4 → STATE 6 separation of concerns is the foundation of pipeline design. Must never be crossed.**

## Phase Lock Rules

These are hard constraints. Violating them leads to the most common AI video failures (character drift, visual inconsistency, narrative incoherence).

| Lock                     | Rule                                                                                                 |
| ------------------------ | ---------------------------------------------------------------------------------------------------- |
| **Story Lock**           | Story structure and emotional arc must be confirmed before visual design                             |
| **Visual Lock**          | Camera language and lighting system must be defined before prompt packaging                          |
| **Character Lock**       | Character identity definitions must be confirmed before prompt packaging                             |
| **Package Lock**         | The film-level prompt package must be user-confirmed before entering storyboard blueprint generation |
| **Storyboard Lock**      | Storyboard blueprint images must be confirmed before Seedance prompts                                |
| **Prompt Lock**          | All pre-flight checks must pass before final export                                                  |
| **Output Boundary Lock** | STATE 4 output must not mention Seedance/Kling video platforms                                       |

If any lock is broken, stop immediately and return to the earliest incomplete state.

## State Machine

### STATE 0 — Input Collection

Collect the minimum viable brief needed to produce the film.

**Step 1: Assess creative maturity**

Based on the quality of user input, choose one of two paths:

| Input quality | Path | Description |
|---|---|---|
| Detailed script / complete scene description provided | **Fast track**: collect params directly | Skip interview |
| One-liner / vague concept / keywords only (< 20 words of substance) | **Creative interview**: develop idea first | Max 3 questions |

**Creative interview (for vague input):**

Adapted from `seedance-interview` patterns. Ask at most 3 high-impact questions:

1. **Subject + change**: "Who is the main subject in this video? What are they doing? What changes by the end?"
2. **Feeling + genre**: "What should it feel like? Product showcase, dramatic tension, comedy, realism, animation, or atmosphere?"
3. **Reference materials**: "Do you have any reference images/videos/audio? Or a film style in mind?"

Build a concise creative brief from the answers (concept summary, genre path, core scene, emotional direction), then collect production params below.

**Step 2: Collect production params**

- Project idea or script (refined through interview if applicable)
- Target duration (15s / 30s / 60s / custom)
- Visual style (cinematic / commercial / documentary / anime / sci-fi / etc.)
- Delivery platform (Seedance / Kling)
- Aspect ratio (16:9 / 9:16 / 1:1)
- Any existing reference images or character descriptions

If the user already provided sufficient info (≥ 4 items with clear creative intent), confirm and proceed to STATE 1. If they say "just do it", fill in reasonable defaults with annotations.

**State 0 output**: Confirmed production brief. Proceed to STATE 1.

### STATE 1 — Story & Emotion Design

Route to `director-story` and `director-emotion`.

**Required deliverables:**

- Narrative structure (three-act or five-act breakdown)
- Scene list, each scene with narrative purpose
- Emotional arc diagram (calm → tension → climax → resolution)
- Emotional intensity timeline

**Verification Gates:**

- [ ] Every scene has a narrative purpose
- [ ] Emotional arc covers full duration
- [ ] Causal chain defined (A leads to B leads to C)
- [ ] User confirmed structure

**State 1 output**: Script blueprint + emotional timeline. Proceed to STATE 2.

### STATE 2 — Visual Design

Route to `director-camera` and `director-light`.

**Required deliverables:**

- Camera language blueprint (primary shot types, movement vocabulary, angle philosophy)
- Lighting design system (key light strategy, color temperature arc, contrast rules)
- Color script (dominant colors per act/scene, temperature curve)
- Composition rules (primary and secondary framing approaches)

**Verification Gates:**

- [ ] Camera language matches emotional tone
- [ ] Lighting evolves with narrative
- [ ] Color script covers full duration
- [ ] User confirmed visual language

**State 2 output**: Visual language blueprint. Proceed to STATE 3.

### STATE 3 — Character Lock

Route to `director-character`.

**Required deliverables:**

- Character identity definition for each character
- Visual lock parameters (face, hair, body type, wardrobe, props)
- Behavior system (action signature, eye direction, emotion→action mapping)
- Multi-character relationship map (if applicable)

**Verification Gates:**

- [ ] All characters have identity locks
- [ ] Visual parameters are specific enough to be reproducible
- [ ] Behavior system covers emotional range
- [ ] User confirmed all character identity definitions

**State 3 output**: Character identity definitions (text-level design document).

**STATE 3 confirmed — ask the user:**

> Character identity definitions are locked. Do you want to generate character reference images?

- **Yes →** Route to `character-image-prompt` to compile definitions into platform-ready Character Sheet prompts (MJ/Flux/Jimeng/Kling). User then generates actual character reference images. These images serve as character reference input for STATE 6, improving cross-shot identity consistency.
- **No / Not needed →** Skip character image generation. Character identity will be described textually in the prompt package. Note: this may reduce identity consistency in video output compared to using reference images.

Character image generation (if chosen) and STATE 4 prompt package compilation can proceed in parallel.

### STATE 4 — Prompt Packaging (Film-Level Short Film Prompt Package)

Route to `director-prompt-packager`.

**This is a text-level compiler.** It takes all design deliverables from STATE 1-3 (story structure + emotional arc + camera language + lighting system + character identity) and compiles them into a complete **film-level short film prompt package**. This prompt package is the director's vision master document, containing:

- Structured storyboard design (per-shot scene, action, emotional purpose)
- Camera language specification (shot size, angle, movement, composition)
- Lighting and color script
- Sound design direction
- Seedance-compatible Part decomposition plan (each Part ≤ 15s, multi-Part continuity binding)

The output is **not** a Seedance video prompt — it is the design foundation for downstream video generation stages.

**Output Boundary (hard constraint):**

- STATE 4 output must **never** mention video platform names such as Seedance 2.0 / Kling
- Must not contain phrases like "generate in Seedance", "Seedance 2.0 prompt", "generate shot by shot in Seedance"
- The prompt package is a platform-agnostic director-level design document — not bound to any specific image or video generation tool

**Pre-flight Checklist (all must be YES):**

- [ ] Story structure confirmed?
- [ ] Emotional arc confirmed?
- [ ] Visual language (camera + lighting) defined?
- [ ] Character identity locked and confirmed?
- [ ] Duration and aspect ratio locked?
- [ ] **Output boundary compliant: no mention of Seedance / Kling?**

If any answer is NO, stop and return to the missing stage.

**State 4 output**: Film-level short film prompt package (text-level director's vision document). Proceed to routing decision.

**User next step**: Confirm the prompt package content. After confirmation, do NOT proceed directly to STATE 5. First execute the routing decision to determine the best path forward (see STATE 6 mode selection table for available modes based on resources).

### After STATE 4: Routing Decision

After the prompt package is confirmed, determine the best path based on project needs and available resources. Refer to STATE 6 mode selection for which inputs are required per mode. Present 2-3 route options:

| Route | Path | Best for |
|---|---|---|
| **A: Storyboard** | STATE 4 → STATE 5 → STATE 6 (I2V storyboard) | Narrative films, complex multi-shot with storyboard-controlled camera |
| **B: Direct** | STATE 4 → STATE 6 (I2V minimal / FLF2V / T2V / R2V) | Existing ref images, product demos, simple actions, text-only |
| **C: Hybrid** | STATE 4 → STATE 5 (key shots) + STATE 6 (non-key) | Mix of storyboard-needed and direct-reference shots |

### STATE 5 — Storyboard Blueprint Generation (Image Level, Conditional)

**This stage is only executed when Route A or C is selected.** If Route B (direct to video) is chosen, skip STATE 5.

Route to `storyboard-sketch` (for Seedance I2V rough sketches) or `storyboard-prompt` / `storyboard-master` / `storyboard-ecommerce` (for generating complete storyboard blueprint images).

**This is the image generation phase after STATE 4 confirmation.** Compiles the confirmed prompt package's storyboard design into AI image generator-executable storyboard blueprint prompts, generating visual storyboard board images. These images serve as storyboard reference inputs for STATE 6.

**Core insight: In production, only storyboard blueprint boards (one or more overview boards) are needed — not per-frame standalone images.** Storyboard blueprints display the full shot sequence, rhythm structure, and visual language — serving as Seedance's narrative blueprint input, not per-shot render assets.

**Required deliverables:**

- Storyboard blueprint boards (1-N overview boards showing shot sequence + rhythm structure)
- Per-shot visual descriptions (subject, composition, camera, lighting mood for each shot)
- Cross-frame continuity anchors

**Verification Gates:**

- [ ] Storyboard blueprint boards cover all shots
- [ ] Every frame has narrative purpose
- [ ] Character identity consistent across all frames (referencing STATE 3 locks)
- [ ] Visual language consistent with STATE 2 definitions
- [ ] User confirmed storyboard blueprints

**State 5 output**: Storyboard blueprint images (for Seedance reference). Proceed to STATE 6.

### STATE 6 — Seedance Video Prompts (Image Reference Level)

Route to `seedance-video-prompt`.

**This is the L5 video generation compiler.** Selects the generation mode based on available reference assets (see mode selection below), compiling image/video/audio references into Seedance 2.0 / Kling platform-executable video prompts.

**Storyboard images are NOT mandatory — they are only one input for I2V storyboard mode.** The compiler supports seven modes: T2V / I2V minimal / I2V storyboard / R2V / FLF2V / V2V Edit / V2V Extend.

**Platform hard constraints:**

- Chinese prompts ≤ 500 characters, English prompts ≤ 1000 words, total characters ≤ 2000
- Each reference asset must be assigned a unique primary role (identity / product / environment / action rhythm), using role mapping declaration format
- Pass anti-slop check: no empty evaluative words (cinematic / epic / beautiful and other non-physically-referable terms)

**Available inputs (mode-dependent):**

- Storyboard blueprint images (from AI image generators) — only required for I2V storyboard mode
- Character reference images (recommended for identity locking; if user chose to skip at STATE 3, use text descriptions)
- Product reference images (optional, for product locking)
- Background reference images (optional, for environment locking)
- First/last frame images — only required for FLF2V mode
- Video clips — only required for V2V Edit/Extend mode
- Audio clips (optional, for rhythm/atmosphere reference)

**Mode selection (based on available inputs):**

| User has... | Select mode |
|---|---|
| Storyboard blueprint images | I2V (storyboard) |
| Single reference image only (product/character/scene) | I2V (minimal) |
| First + last frame images | FLF2V |
| Multiple different ref types | R2V |
| Video source to modify | V2V Edit |
| Video to continue | V2V Extend |
| Text description only | T2V |

**Pre-flight Checklist (mode-aware):**

- [ ] Required inputs for selected mode ready?
- [ ] Character reference images available? (or user explicitly chose to skip)
- [ ] Product images locked (if applicable)?
- [ ] Background images locked (if applicable)?
- [ ] Music style and BPM determined?
- [ ] **Prompt word count compliant (Chinese ≤ 500 chars)?**
- [ ] **Anti-slop check passed?**

If any required input is missing, prompt the user for the corresponding reference.

**State 6 output**: Seedance 2.0 video prompts (platform-executable). Proceed to STATE 7.


### STATE 7 — Final Validation

Quality check on all deliverables following a professional review loop:

**Per-Part generation review:**
- [ ] Identity check: character/product appearance matches reference images?
- [ ] Action check: motion continuous, no jumps, no deformation?
- [ ] Camera check: movement matches specification, no accidental jump cuts?
- [ ] Continuity check: spatial geography, lighting, time flow consistent across Parts?
- [ ] Audio check: lip-sync aligned, SFX in sync, no end-clip noise?

**Global checks:**
- **Narrative check**: Does the complete sequence tell a coherent story?
- **Visual check**: Is the visual language consistent across all shots?
- **Word count check**: Each prompt Chinese ≤ 500 characters?
- **Anti-slop check**: No hollow evaluation words?

**State 7 output**: Validated video prompts. Proceed to STATE 8.

### STATE 8 — Export Ready

Package final deliverables to professional delivery standards:

**Generation package:**
- Complete Seedance 2.0 prompts (in Part execution order, with per-prompt reference image mapping)
- Image reference character mapping (which `` `ImageN` `` corresponds to which asset, character tag mapping table)
- Multi-Part continuity notes (previous video reference instructions for Part 2+)
- Delivery format notes (duration, aspect ratio, target platform)

**Post-production delivery notes (if applicable):**
- Frame rate, resolution, color pipeline (HDR/SDR) recommendations
- Subtitle/localization plan (subtitle safe area, textless version export)
- End-clip audio fade-out reminder
- Multi-Part splice point frame alignment guide (trim 6 frames from previous clip end + 1 frame from next clip start)
- Asset rights status notes (character reference images, audio clip authorization/source)

## Dependency Graph

```
director-story ────→ director-emotion
       │                    │
       └────────┬───────────┘
                ↓
         director-camera ──→ director-light
                │
                ↓
         director-character ──→ [User: generate character images?]
                │                   │ YES                    │ NO
                │                   ↓                        │
                │         character-image-prompt             │
                │         [Character Sheet prompts]          │
                │                   │                        │
                │                   ↓ (User generates        │
                │               character ref images)        │
                │                   │                        │
                ↓                   ↓                        ↓
         director-prompt-packager [STATE 4: Film-Level Prompt Package]
                │
                ↓ (User confirms package)
                │
         storyboard-sketch / storyboard-prompt / storyboard-master / storyboard-ecommerce
         [STATE 5: Generate storyboard blueprint images]
                │
                ↓
         seedance-video-prompt [STATE 6: Image-ref video prompts → Seedance 2.0]
                │
                ↓
         [Final Validation → Export]
```

## Routing Guide

| User Intent                                                                        | Load First                                                                                         |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| "I have a creative idea, help me make it into a film"                              | Stay in director-core, start from STATE 0                                                          |
| "I already have a script, need visual design"                                      | Enter from STATE 2                                                                                 |
| "I have character identity definitions, need image generation prompts"             | Route to `character-image-prompt`                                                                  |
| "I have story + visual + character design, need to compile a prompt package"       | Enter from STATE 4                                                                                 |
| "I have a prompt package (text), need to generate storyboard blueprint images"     | Enter from STATE 5                                                                                 |
| "I have storyboard blueprint images + character images, need Seedance 2.0 prompts" | Enter from STATE 6                                                                                 |
| "I only want character identity definitions"                                       | Route directly to director-character                                                               |
| "Fix my broken AI video, characters keep changing faces"                           | Enter from STATE 3 (re-lock characters), then STATE 6                                              |
| "E-commerce livestream / product showcase / fashion video storyboard"              | Enter from STATE 4 to compile prompt package, or STATE 5 to directly generate storyboard blueprint |

## Session Resume

**On every director-core load, first check if a checkpoint file exists.**

1. Read `STATE.md`
2. **File not found** → Start from STATE 0, begin input collection
3. **File found** → Parse current state, inform user of progress and ask:

```
ð Production checkpoint found:
- Project: [project name]
- Current progress: STATE N â [name]
- Completed: STATE 0 â STATE N-1
- Next step: [action description]

Continue? (reply "continue" to resume from checkpoint, or "restart" to clear progress)
```

If user chooses "restart", delete or archive the old checkpoint file, start from STATE 0.

## Production Progress Persistence

Production state is persisted via a checkpoint file to ensure recoverability across session interruptions.

### Checkpoint File

- **Path**: `STATE.md`
- **Write triggers**: Immediately after each STATE completion; after each user confirmation of deliverables; at session end
- **Read trigger**: Every `director-core` load (see "Session Resume" above)

### Checkpoint File Format

```markdown
## Production Checkpoint

- **Project**: [project name]
- **Last updated**: [ISO timestamp, e.g. 2026-06-10T14:30:00+08:00]
- **Current state**: STATE N â [name]
- **Completed states**: STATE 0, STATE 1, ..., STATE N-1
- **Pending states**: STATE N+1, STATE N+2, ..., STATE 8
- **Active locks**: [list of locks in effect]
- **Next action**: [what the user needs to do or confirm]

### State Artifacts

| State   | Status | Summary              | Key Output                                              |
| ------- | ------ | -------------------- | ------------------------------------------------------- |
| STATE 0 | â      | Input Collection     | [Brief: project / duration / style / platform / aspect] |
| STATE 1 | â      | Story & Emotion      | [Story structure + emotional arc summary]               |
| STATE 2 | â      | Visual Design        | [Camera language + lighting/color plan summary]         |
| STATE 3 | â      | Character Lock       | [Characters Ã N, visual lock params summary]            |
| STATE 4 | ð      | Prompt Packaging     | [Prompt pack file path or in-progress marker]           |
| STATE 5 | â³     | Storyboard Blueprint | â                                                       |
| STATE 6 | â³     | Video Prompts        | â                                                       |
| STATE 7 | â³     | Final Verification   | â                                                       |
| STATE 8 | â³     | Export               | â                                                       |

### Production Brief

- **Duration**: [15s / 30s / 60s / custom]
- **Aspect ratio**: [16:9 / 9:16 / 1:1]
- **Platform**: [Seedance / Kling]
- **Style**: [Cinematic / Commercial / Documentary / Anime / ...]
- **Director mode**: [Observer / Emotional / Immersive / Epic / Commercial]
```

### End-of-Session Output

In addition to writing the checkpoint file, output a brief status summary in conversation at the end of each session:

```markdown
**Production Status**

- Current state: [STATE N â Name]
- Completed states: [list]
- Pending states: [list]
- Active locks: [which locks are in effect]
- Next action: [what the user needs to do or confirm]
- ð Progress saved to `STATE.md`
```
