---
name: storyboard-sketch
description: "为 Seedance I2V 工作流生成文本级逐帧分镜草图描述——不生图，仅产出每帧的运动/镜头/光影/音效文字说明。用于 I2V 分镜规划、逐帧动作描述、animatic 草图、Seedance 首帧提示词，或需要将剧本拆解为连续帧序列指导 I2V 生成时。注意：如需多镜头总览图（生图），请用 `storyboard-master`；如需单帧生图提示词，请用 `storyboard-prompt`；如需电商板，请用 `storyboard-ecommerce`。Use for Seedance I2V frame planning, per-frame motion/text descriptions, animatic sketches. NOT for multi-shot overview boards or single-frame image prompts."
---

# Seedance 分镜草图

## 概览

将场景创意、剧本或概念转化为 Seedance 图像生成视频的分镜计划。此技能支持两种输出模式，由下方的模式门自动选择：

- **Compact Frame Prompts 紧凑帧提示词**（默认）: 3-8 个简洁的粗糙草图帧提示词，针对 Seedance I2V 种子图像优化。
- **Storyboard Master Sheet 分镜总览图**（按需）: 包含镜头网格、节奏时间轴、摄影机运动图和视觉语言设计的完整视觉规划板——适用于导演提案、品牌比稿或前期制作蓝图。

两种模式下均优先追求清晰性、连续性和草图可绘制性，而非华丽的电影化文笔。

## 模式选择门

生成输出前，决定使用哪种模式：

| 用户说... | 使用此模式 |
|---|---|
| "分镜草图", "keyframe prompts", "I2V storyboard", "shot-by-shot prompts", "quick preview board", "rough visual frames"，或任何 Seedance 相关的提示词请求 | **Compact Frame Prompts** |
| "分镜总览图", "Master Sheet", "导演分镜板"，或明确要求完整的视觉规划布局 | 路由到 `storyboard-master` 技能 |

当用户提供多面板板图时：识别是 ≤4 面板（按紧凑帧处理）还是 ≥5 面板（作为总览图结构的数据源）。

不确定时，默认使用紧凑帧提示词但简要提及总览图选项。

---

# Mode A: Compact Frame Prompts 紧凑帧提示词

## 工作流

1. 在写入任何帧提示词之前，先运行输入门。
2. 识别场景目标、角色、地点、情绪节拍、参考素材、目标模式、画幅比例和预期输出时长。
3. 将创意或剧本转化为紧凑的分镜计划：3-8 帧，除非用户指定数量。
4. 为每帧定义一个可读的视觉时刻，包括：主体、动作、构图、摄影机角度、灯光情绪、故事目的和连续性备注。
5. 将每帧写为粗糙草图提示词，而非最终视频提示词。
6. 添加一段简短的 Seedance I2V 备注，说明该帧应如何动画过渡到下一个时刻。

仅在缺失信息会实质性改变规划板时才问一个简洁的问题，如目标画幅比例、帧数，或规划板应为写实、动画、广告风格还是电影风格。

## 输入门

生成分镜草图提示词前，判断用户是否已提供足够的场景素材来转化为紧凑的分镜计划。

满足以下条件时视为输入充足：

- 一个核心场景创意、剧本、节拍列表或图像/视频参考。
- 一个主体或角色。
- 一种情境、地点或动作。
- 一个期望用途，如 Seedance I2V、预览板、animatic 或镜头规划。

若充足，直接进行并在"Storyboard Setup"中说明任何轻量假设。

若不充足，从可用上下文中推断草稿简报后再询问用户。使用对话上下文、已提供的文件、项目名称、已有提示词文本、上传的图像或附近的项目素材。然后请用户确认或修正简报后再生成帧提示词。

使用此确认格式：

```markdown
我先确认一下分镜基础：
- 场景核心：[推断的或缺失的]
- 主体/角色：[推断的或缺失的]
- 地点/情境：[推断的或缺失的]
- 输出目标：Seedance image-to-video storyboard sketch
- 建议规格：[画幅比例, 帧数, 风格]

确认这些方向吗？也可以直接改一句，我再生成分镜草图提示词。
```

若请求紧急或用户明确说"直接生成"，以合理假设进行并清晰标注。

## 输出格式

默认使用此结构：

```markdown
**Storyboard Setup**
- Aspect ratio:
- Visual style:
- Scene context: [一行场景描述——时间、地点、环境]
- Continuity anchors: [角色服装、关键道具、空间地理、屏幕方向]

**Frame 1 - [简短节拍名称]**
Sketch prompt: [一个干净的粗糙分镜图像提示词]
Scene: [此节拍的时间 · 地点 · 环境上下文]
Composition: [景别、摄影机角度、构图]
Lighting & Mood: [主光、氛围]
I2V motion note: [一句描述进入此节拍或在节拍内的运动]
Story purpose: [此镜头传达什么——揭示、张力、过渡、建立等]
Continuity: [哪些必须保持一致]

**Frame 2 - [简短节拍名称]**
...
```

为每个镜头重复帧块。仅在有用时才以紧凑的"Board Notes"部分收尾。

### Field Guide 字段指南

