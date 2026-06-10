---
name: storyboard-sketch
description: 从场景创意、剧本、节拍或视觉概念生成简洁干净的粗糙草图分镜提示词，用于 Seedance 图像生成视频工作流。用于分镜、预览板、animatic 规划、动画镜头计划、关键帧板、粗糙视觉帧、首帧提示词、逐镜头草图提示词，或快速规划板来指导 Seedance I2V 生成。也用于分镜总览图、导演分镜板、故事板规划，或影视/广告/动画前期制作的完整视觉规划板。Use when the user asks for a storyboard, preview board, animatic planning, animation shot plan, keyframe board, rough visual frames, first-frame prompts, shot-by-shot sketch prompts, or a quick board to guide Seedance I2V generation. Also use for storyboard master sheet, shot list board, director treatment board, or full visual planning board.
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
| "分镜总览图", "Master Sheet", "导演分镜板", "shot list board", "director treatment board", "storyboard planning board", "完整分镜规划"，或明确要求完整的视觉规划布局 | **Storyboard Master Sheet** |

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

# Mode B: Storyboard Master Sheet 分镜总览图

## 何时使用

当用户要求视觉规划板而非单独的帧提示词时触发此模式。此模式生成一个结构化描述，可喂入图像生成器创建一张包含所有信息的完整分镜图——适用于导演提案、品牌比稿和前期制作可视化。

总览图采用从电影/电视/广告专业分镜实践中提炼的四区结构。

## 总览图结构

```markdown
**Master Sheet Setup**
- Project: [项目名称或主题]
- Aspect ratio: [横向板通常为 16:9]
- Style: [director treatment board, clean infographic, professional production document]
- Total shots: [推荐 6-18，根据内容自动调整]

## Section 1: Shot Grid 分镜展示区

[所有镜头的网格布局。每个镜头卡片包含:]

| # | Shot Size | Timecode | Frame Preview | Action | Camera | Purpose |
|---|-----------|----------|---------------|--------|--------|---------|
| 01 | WS | 00:00-00:02 | [一行视觉描述] | [主体动作] | [摄影机设置] | [故事目的] |
| 02 | MS | 00:02-00:04 | ... | ... | ... | ... |
...

## Section 2: Rhythm & Structure 节奏设计区

叙事弧线:
[平静] → [推进] → [张力/强化] → [峰值/高潮] → [释放/收束]

按阶段分配镜头:
- Phase 1 (建立): Shots 01-02 — [发生什么]
- Phase 2 (发展): Shots 03-04 — [发生什么]
- Phase 3 (强化): Shots 05-06 — [发生什么]
- Phase 4 (高潮): Shots 07-08 — [发生什么]
- Phase 5 (收束): Shots 09-10 — [发生什么]

节奏密度: [平静 → 加速 → 峰值 → 减速]
音乐卡点对齐: [关键节拍点及其落在哪些镜头上]

## Section 3: Camera Movement Diagram 运镜设计区

俯视图布局:
- 摄影机位置以镜头编号标记（① ② ③ ...）
- 运动轨迹以虚线箭头显示
- 每镜头运动类型: [Static / Push-in / Lateral track / Orbit / Handheld / 等]

## Section 4: Visual Language 视觉设计区

灯光设计: [主光、辅光、轮廓光、色温、每阶段氛围]
色彩方案: [暖/冷/中性、主色、对比度级别]
构图风格: [三分法、居中、引导线、负空间、对称]
情绪关键词: [3-5 个词概括整体情绪基调]
美术指导备注: [关键视觉参考、质感、制作设计意图]
```

## 叙事推进模板

构建总览图时，按内容类型适配叙事弧线。选择并填入：

**Film / Drama 电影/剧情:**
```
世界观建立 → 人物发展 → 冲突升级 → 高潮爆发 → 结局
```

**Advertising / Commercial 广告:**
```
场景建立 → 产品展示 → 卖点强化 → 情绪高潮 → 品牌收尾
```

**E-commerce / Product 电商/产品:**
```
建立氛围 → 整体展示 → 细节特写 → 使用场景 → 转化收尾
```

**Documentary / Explainer 纪录片/说明:**
```
背景介绍 → 内容展开 → 重点分析 → 观点强化 → 总结结束
```

**Short Video / Social 短视频/社交:**
```
Hook抓眼球 → 问题呈现 → 解决方案 → 效果展示 → CTA引导
```

## 总览图示例

用户请求: "做一个高端腕表品牌广告的分镜总览图，6个镜头"

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

叙事弧线: Mysterious → Elegant → Impressive → Aspirational → Iconic

- Phase 1 (神秘): Shots 01 — 制造悬念
- Phase 2 (细节): Shots 02-03 — 工艺展示
- Phase 3 (生活方式): Shots 04-05 — 场景代入
- Phase 4 (品牌): Shot 06 — 品牌收尾

节奏密度: slow → steady → gentle peak → hold
音乐节拍: 舒缓弦乐起 → 02处轻鼓点 → 04处旋律推进 → 06处收束

## Section 3: Camera Movement Diagram

俯视图: ①(正上方) → ②(右环绕) → ③(正上方) → ④(正面推近) → ⑤(后退) → ⑥(静止)

运动类型: Static → Slow orbit → Static → Push-in → Dolly back → Hold

## Section 4: Visual Language

灯光设计: 柔光主光源, 黑色背景吸收光, 金属高光点缀, 城市暖色夜景
色彩方案: 黑/金/银 为主, 暖白点缀, 低饱和高级感
构图风格: 居中构图为主, 01用负空间, 04用三分法
情绪关键词: 奢华 / 克制 / 精密 / 优雅 / 永恒
美术指导备注: 避免过度炫光, 强调材质真实感, 金属拉丝纹理清晰
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
