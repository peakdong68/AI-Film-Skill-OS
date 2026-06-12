# 电商分镜格式 — 内置参考

供 `storyboard-ecommerce` 按需加载。包含三种商业格式的完整规格。

---

## Format A: Social Commerce Board 社交商业板

用于 TikTok/Reels/Shorts 风格的产品视频，创作者/主播出镜展示产品。

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

画幅比例: 4:3 或 16:9。白色背景，黑色细边框，干净网格布局。

### Top Info Bar 顶部信息栏

一行 6 个信息单元格:

| 单元格 | 内容 |
|---|---|
| **Product** | 产品名称 |
| **Audience** | 目标受众 |
| **Core Selling Point** | 一句话价值主张 |
| **Hook** | 开场钩子文案 |
| **Video Goal** | 结构流程（Hook → Problem → Reveal → Detail → Display → CTA） |
| **Format** | 平台 / 画幅比例 / 时长 / 语言 |

### Creator Reference Area 创作者参考区（左侧）

标题: **Creator Reference**。三张同一创作者小参考图:

| # | Image | Label |
|---|---|---|
| 1 | 正面半身照 | Front half-body |
| 2 | 表情特写 | Expression close-up |
| 3 | 侧面半身照 | Side half-body |

要求: 同一人——脸型、发型、服装、肤色、气质必须一致。看起来像真实的短视频创作者。背景可暗示直播/使用环境。每张图下方英文标签。

### Product Reference Area 产品参考区（右侧）

标题: **Product Reference**。三张同一产品小参考图:

| # | Image | Label |
|---|---|---|
| 1 | 包装盒 | Packaging box |
| 2 | 正面视图 | Front view |
| 3 | 侧面/细节视图 | Side/detail view |

要求: 产品严格一致。若无包装盒，生成风格匹配的包装盒——不得改变产品本体。干净、居中、电商风格产品摄影。每张图下方英文标签。

### 6 镜头卡片格式

```
┌─────────────────────────────┐
│     Shot 01: Hook           │
│                             │
│   [Keyframe Preview]        │
│                             │
│ Time: 0–2s                  │
│ Shot type: Medium close-up  │
│ Action: [一行]              │
│ Camera: [一行]              │
│ Subtitle/Line: "[字幕]"     │
└─────────────────────────────┘
```

### 默认 6 镜头结构

| 镜头 | 名称 | 时间 | 景别 | 画面 | 运镜 | 字幕 |
|---|---|---|---|---|---|---|
| 01 | Hook 钩子 | 0–2s | Medium close-up | 创作者展示产品亮相 | Fast push-in | 吸引注意的一句话 |
| 02 | Problem 问题 | 2–4s | Medium | 展示使用场景中的痛点 | Quick side move | 引起共鸣的提问 |
| 03 | Reveal 揭示 | 4–6s | Product MCU | 产品放入场景，成为视觉中心 | Gentle push-in | 宣告产品为解决方案 |
| 04 | Detail 细节 | 6–8s | Close-up | 产品材质/质感/特征特写 | Detail push-in | 品质或工艺陈述 |
| 05 | Display 展示 | 8–10s | Medium | 产品在真实使用环境中 | Slow lateral move | 生活方式利益陈述 |
| 06 | CTA 行动号召 | 10–12s | Medium close-up | 创作者与产品同框推荐 | Hold on product | 行动号召/购买提示 |

### 连续性要求

- [ ] 所有镜头中同一创作者——发型、服装、脸型、肤色、气质一致
- [ ] 所有镜头中同一产品——颜色、形状、包装、关键细节不变
- [ ] 场景风格跨镜头统一——相同灯光方向、背景风格、色彩方案
- [ ] 动作推进清晰——不是重复摆拍
- [ ] 字幕安全构图——每帧底部 20% 预留为文字叠加区域
- [ ] 全部 6 镜头映射到脚本节奏——无不服务于流程的孤立镜头

### 视觉风格关键词

```
clean commercial storyboard, professional production board, TikTok AI video planning sheet, white background, black thin borders, neat grid layout, infographic style, readable text, high information density, practical structured layout, subtitle-safe framing
```

不要生成: 海报风格、电影概念图、花哨PPT、赛博朋克、过度广告图、混乱电商拼图、不可读小字、乱码文字、多个不同创作者身份、产品外观不一致。

---

## Format B: Fashion Director Board 服装导演板

用于服装/时尚/穿搭风格拍摄，模特展示服饰，无口播主播。

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

画幅比例: 16:9。白色或浅灰背景。干净导演分镜风格。

### 镜头卡片格式

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

导演备注规则: 中文 ≤15 字，读起来像导演现场边际笔记，描述核心视觉时刻。示例: `整理衣摆突出版型` / `45°侧身展示廓形` / `推近展示印花细节`

### Bottom Module 1: Rhythm Structure 节奏结构图

标题: **节奏结构（XX秒 / 卡点剪辑）**

```
| 0–5s   | 铺垫 & 建立  | Kick / Snare          |
| 5–10s  | 动作展示     | 节奏律动              |
| 10–15s | 版型细节     | 旋律推进              |
| 15–20s | 收尾强化     | Drop / 重低音          |
```

添加强度波形图，以镜头编号（①②③...）标记时间点。

### Bottom Module 2: Camera Movement Diagram 镜头运动路径图

标题: **镜头运动路径图（参考）**

俯视空间平面图，含编号摄影机位置、虚线轨迹箭头、运动类型标注（缓推 / 侧移 / 半环绕 / 定镜 / 推近 / 回拉）。

### Bottom Module 3: Lighting & Atmosphere 光影与氛围

标题: **光影与氛围（与原图一致）**

```
✓ 左前方暖色主光
✓ 辅助柔光
✓ 右后方轮廓光
✓ 墙面干净通透
✓ 暖白色空间
✓ 柔和景深
```

关键词: 潮流 / 街头 / 高级感 / 松弛 / 质感

### Replaceable Zone

The only area that needs customization per project. Choose the matching mode based on whether the user has provided reference images.

**Mode 1: No reference images (detailed subject appearance description required)**

```
[Scene] [Location description, lighting environment, scene details]
[Model] [Single model: gender, age range, hairstyle, accessories, clothing style, expression]
[Product] [Garment: color, wash effect, fit, print pattern, collar, cuff, length, hem, fabric texture, proportions]
[Shot Action] [Key action list: walk in naturally / adjust hem / pull cuff / 45° side profile / front pose / slight head tilt]
```

**Mode 2: Reference images exist (do not enumerate appearance already locked in reference images)**

When the user has provided model/product reference images registered in material slots, the Replaceable Zone only needs slot references — do not enumerate appearance details:

```
[Scene] [Location description, lighting environment]
[Model] See @[model ref] — [1-2 most distinctive identifiers], keep face, body type, hairstyle from reference unchanged
[Product] See @[product ref] — [category + 1 key feature], keep fit, fabric, print from reference unchanged
[Shot Action] [Key action list]
```

> **Core principle: the reference image already locks visual identity — do not enumerate model facial structure, hairstyle, body type, or wardrobe details in the Replaceable Zone or Compressed Prompt, nor product fit, fabric, or collar details. This information is carried by the reference image; re-enumeration causes the image generation model to reinterpret rather than directly reference.**

**Compressed Prompt rules:**
- With reference images: shot preview descriptions use `` See @[model ref] `` format, only describing newly added motion and lighting
- Without reference images: include subject appearance description in shot previews


