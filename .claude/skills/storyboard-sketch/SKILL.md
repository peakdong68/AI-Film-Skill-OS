---
name: storyboard-sketch
description: Create concise, clean rough-sketch storyboard prompts from scene ideas, scripts, beats, or visual concepts for Seedance image-to-video workflows. Use when the user asks for a storyboard, preview board, animatic planning, animation shot plan, keyframe board, rough visual frames, first-frame prompts, shot-by-shot sketch prompts, or a quick board to guide Seedance I2V generation. Also use when the user asks for a storyboard master sheet, shot list board, director treatment board, 分镜总览图, 导演分镜板, 故事板规划, or a full visual planning board for film/TV/ad/animation pre-production.
---

# Seedance Storyboard Sketch

## Overview

Turn a scene idea, script, or concept into a storyboard plan for Seedance image-to-video. This skill supports two output modes, selected automatically by the Mode Gate below:

- **Compact Frame Prompts** (default): 3-8 concise rough-sketch frame prompts optimized for Seedance I2V seed images.
- **Storyboard Master Sheet** (on request): a full visual planning board with shot grid, rhythm timeline, camera movement diagram, and visual language design — suitable for director treatment, campaign pitch, or pre-production blueprint.

Favor clarity, continuity, and sketchability over polished cinematic prose in both modes.

## Mode Selection Gate

Before generating output, decide which mode to use:

| If the user says... | Use this mode |
|---|---|
| "分镜草图", "keyframe prompts", "I2V storyboard", "shot-by-shot prompts", "quick preview board", "rough visual frames", or any Seedance-focused prompt request | **Compact Frame Prompts** |
| "分镜总览图", "Master Sheet", "导演分镜板", "shot list board", "director treatment board", "storyboard planning board", "完整分镜规划", or explicitly asks for a full visual planning layout | **Storyboard Master Sheet** |

When the user provides a multi-panel board image: identify whether it's ≤4 panels (treat as Compact Frame Prompts) or ≥5 panels (treat as source for Master Sheet structure).

When uncertain, default to Compact Frame Prompts but mention the Master Sheet option briefly.

---

# Mode A: Compact Frame Prompts

## Workflow

1. Run the Input Gate before writing any frame prompts.
2. Identify the scene goal, characters, location, emotional beat, references, target mode, aspect ratio, and intended output length.
3. Convert the idea or script into a compact storyboard plan: 3-8 frames unless the user specifies a count.
4. For each frame, define one readable visual moment including: subject, action, composition, camera angle, lighting mood, story purpose, and continuity notes.
5. Write each frame as a rough sketch prompt, not a final video prompt.
6. Add a short Seedance I2V note for how the frame should animate into the next moment.

Ask one concise question only when missing information would materially change the board, such as the target aspect ratio, number of frames, or whether the board should be realistic, anime, ad-like, or cinematic.

## Input Gate

Before generating storyboard sketch prompts, decide whether the user has already provided enough scene material to convert into a compact storyboard plan.

Treat the input as sufficient when it includes at least:

- A core scene idea, script, beat list, or image/video reference.
- A subject or character.
- A situation, location, or action.
- A desired use, such as Seedance I2V, preview board, animatic, or shot planning.

If sufficient, proceed directly and state any light assumptions inside "Storyboard Setup".

If insufficient, infer a draft brief from available context before asking the user. Use conversation context, provided files, project names, existing prompt text, uploaded images, or nearby project materials when available. Then ask the user to confirm or correct the brief before generating frame prompts.

Use this confirmation format:

```markdown
我先确认一下分镜基础：
- 场景核心：[inferred or missing]
- 主体/角色：[inferred or missing]
- 地点/情境：[inferred or missing]
- 输出目标：Seedance image-to-video storyboard sketch
- 建议规格：[aspect ratio, frame count, style]

确认这些方向吗？也可以直接改一句，我再生成分镜草图提示词。
```

If the request is urgent or the user explicitly says "直接生成", proceed with reasonable assumptions and mark them clearly.

