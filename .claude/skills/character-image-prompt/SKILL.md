---
name: character-image-prompt
description: 将 director-character 产出的角色身份定义编译为多视角电影级角色设计板（Character Sheet）提示词，适配 AI 图像生成平台（MJ/Flux/即梦/GPT Image）。产出用于 AI 视频一致性控制的角色设定图——非单人肖像，非艺术身份板。当用户已有角色参考图像或 director-character 角色定义，需要生成可在生图平台使用的 Character Sheet 提示词时使用。亦在 director-core 于 STATE 3 完成后路由至此。
---

# 角色生图提示词 — Character Sheet 编译器

## 概览

```
[参考图像] 或 [director-character 关键字段]
              +
        [项目上下文]
              ↓
          [编译器]
              ↓
  Character Sheet 提示词（MJ / Flux / 即梦 / GPT Image）
```

**核心定义：**

> 角色设定参考图 = **"用于AI视频一致性控制的多视角电影级角色设计板（Character Sheet）"**
>
> 本技能产出的是 **Character Sheet 生图提示词**，不是单人肖像，不是艺术身份板。
> 目的是 AI 视频跨镜头角色一致性——Character Sheet 是锁定角色身份、贯穿所有生成视频帧的参考资产。

**输入来源：**

| 来源 | 作用 |
|------|------|
| 参考图像（推荐） | 角色外观的视觉锚点 |
| director-character 输出 | 完整角色档案：面部、发型、体型、服装、道具、表情系统 |
| 项目上下文 | 项目类型、情绪基调——用于推导视觉风格方向 |

---

## 输出结构 — 12段角色设计板档案

| 段 | 内容 | 用途 |
|----|------|------|
| [0] | Character Reference ID | 角色标识、叙事角色、优先级、一致性权重、引用标签 |
| [1] | Core Identity | 年龄、职业、性格、情绪功能、视觉签名、关键词 |
| [2] | Face Identity Lock | 脸型、肤色、眼型眼色、眉型、鼻型、嘴型、下颌、识别特征 |
| [3] | Hair Lock | 长度、发型、发色、发质、分线、动态 |
| [4] | Body Lock | 身高、体型、体态、动作风格、标志性手势 |
| [5] | Wardrobe Lock | 主服装、颜色调色板、面料、合身度、配饰、替换服装 |
| [6] | Prop Lock | 主/次要道具、标志物品、互动方式 |
| [7] | Expression System | 表情范围及体态表现（3-5种关键情绪） |
| [8] | Character Sheet View Requirements | 必含视角清单 |
| [9] | Visual Style Settings | 风格、写实度、灯光、色彩情绪、镜头感、背景 |
| [10] | Seedance Reference Settings | 锁定开关、引用优先级、引用边界 |
| **[11]** | **Character Sheet Image Prompt** | **← 最终交付物。可直接粘贴到 AI 生图平台。** |
| [12] | Negative Prompt | 负面约束清单 |

---

## [11] Character Sheet Image Prompt — 模板

### 无参考图像时

```
Professional cinematic character sheet showing {角色名称},
age {年龄},

{脸型}, {下颌}, {肤色}, {肤质},
{眼型}, {眼色},
{眉型},
{鼻型}, {嘴型/唇型},
{发长}, {发型}, {发色}, {发质},

{体型}, {身高}, {体态},

wearing {全套服装描述},
{配饰列表},

show front view, side view, 3/4 view, rear view,
full body standing pose, {签名姿态1}, {签名姿态2},
face close-up, hair detail, hand detail,
expression sheet: {情绪1}, {情绪2}, {情绪3}, {情绪4}, {情绪5},

professional character design sheet,
neutral background,
cinematic realism,
high detail skin texture, visible fabric weave,
clean presentation layout,
consistent identity across all views
```

### 有参考图像时

```
Professional cinematic character sheet using the reference image as identity source,
perform color correction, maintain subject identity accuracy,

show front view, side view, 3/4 view, rear view,
full body standing pose, {签名姿态1}, {签名姿态2},
face close-up, hair detail, hand detail,
expression sheet: {情绪1}, {情绪2}, {情绪3}, {情绪4}, {情绪5},

same face, same hair, same body, same wardrobe as reference image,
professional character design sheet,
neutral background,
cinematic realism,
clean presentation layout,
consistent identity across all views
```

---

## [12] Negative Prompt

```
no face change
no hairstyle change
no body proportion change
no random age shift
no wardrobe change
no extra accessories
no extra characters
no duplicate characters
no distorted face
no bad anatomy
no extra fingers
no identity drift
no inconsistent skin tone
no random props
no cartoon style unless requested
no anime unless requested
no over-stylization
no watermark
no logo
no text
no poster layout
no text-heavy poster layout
```

---

## 必含视角（强制）

每个 Character Sheet 必须包含：

