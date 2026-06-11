---
name: storyboard-master
description: "为 AI 图像生成器（Midjourney, Flux, 即梦, 可灵, GPT Image）生成多镜头分镜总览图/导演提案板提示词——产出为一张含全部镜头的规划板。用于分镜总览图、导演提案板、完整视觉规划板、前期制作蓝图、分镜规划图，或需要将镜头网格+节奏时间轴+摄影机运动图+视觉设计融合为一张综合多镜头规划板时。注意：单帧镜头画面请用 `storyboard-prompt`；电商带货板请用 `storyboard-ecommerce`；I2V 文本规划请用 `storyboard-sketch`。Use for multi-shot master sheets, director treatment boards, full visual planning boards — one image containing all shots."
---

# Storyboard Master Sheet 分镜总览图

## 概览

生成一份综合的分镜总览图提示词——一份将镜头网格、节奏时间轴、摄影机运动图和视觉语言设计融合为一张专业规划板的单一视觉文档。这是导演、代理商和制作团队用于提案、项目阐述和前期制作蓝图的格式。

此技能用于多镜头总览图。单帧分镜提示词请用 `storyboard-prompt`。含产品/创作者参考区的电商/直播分镜请用 `storyboard-ecommerce`。Seedance I2V 规划请用 `storyboard-sketch`。

## 加载资源

- 需要去水词替换时，阅读共享参考 `../references/anti-slop-lexicon.md`。
- 获取双语电影摄影速查表，阅读 `../references/cinematography-quick-reference.md`。

## 模式门

总览图有两种输出密度。根据用户意图选择：

| 用户说...                                                                                                      | 输出                                       |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| "storyboard master sheet", "Master Sheet", "Director Treatment Board", "director treatment board", "完整规划", "pre-production blueprint" | **完整总览图**（4 区，6-24 镜头）          |
| "简版分镜图", "分镜图板", "quick board", "简洁版"                                                              | **简洁导演板**（仅镜头网格 + 底部 3 模块） |

镜头数量按以下优先级确定：
1. **用户显式指定** → 直接使用
2. **存在上游管线产物**（如 `director-story` 的场景拆解、`director-prompt-packager` 的分镜方案、`director-core` 已执行的 STATE 产出）→ 从已有镜头/场景拆解中推导
3. **无任何上下文时的兜底** → 简洁模式默认 6 镜头，完整模式默认 12 镜头

## 完整总览图结构

完整总览图有四个必选区。撰写提示词时应使图像生成器在单一协调布局中生成全部四个区。

### 4 区布局

```
┌─────────────────────────────────────────┐
│         区域 1：分镜展示区               │
│   (上部约 60% 的区域)                     │
│   带编号的镜头卡片网格                     │
├──────────────┬──────────────┬───────────┤
│ 区域 2：     │ 区域 3：     │区域 4：   │
│ 节奏时间轴   │ 运镜设计图   │视觉语言   │
│ (左下)        │ (中下)        │ (右下)     │
└──────────────┴──────────────┴───────────┘
```

### 区域 1：分镜展示区

主要区域。网格中的每个镜头卡片必须包含：

```
┌──────────────────────────┐
│ #01 | WS | 00:00-00:02  │  ← 灰色标题栏
│                          │
│    [Frame Preview]       │  ← 镜头可视化预览
│                          │
│ Action: [一行]           │  ← 镜头中主体动作
│ Camera: [景别+运动]       │  ← 摄影机设置
│ Purpose: [故事原因]       │  ← 为什么这个镜头存在
└──────────────────────────┘
```

镜头卡片信息格式: `编号 | 景别 | 时间码`

布局规则:

- 按阅读顺序排列镜头（左→右，上→下）
- 卡片之间使用细灰边框
- 网格中保持统一卡片尺寸
- 板面为白色或浅灰背景

### 区域 2：节奏设计区

展示叙事节奏和剪辑结构:

- **时间轴**: 全视频时长，标有镜头标记（①②③...）
- **节奏曲线**: 显示强度变化的波形（平静 → 推进 → 峰值 → 释放）
- **阶段标注**: 命名每个叙事阶段及所属镜头
- **音乐/节拍对齐**: 关键节拍点及对应镜头

节奏阶段应遵循叙事弧线。根据内容类型使用以下模板之一：

| 内容类型                         | 弧线模式                             |
| -------------------------------- | ------------------------------------ |
| Film / Drama 电影/剧情           | 建立 → 发展 → 冲突 → 高潮 → 收束     |
| Advertising 广告                 | Hook → 展示 → 强化 → 峰值 → 品牌收尾 |
| E-commerce 电商                  | 氛围 → 展示 → 细节 → 场景 → CTA      |
| Documentary 纪录片               | 背景 → 展开 → 分析 → 强化 → 总结     |
| Short Video / Social 短视频/社交 | Hook → 问题 → 方案 → 效果 → CTA      |

阶段标注格式: `Phase 1: [名称] (Shots XX-XX) — [发生什么]`

添加节奏密度线: `[平静] →→ [推进] →→→ [峰值] →→ [减速]`

