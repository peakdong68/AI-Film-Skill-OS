---
name: seedance-video-prompt
description: 将图像、视频、音频等多模态参考编译为 Seedance 2.0 / Runway / Sora / Kling 视频平台可执行的视频生成提示词。支持七种生成模式（T2V / I2V minimal / I2V storyboard / R2V / FLF2V / V2V Edit / V2V Extend），按可用参考资源自动选择。分镜图像不是必须的——仅在 storyboard 驱动模式下需要。这是 AI Film OS 管线中 L5 视频生成层的最终编译器。用于生成 Seedance 2.0 提示词、视频生成提示词，或 director-core 路由到 STATE 6 时。触发词：Seedance 2.0 提示、视频生成提示词、Seedance prompt、video generation prompt、I2V、首帧尾帧、FLF2V。
---

# Seedance Video Prompt — L5 Video Generation Compiler

## Overview

This is the final compiler of **L5 — VIDEO GENERATION LAYER** in the AI Film OS pipeline. It receives visual references (storyboard images, character images, product images, background images, first/last frame images, video clips, audio clips) and compiles them into executable video generation prompts for Seedance 2.0 / Runway / Sora / Kling platforms.

**Key Distinction:**
- `director-prompt-packager` (STATE 4): Text-level compiler → produces a film-level short film prompt package. **Not a video platform prompt.**
- `seedance-video-prompt` (STATE 6): Image-reference-level compiler → produces platform-executable video prompts.

**Critical: Storyboard frame images are NOT mandatory.** They are one mode (storyboard-driven I2V). The compiler supports seven modes, each with different input requirements.

## Mode Gate

Choose the mode BEFORE drafting. Each mode has different input requirements. **Storyboard images are only required for storyboard-driven I2V mode.**

| Mode | Required Inputs | Optional Inputs | What the prompt does |
|---|---|---|---|
| **T2V** | Text description (subject, action, scene, camera, light, style) | None | Build the whole shot from text only |
| **I2V (minimal)** | `@[Image1]` — product/character/scene reference | Background ref, audio ref | Preserve visible identity; add only motion, camera, light changes, sound |
| **I2V (storyboard)** | `@[Storyboard]` — storyboard blueprint images | Character ref, product ref, background ref, audio ref | Drive continuous camera movement through storyboard panels |
| **R2V** | Multiple refs: image(s) + optional video/audio | — | Assign independent roles to each asset; declare what must NOT transfer |
| **FLF2V** | `@[Image1]` first frame + `@[Image2]` last frame | Audio ref | Generate continuous transition from first frame to last frame target |
| **V2V Edit** | `@[Video1]` source clip | — | Preserve source clip; change only one layer (lighting, background, VFX) |
| **V2V Extend** | `@[Video1]` previous clip | — | Continue from the existing final state; change one variable |

### Mode Decision Tree

```
User has storyboard images? → I2V (storyboard)
User has single reference image only? → I2V (minimal)
User has first + last frame images? → FLF2V
User has multiple different ref types? → R2V
User has video source to modify? → V2V Edit
User has video to continue? → V2V Extend
User has text description only? → T2V
```

## Director Formula

```
Subject + Action + Scene + Camera + Lighting/Style + Audio + Constraints
```

Put the subject and primary action first — early clauses set the shot hierarchy. Do not force every slot if a reference asset already shows the information. For all I2V/FLF2V modes: describe only the motion, camera, timing, transformation, audio, and preservation constraints that the still image cannot show.

| Slot | Use for | Prompt-ready pattern |
|---|---|---|
| Subject | The anchor the model must track. | `Original ceramic perfume bottle on black acrylic, label preserved exactly` |
| Action | The visible change. | `condensation beads form and slide down the glass over five seconds` |
| Scene | Only what is not already in references. | `quiet rain-lit kitchen counter, shallow depth of field` |
| Camera | One primary move with endpoint. | `slow dolly-in from medium product shot to macro label detail` |
| Light/Style | Physical light plus safe visual language. | `warm practical key from frame left, cool blue rim, clean commercial realism` |
| Audio | Ambient bed, SFX, dialogue, or silence. | `Sound: low room tone, soft glass chime on final frame` |
| Constraints | Preservation and exclusions. | `do not alter logo, shape, label, or cap geometry` |

## Platform Hard Constraints

### Prompt Word Count Limits

