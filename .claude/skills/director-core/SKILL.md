---
name: director-core
description: Master orchestrator for the AI film production pipeline. Controls the production state machine, enforces phase locking, manages checkpoints, and routes to all director sub-skills in the correct sequence. Use when the user wants to produce a complete AI film/video from an idea or script — this is the entry point that ensures every phase is validated before the next begins. Triggers on: making an AI film, producing a video from idea, directing a Seedance project, 拍AI电影, 制作AI视频, AI导演流程, film production pipeline, or any multi-phase video creation request. Also triggers on any video/film production request including电商直播, 带货视频, 服装视频, 品牌视频, product video, fashion film, commercial video.
---

# Director Core — Production State Machine

## Overview

This is the master orchestrator for the AI Film OS pipeline. It ensures every AI film/video project flows through a validated, phase-gated production sequence — from initial idea to final Seedance-ready video prompts. The state machine prevents the most common failure mode in AI video production: jumping to prompt generation before the story, visual language, and character identity are locked.

This skill does not generate creative content itself. It routes to the appropriate sub-skills at each phase and validates outputs before advancing.

## Loaded Resources

This skill ships with reference knowledge files. Load them when:
- For detailed state flow rules and multi-part structure specifications, read `references/production-state-machine.md`
## The Production Pipeline

```
STATE 0 → INPUT INGESTION
STATE 1 → STORY & EMOTION DESIGN
STATE 2 → VISUAL DESIGN (CAMERA + LIGHTING)
STATE 3 → CHARACTER LOCK
STATE 4 → STORYBOARD PLANNING
STATE 5 → PROMPT PACKAGING (TEXT-LEVEL)
STATE 6 → SEEDANCE VIDEO PROMPT (IMAGE-REF LEVEL)
STATE 7 → FINAL VALIDATION
STATE 8 → EXPORT READY
```

Each state produces a validated artifact before the next state unlocks. Skipping states is forbidden.

**Key distinction between STATE 5 and STATE 6:**
- STATE 5 (`director-prompt-packager`): Compiles TEXT-LEVEL storyboard prompt packages for AI image generators (MJ/Flux/Jimeng). Output: structured text prompts to generate storyboard images. **Never produces video platform prompts.**
- STATE 6 (`seedance-video-prompt`): Compiles IMAGE-REFERENCE video prompts for Seedance 2.0 / Runway / Sora / Kling. Input: generated storyboard images + character images. Output: platform-executable video generation prompts.

**The STATE 5 → STATE 6 separation of concerns is foundational to the pipeline design. Never cross it.**

## Phase Lock Rules

These are hard constraints. Violating them causes the most common AI video failures (character drift, visual inconsistency, incoherent narrative).

| Rule | Lock |
|------|------|
| **Story Lock** | Story structure and emotion arc must be confirmed before visual design | 
| **Visual Lock** | Camera language and lighting system must be defined before storyboard |
| **Character Lock** | Character identity sheet must be confirmed before prompt generation |
| **Storyboard Lock** | All storyboard frames must be confirmed before Seedance prompts |
| **Prompt Lock** | All pre-check items must pass before final export |
| **Output Boundary Lock** | STATE 5 output must not mention Seedance / Runway / Sora / Kling video platforms |

If any lock is broken, halt and return to the earliest incomplete state.

## State Machine

### STATE 0 — INPUT INGESTION

Gather the minimum viable brief. Ask only what's needed to begin:

- Project idea or script (one sentence minimum)
- Intended duration (15s / 30s / 60s / custom)
- Visual style (cinematic / commercial / documentary / anime / sci-fi / etc.)
- Delivery platform (Seedance / Runway / Sora / Kling)
- Aspect ratio (16:9 / 9:16 / 1:1)
- Any existing reference images or character descriptions

If the user provides fewer than 4 of these, ask the missing ones. If they say "直接生成" or "just do it", fill gaps with reasonable defaults and mark them.

**State 0 output**: A confirmed production brief. Proceed to STATE 1.

### STATE 1 — STORY & EMOTION DESIGN

Route to `director-story` and `director-emotion`.