### 区域 3：运镜设计区

显示摄影机位置和运动的俯视空间图:

- **摄影机位置**: 在空间位置上的编号圆圈（①②③...）
- **运动轨迹**: 连接位置的虚线箭头，显示路径
- **运动类型标注**: Static / Push-in / Pull-out / Pan / Tilt / Dolly / Crane / Orbit / Handheld / Steadicam / Tracking
- **主体位置**: 简单标记显示主体相对于摄影机的位置

将此呈现为图像生成器可渲染的描述: "Top-down floor plan with numbered camera positions connected by dashed trajectory arrows..."

### 区域 4：视觉设计区

适用于所有镜头的设计规格:

- **灯光设计**: 主光、辅光、轮廓光、色温、氛围
- **色彩方案**: 主色、对比度级别、饱和度
- **构图规则**: 主要和辅助构图技法
- **情绪关键词**: 5-8 个情绪/氛围描述词
- **美术指导备注**: 关键视觉参考、质感、制作设计意图

格式为清晰的规格块:

```
LIGHTING: [主光方向+质感] / [辅光] / [色温]
COLOR: [调色板描述] / [对比度级别]
COMPOSITION: [技法 1] + [技法 2]
MOOD: [关键词 1] · [关键词 2] · [关键词 3] · [关键词 4] · [关键词 5]
ART DIRECTION: [1-2 行设计指导]
```

## 简洁导演板

当用户需要更短的格式时，简化为:

```
┌─────────────────────────────────┐
│    Shot Grid (3 rows × 4-5 cols)│
│    12-15 shot cards             │
├─────────────────────────────────┤
│ Rhythm │ Camera  │ Lighting     │
│ Struct │ Movement│ & Mood       │
└─────────────────────────────────┘
```

简洁模式镜头卡片: `#01 | LS 全景 | 0:00-0:02` 作为标题、预览图像和一行导演风格描述（中文 ≤15 字）。

底部模块简化但仍必须包含:

- 节奏结构: 含节拍点的时间分段
- 摄影机运动: 含镜头编号的轨迹箭头
- 灯光与氛围: 主光源 + 情绪关键词

## 输出格式

两种模式下，均先呈现结构化计划供用户审核，再呈现图像生成器的压缩提示词。

```markdown
## Master Sheet Plan

### Project Info

- Project: [名称/主题]
- Style: [director treatment board / clean infographic / production document]
- Aspect ratio: [推荐 16:9]
- Total shots: [N]

### Section 1: Shot Grid

| #   | Size | Timecode | Preview | Action | Camera | Purpose |
| --- | ---- | -------- | ------- | ------ | ------ | ------- |
| 01  | ...  | ...      | ...     | ...    | ...    | ...     |
| 02  | ...  | ...      | ...     | ...    | ...    | ...     |

...

### Section 2: Rhythm & Structure

Arc: [阶段 1 → 阶段 2 → 阶段 3 → 阶段 4 → 阶段 5]
[含镜头分配的阶段拆解]
Rhythm density: [曲线描述]
Music beats: [关键点]

### Section 3: Camera Movement

Top-down: [镜头编号及位置]
Trajectories: [每过渡段落的运动类型]

### Section 4: Visual Language

LIGHTING: [...]
COLOR: [...]
COMPOSITION: [...]
MOOD: [...]
ART DIRECTION: [...]

## Compressed Master Sheet Prompt

[一条覆盖全部 4 区的完整图像生成器提示词。80-200 词。包含规划板级风格关键词。]
```

## 总览图风格关键词

始终将此关键词块附加到总览图提示词（选择适当子集）:

```
Storyboard master sheet, director treatment board, creative production blueprint, shot list layout, camera movement diagram, editing rhythm timeline, visual language board, film production planning document, professional storyboard presentation, information-rich infographic, cinematographic production guide, high-end editorial layout, clean grid system, architectural information graphics, ultra detailed, production ready
```

简洁板简化为:

```
Director storyboard sheet, shot list board, camera movement diagram, rhythm structure, professional production board, clean infographic layout, white background, thin grid borders, ultra detailed
```

## Quality Bar 质量门槛

- 计划和提示词中都必须包含四个区（或简洁模式的三个区）。
- 叙事弧线必须匹配内容类型——不得为电商视频使用电影弧线。
- 镜头卡片必须包含: 编号、景别、时间码、预览描述、动作、摄影机和目的。
- 摄影机运动图必须包含编号位置和轨迹箭头。
- 风格关键词必须强调"board"和"sheet"概念——这可以防止图像生成器生成完整的电影画面而非规划文档。
- 若用户指定中文输出，计划中所有描述性文字保持中文；风格关键词保持英文以获得更好的图像生成器表现。


## 保存输出

交付最终输出后，提示用户以带日期和主题的文件名保存：

```
保存到 outputs/YYYY-MM-DD-[主题]-storyboard-master.md？
示例：outputs/2026-06-10-赛博朋克短片-seedance-prompt.md
```

用户确认后，将输出写入指定路径。
