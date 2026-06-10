# Seedance 2.0 Prompt Methodology — Bundled Reference

Load-on-demand reference for the `seedance-video-prompt` skill. Contains complete templates, failure fixes, compression rules, and scene adaptations.

---

## Complete Per-Mode Templates

### I2V Preservation

**Chinese:**
```
`图片1`为参考；精确保留[身份/产品/场景]。仅[运动]发生变化。
镜头：[单一运镜]。光影：[光源或过渡]。音效：[提示音]。约束：[不变项]。
```

**English:**
```
`Image1` as reference, strictly preserve [identity/product/scene].
Only [motion] changes. Camera: [one movement]. Light: [source or transition].
Sound: [cue]. Constraints: [what must not change].
```

**Example — Product:**
```
`Image1` as product reference; strictly preserve bottle label, logo, shape, color.
Only condensation beads form and slide down the glass. Camera: locked medium product shot, slow push-in.
Light: warm strip light sweeps left across the label. Sound: <crisp glass tick>.
Constraints: keep subtitle-free, no logos. Word count: 96 chars ✅
```

**Example — Character:**
```
`Image1` as character reference; strictly preserve facial structure, hairstyle, jacket.
Only eyes blink once slowly, gaze drops slightly. Camera: locked medium close-up, no reframing.
Light: soft window natural light. <quiet room tone>.
```

### I2V Storyboard-Driven

```
Use the storyboard in `Image1` as motion planning reference; do not render the storyboard itself.
Ignore all borders, panel frames, text, labels.
Define [character features] in `Image2` as `Subject1`.

Shot 1: [Panel 1 — establish space and initial state]
Shot 2: [Panel 2 — character action or environment change]
Shot 3: [Panel 3 — continuing progression]
...

(Play [music style] in background, BPM [range])

Constraints: keep subtitle-free, no logos, no watermarks.
No facial distortion, no identity drift, no scene jumps.
```

### R2V Multi-Reference Role Mapping

```
Define [features] in `Image1` as `Subject1`.
`Video1` controls camera rhythm only; do not transfer performer, room, brand, or costume.
`Audio1` controls tempo and energy only.

`Subject1` [action], [scene environment].
Camera: [movement]. Sound: [SFX]. Constraints: [what must not change].
```

**Example:**
```
Define the man in `Image1` wearing a black trench coat and sunglasses as `Subject1`.
`Video1` controls lateral tracking camera rhythm only; do not transfer performer, interior layout, or brand identity.
`Audio1` controls tempo and energy only.

`Subject1` walks across a wet train platform, stops under a flickering sign, and turns left on the final beat.
Camera: 35mm locked medium-wide, one slow side track.
<rain><footsteps>. (No music).

Constraints: keep subtitle-free, no logos, no watermarks.
```

### FLF2V First/Last Frame

```
`Image1` is the first frame. `Image2` is the last frame.
Preserve the same subject's facial structure, hairstyle, outfit, and scene layout.
Generate a continuous transition from [starting state] to [ending state].
Motion: [one physical action path]. Camera: [locked medium or one slow push-in].
Light: [source and continuity]. Sound: [ambience]. Constraints: [what must not change].
```

**Example:**
```
`Image1` is the first frame. `Image2` is the last frame.
Preserve `Subject1`'s facial structure, hairstyle, jacket, and room layout.
Generate a continuous transition from sitting to standing: `Subject1` slowly rises from the chair, walks to the window, and stops in the final pose.
Camera: locked medium shot, slight push-in. Light: same cool window light, warm lamp glow at end.
<quiet room tone><soft floor creak>.
```

### T2V Text-to-Video

```
[Subject] [action] in [scene]. Camera: [one primary movement].
Light: [source and quality]. Style: [tone]. Constraints: [exclusions].
```

### V2V Edit

```
Edit `Video1`, change [original feature] to [new feature].
Elements not mentioned remain unchanged by default.
Constraints: keep subtitle-free, no logos.
```

### V2V Extend

```
Extend `Video1` forward, [subject] continues [action].
Audio-visual style, subject, and narrative remain consistent.
Constraints: keep subtitle-free, no logos, no watermarks.
```

---

## Role Mapping

