---
name: director-core
description: "Master controller for the AI film production pipeline — manages the production state machine, enforces phase locks, maintains checkpoints, and routes tasks to director sub-skills in the correct order. Use when users want to produce a complete AI film/video from a creative idea or script. Trigger scenarios: making an AI film, generating video from creative ideas, directing a Seedance project, AI filmmaking, AI video production, AI director workflow, film production pipeline, or any multi-stage video creation request. Also triggers on any video/film production request, including e-commerce livestreams, product showcase videos, fashion videos, brand videos, product videos, fashion films, and commercial videos.
  中文触发: 制作 AI 电影、从创意生成视频、导演 Seedance 项目、拍AI电影、制作AI视频、AI导演流程、film production pipeline、电商直播、带货视频、服装视频、品牌视频、product video、fashion film、commercial video."
---

# Director Core — Production State Machine

## Overview

The master controller for the AI Film OS pipeline. Ensures every AI film/video project flows through a proven, phase-gated production sequence — from initial creative idea to final Seedance-ready video prompts. The state machine prevents the most common failure mode in AI video production: jumping to prompt generation before the story, visual language, and character identity are locked in.

This skill does not generate creative content itself. It routes tasks to sub-skills at each stage and validates outputs before advancing.

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
    ↓
[Routing Decision: inventory resources → match mode → select route]
    ↓                        ↓
STATE 5 (conditional)    Direct to STATE 6
Storyboard Blueprint     (skip STATE 5)
    ↓                        ↓
    └────────┬───────────────┘
             ↓