**Required artifacts:**
- Narrative structure (3-act or 5-act breakdown)
- Scene list with scene purpose per scene
- Emotional arc map (calm → tension → climax → resolution)
- Emotional intensity timeline

**Validation gate:**
- [ ] Every scene has a narrative purpose
- [ ] Emotional arc covers the full duration
- [ ] Causal chain is defined (A causes B causes C)
- [ ] User has confirmed the structure

**State 1 output**: Script Blueprint + Emotional Timeline. Proceed to STATE 2.

### STATE 2 — VISUAL DESIGN

Route to `director-camera` and `director-light`.

**Required artifacts:**
- Camera language blueprint (primary shot types, movement vocabulary, angle philosophy)
- Lighting design system (key light strategy, color temperature arc, contrast rules)
- Color script (dominant colors per act/scene, temperature curve)
- Composition rules (primary and secondary framing approaches)

**Validation gate:**
- [ ] Camera language matches the emotional tone
- [ ] Lighting evolves with the narrative
- [ ] Color script is defined across the full duration
- [ ] User has confirmed the visual language

**State 2 output**: Visual Language Blueprint. Proceed to STATE 3.

### STATE 3 — CHARACTER LOCK

Route to `director-character`.

**Required artifacts:**
- Character Identity Sheet per character
- Visual lock parameters (face, hair, body, wardrobe, props)
- Behavior system (movement signature, eye direction, emotion-to-motion mapping)
- Multi-character relationship map (if applicable)

**Validation gate:**
- [ ] All characters have identity locks
- [ ] Visual parameters are specific enough to reproduce
- [ ] Behavior system accounts for emotional range
- [ ] User has confirmed all character identity definitions

**State 3 output**: Character Identity Definitions (text-level design docs).

**After STATE 3 confirmation, route to `character-image-prompt`:**
This sub-skill compiles the character identity definitions into platform-ready character sheet image generation prompts (MJ/Flux/Jimeng/Kling). The user then generates actual character reference images. These images are required as `@[character ref]` inputs for STATE 6 (Seedance Video Prompt).

Proceed to STATE 4 (Storyboard) — Storyboard and character image generation can run in parallel.

### STATE 4 — STORYBOARD PLANNING

Route to `storyboard-sketch` (for Seedance I2V) or `storyboard-prompt` / `storyboard-master` / `storyboard-ecommerce` (for image generator boards).

**Required artifacts:**
- Storyboard frame plan (3-8 frames per board)
- Shot-by-shot breakdown with camera, action, emotion, purpose
- Continuity anchors across all frames

**Validation gate:**
- [ ] Number of boards matches the planned duration
- [ ] Every frame has a narrative purpose
- [ ] Character identity is maintained across all frames
- [ ] User has confirmed all storyboard frames

**State 4 output**: Storyboard Boards + Shot Plan. Proceed to STATE 5.

### STATE 5 — PROMPT PACKAGING (TEXT-LEVEL)

Route to `director-prompt-packager`.

**This is a text-level compiler.** It produces structured prompt packages for AI image generators (Midjourney, Flux, Jimeng, Kling). The output is NOT a Seedance video prompt — it is the input for generating storyboard images.

**Output boundary (hard constraint):**
- STATE 5 output must **never** mention Seedance 2.0 / Runway / Sora / Kling video platform names
- Must not contain "generate in Seedance", "Seedance 2.0 prompt", "generate sequentially in Seedance", etc.
- All generation instructions must point to image generators (Jimeng/MJ/Flux/Kling image mode)

**Required artifacts:**
- Structured prompt blocks per storyboard frame
- Continuity context locks between shots
- Negative constraint blocks per shot
- Multi-part continuity bindings (for videos > 15s)

**Pre-Check Checklist (all must be YES):**
- [ ] All storyboards completed?
- [ ] User confirmed all storyboards?
- [ ] Character sheets completed?
- [ ] User confirmed characters?
- [ ] Visual language defined?
- [ ] Duration and aspect ratio locked?
- [ ] **Output boundary compliant: no mention of Seedance / Runway / Sora / Kling?**

If any answer is NO, halt and return to the missing phase.

**State 5 output**: Storyboard Prompt Package (text-level, for AI image generators). Proceed to STATE 6.

**Next step for user**: Use the prompt package to generate storyboard images in MJ/Flux/Jimeng.

