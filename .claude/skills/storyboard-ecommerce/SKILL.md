---
name: storyboard-ecommerce
description: 为 AI 图像生成器（Midjourney, Flux, 即梦, 可灵, GPT Image）生成专业的电商带货/直播/社交电商分镜提示词。用于电商分镜、带货视频故事板、TikTok 购物视频分镜、直播镜头规划、产品展示板、产品展示分镜、时尚穿搭分镜、服装分镜，或任何需要产品参考区、创作者参考区和字幕安全区镜头拆解的商业导向视频规划板。Use when the user asks for an e-commerce storyboard, 带货视频故事板, 电商分镜, TikTok shopping video storyboard, livestream shot plan, 直播分镜, product showcase board, fashion lookbook storyboard, or any commerce-oriented video planning board that needs product reference areas, creator reference areas, and subtitle-safe shot breakdowns.
---

# Storyboard E-Commerce 电商分镜

## 概览

为 AI 图像生成器生成专业的电商和社交电商分镜提示词。与普通电影分镜不同，电商板需要产品一致性区、创作者/主播参考区、字幕安全构图，以及商业导向的镜头结构（Hook → Problem → Reveal → Detail → Display → CTA）。

此技能用于商业/直播/社交购物类分镜。普通电影/动画分镜提示词请用 `storyboard-prompt`。非电商总览图请用 `storyboard-master`。Seedance I2V 规划请用 `storyboard-sketch`。


## 加载资源

需要去水词替换时，阅读共享参考 `../references/anti-slop-lexicon.md`

## 子模式门

此技能支持两种商业特定格式。自动选择：

| 用户说... | 输出格式 |
|---|---|
| "带货视频故事板", "TK storyboard", "TikTok shop video", "短视频带货"，带主播/创作者的产品演示 | **Social Commerce Board 社交商业板**（产品参考 + 创作者参考 + 6 镜头拆解） |
| "服装分镜", "fashion storyboard", "电商直播分镜", "导演版分镜图"，模特展示服装，无口播主播 | **Fashion Director Board 服装导演板**（镜头网格 + 节奏 + 摄影机 + 灯光模块） |

---

## Format A: Social Commerce Board 社交商业板

用于 TikTok/Reels/Shorts 风格的产品视频，其中创作者/主播展示产品。源自 TK 英文 AI 视频故事板模板。

### 布局结构

```
┌──────────────────────────────────────────────┐
│              Top Info Bar                     │
│  Product | Audience | Selling Point | ...    │
├──────────────────┬───────────────────────────┤
│ Creator Ref (L)  │  Product Ref (R)          │
│ 3 ref images     │  3 ref images             │
├──────────────────┴───────────────────────────┤
│        6-Shot AI Video Storyboard            │
│  Shot 01 │ Shot 02 │ Shot 03 │ ... │ Shot 06│
│  [card]  │ [card]  │ [card]  │     │ [card]  │
└──────────────────────────────────────────────┘
```

画幅比例: 4:3 或 16:9。白色背景。黑色细边框。干净网格布局。可读的中英文字。高信息密度但不杂乱。

### Top Info Bar 顶部信息栏

一行包含 6 个信息单元格的横向表格:

| 单元格 | 内容 |
|------|---------|
| **Product** | 来自用户输入的产品名称 |
| **Audience** | 目标受众（如动漫粉丝、桌搭爱好者、收藏控） |
| **Core Selling Point** | 一句话价值主张 |
| **Hook** | 开场钩子文案 |
| **Video Goal** | 结构流程（如 Hook → Problem → Reveal → Detail → Display → CTA） |
| **Format** | 平台 / 画幅比例 / 时长 / 语言 |

### Creator Reference Area 创作者参考区（左侧）

标题: **Creator Reference**

三张同一创作者的小参考图，展示视觉一致性:

| # | Image | Label |
|---|-------|-------|
| 1 | 正面半身照 | Front half-body |
| 2 | 表情特写 | Expression close-up |
| 3 | 侧面半身照 | Side half-body |

要求:
- 三张图中必须是同一人——脸型、发型、服装、肤色和气质必须一致。
- 看起来像真实的 TikTok/短视频创作者。
- 背景可暗示居家桌面布置、直播间或产品使用环境。
- 每张图下方有英文标签。

### Product Reference Area 产品参考区（右侧）

标题: **Product Reference**

三张同一产品的小参考图:

| # | Image | Label |
|---|-------|-------|
| 1 | 包装盒 | Packaging box |
| 2 | 正面视图 | Front view |
| 3 | 侧面/细节视图 | Side/detail view |

要求:
- 三张图中产品必须严格一致——颜色、形状、材质、包装、Logo、底座、关键细节。
- 若用户产品没有包装盒，生成一个与产品风格匹配的包装盒——但不得改变产品本体。
- 干净、居中、电商风格产品摄影。
- 每张图下方有英文标签。

### 6-Shot Breakdown 6 镜头拆解

标题: **6-Shot AI Video Storyboard** 或 **6-Shot TikTok Video Breakdown**

每个镜头卡片包含:

```
┌─────────────────────────────┐
│     Shot 01: Hook           │  ← 镜头标题
│                             │
│   [Keyframe Preview]        │  ← 关键帧预览
│                             │
│ Time: 0–2s                  │
│ Shot type: Medium close-up  │
│ Action: [一行]              │
│ Camera: [一行]              │
│ Subtitle/Line: "[字幕]"     │
└─────────────────────────────┘
```

### 默认 6 镜头结构

若用户未提供自定义镜头列表，使用此经过验证的商业结构:

**Shot 01: Hook 钩子**
- 画面: 创作者展示包装或产品亮相，面对镜头，做出吸引注意的表情或动作。
- Time: 0–2s
- Shot type: Medium close-up
- Action: 创作者将产品推向镜头或戏剧性地揭示
- Camera: Fast push-in
- Subtitle: 能钩住观众的有趣一句话

**Shot 02: Problem 问题**
- 画面: 展示使用场景中的问题或缺口——空桌面、缺乏氛围、常见痛点。
- Time: 2–4s
- Shot type: Medium
- Action: 创作者向空位或有问题的地方做手势
- Camera: Quick side move
- Subtitle: 能引起受众痛点共鸣的提问

**Shot 03: Reveal 揭示**
- 画面: 创作者将产品放入场景，成为视觉中心。
- Time: 4–6s
- Shot type: Product medium close-up
- Action: 创作者将产品放置到位
- Camera: Gentle push-in
- Subtitle: 宣告产品作为解决方案

**Shot 04: Detail 细节**
- 画面: 产品细节特写——材质、质感、涂装、关键特征。手部可辅助但不得遮挡。
- Time: 6–8s
- Shot type: Close-up
- Action: 展示纹理、雕刻、涂装或底座细节
- Camera: Detail push-in
- Subtitle: 关于品质或工艺的陈述

**Shot 05: Display 展示**
- 画面: 产品在真实使用环境中——桌面、柜架或实际场景中。创作者欣赏或互动。
- Time: 8–10s
- Shot type: Medium
- Action: 产品在生活场景中展示
- Camera: Slow lateral move
- Subtitle: 生活方式利益陈述

**Shot 06: CTA 行动号召**
- 画面: 创作者与产品同框。创作者自然推荐。产品清晰露出。
- Time: 10–12s
- Shot type: Medium close-up
- Action: 创作者指向产品并推荐
- Camera: Hold on product
- Subtitle: 行动号召或购买提示

### Continuity Requirements 连续性要求（社交商业板）

每板必须验证:

- [ ] 所有镜头中同一创作者——发型、服装、脸型、肤色、气质一致。
- [ ] 所有镜头中同一产品——颜色、形状、包装、底座、关键细节不变。
- [ ] 场景风格跨镜头统一——相同灯光方向、背景风格、色彩方案。
- [ ] 动作推进清晰——不是重复摆拍。
- [ ] 字幕安全构图——每帧底部 20% 预留为文字叠加区域。
- [ ] 全部 6 镜头映射到脚本节奏——无不服务于流程的孤立镜头。

### Visual Style Requirements 视觉风格要求

```
clean commercial storyboard, professional production board, TikTok AI video planning sheet, white background, black thin borders, neat grid layout, infographic style, readable text, high information density, practical structured layout, subtitle-safe framing
```

不要生成: 海报风格、电影概念图、花哨PPT、赛博朋克、过度广告图、混乱电商拼图、不可读小字、乱码文字、多个不同创作者身份、产品外观不一致。

---

## Format B: Fashion Director Board 服装导演板

用于服装/时尚/穿搭风格拍摄，模特展示服饰，无口播主播。源自服装直播导演分镜模板。

### 布局结构