STATE 6 → Seedance Video Prompts (multi-mode, image reference level)
STATE 7 → Final Validation
STATE 8 → Export Ready
```

STATE 0-4 are mandatory, must not be skipped. STATE 5 is conditional — only executed when routing decision selects the storyboard blueprint route. STATE 6-8 are mandatory.

**Key distinction between STATE 4 and STATE 5/6:**

- STATE 4 (`director-prompt-packager`): Compiles a **text-level** film-level short film prompt package — integrating story, visual design, and character identity into structured storyboard design, camera language, sound design, and Seedance decomposition plan. The output is a complete director's vision document, which serves as the design foundation for subsequent stages after user confirmation. **Never outputs video platform prompts.**
- STATE 5 (conditional): Only executed when storyboard blueprint boards are needed for I2V storyboard mode. Compiles the prompt package into AI image generator-executable storyboard blueprint prompts.
- STATE 6 (`seedance-video-prompt`): Compiles **image-reference-level** video prompts for Seedance 2.0 / Kling. Supports 7 modes (T2V / I2V / R2V / FLF2V / V2V / ...). **Storyboard images optional** — only required for I2V storyboard mode. Output: platform-executable video generation prompts.

**The STATE 4 → STATE 6 separation of concerns is the foundation of pipeline design. Must never be crossed.**

## Phase Lock Rules

These are hard constraints. Violating them leads to the most common AI video failures (character drift, visual inconsistency, narrative incoherence).

| Lock                     | Rule                                                                                                 |
| ------------------------ | ---------------------------------------------------------------------------------------------------- |
| **Story Lock**           | Story structure and emotional arc must be confirmed before visual design                             |
| **Visual Lock**          | Camera language and lighting system must be defined before prompt packaging                          |
| **Character Lock**       | Character identity definitions must be confirmed before prompt packaging                             |
| **Package Lock**         | The film-level prompt package must be user-confirmed before entering subsequent stages               |
| **Storyboard Lock**      | If going through STATE 5, storyboard images must be confirmed before Seedance prompts                |
| **Prompt Lock**          | All pre-flight checks must pass before final export                                                  |
| **Output Boundary Lock** | STATE 4 output must not mention Seedance/Kling video platform names                                  |

If any lock is broken, stop immediately and return to the earliest incomplete state.

## State Machine

### STATE 0 — Input Collection

First assess input quality, then decide whether to call :

| Input quality | Criteria | Action |
|---|---|---|
| Creative complete | Has subject + action + scene + emotional direction | **Skip interview**, collect params directly |
| Descriptive but no plot | Has scene/style/tone, lacks narrative action | Call  → Creative expansion |
| Vague creative | Only keywords / broad concepts | Call  → Creative interview |

Collect production params (duration, style, platform, aspect ratio, reference materials). If user says "just do it", fill reasonable defaults with annotations.### STATE 1 — Story & Emotion Design

Route to `director-story` and `director-emotion`.

**Required deliverables:**

- Narrative structure (three-act or five-act breakdown)
- Scene list, each scene with narrative purpose
- Emotional arc diagram (calm → tension → climax → resolution)
- Emotional intensity timeline

**Verification Gates:**

- [ ] Every scene has a narrative purpose
- [ ] Emotional arc covers full duration
- [ ] Causal chain defined (A causes B causes C)
- [ ] User confirmed structure

**State 1 output**: Script blueprint + Emotional timeline.

> Save to `outputs/YYYY-MM-DD-[topic]-State-1-story-emotion.md`

Proceed to STATE 2.

### STATE 2 — Visual Design

Route to `director-style` (director style), `director-camera` (camera system), and `director-light` (lighting system).

**Required deliverables:**

- Camera language blueprint (primary shot types, movement vocabulary, angle philosophy)
- Lighting design system (key light strategy, color temperature arc, contrast rules)
- Color script (dominant colors per act/scene, temperature curve)
- Composition rules (primary and secondary framing approaches)

**Verification Gates:**

- [ ] Camera language matches emotional tone
- [ ] Lighting evolves with the narrative
- [ ] Color script covers full duration
- [ ] User confirmed visual language

**State 2 output**: Visual language blueprint.

> Save to `outputs/YYYY-MM-DD-[topic]-State-2-visual.md`

Proceed to STATE 3.

### STATE 3 — Character Lock

Route to `director-character`.

**Required deliverables:**

- Character identity definition for each character
- Visual lock parameters (face, hairstyle, body type, wardrobe, props)
- Behavior system (movement signature, eyeline direction, emotion→action mapping)
- Multi-character relationship map (if applicable)

**Verification Gates:**

- [ ] All characters have identity locks
- [ ] Visual parameters are specific enough to be reproducible
- [ ] Behavior system covers emotional range
- [ ] User confirmed all character identity definitions

**State 3 output**: Character identity definitions (text-level design document).

**After STATE 3 confirmation — ask the user:**

> Character identity definitions are locked. Do you need to generate character reference images?

- **Yes →** Route to `character-image-prompt` to compile definitions into platform-ready Character Sheet image generation prompts (MJ/Flux/Jimeng/Kling). User then generates actual character reference images. These images serve as character reference input for STATE 6, improving cross-shot identity consistency.
- **No / Skip →** Skip character image generation. Character identity will be presented as text descriptions in the prompt package. Note: this may reduce identity consistency in video output compared to using reference images.

Character image generation (if selected) and STATE 4 prompt package compilation can run in parallel.

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

**User next step**: Confirm the prompt package content. After confirmation, do NOT proceed directly to STATE 5 — first execute the routing decision to determine the best path forward.

### After STATE 4: Routing Decision

After the prompt package is confirmed, **do NOT proceed directly to STATE 5.** First determine the best path based on project needs, available resources, and the target STATE 6 mode.

**Step 1: Inventory available resources**

Ask the user what multimodal resources they currently have (multi-select):

```
Which visual/multimodal resources do you currently have?
- [ ] Character reference images (from STATE 3 character generation or user-provided)
- [ ] Product reference images
- [ ] Background/environment reference images
- [ ] First/last frame images
- [ ] Video reference clips
- [ ] Audio reference clips
- [ ] None of the above — start from text only
```

**Step 2: Match STATE 6 modes**

Based on available resources, match against the STATE 6 mode selection table:

| Available resources | Eligible modes |
|---|---|
| None of the above | T2V |
| Single reference image (product/character/scene) | I2V (minimal) |
| First + last frame images | FLF2V |
| Multiple different ref types (product+video+audio etc.) | R2V |
| Video source clip | V2V Edit / V2V Extend |
| Need storyboard boards for multi-shot continuous camera | I2V (storyboard) → requires STATE 5 first |

**Step 3: Present 2-3 route options**

Recommend the most suitable route based on project characteristics, with alternatives:

| Route | Path | Best for | User needs to provide |
|---|---|---|---|
| **A: Storyboard Blueprint** | STATE 4 → STATE 5 → STATE 6 (I2V storyboard) | Narrative short films, complex multi-shot sequences, precise storyboard-controlled camera movement | Nothing extra (STATE 5 generates storyboard images) |
| **B: Direct to Video** | STATE 4 → STATE 6 (I2V minimal / FLF2V / T2V / R2V) | Existing reference images, product showcases, simple actions, first/last frame transitions, text-only generation | Single/multiple reference images / first-last frames / video-audio clips |
| **C: Hybrid** | STATE 4 → STATE 5 (key shots) + STATE 6 (non-key shots in parallel) | Some shots need storyboard control, others can use direct references | Reference images for non-key shots |

After user selects a route, proceed accordingly. Route A enters STATE 5; Route B skips STATE 5 directly to STATE 6; Route C partially executes STATE 5 as needed.

### STATE 5 — Storyboard Blueprint Generation (Image Level, Conditional)

**This stage is only executed when Route A or C is selected in the routing decision.** If the user selects Route B (direct to video), skip STATE 5 and proceed directly to STATE 6.

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
         [Routing Decision: inventory resources → match mode → select route]
                │                    │
        Route A: Storyboard    Route B: Direct to Video
                │                    │
         storyboard-sketch /         │
         storyboard-prompt /         │
         storyboard-master /         │
         storyboard-ecommerce        │
         [STATE 5: Conditional]      │
                │                    │
                └────────┬───────────┘
                         ↓
         seedance-video-prompt [STATE 6: Image-ref video prompts → Seedance 2.0]
                │
                ↓
         [Final Validation → Export]
```