### STATE 6 — SEEDANCE VIDEO PROMPT (IMAGE-REF LEVEL)

Route to `seedance-video-prompt`.

**This is the L5 video generation compiler.** It takes generated storyboard images, character reference images, and product/background references as `@[ref]` inputs, and compiles them into Seedance 2.0 / Runway / Sora / Kling platform-executable video prompts.

**Platform hard constraints:**
- Chinese prompts ≤ 500 characters, English prompts ≤ 1000 words, total ≤ 2000 characters
- Each @[ref] must be assigned a single primary role (identity / product / environment / action rhythm), using role mapping declaration format
- Pass anti-slop check: no empty evaluation words (cinematic / epic / beautiful, etc. without physical referents)

**Required inputs:**
- Generated storyboard images (from AI image generators)
- Character reference images (for identity lock)
- Product reference images (optional, for product lock)
- Background reference images (optional, for environment lock)

**Pre-Check Checklist (all must be YES):**
- [ ] Storyboard images generated?
- [ ] Character reference images available?
- [ ] Product images locked (if applicable)?
- [ ] Background images locked (if applicable)?
- [ ] Music style and BPM decided?
- [ ] **Prompt character count compliant (ZH ≤ 500 chars)?**
- [ ] **Anti-slop check passed?**

If any answer is NO, prompt the user to provide the missing references.

**State 6 output**: Seedance 2.0 Video Prompt (platform-executable). Proceed to STATE 7.

### STATE 7 — FINAL VALIDATION

Quality pass across all artifacts:

- **Narrative check**: Does the full sequence tell a coherent story?
- **Visual check**: Is the visual language consistent across all shots?
- **Character check**: Is character identity preserved in every prompt?
- **Continuity check**: Do spatial geography, lighting, and time flow feel continuous?
- **Execution check**: Is the Seedance prompt directly usable in the target platform?
- **Character count check**: Are Chinese prompts ≤ 500 characters?

**State 7 output**: Validated video prompt. Proceed to STATE 8.

### STATE 8 — EXPORT READY

Package the final deliverable:
- Full Seedance 2.0 prompt in execution order
- Image reference role map (which @[ref] maps to which image)
- Context continuity notes for multi-part generation
- Delivery format notes (duration, aspect ratio, platform)

## Dependency Graph

```
director-story ────→ director-emotion
       │                    │
       └────────┬───────────┘
                ↓
         director-camera ──→ director-light
                │
                ↓
         director-character ──→ character-image-prompt [character image prompts for MJ/Flux/Jimeng]
                │                         │
                │                         ↓ (user generates character reference images)
                ↓                         │
         storyboard-sketch / storyboard-prompt / storyboard-master / storyboard-ecommerce
                │                         │
                ↓                         │
         director-prompt-packager [STATE 5: text-level prompt package for image generators]
                │                         │
                ↓ (user generates storyboard images via MJ/Flux/Jimeng)
                │                         │
                └─────────┬───────────────┘
                          ↓
         seedance-video-prompt [STATE 6: image-ref video prompt for Seedance 2.0]
                          │
                          ↓
         [FINAL VALIDATION → EXPORT]
```

## Routing Guide

| User intent | Load first |
|---|---|
| "I have an idea, make it into a film" | Stay in director-core, start STATE 0 |
| "I already have a script, need visual design" | Enter at STATE 2 |
| "I have a character identity, need image generation prompts" | Route to `character-image-prompt` |
| "I have storyboard frames (text), need image prompts" | Enter at STATE 5 |
| "I have storyboard images + character images, need Seedance 2.0 prompts" | Enter at STATE 6 |
| "I just want the character identity definition" | Route directly to director-character |
| "Fix my broken AI video, character keeps changing" | Enter at STATE 3 (re-lock character), then STATE 6 |
| "电商直播/带货/服装视频分镜" | Enter at STATE 4, route to storyboard-ecommerce |

## Status Tracker

At the end of every production session, output:

```markdown
**Production Status**
- Current state: [STATE N — name]
- Completed states: [list]
- Pending states: [list]
- Active locks: [which locks are in effect]
- Next action: [what the user needs to do or confirm]
```
