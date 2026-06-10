---
name: director-core
description: Master controller for the AI film production pipeline — manages the production state machine, enforces phase locks, maintains checkpoints, and routes tasks to director sub-skills in the correct order. Use this skill when users want to produce a complete AI film/video from a creative idea or script. Trigger scenarios: making an AI film, generating a video from a creative idea, directing a Seedance project, AI filmmaking, AI video production, AI director workflow, film production pipeline, or any multi-stage video creation request. Also triggers on any video/film production request, including e-commerce livestreams, product showcase videos, fashion videos, brand videos, product videos, fashion films, and commercial videos.
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
STATE 6 → Seedance 视频提示词（多模式，图像引用级）
STATE 7 → Final Validation
STATE 8 → Export Ready
```

Each state produces validated deliverables before the next state is unlocked. Skipping states is strictly prohibited.

**Key distinction between STATE 4 and STATE 6:**

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

Collect the minimum viable brief needed to produce the film. Only ask what is needed to begin:

- Project idea or script (at least one sentence)
- Target duration (15s / 30s / 60s / custom)
- Visual style (cinematic / commercial / documentary / anime / sci-fi, etc.)
- Delivery platform (Seedance / Kling)
- Aspect ratio (16:9 / 9:16 / 1:1)
- Any existing reference images or character descriptions

If the user provides fewer than 4 of these items, ask for the missing ones. If they say "just generate" or "just do it", fill with reasonable defaults and annotate.

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

- **Yes →** Route to `character-image-prompt` to compile definitions into platform-ready Character Sheet prompts (MJ/Flux/Jimeng/Kling). User then generates actual character reference images. These images serve as `@[character ref]` input for STATE 6, improving cross-shot identity consistency.
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

The output is **not** a Seedance video prompt — it is the design foundation for STATE 5 (storyboard blueprint generation) and STATE 6 (Seedance video prompts).

**Output Boundary (hard constraint):**

- STATE 4 output must **never** mention video platform names such as Seedance 2.0 / Kling
- Must not contain phrases like "generate in Seedance", "Seedance 2.0 prompt", "generate shot by shot in Seedance"
- All generation instructions must point to image generators (Jimeng/MJ/Flux/Kling image mode)

**Pre-flight Checklist (all must be YES):**

- [ ] Story structure confirmed?
- [ ] Emotional arc confirmed?
- [ ] Visual language (camera + lighting) defined?
- [ ] Character identity locked and confirmed?
- [ ] Duration and aspect ratio locked?
- [ ] **Output boundary compliant: no mention of Seedance / Kling?**

If any answer is NO, stop and return to the missing stage.

**State 4 output**: Film-level short film prompt package (text-level director's vision document). Proceed to STATE 5.

**User next step**: Confirm the prompt package content. After confirmation, proceed to STATE 5 to generate storyboard blueprint images.

### STATE 5 — Storyboard Blueprint Generation (Image Level)

Route to `storyboard-sketch` (for Seedance I2V rough sketches) or `storyboard-prompt` / `storyboard-master` / `storyboard-ecommerce` (for generating complete storyboard blueprint images).

**This is the image generation phase after STATE 4 confirmation.** Compiles the confirmed prompt package's storyboard design into AI image generator-executable storyboard blueprint prompts, generating visual storyboard board images. These images serve as `@[storyboard ref]` inputs for STATE 6.

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

**State 5 output**: Storyboard blueprint images (for Seedance `@[ref]` reference). Proceed to STATE 6.

### STATE 6 — Seedance 视频提示词（图像引用级）

路由到 `seedance-video-prompt`。

**这是 L5 视频生成编译器。** 根据可用参考资源选择生成模式（见下方模式选择），将参考图像/视频/音频编译为 Seedance 2.0 / Kling 平台可执行的视频提示词。

**分镜蓝图图像不是必须的——它只是 I2V storyboard 模式的一种输入。** 编译器支持七种模式：T2V / I2V minimal / I2V storyboard / R2V / FLF2V / V2V Edit / V2V Extend。

**平台硬约束：**

- 中文提示词 ≤ 500 字，英文提示词 ≤ 1000 词，总字符数 ≤ 2000
- 每个 @[ref] 必须分配唯一主角色（身份 / 产品 / 环境 / 动作节奏），使用角色映射声明格式
- 通过 anti-slop 检查：无空洞评价词（cinematic / epic / beautiful 等无物理指涉词汇）

**可用输入（按模式选择所需）：**

- 分镜蓝图图像（来自 AI 图像生成器）——仅 I2V storyboard 模式需要
- 角色参考图（推荐，用于身份锁定。如用户在 STATE 3 选择跳过，则以文本描述替代）
- 产品参考图（可选，用于产品锁定）
- 背景参考图（可选，用于环境锁定）
- 首帧/尾帧图像——仅 FLF2V 模式需要
- 视频片段——仅 V2V Edit/Extend 模式需要
- 音频片段（可选，用于节奏/氛围参考）

**模式选择（根据可用输入判断）：**

| 用户有... | 选择模式 |
|---|---|
| 分镜蓝图图像 | I2V (storyboard) |
| 仅单张参考图（产品/角色/场景） | I2V (minimal) |
| 首帧 + 尾帧图像 | FLF2V |
| 多种不同类型参考 | R2V |
| 视频源需要修改 | V2V Edit |
| 视频需要延续 | V2V Extend |
| 仅有文字描述 | T2V |

**预检清单（按模式验证）：**

- [ ] 所选模式的必需输入已就绪？
- [ ] 角色参考图可用？（或用户已明确选择跳过）
- [ ] 产品图已锁定（如适用）？
- [ ] 背景图已锁定（如适用）？
- [ ] 音乐风格和 BPM 已确定？
- [ ] **提示词字数合规（中文 ≤ 500 字）？**
- [ ] **anti-slop 检查通过？**

如有必需输入缺失，提示用户提供对应参考。

**State 6 输出**：Seedance 2.0 视频提示词（平台可执行）。进入 STATE 7。


### STATE 7 — Final Validation

Quality check on all deliverables:

- **Narrative check**: Does the complete sequence tell a coherent story?
- **Visual check**: Is the visual language consistent across all shots?
- **Character check**: Is character identity preserved in every prompt?
- **Continuity check**: Does spatial geography, lighting, and time flow feel continuous?
- **Execution check**: Can the Seedance prompts be used directly on the target platform?
- **Word count check**: Are Chinese prompts ≤ 500 characters?

**State 7 output**: Validated video prompts. Proceed to STATE 8.

### STATE 8 — Export Ready

Package final deliverables:

- Complete Seedance 2.0 prompts (in execution order)
- Image reference character mapping (which @[ref] corresponds to which image)
- Multi-Part generation context continuity notes
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