## Output Format

Use this structure by default:

```markdown
**Storyboard Setup**
- Aspect ratio:
- Visual style:
- Scene context: [one-line scene description — time, location, environment]
- Continuity anchors: [character wardrobe, key props, geography, screen direction]

**Frame 1 - [short beat name]**
Sketch prompt: [one clean prompt for a rough storyboard image]
Scene: [time · location · environment context for this beat]
Composition: [shot size, camera angle, framing]
Lighting & Mood: [key light, atmosphere]
I2V motion note: [one sentence describing the motion into or within this beat]
Story purpose: [what this shot communicates — reveal, tension, transition, establish, etc.]
Continuity: [what must remain consistent]

**Frame 2 - [short beat name]**
...
```

Repeat the frame block for each shot. End with a compact "Board Notes" section only when useful.

### Field Guide

- **Sketch prompt**: The primary image-generation prompt. 25-60 words. Include subject, action, camera, composition, lighting cues, and rough-board style keywords. This is what gets fed to an image generator to produce the storyboard panel.
- **Scene**: Time, location, and environment context specific to this beat. Keeps the sketch prompt from needing to re-explain the setting.
- **Composition**: Shot size (see Quick Reference), camera angle, framing approach. Use plain terms like "wide shot", "over-shoulder", "low angle", "centered", "rule of thirds".
- **Lighting & Mood**: Key light direction and quality, color temperature, atmosphere. E.g. "warm rim light from window, soft fill, tense atmosphere".
- **I2V motion note**: How the Seedance image-to-video should animate this frame. Camera movement + subject movement + transition logic. One sentence.
- **Story purpose**: What narrative function this shot serves — e.g. "建立场景空间感", "揭示角色情绪转折", "强调产品质感", "为下一镜头制造悬念". This is the single most important addition from professional storyboard practice: every shot must have a clear narrative reason to exist.
- **Continuity**: What must remain identical to other frames — character identity, wardrobe, props, lighting direction, screen geography.

## Prompt Style

- Keep sketch prompts short: usually 25-60 words per frame.
- Use simple physical language: "wide shot", "over-shoulder", "low angle", "profile", "center frame", "foreground silhouette".
- Specify rough-board aesthetics: pencil sketch, grayscale marker, loose storyboard lines, clean thumbnail composition, no finished rendering.
- Include only the objects and expressions needed to understand the beat.
- Preserve character identity, wardrobe, props, geography, and screen direction across frames.
- Prefer visible action over abstract mood words.
- Use plain composition cues instead of bloated cinematic adjectives.

## Seedance Workflow Alignment

Follow the Seedance operating pattern without becoming a full production prompt skill:

- Intake first: clarify goal, duration, aspect ratio, references, deliverable, and safety/IP risks when relevant.
- Mode gate: assume this skill serves I2V planning unless the user says T2V, V2V, R2V, edit, or extend.
- Reference map: if assets exist, assign each one a role such as identity, first frame, environment, motion, camera, timing, or style. State what should not transfer.
- Long-form logic: for videos over 15 seconds, produce a storyboard plan and note that final Seedance generation should be split into shots or segments.
- Storyboard-board input: if the user provides a multi-panel board, first identify whether it is ≤4 panels for one timestamped Seedance prompt or ≥5 panels for separate per-shot prompts plus editing rhythm.
- Quality pass: check every frame has one visible beat, one primary camera setup, continuity anchors, and an I2V motion note.

## Seedance I2V Notes

For each frame, include a motion note that helps a still storyboard become a Seedance image-to-video seed:

- Camera movement: static hold, slow push-in, lateral track, gentle tilt, handheld drift.
- Subject movement: turn, step, reach, glance, pause, reveal, react.
- Transition logic: match action, eye-line match, push through foreground, cut on gesture.
- Avoid asking one frame to contain multiple time-separated actions.

## Example — Compact Frame Prompts

User idea: "A courier discovers the package is ticking in a rainy alley."

