---
name: director-prompt-packager
description: Compiles all pre-production assets (story structure, emotion blueprint, camera language, lighting design, character identity locks) into a complete film-level short film prompt package. This is the text-level compiler in the AI Film OS pipeline — it produces a director's vision master document (containing structured storyboard design, camera language, sound design, and Seedance decomposition plan) for user confirmation, NOT final video platform prompts. Use for short film prompt package compilation, director vision document generation, storyboard design compilation, or when director-core routes to STATE 4 (Prompt Packaging). When the user needs to convert a story idea into an executable storyboard design plan. Note: output is a text-level design document for STATE 5 storyboard blueprint generation and STATE 6 Seedance video prompt compilation.
---

# Director Prompt Packager — Film-Level Short Film Prompt Package Compiler

## Overview

This is the **text-level compiler** in the AI Film OS pipeline, positioned at STATE 4 (before storyboard image generation). It receives all design outputs from STATE 1-3 — narrative structure, emotion blueprint, camera language, lighting design, character identity locks — and compiles them into a complete **film-level short film prompt package**.

This prompt package is the director's vision master document. Any director or producer reading it can fully understand the film's:

- What happens in each shot (structured storyboard design)
- How it is shot (camera language: shot size, movement, composition)
- How light and color drive emotion
- How sound shapes rhythm
- How it is decomposed into Seedance-executable Parts (each Part ≤ 15s)

**This skill produces text-level design documents — NOT Seedance 2.0 / Kling final executable video prompts.**

After the prompt package is confirmed by the user, workflow proceeds to STATE 5 (storyboard blueprint image generation) and STATE 6 (Seedance video prompt compilation).

Can be used standalone for prompt package compilation, or called by `director-core` at STATE 4.

## Load Resources

This skill includes bundled reference knowledge. Load when needed:

- For prompt packaging templates and conversion formulas, read `references/seedance-templates.md`
- For Seedance production pipeline workflows and continuity rules, read `references/pipeline-workflow.md`
- For anti-slop lexicon replacement, read shared reference `../references/anti-slop-lexicon.md`
- For Seedance platform constraints (word limits, @[ref] format), read `../references/seedance-platform.md`
- For genre recipe families and prompt skeletons (product, lifestyle, drama, etc.), read `../references/seedance-genre-recipes.md`

## Pipeline Position

```
STATE 1 → Story & Emotion
STATE 2 → Visual Design (Camera + Lighting)
STATE 3 → Character Locking
STATE 4 → [This Skill] Film-Level Prompt Package Compilation ← User Confirmation
STATE 5 → Storyboard Blueprint Image Generation
STATE 6 → Seedance Video Prompts
```

**Key principle: Prompt package before images.** Let the user confirm the complete director's plan at the text level first, then invest resources in generating visual blueprints. This prevents rework caused by directional errors.

## Output Boundary (Hard Constraint)

> **STATE 4 produces only text-level director vision documents. Never video platform prompts.**

This hard constraint prevents the most common pipeline error — mistakenly feeding text design documents into Seedance 2.0 video platform.

**The following video platform names must NEVER appear in any STATE 4 output:**

- Seedance 2.0
- Kling (Kling video mode)

**The following must absolutely NOT appear in STATE 4 output:**

- "Generate videos shot-by-shot in Seedance 2.0"
- "Directly use for Seedance generation"
- "Seedance 2.0 prompt"
- "Generate in Seedance in shot order"
- Any phrasing suggesting this output can be used directly on video platforms

**Correct downstream phrasing:**

- "After confirming this prompt package, proceed to STATE 5 to generate storyboard blueprint images"
- "Storyboard blueprint images will serve as @[ref] inputs for STATE 6"

Violating this boundary will cause users to mistakenly input text design documents into video platforms, resulting in generation failures or anomalous output.

## Compilation Principles

> A prompt package is not wordplay. It is executable design instruction.

The compiler translates STATE 1-3 design outputs into a self-contained director document — anyone can understand the full film plan without external context.

Three compilation layers:

1. **Creative Layer** (Story + Emotion) → scene purpose + narrative rhythm + emotion curve
2. **Execution Layer** (Camera + Lighting + Character) → shot technical specifications + visual continuity
3. **Delivery Layer** (Part decomposition + platform adaptation) → Seedance-executable decomposition plan

## Input Requirements

Before compilation, verify all upstream outputs are ready:

- [ ] Narrative structure + emotion arc (from STATE 1 — director-story + director-emotion)
- [ ] Camera language blueprint (from STATE 2 — director-camera)
- [ ] Lighting design system + color script (from STATE 2 — director-light)
- [ ] Character identity locks (from STATE 3 — director-character)
- [ ] Project metadata: total duration, aspect ratio, target platform

If any output is missing, halt and route back to the corresponding director skill. Never compile from incomplete inputs.

## Output Structure: Film-Level Short Film Prompt Package

