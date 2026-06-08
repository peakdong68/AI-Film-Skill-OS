---
name: director-core
description: Master orchestrator for the AI film production pipeline. Controls the production state machine, enforces phase locking, manages checkpoints, and routes to all director sub-skills in the correct sequence. Use when the user wants to produce a complete AI film/video from an idea or script — this is the entry point that ensures every phase is validated before the next begins. Triggers on: making an AI film, producing a video from idea, directing a Seedance project, 拍AI电影, 制作AI视频, AI导演流程, film production pipeline, or any multi-phase video creation request.
---

# Director Core — Production State Machine

## Overview

This is the master orchestrator for the AI Film OS pipeline. It ensures every AI film/video project flows through a validated, phase-gated production sequence — from initial idea to final Seedance-ready video prompts. The state machine prevents the most common failure mode in AI video production: jumping to prompt generation before the story, visual language, and character identity are locked.

This skill does not generate creative content itself. It routes to the appropriate sub-skills at each phase and validates outputs before advancing.

## The Production Pipeline

```
STATE 0 → INPUT INGESTION
STATE 1 → STORY & EMOTION DESIGN
STATE 2 → VISUAL DESIGN (CAMERA + LIGHTING)
STATE 3 → CHARACTER LOCK
STATE 4 → STORYBOARD PLANNING
STATE 5 → PROMPT COMPILATION
STATE 6 → FINAL VALIDATION
STATE 7 → EXPORT READY
```

Each state produces a validated artifact before the next state unlocks. Skipping states is forbidden.

## Phase Lock Rules

These are hard constraints. Violating them causes the most common AI video failures (character drift, visual inconsistency, incoherent narrative).

| Rule | Lock |
|------|------|
| **Story Lock** | Story structure and emotion arc must be confirmed before visual design | 
| **Visual Lock** | Camera language and lighting system must be defined before storyboard |
| **Character Lock** | Character identity sheet must be confirmed before prompt generation |
| **Storyboard Lock** | All storyboard frames must be confirmed before Seedance prompts |
| **Prompt Lock** | All pre-check items must pass before final export |

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
- [ ] User has confirmed all character sheets

**State 3 output**: Character Sheets + Identity Locks. Proceed to STATE 4.

### STATE 4 — STORYBOARD PLANNING

Route to `storyboard-sketch` (for Seedance I2V) or `storyboard-prompt` / `storyboard-master` (for image generator boards).

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

### STATE 5 — PROMPT COMPILATION

Route to `director-seedance`.

**Required artifacts:**
- Seedance-ready video prompts per shot
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

If any answer is NO, halt and return to the missing phase.

**State 5 output**: Seedance Video Prompt Pack. Proceed to STATE 6.

### STATE 6 — FINAL VALIDATION

Quality pass across all artifacts:

- **Narrative check**: Does the full sequence tell a coherent story?
- **Visual check**: Is the visual language consistent across all shots?
- **Character check**: Is character identity preserved in every prompt?
- **Continuity check**: Do spatial geography, lighting, and time flow feel continuous?
- **Execution check**: Is every prompt directly usable in the target tool?

**State 6 output**: Validated prompt pack. Proceed to STATE 7.

### STATE 7 — EXPORT READY

Package the final deliverable:
- Full prompt list in execution order
- Context continuity notes for multi-part generation
- Reference image role map (if reference images were provided)
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
         director-character
                │
                ↓
         storyboard-sketch / storyboard-prompt / storyboard-master
                │
                ↓
         director-seedance
                │
                ↓
         [FINAL VALIDATION → EXPORT]
```

## Routing Guide

| User intent | Load first |
|---|---|
| "I have an idea, make it into a film" | Stay in director-core, start STATE 0 |
| "I already have a script, need visual design" | Enter at STATE 2 |
| "I have storyboard frames, need Seedance prompts" | Enter at STATE 5 |
| "I just want the character sheet" | Route directly to director-character |
| "Fix my broken AI video, character keeps changing" | Enter at STATE 3 (re-lock character), then STATE 5 |

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