```markdown
**Storyboard Setup**
- Aspect ratio: 16:9
- Visual style: rough grayscale storyboard sketch, clean readable thumbnails
- Scene context: Midnight, narrow back alley, heavy rain, wet brick walls
- Continuity anchors: red courier jacket, wet alley bricks, small black package

**Frame 1 - Alley Arrival**
Sketch prompt: Wide shot, rainy narrow alley at night, courier in a red jacket enters from screen left holding a small black package, wet brick walls, simple pencil lines, clear silhouette.
Scene: Midnight · narrow alley · rain on brick
Composition: Wide shot, eye level, leading lines from alley walls
Lighting & Mood: Street lamp top light, blue ambient, tense
I2V motion note: Slow lateral track follows the courier walking deeper into the alley.
Story purpose: 建立场景空间和角色进入状态
Continuity: Courier keeps the package in the right hand.

**Frame 2 - The Sound**
Sketch prompt: Medium close shot, courier stops under a dim wall lamp and tilts the package toward one ear, rain streaks behind, anxious face, loose storyboard shading.
Scene: Same alley · under wall lamp
Composition: Medium close-up, eye level, centered on face and package
Lighting & Mood: Overhead lamp as key, rain reflections on face, suspenseful
I2V motion note: Static hold with a small head turn as the courier hears the ticking.
Story purpose: 揭示危机信号，建立悬疑转折
Continuity: Same red jacket, same package size and orientation.
```

---

# Mode B: Storyboard Master Sheet

## When to Use

Trigger this mode when the user asks for a visual planning board, not just individual frame prompts. This mode produces a structured description that can be fed into an image generator to create a single comprehensive storyboard sheet — useful for director pitches, campaign proposals, and pre-production visualization.

The Master Sheet follows a four-section structure derived from professional film/TV/advertising storyboard practice.

## Master Sheet Structure

```markdown
**Master Sheet Setup**
- Project: [project name or theme]
- Aspect ratio: [typically 16:9 for landscape boards]
- Style: [director treatment board, clean infographic, professional production document]
- Total shots: [6-18 recommended, auto-adjusted based on content]

## Section 1: Shot Grid (分镜展示区)

[Grid layout of all shots. Each shot card contains:]

| # | Shot Size | Timecode | Frame Preview | Action | Camera | Purpose |
|---|-----------|----------|---------------|--------|--------|---------|
| 01 | WS | 00:00-00:02 | [one-line visual description] | [subject action] | [camera setup] | [story purpose] |
| 02 | MS | 00:02-00:04 | ... | ... | ... | ... |
...

## Section 2: Rhythm & Structure (节奏设计区)

Narrative arc:
[Calm] → [Build] → [Tension/Emphasis] → [Peak/Climax] → [Release/Resolution]

Shot distribution by phase:
- Phase 1 (Establish): Shots 01-02 — [what happens]
- Phase 2 (Develop): Shots 03-04 — [what happens]
- Phase 3 (Emphasize): Shots 05-06 — [what happens]
- Phase 4 (Climax): Shots 07-08 — [what happens]
- Phase 5 (Resolve): Shots 09-10 — [what happens]

Rhythm density: [calm → accelerating → peak → decelerating]
Music beat alignment: [key beat points and which shots they land on]

## Section 3: Camera Movement Diagram (运镜设计区)

Top-down layout:
- Camera positions marked by shot numbers (① ② ③ ...)
- Movement trajectories shown as dashed arrows
- Movement types per shot: [Static / Push-in / Lateral track / Orbit / Handheld / etc.]

## Section 4: Visual Language (视觉设计区)

Lighting design: [key light, fill, rim, color temp, atmosphere per phase]
Color palette: [warm/cool/neutral, dominant colors, contrast level]
Composition style: [rule of thirds, centered, leading lines, negative space, symmetry]
Mood keywords: [3-5 words capturing the overall emotional tone]
Art direction notes: [key visual references, texture, production design intent]
```

## Narrative Progression Templates

When building a Master Sheet, adapt the narrative arc to the content type. Select and fill in:

**Film / Drama:**
```
世界观建立 → 人物发展 → 冲突升级 → 高潮爆发 → 结局
```

**Advertising / Commercial:**
```
场景建立 → 产品展示 → 卖点强化 → 情绪高潮 → 品牌收尾
```

**E-commerce / Product:**
```
建立氛围 → 整体展示 → 细节特写 → 使用场景 → 转化收尾
```

**Documentary / Explainer:**
```
背景介绍 → 内容展开 → 重点分析 → 观点强化 → 总结结束
```

**Short Video / Social:**
```
Hook抓眼球 → 问题呈现 → 解决方案 → 效果展示 → CTA引导
```

## Master Sheet Example

User request: "做一个高端腕表品牌广告的分镜总览图，6个镜头"

```markdown
**Master Sheet Setup**
- Project: 高端腕表品牌广告
- Aspect ratio: 16:9
- Style: director treatment board, clean infographic, luxury commercial storyboard
- Total shots: 6

## Section 1: Shot Grid

| # | Shot Size | Timecode | Frame Preview | Action | Camera | Purpose |
|---|-----------|----------|---------------|--------|--------|---------|
| 01 | ECU | 00:00-00:02 | 表盘微光闪动, dark void background | 光在表盘上缓缓移动 | Static macro | 制造悬念,建立奢华基调 |
| 02 | CU | 00:02-00:04 | 表冠与表链连接处的精钢质感 | 极慢旋转展示金属拉丝纹理 | Slow orbit | 展示工艺质感 |
| 03 | WS | 00:04-00:06 | 腕表置于大理石基座, 柔光环境 | 水滴落在表镜上弹开 | Top-down static | 强化品质感和防水特性 |
| 04 | MCU | 00:06-00:08 | 模特手腕佩戴, 西装袖口 | 手腕自然抬起看表 | Gentle push-in | 建立佩戴场景和身份感 |
| 05 | MS | 00:08-00:10 | 模特在落地窗前, 城市夜景背景 | 转身面向窗外, 表盘反光 | Slow dolly back | 融入生活方式场景 |
| 06 | CU | 00:10-00:12 | 品牌Logo与表盘同框 | 定格, 光晕收拢到Logo | Static hold | 品牌收尾,强化记忆 |

## Section 2: Rhythm & Structure

Narrative arc: Mysterious → Elegant → Impressive → Aspirational → Iconic

- Phase 1 (Mystery): Shots 01 — 制造悬念
- Phase 2 (Detail): Shots 02-03 — 工艺展示
- Phase 3 (Lifestyle): Shots 04-05 — 场景代入
- Phase 4 (Brand): Shot 06 — 品牌收尾

Rhythm density: slow → steady → gentle peak → hold
Music beat: 舒缓弦乐起 → 02处轻鼓点 → 04处旋律推进 → 06处收束

## Section 3: Camera Movement Diagram

Top-down: ①(正上方) → ②(右环绕) → ③(正上方) → ④(正面推近) → ⑤(后退) → ⑥(静止)

Movement types: Static → Slow orbit → Static → Push-in → Dolly back → Hold

## Section 4: Visual Language

Lighting design: 柔光主光源, 黑色背景吸收光, 金属高光点缀, 城市暖色夜景
Color palette: 黑/金/银 为主, 暖白点缀, 低饱和高级感
Composition style: 居中构图为主, 01用负空间, 04用三分法
Mood keywords: 奢华 / 克制 / 精密 / 优雅 / 永恒
Art direction notes: 避免过度炫光, 强调材质真实感, 金属拉丝纹理清晰
```

---

# Quick Reference

## Shot Size 景别速查