- **Sketch prompt**: 主要的图像生成提示词。25-60 词。包含主体、动作、摄影机、构图、灯光提示和粗糙板风格关键词。这是喂给图像生成器以生成分镜面板的内容。
- **Scene**: 此节拍特定的时间、地点和环境上下文。使草图提示词无需重新解释设定。
- **Composition**: 景别（见速查表）、摄影机角度、构图方式。使用平实术语如"wide shot"、"over-shoulder"、"low angle"、"centered"、"rule of thirds"。
- **Lighting & Mood**: 主光方向和质感、色温、氛围。例如"warm rim light from window, soft fill, tense atmosphere"。
- **I2V motion note**: Seedance 图像生成视频应如何为此帧动画化。摄影机运动 + 主体运动 + 过渡逻辑。一句话。
- **Story purpose**: 此镜头服务的叙事功能——如"建立场景空间感"、"揭示角色情绪转折"、"强调产品质感"、"为下一镜头制造悬念"。这是专业分镜实践中最重要的补充：每个镜头必须有清晰的叙事存在理由。
- **Continuity**: 哪些必须与其他帧保持一致——角色身份、服装、道具、灯光方向、屏幕空间地理。

## 提示词风格

- 保持草图提示词简短：通常每帧 25-60 词。
- 使用简单的物理语言："wide shot"、"over-shoulder"、"low angle"、"profile"、"center frame"、"foreground silhouette"。
- 指定粗糙板美学：pencil sketch, grayscale marker, loose storyboard lines, clean thumbnail composition, no finished rendering。
- 仅包含理解该节拍所需的对象和表情。
- 保持角色身份、服装、道具、空间地理和屏幕方向在帧间一致。
- 优先使用可见动作而非抽象的情绪词。
- 使用朴实的构图提示而非浮夸的电影形容词。

## Seedance 工作流对齐

遵循 Seedance 操作模式，但不成为完整的产品提示词技能：

- 先摄取: 厘清目标、时长、画幅比例、参考素材、交付物和安全/IP 风险（在相关时）。
- 模式门: 假定此技能服务于 I2V 规划，除非用户说 T2V、V2V、R2V、edit 或 extend。
- 参考素材映射: 若有素材存在，为每个素材分配一个角色，如身份、首帧、环境、运动、摄影机、时间或风格。说明哪些不应传递。
- 长视频逻辑: 超过 15 秒的视频，生成分镜计划并注明最终 Seedance 生成应拆分为镜头或段落。
- 分镜板输入: 若用户提供多面板板图，首先识别是 ≤4 面板用于一条带时间戳的 Seedance 提示词，还是 ≥5 面板用于每条独立镜头提示词加剪辑节奏。
- 质量通行: 检查每帧有一个可见节拍、一个主摄影机设置、连续性锚点和一条 I2V 运动备注。

## Seedance I2V 备注

为每帧包含一条运动备注，帮助静态分镜成为 Seedance 图像生成视频的种子：

- 摄影机运动: static hold, slow push-in, lateral track, gentle tilt, handheld drift。
- 主体运动: turn, step, reach, glance, pause, reveal, react。
- 过渡逻辑: match action, eye-line match, push through foreground, cut on gesture。
- 避免要求一帧包含多个时间分离的动作。

## 示例——紧凑帧提示词

用户创意: "一个快递员在雨巷中发现包裹在滴答作响。"

```markdown
**Storyboard Setup**
- Aspect ratio: 16:9
- Visual style: rough grayscale storyboard sketch, clean readable thumbnails
- Scene context: 午夜，狭窄后巷，大雨，湿砖墙
- Continuity anchors: 红色快递员夹克、湿巷砖、黑色小包裹

**Frame 1 - 进入巷子**
Sketch prompt: Wide shot, rainy narrow alley at night, courier in a red jacket enters from screen left holding a small black package, wet brick walls, simple pencil lines, clear silhouette.
Scene: 午夜 · 窄巷 · 雨打砖墙
Composition: Wide shot, eye level, leading lines from alley walls
Lighting & Mood: 路灯顶光，蓝色环境光，紧张
I2V motion note: Slow lateral track follows the courier walking deeper into the alley.
Story purpose: 建立场景空间和角色进入状态
Continuity: 快递员右手持包裹。

**Frame 2 - 听到声音**
Sketch prompt: Medium close shot, courier stops under a dim wall lamp and tilts the package toward one ear, rain streaks behind, anxious face, loose storyboard shading.
Scene: 同一巷子 · 壁灯下
Composition: Medium close-up, eye level, centered on face and package
Lighting & Mood: 头顶灯作为主光，面部雨水反光，悬疑
I2V motion note: Static hold with a small head turn as the courier hears the ticking.
Story purpose: 揭示危机信号，建立悬疑转折
Continuity: 相同红色夹克，相同包裹大小和朝向。
```

---
## 加载资源

此技能包含内置参考知识。需要时加载：

- 获取 Seedance I2V 工作流、操作模式和运动备注规范，阅读 `references/seedance-i2v-workflow.md`
- 需要去水词替换时，阅读共享参考 `../references/anti-slop-lexicon.md`
- 获取双语景别、摄影机运动、角度、构图、灯光和叙事目的速查表，阅读 `../references/cinematography-quick-reference.md`
- 获取 Seedance 平台约束（字数限制、`` `图片N` `` / `` `视频N` `` 参考格式），阅读共享参考 `../references/seedance-platform.md`

---

## Quality Bar 质量门槛

- 读者应能通过浏览帧标题和草图提示词理解整个场景。
- 每条提示词应可作为一张分镜面板绘制。
- 每帧必须有清晰的故事目的——回答"这个镜头为什么存在"。
- 规划板应在最终 Seedance 提示词写作之前就具备可用性。
- 若用户要求中文输出，以简洁中文按相同结构书写全部提示词。
- 对于总览图模式，四个区（分镜网格、节奏、摄影机、视觉语言）应构成一份连贯的规划文档，而非仅仅是镜头罗列。


## 保存输出

交付最终输出后，提示用户保存：

```
保存到 outputs/storyboard-sketch-i2v-frames.md？
```

用户确认后，将输出写入指定路径。
