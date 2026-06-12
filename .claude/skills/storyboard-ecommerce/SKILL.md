---
name: storyboard-ecommerce
description: "为 AI 图像生成器（Midjourney, Flux, 即梦, 可灵, GPT Image）生成电商/直播/带货分镜提示词——三种商业格式（社交商业板/服装导演板/产品展示板）按场景自动选择，含产品参考区、创作者参考区和字幕安全区。用于带货视频故事板、TK购物分镜、直播镜头规划、产品展示板、时尚穿搭分镜、服装分镜。注意：非商业分镜请用 `storyboard-master` 或 `storyboard-prompt`。Use for e-commerce/livestream/shopping storyboards with product reference areas."
---

# Storyboard E-Commerce 电商分镜

## 概览

为 AI 图像生成器生成专业的电商和社交电商分镜提示词。与普通电影分镜不同，电商板需要产品参考区、字幕安全构图、商业导向的镜头结构。此技能覆盖三种商业场景：带主播出镜的社交带货、模特展示的服装走秀、纯产品展示。

此技能用于商业/直播/社交购物类分镜。普通电影/动画分镜请用 `storyboard-prompt`。非电商总览图请用 `storyboard-master`。Seedance I2V 规划请用 `storyboard-sketch`。

## 加载资源

- 三种格式的完整规格（布局、镜头拆解、视觉风格、连续性要求）→ `references/ecommerce-formats.md`
- 去水词替换 → `../references/anti-slop-lexicon.md`
- 电影摄影速查表 → `../references/cinematography-quick-reference.md`
- 产品与商业类型配方 → `../references/seedance-genre-recipes.md`

## 子模式门

三种商业格式，按场景自动选择：

| 用户场景 | 格式 | 特点 |
|---|---|---|
| 带货视频、TK/Reels/Shorts、主播出镜演示产品 | **Format A: 社交商业板** | 产品参考区 + 创作者参考区 + 6 镜头（Hook→Problem→Reveal→Detail→Display→CTA）+ 字幕行 |
| 服装/时尚/穿搭、模特展示、无口播 | **Format B: 服装导演板** | 12-15 镜头网格 + 节奏模块 + 运镜模块 + 光影模块 |
| 纯产品展示、3C/家电/家居/食品/美妆、无人物出镜 | **Format C: 产品展示板** | 产品参考区 + 场景参考区 + 6 镜头（Showcase→Detail→Feature→Use→Atmosphere→Packshot）、无字幕行 |

> 各格式的完整布局结构、镜头卡片规格、默认镜头拆解、连续性要求和视觉风格关键词见 `references/ecommerce-formats.md`

### Format A: 社交商业板（概要）

TikTok 风格带货，创作者/主播出镜。双层参考区（创作者 + 产品），6 镜头 Hook→Problem→Reveal→Detail→Display→CTA 结构，每镜头含字幕行。画幅 4:3 或 16:9。

### Format B: 服装导演板（概要）

服装/时尚走秀，模特展示无口播。三层布局（12-15 镜头网格 + 节奏 + 运镜 + 光影），导演备注 ≤15 字。Replaceable Zone 为唯一定制区。画幅 16:9。

### Format C: 产品展示板（概要）

纯产品展示，无人物出镜。双层参考区（产品 + 场景），6 镜头 Showcase→Detail→Feature→Use→Atmosphere→Packshot 结构，无字幕行。适用于 3C/家电/家居/食品/美妆等非服装品类。画幅 16:9。

## 输出格式

先呈现结构化计划，再呈现压缩的图像生成器提示词：

```markdown
## Storyboard Plan: [产品名称]

### Format: [Social Commerce / Fashion Director / Product Showcase]

[与所选格式匹配的完整结构化拆解]

## Compressed Prompt

[一条完整的图像生成器提示词。包含所有布局指令、风格关键词和反模式清单。]
```

## Quality Bar 质量门槛

**跨格式通用规则：**

- 所有参考图中的主体（创作者/模特/产品）必须保持严格的身份一致性——不得发明变体
- 镜头卡片必须包含所有必填字段：编号、景别、时间码、预览、动作、摄影机
- 视觉风格关键词必须清晰描述板面格式——而非视频内容
- 压缩提示词中必须包含反模式清单，防止 AI 图像生成器漂移到海报/概念图风格
- 若用户提供产品/创作者参考图，精确保持其视觉身份

**格式特定规则：**

- Format A: 字幕安全构图（每帧底部 20% 预留文字区）+ 创作者连续性
- Format B: 节奏模块必须将时间段映射到镜头编号和音乐节拍
- Format C: 无人物出镜——如果手部入镜，保持同一肤色/手势风格


## 保存输出

交付最终输出后，提示用户以带日期和主题的文件名保存：

```
保存到 outputs/YYYY-MM-DD-[主题]-ecommerce-board.md？
示例：outputs/2026-06-10-赛博朋克短片-seedance-prompt.md
```

用户确认后，将输出写入指定路径。