| Language | Limit | Rationale |
|---|---|---|
| **Chinese** | ≤ 500 characters | Excess characters scatter information; the model ignores details |
| **English** | ≤ 1000 words | Same as above |
| **Total characters** | ≤ 2000 characters | Platform budget |

**Violating this constraint will cause missing video elements, character drift, and incomplete motion.** After compilation, count and annotate the character/word count.

### @[ref] Reference Format

All uploaded image/video/audio assets use the `@[description]` format:

| Reference Example | Purpose |
|---|---|
| `@[storyboard image 1]` | Storyboard blueprint — motion planning reference |
| `@[character image 1]` | Character identity lock — face, hair, body type |
| `@[product image 1]` | Product lock — color, print, fit |
| `@[background image 1]` | Environment lock — space, light, color tone |
| `@[Image1]` / `@[图1]` | Generic image reference (I2V minimal mode) |
| `@[Video1]` | Motion/camera/pacing reference (V2V / R2V) |
| `@[Audio1]` | Rhythm/tempo/mood reference |

## Per-Mode Templates

### Mode 1: I2V Minimal Preservation

For single reference images — product shots, character portraits, scene stills. **Only describe what the image cannot convey.**

**Template (Chinese):**
```
@[图1] 为参考；精确保留 [身份/产品/场景]。仅 [运动] 发生变化。
镜头：[单一运镜]。光影：[光源或过渡]。音效：[提示音]。
约束：[禁止变更的内容]。
```

**Template (English):**
```
[Image1] as reference, strictly preserve [identity/product/scene].
Only [motion] changes. Camera: [one movement]. Light: [source or transition].
Sound: [cue]. Constraints: [what must not change].
```

**Example — Product:**
```
@[图1] 为产品参考；精确保留瓶身标签、Logo、瓶型、颜色不变。
仅水珠凝结并沿玻璃滑落。镜头：锁定中景产品镜头，缓慢推近。
光影：左侧暖光条扫过标签表面。音效：低环境音 + 结尾一声清脆玻璃音。
字数：96 字 ✅
```

**Example — Character:**
```
@[图1] 为角色参考；精确保留面部结构、发型、外套不变。
仅眼睛缓慢眨一次，视线微微下移。镜头：锁定中近景，无重新取景。
光影：柔和的窗户自然光。音效：安静的房间底噪。
```

### Mode 2: I2V Storyboard-Driven

For storyboard blueprint images. The storyboard drives continuous camera movement through panels.

```
Seedance 2.0 Prompt:

Use @[storyboard image 1] as the authoritative shot blueprint. Do not render the storyboard itself. Ignore all borders, panel frames, text, labels, titles, color swatches, director bar graphics, and layout elements. Treat each panel as a continuous cinematic beat.
The entire video must play as one continuously developing master shot with no visible cuts; each panel is a sampled stage of the same uninterrupted camera movement, not a separate shot.
Use one virtual lens / same lens continuous camera movement; scale changes come only from physical camera movement.
Use @[character image 1] as the authoritative character reference.

[If multi-character or product references exist, add role mapping declarations here]

Music: [music style, BPM, mood]

1. [Opening shot corresponding to panel 1 — establish space and initial state]
2. [Motion stage corresponding to panel 2 — character action or environment change]
3. [Motion stage corresponding to panel 3 — continuing progression]
...
N. [Closing shot corresponding to panel N — emotional landing point]

No subtitles, no watermarks, no brand logos.
No facial distortion, no identity drift, no character face swaps.
No scene drift, no spatial reset, no environment jumps.
No new characters appearing, no extra figures.
[Scene-specific constraints]
```

**Role mapping declarations (include when applicable):**
```
@[character image 1] controls character identity — strictly preserve the same character's core features, natural face.
@[product image 1] controls product identity — strictly lock color, print pattern, print color, size, position, fit.
@[background image 1] controls environment — strictly preserve spatial structure, lighting, color tone, and display stability.
```

### Mode 3: R2V Multi-Reference

Assign independent roles to each asset. Explicitly declare what transfers and what must not.

**Template (Chinese):**
```
@[图1] 控制产品身份。[视频1] 仅控制运镜速度。[音频1] 仅控制节奏。
保留来自 @[图1] 的主体；请勿从 @[视频1]/@[音频1] 复制角色、Logo、音乐、人声或环境。
```

**Template (English):**
```
[Image1] controls product identity. [Video1] controls camera pace only. [Audio1] controls tempo only.
Preserve the subject from [Image1]; do not copy characters, logos, music, voice, or environment from [Video1]/[Audio1].
```