## Routing Guide

| User Intent                                                                        | Load First                                                                                         |
| ------------------------------------------------------- | ------------------------------------------------------------ |
| "I have a creative idea, help me make it into a film"                              | Stay in director-core, start from STATE 0                                                          |
| "I already have a script, need visual design"                                      | Enter from STATE 2                                                                                 |
| "I have character identity definitions, need image generation prompts"             | Route to `character-image-prompt`                                                                  |
| "I have story + visual + character design, need to compile a prompt package"       | Enter from STATE 4                                                                                 |
| "I have a prompt package (text), need to generate storyboard blueprint images"     | Enter from STATE 5 (default `storyboard-master`)                                                   |
| "Write a single shot frame / how to shoot this scene"                              | Route to `storyboard-prompt`                                                                       |
| "Plan Seedance I2V storyboard frames / per-frame motion"                           | Route to `storyboard-sketch`                                                                       |
| "E-commerce livestream / product showcase / fashion video storyboard"              | Route to `storyboard-ecommerce`                                                                    |
| "I have a prompt package + ref images, need video directly (no storyboard needed)" | Enter from STATE 4 routing → Route B → skip to STATE 6                                             |
| "I have storyboard blueprint images + character images, need Seedance 2.0 prompts" | Enter from STATE 6                                                                                 |
| "I have single ref image / first-last frames, need to generate video"              | Enter from STATE 4 routing → Route B → STATE 6 (I2V minimal / FLF2V)                              |
| "I just want character identity definitions"                                       | Route directly to `director-character`                                                             |
| "Fix my broken AI video, characters keep changing faces"                           | Enter from STATE 3 (re-lock characters), then STATE 6                                              |

## Session Resume

**On every director-core load, first check if a checkpoint file exists.**

1. Read `STATE.md`
2. **File not found** → Start from STATE 0, begin input collection
3. **File found** → Parse current state, inform user of progress and ask:

```
📋 Production checkpoint found:
- Project: [project name]
- Current progress: STATE N — [name]
- Completed: STATE 0 → STATE N-1
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
- **Current state**: STATE N — [name]
- **Completed states**: STATE 0, STATE 1, ..., STATE N-1
- **Pending states**: STATE N+1, STATE N+2, ..., STATE 8
- **Active locks**: [list of locks in effect]
- **Next action**: [what the user needs to do or confirm]

### State Artifacts

| State   | Status | Summary    | Key Output                                  |
| ------- | ------ | ---------- | ------------------------------------------- |
| STATE 0 | ✅     | Input Collection   | [Brief: project / duration / style / platform / aspect] |
| STATE 1 | ✅     | Story & Emotion    | [Story structure + emotional arc summary]              |
| STATE 2 | ✅     | Visual Design      | [Camera language + lighting/color plan summary]        |
| STATE 3 | ✅     | Character Lock     | [Characters × N, visual lock params summary]           |
| STATE 4 | 🔄     | Prompt Packaging   | [Prompt pack file path or in-progress marker]          |
| STATE 5 | ⏳     | Storyboard         | —                                                      |
| STATE 6 | ⏳     | Video Prompts      | —                                                      |
| STATE 7 | ⏳     | Final Verification | —                                                      |
| STATE 8 | ⏳     | Export             | —                                                      |

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

- Current state: [STATE N — Name]
- Completed states: [list]
- Pending states: [list]
- Active locks: [which locks are in effect]
- Next action: [what the user needs to do or confirm]
- 📁 Progress saved to `STATE.md`
```