| 视角 | 必含 | 说明 |
|------|------|------|
| 正面全身（Front view） | ✓ | |
| 侧面全身（Side view） | ✓ | |
| 3/4角度全身（3/4 view） | ✓ | |
| 背面全身/轮廓（Rear view） | ✓ | |
| 面部特写（Face close-up） | ✓ | 中性表情，正面 |
| 发型细节（Hair detail） | ✓ | 展示发质纹理 |
| 手部细节（Hand detail） | ✗ | 若手部有叙事重要性 |
| 全身站姿（Full body standing pose） | ✓ | 标志性站姿 |
| 行走姿态（Walking pose） | ✗ | 若动态重要 |
| 动作姿态（Action pose） | ✗ | 若有标志性动作 |
| 表情变化（Expression sheet） | ✓ | 3-5种情绪变化 |

---

## 视觉风格设置

| 参数 | 默认值 | 可选 |
|------|--------|------|
| 视觉风格 | 电影级写实（cinematic realism） | 风格化动漫、半写实、概念设计风、编辑艺术风、3D渲染——根据项目类型推导 |
| 灯光 | 中性影棚光 + 轻微轮廓光 | 戏剧性轮廓光、柔光漫射、高对比——根据情绪基调推导 |
| 背景 | 中性灰色或柔和渐变影棚背景 | 干净米白色——不能干扰角色识别 |
| 镜头感 | 50mm 人像 | 85mm 编辑风、35mm 场景感 |
| 版式 | 干净专业展示布局 | 非对称编辑布局（如项目风格需要） |

---

## 一致性锁定

所有视图和所有下游 Seedance 提示词必须保持：

| 锁定项 | 范围 |
|--------|------|
| 面部锁定 | 脸型、五官、比例、年龄感 |
| 发型锁定 | 长度、发型、发色、发质 |
| 体型锁定 | 身材比例、身高感、肢体特征 |
| 服装锁定 | 主服装、配饰、鞋子 |
| 道具锁定 | 固定物品、武器、饰品 |
| 情绪锁定 | 性格气质、情绪基调 |

---

## 编译流程

1. 从 `director-character` 输出加载角色档案 → 填入 [0]-[10] 段
2. 根据项目上下文推导 [9] 视觉风格设置
3. 填入 [11] Character Sheet Image Prompt 模板
4. 附加 [12] Negative Prompt
5. 交付：[11] + [12] 可直接粘贴到用户选择的 AI 生图平台

---

## 两种输入模式

### 模式 A：有参考图像

用户已有角色图像。提示词使用图像作为身份来源。

- 提示词中写："using the reference image as identity source"
- 角色外观由参考图像锁定
- 生图平台专注于创建多视角 Character Sheet 布局

### 模式 B：无参考图像

用户仅有 director-character 角色定义。提示词包含完整外观细节。

- 提示词填入所有面部/发型/体型/服装字段
- 生图平台同时创建角色外观和多视角布局

---

## 多Look扩展

角色有多套服装时，为每套额外生成提示词：

```
Same character identity as {角色名称} character sheet,
same face, same hair, same body, same skin tone,

wardrobe changed to: {新服装描述},

show front view, side view, 3/4 view, rear view,
full body standing pose,

neutral background,
cinematic realism,
consistent identity with {角色名称} character sheet
```

---

## 平台适配

Character Sheet 提示词是平台无关的。按目标平台调整：

| 平台 | 语言 | 调整 | 参数 |
|------|------|------|------|
| **Midjourney** | 英文（默认） | 保持原样 | `--ar 16:9 --style raw --v 6.1` |
| **Flux** | 英文（默认） | 保持原样，自然语言流 | 无 |
| **GPT Image** | 英文（默认） | 保持原样 | 无 |
| **即梦 (Jimeng)** | 翻译为中文 | 保留多视角结构，负向提示词追加中文负面关键词 | 无 |
| **可灵 (Kling)** | 翻译为中文 | 强化一致性表述，追加负面关键词 | 无 |

---

## 验证清单

- [ ] [11] Character Sheet Image Prompt 自包含——可直接粘贴
- [ ] 所有必含视角已列出（front, side, 3/4, rear, face close-up, expression sheet）
- [ ] 面部/发型/体型/服装参数与 director-character 定义一致
- [ ] [12] Negative Prompt 覆盖全部约束项
- [ ] 背景为中性，不干扰角色识别
- [ ] 无"艺术身份板"用语——使用"电影级角色设计板"
- [ ] 无强制网格/蓝图/目录式布局——风格由项目上下文推导
- [ ] 若目标平台为即梦/可灵，已翻译为中文并追加中文负面关键词

---

## 集成

由 `director-core` 调用或 STATE 3 后独立使用：

1. 从 `director-character` 加载角色档案
2. 编译为 [0]-[12] 完整 Character Sheet Profile + Image Prompt
3. 用户确认后，将 [11] 粘贴到选择的 AI 生图平台生成 Character Sheet 图像
4. 生成的 Character Sheet 作为 `` `图片N` `` 用于 STATE 6 `seedance-video-prompt`

> ⚠️ 注意：生成的 Character Sheet（多视图角色设定板）适合作为 AI 图像生成器的角色设计参考，但不可直接作为 Seedance 视频生成的角色参考图。Seedance 视频生成建议使用独立的角色面部特写（大头照）和全身照。
