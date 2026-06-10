---
name: storyboard-prompt
description: 为 AI 图像生成器（Midjourney, Flux, 即梦, 可灵, GPT Image, Runway, Veo）生成专业分镜帧提示词。用于分镜提示词、镜头规划提示词、分镜提示词生成、电影预可视化提示词、动画分镜、商业广告分镜、单帧分镜，或需要撰写能产出电影级分镜面板图像的结构化提示词时。当用户给出模糊的场景创意并希望将其转化为专业分镜镜头描述时也适用。Use when the user asks for storyboard prompts, shot planning prompts, storyboard frame generation, film pre-visualization prompts, animation storyboard, commercial storyboard, single-frame storyboard, or needs to write structured prompts that produce cinema-grade storyboard panel images.
---

# Storyboard Prompt 分镜提示词

## 概览

将场景创意、主体或动作转化为专业结构化的提示词，AI 图像生成器可将其转化为电影级分镜帧图像。此技能强制执行一个源自电影行业前期制作标准的 8 要素镜头描述框架，确保每条提示词都能生成可读、技术准确的分镜面板，无论使用哪种图像生成器。

此技能用于单帧分镜提示词。多镜头总览图请用 `storyboard-master`。电商/直播分镜请用 `storyboard-ecommerce`。Seedance I2V 规划提示词请用 `storyboard-sketch`。


## 加载资源

- 需要去水词替换时，阅读共享参考 `../references/anti-slop-lexicon.md`
- 获取双语电影摄影速查表（景别、运动、角度、构图、灯光、叙事目的），阅读 `../references/cinematography-quick-reference.md`

## 输入门

生成提示词前，检查用户是否提供了足够素材来填充 8 要素框架。满足以下条件时视为输入充足：

- 一个场景创意、主体或主题。
- 一个期望的视觉风格或使用上下文（电影/广告/动画/CG）。

若充足，直接进行并用合理默认值填补空白，清晰标注。

若不充足，从上下文中推断后确认：

```markdown
我先确认一下这个分镜的方向：
- 场景/主题：[推断的]
- 主体/角色：[推断的]
- 动作：[推断的]
- 目标风格：电影级故事板 / 黑白线稿 / 动画预演 / 广告提案
- 目标工具：Midjourney / Flux / 即梦 / 可灵 / GPT Image

确认吗？调整一句我就生成提示词。
```

若用户说"直接生成"，以假设进行并标注。

## 8 要素框架

每条分镜提示词必须涵盖这八个维度。模型不能凭空发明缺失的关键信息——若用户未提供，做合理假设并注明。

| # | Element | 中文 | What it answers |
|---|---------|------|-----------------|
| 1 | Scene | 场景 | 发生在何时何地？ |
| 2 | Subject | 主体 | 聚焦于谁或什么？外观？服装？ |
| 3 | Action | 动作 | 主体在做什么？状态、方向？ |
| 4 | Camera | 镜头 | 景别、角度、运动？ |
| 5 | Composition | 构图 | 画框如何安排？主体位置？ |
| 6 | Lighting | 光线 | 主光、辅光、色温、质感？ |
| 7 | Mood | 情绪 | 什么样的情绪氛围？ |
| 8 | Story Purpose | 叙事目的 | 为什么这个镜头存在？它传达了 什么？ |

此框架适用于用户需要黑色电影侦探场景、动画奇幻镜头或奢侈品广告。要素不变，只改变值。

## 输出格式

分两层写出提示词。首先展示结构化拆解，让用户验证每个要素。然后提供可粘贴到图像生成器的压缩提示词。

```markdown
## Shot Breakdown

**Scene:** [时间 · 地点 · 环境细节]
**Subject:** [角色/物体 · 外观 · 服装 · 状态]
**Action:** [主体在做什么 · 运动方向 · 状态]
**Camera:** [景别] · [角度] · [运动]
**Composition:** [构图方式 · 主体位置 · 层次深度]
**Lighting:** [主光方向/质感] · [辅光] · [色温] · [氛围]
**Mood:** [2-3 个情绪关键词]
**Story Purpose:** [叙事功能——establish/reveal/emphasize/transition]

## Prompt

[压缩提示词，40-100 词，根据用户偏好使用英文或中文。以风格关键词收尾。]
```

### 提示词压缩规则

压缩提示词应作为一个自然段落流畅展开。按视觉优先级排列要素: Scene → Subject → Action → Camera → Composition → Lighting → Mood，然后附加风格关键词。压缩提示词中不得使用项目符号或标签——它必须读起来像一段图像生成器能良好解析的单一描述性段落。

### 风格关键词

始终将这些附加到压缩提示词末尾。选择与用户意图匹配的集合：