| Code | Name | 中文 | Use |
|------|------|------|-----|
| EWS | Extreme Wide Shot | 超远景 | Establish vast environment |
| WS | Wide Shot | 全景/远景 | Full body in environment |
| FS | Full Shot | 全身 | Full figure, head to toe |
| MLS | Medium Long Shot | 中全景 | Knees up |
| MS | Medium Shot | 中景 | Waist up |
| MCU | Medium Close-Up | 中特写 | Chest up |
| CU | Close-Up | 特写 | Face or product detail |
| ECU | Extreme Close-Up | 超特写 | Eyes, texture, small detail |
| OTS | Over-Shoulder | 过肩 | From behind, showing subject |
| POV | Point of View | 主观视角 | Through character's eyes |

## Camera Movement 运镜速查

| Type | 中文 | Behavior |
|------|------|----------|
| Static | 定镜 | No movement, locked frame |
| Push-in | 推 | Camera moves toward subject |
| Pull-out | 拉 | Camera moves away from subject |
| Pan | 摇 | Horizontal rotation on axis |
| Tilt | 俯仰 | Vertical rotation on axis |
| Dolly/Track | 移/轨道 | Camera physically moves laterally |
| Crane | 升降 | Camera rises or lowers |
| Orbit | 环绕 | Circular movement around subject |
| Handheld | 手持 | Slight natural shake |
| Steadicam | 稳定器 | Smooth floating movement |
| FPV | 第一人称 | Drone-like dynamic movement |

## Camera Angle 机位角度速查

| Angle | 中文 | Effect |
|-------|------|--------|
| Eye Level | 平视 | Neutral, relatable |
| Low Angle | 仰拍 | Power, dominance, epic |
| High Angle | 俯拍 | Vulnerability, overview |
| Bird's Eye | 鸟瞰 | God-like perspective, map view |
| Dutch Angle | 斜角 | Unease, disorientation |
| Profile | 侧面 | Observation, silhouette |

## Composition 构图速查

| Type | 中文 | When to use |
|------|------|-------------|
| Rule of Thirds | 三分法 | Balanced, natural framing |
| Centered | 居中 | Emphasis, symmetry, product focus |
| Leading Lines | 引导线 | Depth, draw eye to subject |
| Symmetry | 对称 | Order, formality, architecture |
| Negative Space | 负空间 | Isolation, minimalism, breathing room |
| Frame Within Frame | 框中框 | Layers, voyeurism, focus |
| Foreground Silhouette | 前景剪影 | Depth, mystery |

## Lighting 光线速查

| Type | 中文 | Mood |
|------|------|------|
| High Key | 高调光 | Bright, optimistic, commercial |
| Low Key | 低调光 | Dark, dramatic, film noir |
| Rim Light | 轮廓光 | Separation, hero shot, product edge |
| Volumetric | 体积光 | Atmospheric, beams, god rays |
| Golden Hour | 黄金时刻 | Warm, nostalgic, natural beauty |
| Soft Diffuse | 柔光 | Gentle, flattering, beauty |
| Hard Light | 硬光 | Gritty, harsh, high contrast |
| Practical Light | 实景光 | Diegetic sources, realism |

## Narrative Purpose 叙事目的速查

| Purpose | 中文 | Typical shot |
|---------|------|--------------|
| Establish | 建立空间 | Wide/environment opening |
| Introduce | 引入角色 | Character entrance or reveal |
| Emphasize | 强化信息 | Detail close-up, product focus |
| Reveal | 揭示转折 | Key object discovery, emotion shift |
| Transition | 过渡衔接 | Bridge between scenes or beats |
| Build tension | 制造悬念 | Slow push, dark framing, off-screen sound |
| Release | 释放/收尾 | Resolution, brand tag, CTA |
| Contrast | 对比冲突 | Juxtaposition of scale, mood, or status |

---

## Quality Bar

- A reader should understand the whole scene by scanning frame titles and sketch prompts.
- Each prompt should be drawable as one storyboard panel.
- Every frame must have a clear story purpose — it answers "why this shot exists."
- The board should be useful even before final Seedance prompt writing.
- If the user asks for Chinese output, write all prompts in concise Chinese with the same structure.
- For Master Sheet mode, the four sections (Shot Grid, Rhythm, Camera, Visual Language) should form a coherent planning document, not just a list of shots.
