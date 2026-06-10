# AI Film Skill OS — Skill System Documentation

## Overview

This project provides 13 Claude Code skills for AI video/film production, organized into two suites:

- **Storyboard Series (4)**: Generate storyboard image prompts for AI image generators and Seedance I2V
- **Director Series (9)**: Complete AI film production pipeline, from creative concept to executable video prompts

## Skill Map

```
                    ┌─────────────────────────┐
                    │     director-core         │
                    │  (State Machine · Phase  │
                    │   Locks · Orchestrator)  │
                    └──────────┬──────────────┘
           ┌─────────┬────────┼────────┬─────────┬──────────┬──────────────┬──────────────────┐
           ▼         ▼        ▼        ▼         ▼          ▼              ▼                  ▼
    director-    director-  director-  director-  director-  director-    character-       seedance-
     story       emotion    camera     light     character   prompt-       image-           video-
 (Script Struct) (Emotion)  (Camera)   (Lighting) (Char Lock) packager      prompt           prompt
                                                         (Prompt Package) (Char Img Prompt) (L5 Video Gen)

                  Storyboard Series (Standalone)
                  ┌─────────────────────────────┐
                  │ storyboard-sketch            │
                  │ Seedance I2V Storyboard Plan │
                  ├─────────────────────────────┤
                  │ storyboard-prompt            │
                  │ Single Frame Prompts → MJ/Flux/Jimeng │
                  ├─────────────────────────────┤
                  │ storyboard-master            │
                  │ Master Sheet → Director Board │
                  ├─────────────────────────────┤
                  │ storyboard-ecommerce         │
                  │ E-commerce/Livestream/Fashion │
                  └─────────────────────────────┘
```

## Director Pipeline (AI Film Production Workflow)

```
STATE 0   INPUT            Collect creative brief, duration, style, references
   │
STATE 1   STORY            Script structure + emotional arc
   │      (director-story + director-emotion)
   │      Output: Script Blueprint + Emotional Timeline
   ▼
STATE 2   VISUAL           Camera language + color script
   │      (director-camera + director-light)
   │      Output: Visual Language Blueprint
   ▼
STATE 3   CHARACTER        Character identity definitions
   │      (director-character)
   │      Output: Character Identity Definitions
   │
   ├──→ character-image-prompt  → Compile to image gen prompts → User generates character refs on MJ/Flux/Jimeng
   │
   ▼
STATE 4   PROMPT PKG       Compile to film-level short film prompt package (storyboard design + camera language + sound design + Seedance decomposition)
   │      (director-prompt-packager)
   │      Output: Film-Level Prompt Package → User confirms
   ▼
STATE 5   STORYBOARD       Generate storyboard blueprint images (can run parallel with character image gen)
   │      (storyboard-sketch / storyboard-prompt / storyboard-master / storyboard-ecommerce)
   │      Output: Storyboard Blueprint Images → for STATE 6 @[ref] inputs
   ▼
STATE 6   SEEDANCE         Compile to Seedance 2.0 video platform executable prompts
   │      (seedance-video-prompt)
   │      Input: generated storyboard images + character refs + product images
   │      Output: Seedance 2.0 / Kling Video Prompt
   ▼
STATE 7   VALIDATE         Quality verification
   ▼
STATE 8   EXPORT           Package deliverables
```

### Phase Locks

Each phase must pass verification before the next unlocks. Skipping is forbidden:

| Lock | Rule |
|------|------|
| Story Lock | Script structure must be confirmed before visual design |
| Visual Lock | Camera + lighting must be defined before prompt package compilation |
| Character Lock | Character identity must be confirmed before prompt package compilation |
| Package Lock | Prompt package must be user-confirmed before storyboard blueprint generation |
| Storyboard Lock | Storyboard blueprint must be confirmed before video prompt generation |
| Prompt Lock | All pre-checks must pass before final export |

## Skill Details

### director-core
- **Role**: Master orchestrator; does not generate content—routes and validates
- **Triggers**: AI film production, full video projects, multi-phase video creation
- **Routing**: Automatically invokes other Director skills per phase

### director-story
- **Role**: Script → director-grade narrative structure
- **Capabilities**: 3/5-act structure, scene purpose analysis, causal chain construction, director intent layer
- **Output**: Script Director Blueprint

### director-emotion
- **Role**: Design the audience's emotional journey
- **Capabilities**: Emotion curve, emotional beats, intensity scoring, emotion→visual mapping table
- **Output**: Emotional Blueprint

### director-camera
- **Role**: Camera language system design
- **Capabilities**: Shot type grammar, movement syntax, emotion→camera mapping, composition rules
- **Output**: Cinematography Blueprint

### director-light
- **Role**: Color script and lighting design
- **Capabilities**: Color Script, emotion→color mapping, lighting progression diagram, scene-specific palettes
- **Output**: Color & Lighting Blueprint

### director-character
- **Role**: Character identity definition and locking (prevents face drift / outfit changes)
- **Capabilities**: Face/hair/body/wardrobe 4-axis locking, emotion→action mapping, multi-layer locking system
- **Output**: Character Identity Definitions (text-level design document)
- **Note**: This skill produces character identity **definitions**, not image generation prompts. Image prompts are compiled by `character-image-prompt`