**Film storyboard 电影分镜:**
```
professional storyboard panel, film storyboard frame, director treatment, cinematic composition, pre-production visualization, black and white storyboard sketch, clean pencil drawing, highly detailed, production-ready storyboard
```

**Animation storyboard 动画分镜:**
```
animation storyboard, pre-production planning board, clean pencil sketch, animation keyframe planning, animatic reference frame, production storyboard panel
```

**Commercial storyboard 商业广告分镜:**
```
commercial storyboard, advertising shot planning, director treatment frame, high-end product storyboard, professional production board, clean composition, white background
```

**Color/finished style 彩色/完成风格（用户明确要求彩色时）:**
```
professional storyboard panel, cinematic composition, color storyboard, production design, film pre-visualization, highly detailed
```

## 领域模板

### Film / Drama Template 电影/剧情模板

当用户描述含角色、张力或情绪弧线的叙事场景时使用。

```
Scene: [时间段] · [地点] · [天气/氛围]
Subject: [角色名称/类型] · [年龄] · [外观] · [服装]
Action: [含方向和状态的物理动作]
Camera: [WS 到 ECU 的景别] · [low/high/eye 角度] · [static/push/track]
Composition: [rule of thirds / centered / leading lines] · [前景/中景/背景层次]
Lighting: [主光源] · [soft/hard 质感] · [warm/cool 色温] · [特殊: rim/volumetric/practical]
Mood: [2-3 词: tense/suspenseful/melancholic/hopeful/epic]
Story Purpose: [establish location / introduce character / build tension / reveal clue / transition]
```

### Animation Template 动画模板

当用户描述动画或奇幻内容时使用。

```
Scene: [奇幻/现实地点] · [时间/魔法氛围]
Subject: [角色类型] · [年龄] · [设计特征] · [服装]
Action: [含流动方向的动态或情绪化动作]
Camera: [景别] · [three-quarter view / profile / bird's eye] · [动态运动]
Composition: [rule of thirds / dynamic perspective] · [层次深度]
Lighting: [soft/diffuse magical light] · [warm/cool/fantasy glow] · [氛围]
Mood: [wonder / adventure / fantasy / dreamlike / epic]
Story Purpose: [introduce world / show character emotion / reveal destination / emphasize scale]
```

### Advertising / Product Template 广告/产品模板

用于产品广告、奢侈品、品牌影片。

```
Scene: [干净影棚 / 生活方式环境 / 抽象背景]
Subject: [产品名称/类型] · [关键视觉特征] · [材质/质感]
Action: [缓慢揭示 / 旋转 / 与光或环境的交互]
Camera: [CU / ECU for product detail] · [eye level / top-down] · [slow push-in / orbit / static]
Composition: [centered / negative space] · [产品为主角，最小干扰]
Lighting: [rim light for edge definition] · [soft fill] · [dramatic / elegant / high key]
Mood: [luxury / elegant / premium / minimal / aspirational]
Story Purpose: [hero product / emphasize craftsmanship / lifestyle association / brand closer]
```

### Universal Template 通用模板（领域不明确时）

最通用的模板——当用户领域不适用以上分类时使用，或作为默认。

```
Scene: [时间 · 地点 · 环境]

Subject: [角色 / 物体 · 外观 · 状态]

Action: [正在发生什么 · 运动方向]

Camera: [景别 · 角度 · 运动]

Composition: [构图 · 主体位置 · 深度]

Lighting: [主光 · 辅光 · 色温 · 特殊质感]

Mood: [情绪关键词]

Story Purpose: [这个镜头为什么重要]

Style: [professional storyboard panel, cinematic composition, clean pencil sketch, highly detailed, production-ready storyboard]
```

## Scene Generator 场景生成器

当用户只提供主题（如"未来赛博朋克城市"或"暴雨中的侦探"）而没有完整场景细节时，先生成场景拆解，然后基于它构建提示词。

模板：

```markdown
根据主题「[用户的主题]」，我先展开一个场景方案：

**场景描述:** [2-3 句建立时间、地点、氛围]
**主体描述:** [1-2 句关于主要主体]
**动作描述:** [1 句关于关键动作]
**镜头建议:** [景别 + 角度]
**光线建议:** [主光 + 氛围]
**情绪建议:** [2-3 个情绪词]
**分镜重点:** [此镜头应强调什么]

确认这个方向后，我生成完整提示词。
```

## Quality Bar 质量门槛

- 每条提示词必须涵盖全部 8 个要素。若用户未提供某个，标注假设。
- 压缩提示词应可直接用于任何主流图像生成器而无需修改。
- 风格关键词不得包含不安全的工作室/系列/名人名称——使用描述性等效词。
- 若用户要求中文输出，以中文写拆解部分但保留风格关键词为英文（它们在图像生成器中表现更好）。
- 不熟悉项目的读者仅凭压缩提示词就应能理解整个场景。