**Example — Multimodal Reference:**
```
@[产品图1] 控制产品身份——严格锁定瓶身标签、Logo、形状、颜色、瓶盖几何形态。
@[视频1] 仅控制侧向平移的摄影机节奏；不复制表演者、房间、品牌或服装。
@[音频1] 仅控制节奏和能量。

角色穿过湿漉漉的站台，在一盏闪烁的招牌下停住，最后向左转头。
镜头：35mm 锁定中全景，一次缓慢侧向平移。
音效：雨声 + 脚步声，无音乐。
```

### Mode 4: FLF2V First/Last Frame

Generate continuous transition from first frame to last frame target.

**Template:**
```
[Image1] is the first frame. [Image2] is the last frame.
Preserve the same [subject/character/product], [outfit/logo/shape], and scene layout.
Generate a continuous transition from [starting state] to [ending state].
Motion: [one physical action path].
Camera: [one controlled move or locked frame].
Lighting: [source and continuity].
Sound: [ambience/dialogue/SFX/music/silence].
Constraints: no new text, no watermark, no identity change, no object redesign.
```

**Example — Character:**
```
[Image1] 为首帧。[Image2] 为尾帧。
保持同一角色面部结构、发型、外套和房间布局不变。
生成从坐姿到站姿的连续过渡：角色从椅子缓慢起身，走向窗户，停在最终姿势。
镜头：锁定中景，轻微推近。光影：相同冷窗光，结尾暖台灯光。
音效：安静房间底噪 + 轻柔地板吱嘎声。
```

**Common FLF2V Failures:**
| Failure | Repair |
|---|---|
| Subject morphs | Lock only the identity anchors that matter; remove extra style changes |
| Product/logo redraws | Use locked camera and say only light/weather moves |
| Jump cut | Add "continuous transition" and one physical action path |
| Camera chaos | Replace multiple moves with locked frame or one slow push-in |
| Ending misses target | State that `[Image2]` is the final visual target, not just mood reference |

### Mode 5: T2V Text-to-Video

Build complete shot from text only — no reference images.

**Template:**
```
[Subject] + [Action] + [Scene]. Camera: [one primary move]. Lighting: [source and quality].
Sound: [ambience/SFX]. Constraints: [exclusions].
```

### Mode 6: V2V Edit

Preserve the source clip while changing one layer.

**Template:**
```
[Video1] is the source clip; preserve composition and timing, change only [lighting/background/VFX].
Do not change subject identity, clothing, background layout, or motion rhythm.
```

### Mode 7: V2V Extend

Continue from the existing final state.

**Template:**
```
[Video1] is the previous clip; continue the same shot for [duration] and preserve last-frame continuity.
The [subject] completes [one continuing action]. Camera remains [locked/same move].
Lighting and layout stay continuous.
```

## @[ref] Role Mapping

Before writing prompts, assign a **unique primary role** to each uploaded asset. Role mapping prevents accidental cross-contamination between identity, logo, scene ownership, and camera instructions.

| Asset | Recommended Role | Avoid |
|---|---|---|
| Image | identity, product, pose, costume, environment, first frame, last frame | Asking it to define unseen motion |
| Video | motion, camera, pacing, blocking, timing, gesture rhythm | Copying protected identity, logo, or scenes |
| Audio | rhythm, tempo, mood, ambience, delivery tone, music texture | Assuming voice/song/portrait rights are cleared |

**Core Rules:**
- Each referenced asset gets one primary role; do not layer additional style descriptions on top
- Explicitly declare "what must be preserved" and "what must not transfer"
- If authorization is unclear, only transfer generalized motion/rhythm/mood/production function, not protected identity
- When audio and video references compete: make video silent when audio timing must dominate, or state that video controls camera/motion only and `[Audio1]` controls tempo

## I2V Core Principles

**Only describe what the image cannot convey.** A static image already contains subject identity, product form, clothing, color palette, composition, background. Re-describing these static details typically causes drift. Only add to the image: motion, camera, time progression, lighting changes, sound, preservation constraints.

| Good I2V Addition | Example |
|---|---|
| Micro-expression | `subject blinks once and lowers their eyes` |
| Product light sweep | `thin highlight travels across the label` |
| Weather | `rain streaks behind the subject; droplets bead on the surface` |
| Camera | `slow dolly-in from current composition to tighter detail` |
| Atmosphere | `dust catches the doorway beam and settles` |
| Audio | `soft room tone, one key click at the endpoint` |