```
┌─────────────────────────────────────┐
│   Shot Grid (3 rows × 4-5 columns)  │
│   12-15 individual shot cards       │
├─────────────────────────────────────┤
│ Rhythm  │ Camera   │ Lighting &     │
│ Struct  │ Movement │ Atmosphere     │
└─────────────────────────────────────┘
```

画幅比例: 16:9。白色或浅灰背景。干净导演分镜风格。专业商业感。

### 镜头卡片格式

每个镜头卡片遵循严格的统一结构:

```
┌──────────────────────────┐
│ 01 | LS 全景 | 0:00-0:02 │  ← 灰色标题栏
│                          │
│   [Cinematic Preview]    │  ← 写实时尚镜头预览
│                          │
│ 自然入画，建立人物关系    │  ← ≤15 字导演备注
└──────────────────────────┘
```

标题格式: `编号 | 景别缩写 | 时间码`

导演备注规则:
- 中文 ≤15 字
- 读起来像导演现场边际笔记
- 描述核心视觉时刻，而非抽象概念
- 示例: 整理衣摆突出版型 / 45°侧身展示廓形 / 推近展示印花细节

### Bottom Module 1: Rhythm Structure 节奏结构图

标题: **节奏结构（XX秒 / 卡点剪辑）**

按音乐阶段组织内容:

```
| 0–5s   | 铺垫 & 建立  | Kick / Snare          |
| 5–10s  | 动作展示     | 节奏律动              |
| 10–15s | 版型细节     | 旋律推进              |
| 15–20s | 收尾强化     | Drop / 重低音          |
```

添加强度波形图，以镜头编号（①②③...）标记时间点。

### Bottom Module 2: Camera Movement Diagram 镜头运动路径图

标题: **镜头运动路径图（参考）**

俯视空间平面图，包含:
- 编号摄影机位置（①→③→④→⑥→⑧→⑩→⑫）
- 虚线轨迹箭头
- 运动类型标注: 缓推 / 侧移 / 半环绕 / 定镜 / 推近 / 回拉

### Bottom Module 3: Lighting & Atmosphere 光影与氛围

标题: **光影与氛围（与原图一致）**

清单格式:
```
✓ 左前方暖色主光
✓ 辅助柔光
✓ 右后方轮廓光
✓ 墙面干净通透
✓ 暖白色空间
✓ 柔和景深
```

关键词: 潮流 / 街头 / 高级感 / 松弛 / 质感

### Replaceable Zone 主体替换区域

这是用户每项目唯一需要自定义的区域。其余结构保持固定。

```
【场景】[地点描述、灯光环境、场景细节]
【模特】[单一模特: 性别、年龄范围、发型、配饰、服装风格、表情]
【产品】[服装: 颜色、水洗效果、版型、印花图案、领口、袖口、衣长、下摆、面料质感、比例]
【镜头动作】[关键动作列表: 自然走入 / 整理衣摆 / 拉袖口 / 45°侧身 / 正面站姿 / 微低头]
```

### Visual Style Requirements 视觉风格要求（服装导演板）

```
导演分镜提案板, 商业广告导演分镜板, 电商服装广告Storyboard, 专业镜头语言, 信息层级清晰, 排版整洁, 高级感强, 真实摄影感, 白底或浅灰底
```

不要生成: 插画风格、海报风格、漫画风格、UI 界面风格。必须看起来像真实的导演分镜提案板。

---

## 输出格式

两种子模式，均先呈现结构化计划，再呈现压缩的图像生成器提示词。

```markdown
## Storyboard Plan: [产品名称]

### Format: [Social Commerce / Fashion Director]

[与上述所选格式匹配的完整结构化拆解]

## Compressed Prompt

[一条完整的图像生成器提示词。包含所有布局指令、风格关键词和反模式清单。]
```

## Quality Bar 质量门槛

- 所有参考图（社交商业板的创作者 + 产品）必须保持严格的身份一致性。
- 镜头卡片必须包含所有必填字段: 编号、景别、时间码、预览、动作、摄影机，以及（社交商业板）字幕行。
- 节奏模块必须将时间段映射到镜头编号和音乐节拍。
- 视觉风格关键词必须清晰描述板面格式——而非视频内容。
- 社交商业板必须提及字幕安全构图。
- 若用户提供产品/创作者参考图，精确保持其视觉身份——不得发明变体。
- 压缩提示词中必须包含反模式清单，防止常见的 AI 图像生成器漂移到海报/概念图风格。
