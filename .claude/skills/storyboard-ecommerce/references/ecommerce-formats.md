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

### Replaceable Zone 主体替换区域

每个项目唯一需要自定义的区域。根据用户是否提供了参考图，选择对应模式。

**模式 1：无参考图（需要详细描述主体外观）**

```
【场景】[地点描述、灯光环境、场景细节]
【模特】[单一模特: 性别、年龄范围、发型、配饰、服装风格、表情]
【产品】[服装: 颜色、水洗效果、版型、印花图案、领口、袖口、衣长、下摆、面料质感、比例]
【镜头动作】[关键动作列表: 自然走入 / 整理衣摆 / 拉袖口 / 45°侧身 / 正面站姿 / 微低头]
```

**模式 2：有参考图（禁止复述参考图已锁定的外观）**

当用户已提供模特/产品参考图并注册到素材槽位时，Replaceable Zone 仅需标注槽位引用，不逐项描述外貌：

```
【场景】[地点描述、灯光环境]
【模特】见 @[模特 ref] — [1-2个最显著标识]，保持参考图中面部、体型、发型不变
【产品】见 @[产品 ref] — [品类+1个关键特征]，保持参考图中版型、面料、印花不变
【镜头动作】[关键动作列表]
```

> **核心原则：参考图已锁定视觉身份——Replaceable Zone 和 Compressed Prompt 中不得逐项复述模特的面部结构、发型、体型、服装细节，也不得逐项复述产品的版型、面料、领型。这些信息由参考图承载，复述会导致生图模型重新解读而非直接引用。**

**Compressed Prompt 规则：**
- 有参考图时：镜头预览画面描述使用 ``见 @[模特 ref]`` 格式，仅描述新出现的动作和光影
- 无参考图时：需在镜头预览画面中包含主体外观描述

### 视觉风格关键词

```
导演分镜提案板, 商业广告导演分镜板, 电商服装广告Storyboard, 专业镜头语言, 信息层级清晰, 排版整洁, 高级感强, 真实摄影感, 白底或浅灰底
```

不要生成: 插画风格、海报风格、漫画风格、UI 界面风格。必须看起来像真实的导演分镜提案板。

---

## Format C: Product Showcase Board 产品展示板（通用）

用于纯产品展示——无主播/创作者/模特出镜，适用于 3C 数码、家电、家居、食品、美妆等非服装品类。产品自行在场景中展示，镜头围绕产品运动。

### 布局结构

```
┌──────────────────────────────────────────────┐
│              Top Info Bar                     │
│  Product | Category | Key Feature | Format   │
├──────────────────┬───────────────────────────┤
│ Product Ref (L)  │  Scene Ref (R)            │
│ 3 ref images     │  3 ref images             │
├──────────────────┴───────────────────────────┤
│        6-Shot Product Storyboard             │
│  Shot 01 │ Shot 02 │ Shot 03 │ ... │ Shot 06│
│  [card]  │ [card]  │ [card]  │     │ [card]  │
└──────────────────────────────────────────────┘
```

画幅比例: 16:9。白色或浅灰背景，黑色细边框，干净电商产品摄影风格。无创作者区——产品为绝对视觉中心。

### Top Info Bar 顶部信息栏

| 单元格 | 内容 |
|---|---|
| **Product** | 产品名称 |
| **Category** | 品类（3C/家电/家居/食品/美妆/...） |
| **Key Feature** | 一句话核心卖点 |
| **Format** | 平台 / 画幅比例 / 时长 |

### Product Reference Area 产品参考区（左侧）

标题: **Product Reference**。三张同一产品的不同角度:

| # | Image | Label |
|---|---|---|
| 1 | 正面主视图 | Front hero view |
| 2 | 45°侧视图 | 3/4 angle view |
| 3 | 细节特写 | Detail close-up |

要求: 产品严格一致——颜色、形状、材质、Logo、关键细节。干净、居中、电商风格产品摄影。每张图下方英文标签。

### Scene Reference Area 场景参考区（右侧）

标题: **Scene Reference**。三张使用场景/氛围参考图:

| # | Image | Label |
|---|---|---|
| 1 | 主场景 | Main scene |
| 2 | 光影参考 | Lighting ref |
| 3 | 氛围/风格 | Mood/style ref |

要求: 三张图保持统一灯光方向和色调。展示产品预期使用环境，非产品本身。每张图下方英文标签。

### 6 镜头卡片格式

```
┌─────────────────────────────┐
│     Shot 01: Showcase       │
│                             │
│   [Keyframe Preview]        │
│                             │
│ Time: 0–2s                  │
│ Shot type: [景别]           │
│ Action: [一行]              │
│ Camera: [一行]              │
└─────────────────────────────┘
```

无字幕行——纯产品展示，字幕由后期叠加。

### 默认 6 镜头结构

| 镜头 | 名称 | 时间 | 景别 | 画面 | 运镜 |
|---|---|---|---|---|---|
| 01 | Showcase 亮相 | 0–2s | Medium product | 产品在场景中的初始亮相，建立空间和产品位置 | Slow push-in |
| 02 | Detail 细节 | 2–4s | Close-up / Macro | 材质、纹理、工艺细节特写 | Locked / slow dolly |
| 03 | Feature 功能 | 4–6s | Medium close-up | 展示核心功能或使用方式（开合/旋转/交互） | Gentle orbit |
| 04 | Use 使用场景 | 6–8s | Medium | 产品在真实使用环境中——手部入镜自然操作（若适用） | Lateral track |
| 05 | Atmosphere 氛围 | 8–10s | Wide / Medium | 产品完整呈现于场景中，灯光烘托氛围 | Slow crane up or pull-back |
| 06 | Packshot 定妆 | 10–12s | Product hero | 产品正面主视觉，干净背景，Logo 清晰 | Locked / subtle push-in |

### 连续性要求

- [ ] 所有镜头中同一产品——颜色、形状、材质、Logo 不变
- [ ] 所有镜头中同一灯光方向——光源位置、色温、强度一致
- [ ] 场景色调跨镜头统一——背景色/材质/道具不跳变
- [ ] 动作推进清晰——不是重复摆拍
- [ ] 无创作者/模特——若手部入镜，保持同一肤色/手势风格
- [ ] 产品比例在所有镜头中一致——无扭曲或缩放异常

### 视觉风格关键词

```
clean product photography storyboard, commercial product showcase board, e-commerce product planning sheet, white background, black thin borders, neat grid layout, professional product lighting, centered composition, high detail product texture, studio photography style
```

不要生成: 海报风格、电影概念图、花哨PPT、赛博朋克、过度广告图、混乱电商拼图、不可读小字、乱码文字、人物/模特/创作者、产品外观不一致、手部变形。