**Common I2V Failure Fixes:**
| Failure | Fix |
|---|---|
| Identity drift | Reduce new visual descriptions, strengthen preservation constraints |
| Camera jumps | Use one camera movement, note start and end frames |
| Product deformation | Declare preserved, static identity, no shape change |
| Static image | Add one physical action and one temporal cue |
| Background change | Preserve environment layout, only animate lighting/weather/atmosphere |
| Hand deformation | Simplify hand motion or exclude hands from the main action |

## Compression Rules

When prompts are too long, trim in this order:

1. **Delete**: repeated style adjectives, generic quality words, background details already visible in references, secondary camera movements, secondary actions, speculative emotion labels
2. **Keep**: reference tags and their roles, subject/product identity, one action verb + visible endpoint, one camera movement, physical light source or atmosphere, sound cue, safety/IP/continuity constraints

**Compressed Chinese I2V Template:**
```
@[图1]为参考，严格保持[主体]不变；仅加入[动作/光线/镜头]。声音：[提示]。约束：[不变项]。
```

## Anti-Slop Lexicon

Replace hollow evaluation words with observable production language:

| Hollow Word | Replace With |
|---|---|
| cinematic | shot size + camera movement + lighting + color grading |
| epic | physical scale + stakes + lens distance |
| beautiful | color + texture + composition + material + light behavior |
| stunning | visible contrast + reveal + motion + detail |
| dynamic | specific motion + speed + endpoint |
| dramatic | blocking + shadow + silence + camera pressure |
| ultra-realistic | material performance + skin texture + lens characteristics + natural motion |

**Rule: If a camera, microphone, light meter, or stopwatch cannot detect it — rewrite.**

## Common Scenario Adaptations

### Fashion / Apparel Videos
- Role mapping is mandatory: `@[product image 1]` locks color/print/fit
- Fabric dynamics (folds, sway) must be described
- Back constraint: solid color, no print, no text
- Music: lo-fi hip-hop / chill trap, BPM 90-110
- **Compactness: prioritize Chinese compression, within 500 characters**

### Product Showcase Videos
- Product image locks appearance, background image locks environment
- Camera: push-in / orbit / detail, **one primary movement**
- **Key principle: let light/particles/camera move around the product, not deform the product itself**

### Narrative Short Films
- Character image locks identity, storyboard image (if used) locks narrative pacing
- Continuous camera movement throughout the film
- Emotion evolves, never resets
- **One segment = one beat = one emotional turn**

### Multi-Character Scenes
- Each character gets a separate `@[character image N]` reference + role mapping
- Declare spatial relationships between characters remain unchanged
- No character identity swapping or drift

## Validation Checklist

Before delivering the final prompt, verify item by item:

- [ ] Mode is explicitly declared and correct for the available inputs
- [ ] **I2V modes**: storyboard image declaration is correct ONLY if storyboard-driven mode
- [ ] **I2V minimal / FLF2V**: "only describe what the image cannot show" is followed
- [ ] Role mapping is declared for ALL reference assets
- [ ] Each @[ref] has one primary role, no layered style descriptions
- [ ] "What must preserve" and "what must not transfer" are both declared (R2V mode)
- [ ] For storyboard-driven I2V: "do not render the storyboard itself" is declared
- [ ] One primary camera movement is used, not stacked multiples
- [ ] Music style and BPM are specified (or silence is declared)
- [ ] Fabric/hair dynamics described (if applicable)
- [ ] Back constraint declared (if applicable)
- [ ] Negative constraint list is complete
- [ ] **Word count compliant: Chinese ≤ 500 characters / English ≤ 1000 words (count annotated)**
- [ ] **Anti-slop check: no hollow evaluation words with no physical referent**
- [ ] Prompt can be directly pasted into the target platform for use

## Integration with director-core

When called by `director-core` at STATE 6:

1. **Check what inputs are available** — DO NOT assume storyboard images exist
2. Determine the appropriate mode based on available inputs (see Mode Decision Tree)
3. If in storyboard-driven mode: confirm storyboard images are available
4. If in other modes: accept whatever references the user provides
5. Load all visual reference assets
6. Assign @[ref] role mapping for each asset
7. Compile executable prompts per the selected mode template
8. Count and annotate character/word count (Chinese ≤ 500 characters)
9. Execute validation checklist
10. Present for final user review
11. Upon confirmation, mark STATE 6 complete