| Asset Type | Recommended Role | Avoid |
|---|---|---|
| Image | identity, product, pose, costume, environment, first frame, last frame | Asking it to define unseen motion |
| Video | motion, camera, pacing, blocking, timing | Copying protected identity, logo, or scenes |
| Audio | rhythm, tempo, mood, timbre, music texture | Assuming voice/song/likeness authorization |

**Core Rules:**
- Assign one primary role per reference; no stacking additional style descriptions
- Explicitly declare "what to preserve" and "what must not transfer"
- When authorization is unclear, transfer only broad motion/rhythm/mood, not protected identity
- Audio/video conflict: mute video or declare video controls camera/motion only

---

## I2V Failure Fixes

| Failure | Fix |
|---|---|
| Identity drift | Reduce new visual description, strengthen preservation constraints; place face ref first |
| Camera jumps | Use one camera movement, note start and end frames |
| Product deformation | Declare preserved static identity, no shape change |
| Output is static | Add one physical action and one temporal cue |
| Background changes | Preserve environment layout, animate only light/weather/atmosphere |
| Hand deformation | Simplify hand motion or exclude hands from main action |
| Twin problem | Define subjects with explicit binding; add constraint prohibiting identical duplicates |

---

## Compression Rules

When prompts are too long, trim in this order:

**Delete:** duplicate style adjectives → generic quality words → background details visible in refs → secondary camera moves → secondary actions → speculative emotion labels

**Preserve:** reference tags and roles → subject/product identity → action verb + visible endpoint → one camera move → physical light source or atmosphere → sound cue → safety/continuity constraints

**Compact Chinese I2V template:**
```
`图片1`为参考，严格保持[主体]不变；仅加入[动作/光线/镜头]。音效：[提示]。约束：[不变项]。
```

---

## Common Scene Adaptations

### Fashion / Apparel Videos
- Role mapping mandatory: `` `Image1` `` locks color/print/fit
- Fabric dynamics (folds, sway) must be described
- Back constraint: solid color, no print, no text
- Music: lo-fi hip-hop / chill trap, BPM 90-110
- Prioritize Chinese compression, within 500 characters

### Product Showcase Videos
- Product image locks appearance, background image locks environment
- Camera: push-in / orbit / detail, one primary movement
- **Let light/particles/camera move around the product — do not deform the product itself**

### Narrative Short Films
- Character image locks identity, storyboard image (if used) locks narrative pacing
- Emotion evolves, never resets
- One segment = one beat = one emotional turn

### Multi-Character Scenes
- Each character independently defined + reference-bound (`` Define [features] in `ImageN` as `SubjectN` ``)
- Declare spatial relationships remain unchanged
- Add constraint at end: `Prohibit figures with identical appearance, clothing, or accessories; prohibit duplicate clones or twin effects`
- Over 4 reference characters: generate in groups (group images first, then feed into video)

---

## Asset Configuration Strategy

Recommended total: 4-5 assets — 1-2 character images (separate face close-up + full-body) + 1 scene image + 1 camera reference video + 1 audio clip. Avoid maxing out asset slots; too many assets cause feature priority confusion.

---

## 故障诊断

诊断失败原因再重写。不要简单地堆砌形容词。先判断失败来自模式不匹配、过载、歧义、脆弱的身份锁定、不安全措辞、不支持的操作，还是缺失保留约束。

| 症状 | 根因 | 优先修复 |
|---|---|---|
| 产品/面部变化 | I2V 提示词重新描述了可见身份或多重运动叠加 | 添加保留约束（`精确保留[主体]不变`）；删除重复的静态细节描述 |
| 镜头跳变 | 指定了多个不兼容的运镜方式，或无明确终点 | 只选择一种运镜方式，指定起止点 |
| 画面静止/动作被忽略 | 提示词过于静态，无可见后果 | 添加主体、动词、时间线索和改变的终点状态 |
| 口型对不上 | 镜头移动、台词太长、说话人未指定 | 锁定取景、缩短台词、明确指定说话人 |
| VFX 噪点过多 | 特效无来源、物理逻辑或消散过程 | 添加来源、材质、路径、交互方式和终点 |
| 提示词被拒 | 涉及受保护 IP、真人、暴力或规避性措辞 | 用安全的产品语言重写意图，不绕弯 |
| 延长画质劣化 | 无末帧锚点、连续多次叠加过多新变量 | 用上一段返回的末帧作为新首帧，每次只修改一个变量 |
| 音频参考被忽略 | 视频自带声音竞争、无视觉节拍映射 | 静音竞争视频，将一个可见事件映射到节拍上 |
| 文本/Logo 崩坏 | 小文字被要求运动或重绘 | 文字保持静态、居中、受保护；让光线围绕文字运动 |
| 通用/无风格输出 | 空洞风格词、动作描述弱 | 替换为物理动作、光源、材质和声音描述 |