```markdown
# [Project Name] — Film-Level Short Film Prompt Package

## Project Metadata

- Total Duration: [Ns]
- Aspect Ratio: [16:9 / 9:16 / 1:1]
- Visual Style: [style description]
- Target Platform: [Image Generation → Seedance 2.0]

---

## I. Narrative Overview

### Story Synopsis

[One-paragraph summary of the full narrative]

### Narrative Structure

[Three-act or five-act breakdown, each act with scene purposes]

### Emotion Arc

[Emotion intensity timeline: calm → build → climax → resolution]
[Emotion keywords and intensity markers for each scene]

---

## II. Storyboard Design Plan

For each shot within each Part, describe:

- Scene Purpose (why this shot exists)
- Visual Content (what the audience sees)
- Action Description (what the subject is doing)
- Camera Deployment (shot size + angle + movement)
- Lighting Direction (key + fill + color temperature)
- Emotion Progression (from state A → toward state B)

### Part 1: [Part Title] (0-Ns)

#### SHOT 01: [Shot Title]

- Duration: [N] seconds
- Scene: [location + time + environmental context]
- Purpose: [narrative purpose — establish/reveal/transition/intensify/resolve]
- Visual: [visual description — subject, composition, background]
- Action: [subject physical action, concrete and observable]
- Camera: [shot size] [angle] [movement] [lens behavior]
- Lighting: [key light direction/color temp] + [fill] + [rim] + [atmosphere]
- Emotion: [current emotional state → progression direction]
- Character Lock: [character identity lock reference]

#### SHOT 02: ...

...

### Part 2: [Part Title] (Ns-Ns)

...

---

## III. Camera Language Specification

### Camera Movement Vocabulary

[Movement types used throughout the film and their narrative intent]

### Composition Philosophy

[Primary and secondary framing approaches, when to use centered/rule of thirds/negative space, etc.]

### Shot Size Distribution

[Film-wide shot size ratio: WS% / MS% / CU% and narrative justification]

---

## IV. Lighting & Color Script

### Lighting System

- Key light strategy: [key light strategy]
- Color temperature arc: [color temperature progression curve]
- Contrast rules: [contrast rules — when low-key / high-key]

### Color Script

[Primary colors and visual temperature per act/scene]

---

## V. Sound Design Direction

### Music Style

[Style + BPM range]

### Sound Narrative

- Ambience: [ambient sound strategy]
- Emotional cues: [sound design for key emotional moments]
- Silence usage: [when to use silence]

---

## VI. Seedance Decomposition Plan

### Part Structure

| Part | Time Range | Shot Count | Core Narrative | Continuity Requirements |
| ---- | ---------- | ---------- | -------------- | ----------------------- |
| 1    | 0-Ns       | N          | [content]      | Establish baseline      |
| 2    | Ns-Ns      | N          | [content]      | Continue from Part 1    |
| ...  | ...        | ...        | ...            | ...                     |

### Required Visual Asset Checklist

- [ ] Storyboard blueprint images (1-N images, generated by STATE 5)
- [ ] Character reference images: [Character Name 1], [Character Name 2], ...
- [ ] Product reference images (optional): [Product Name]
- [ ] Background reference images (optional): [Scene Name]

### Continuity Binding Strategy

- Part 1: storyboard-driven
- Part 2+: previous video continuity + current storyboard blueprint

---
```

## Compilation Rules

### Rule 1: Action Must Be Precise

- Each shot must describe one clear physical action, not an abstract emotional state.
- ❌ "She is sad" → ✔ "Her shoulders drop, jaw lowers, eyes avert, breathing slows"
- Use emotion→action mappings from `director-character`.

### Rule 2: Camera Must Be Explicit

- Each shot must have shot size, angle, and movement from `director-camera`.
- Camera decisions must trace back to emotional intent — no unmotivated camera behavior.

### Rule 3: Timing Must Be Executable

- 1 shot = 1 action unit = 2-5 seconds
- A single shot must not contain multiple temporally separated actions

### Rule 4: Characters Must Be Locked

- Each shot must reference character identity locks from `director-character`
- Explicitly state character name + appearance lock parameters
- Do not regenerate or redescribe characters — reference the lock

### Rule 5: Parts Must Be Platform-Aware

- Each Part ≤ 15 seconds (Seedance single-generation limit)
- Part 1 establishes the world baseline
- Part 2+ must declare continuity: continue from previous Part's endpoint
- Emotion must evolve, not reset

### Rule 6: Output Platform Boundary

- The prompt package is a text design document, not video platform commands
- Never write "generate in Seedance" or include @[ref] syntax
- @[ref] syntax belongs to STATE 6's domain

---

## Verification Checklist

Before delivering the final prompt package, verify:

- [ ] Narrative structure is complete with a clear causal chain
- [ ] Each shot has a clear narrative purpose
- [ ] Each shot has a concrete physical action
- [ ] Each shot has camera behavior defined (shot size + angle + movement)
- [ ] Lighting direction is consistent and evolves with the narrative
- [ ] Character identity is locked in every shot
- [ ] Sound design direction covers the entire film
- [ ] Part decomposition plan: each segment ≤ 15s
- [ ] Part 2+ has continuity declaration
- [ ] **Output boundary compliant: no mention of Seedance / Kling video platforms**
- [ ] **No @[ref] syntax included (belongs to STATE 6 domain)**
- [ ] Required visual asset checklist is complete

---

## Downstream Integration

After this skill produces the text-level prompt package, the workflow continues:

1. **User confirms prompt package** → all storyboard design, camera language, and sound direction confirmed
2. **STATE 5** → use `storyboard-sketch` / `storyboard-prompt` / `storyboard-master` / `storyboard-ecommerce` to generate storyboard blueprint images
3. **STATE 6** → use `seedance-video-prompt` to compile storyboard blueprint images + character references into Seedance 2.0 executable video prompts

---

## Integration

When called by `director-core`:

- Load all STATE 1-3 upstream outputs (story, emotion, camera, lighting, character)
- Verify upstream output completeness
- Compile the complete film-level short film prompt package
- Execute the verification checklist (including output boundary check)
- Present for final user review
- Upon confirmation, mark STATE 4 complete, unlock STATE 5