### character-image-prompt (NEW)
- **Role**: Character identity definitions → image generation platform executable prompts (MJ/Flux/Jimeng/Kling)
- **Capabilities**: 12-section character profile + multi-view character sheet image prompts + Negative Prompt
- **Input**: Character identity definitions from `director-character`
- **Output**: Copy-paste-ready character sheet prompts for image generation platforms

### director-prompt-packager
- **Role**: Text-level compiler — all STATE 1-3 design outputs → complete film-level short film prompt package
- **Capabilities**: Structured storyboard design + camera language specs + sound design direction + Seedance Part decomposition plan
- **Output**: Film-Level Prompt Package (Director's Vision Master Document; after user confirmation, proceeds to STATE 5 storyboard blueprint generation)
- **Note**: This is a text intermediate artifact, **NOT** a Seedance video prompt. Storyboard blueprint images are generated by STATE 5 after package confirmation

### seedance-video-prompt (NEW)
- **Role**: L5 video generation compiler — storyboard images + character refs → Seedance 2.0 executable prompts
- **Capabilities**: @[ref] image reference syntax, continuous long-take motion description, music tempo specification, negative constraints
- **Input**: Generated storyboard images + character reference images + product images
- **Output**: Seedance 2.0 / Kling platform-ready video generation prompts

---

### storyboard-sketch
- **Role**: Seedance I2V storyboard planning (text description)
- **Dual Mode**: Compact Frame Prompts + Storyboard Master Sheet
- **Output**: Text storyboard frame descriptions + I2V motion notes

### storyboard-prompt
- **Role**: Single-frame storyboard image prompts (→ MJ/Flux/Jimeng/Kling)
- **Framework**: 8 elements (Scene/Subject/Action/Camera/Composition/Lighting/Mood/Story Purpose)
- **Output**: Copy-paste-ready storyboard frame prompts for image generators

### storyboard-master
- **Role**: Storyboard master sheet / director treatment board (→ image generators)
- **Structure**: 4 zones (Shot Grid + Rhythm + Camera Movement + Visual Language)
- **Output**: Complete director treatment board prompt

### storyboard-ecommerce
- **Role**: E-commerce / livestream / fashion storyboard
- **Sub-modes**: Social Commerce Board + Fashion Director Board
- **Output**: E-commerce storyboard prompts with product reference zones + character reference zones

## Usage Scenario Routing

| What you want to do | Which skill to load |
|---------------------|---------------------|
| "I have a story idea, help me make an AI film" | `director-core` (auto-schedules full pipeline) |
| "Analyze this script's structure" | `director-story` |
| "Design this film's emotional curve" | `director-emotion` |
| "Design camera language and movement" | `director-camera` |
| "Design lighting style and color script" | `director-light` |
| "Create and lock character identity definitions" | `director-character` |
| "Compile character identity definitions into image prompts" | `character-image-prompt` |
| "Compile story+visuals+characters into a film prompt package" | `director-prompt-packager` |
| "Compile storyboard images + character refs into Seedance 2.0 video prompts" | `seedance-video-prompt` |
| "Generate storyboard blueprint for Seedance" | `storyboard-sketch` |
| "Write a storyboard frame prompt for MJ" | `storyboard-prompt` |
| "Create a director treatment board master sheet" | `storyboard-master` |
| "Create TikTok commerce video / fashion director storyboard" | `storyboard-ecommerce` |

## File Structure

```
.claude/skills/
├── director-core/SKILL.md + references/
├── director-story/SKILL.md + references/
├── director-emotion/SKILL.md + references/
├── director-camera/SKILL.md + references/
├── director-light/SKILL.md + references/
├── director-character/SKILL.md + references/
├── character-image-prompt/SKILL.md
├── director-prompt-packager/SKILL.md + references/
├── seedance-video-prompt/SKILL.md
├── storyboard-sketch/SKILL.md
├── storyboard-prompt/SKILL.md
├── storyboard-master/SKILL.md
└── storyboard-ecommerce/SKILL.md
```

## Key Design Principles

1. **No Phase Skipping**: Forbidden to jump from idea directly to Seedance prompts — must verify each phase
2. **Character Lockdown**: Face/hair/body/wardrobe 4-axis parameters must remain consistent across every frame
3. **Emotion-Driven**: Camera, lighting, and pacing choices must all have emotional justification
4. **Action-First**: AI video models need physical action descriptions, not emotion labels
5. **Continuity Binding**: Multi-part videos must reference the previous output as continuity baseline
6. **Three-Tier Compilation**: director-character(definition) → character-image-prompt(character image gen) + director-prompt-packager(prompt package) → storyboard-*(storyboard blueprint) → seedance-video-prompt(video)
7. **Definition/Prompt Separation**: Character and storyboard "definition documents" and "image generation prompts" are produced by different skills

## Knowledge Sources

- `reference/Director/` — AI Film OS complete architecture, core skill systems, engine specifications, modular rules
- `reference/Storyboard/` — Storyboard prompt specifications, master sheet design framework, e-commerce storyboard templates
- `reference/seedance-20/` — Seedance 2.0 operating system skill package (reference)