**保守修复模板：**
```
[参考角色（如适用）]。精确保留[身份/产品/环境]。
一个可见动作：[具体动词+后果]。镜头：[单一运镜]。
光影：[物理光源]。声音：[环境/音效/对白]。约束：[不变项]。
```

**升级规则：** 同一错误重复出现时 → 拆分更短片段、减少角色数、简化手部/面部动作、增强角色映射、或切换模式。对于编辑/延长失败，先保留源片段，仅修改失败的图层。如平台支持返回末帧，使用该静帧作为下一次延长的首帧锚点。

---

## 运镜选择指南

使用一个明确的镜头思路。最好的摄影指导包含：起幅、运动方式、速度、与主体的关系、落幅。避免在一个 5 秒镜头中堆叠互相矛盾的运镜。

**运镜匹配表：**

| 需求 | 推荐运镜 | 示例 |
|---|---|---|
| 口型同步/产品身份/精细 VFX | 锁定镜头 | `锁定中景，焦点保持在产品标签上` |
| 发现感/情绪领悟 | 推近 (dolly-in) | `从中近景缓慢推近至面部特写，角色A放下信封` |
| 旅行/追逐/产品运动 | 跟踪 (tracking) | `平稳侧向平移，跟拍主体穿过场景` |
| 尺度/登场/揭示 | 航拍/摇臂 (crane) | `低角度摇臂上升，从靴子升至天际线，落点在角色肩后` |
| 真实感（精度次要） | 手持 (handheld) | `轻微手持呼吸感晃动，主体保持居中` |
| 主体各角度均清晰时 | 环绕 (orbit) | `缓慢环绕主体半圈，从正面推至背影` |

**镜头焦距锚点：** `24mm 广角空间能量`、`35mm 自然街拍视角`、`50mm 肖像压缩感`、`85mm 浅景深特写`、`微距镜头 材质细节`。将焦距词与主体距离和运动配对，不堆砌焦距数字作为装饰。

**冲突规则：** 如果用户给出多个不兼容运镜 → 选择一个主要运镜，其余放入可选变体。需多节拍时 → 拆分为独立片段或时序分镜提示词。

**多角色相机锚定：** `镜头将角色A保持在前景，角色B从后方穿过`。I2V 保留图像构图，除非用户明确要求重新取景。视频参考声明：`` `视频1`仅控制运镜节奏；不复制表演者、房间、Logo 或身份``。

---

## 角色合同

角色提示词必须先消除歧义，再添加风格。

### 角色标签

每个角色分配稳定标签：`角色A`、`角色B`、`主体1`。角色超过一个后不使用模糊代词。

| 字段 | 提示词用法 |
|---|---|
| 标签 | `角色A` 或 `主体1` |
| 身份锚点 | 年龄段、轮廓、发型、服装、授权参考角色 |
| 位置 | 前景/背景、左/右、坐/站 |
| 动作 | 一个分配的动词和终点 |
| 表情 | 可观察行为：眨眼、瞥视、微笑、攥紧、停顿 |
| 约束 | 必须保持不变的内容 |

### 多角色调度

分别分配动作：
- ✅ `角色A 放下信封；角色B 停留在门口`
- ❌ `他们激烈争吵`——模型需要知道谁做什么

接触场景：描述接触点和终点。人群场景：识别主角，保持背景运动简单。

### 手部与面部稳定性

- 保持手部可见但简单
- 避免快速手指动作
- 对白时避免面部触摸
- 口型同步或肖像保留时锁定镜头
- 面部精度脆弱时用道具传达情绪

### 肖像规则

对真人肖像不推断授权。如授权不明确 → 改写为原创角色原型，保留场景功能。
