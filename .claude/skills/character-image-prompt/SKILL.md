---
name: character-image-prompt
description: 将 director-character 产出的角色身份定义（文本级设计文档）编译为可直接粘贴到 AI 图像生成平台（Midjourney / Flux / 即梦 / 可灵）的角色设定图提示词。遵循 Seedance 2.0 Character Sheet 规范（prd2.md / prd3.md）——多视角角色设计板，非单人肖像。用于角色生图提示词、character sheet image prompt、角色参考图生成提示词，或 director-core 在 STATE 3 完成后路由至此。当用户已有角色身份定义，需要将其转化为可在 MJ/Flux/即梦 直接使用的角色设定板提示词时使用。
---

# Character Image Prompt — 角色生图提示词编译器

## 概览

这是 **角色身份定义 → 生图平台提示词** 的编译器。它接收 `director-character` 产出的角色身份定义（Character Identity Definition），按 Seedance 2.0 Character Sheet 规范（prd2.md / prd3.md）编译为可直接粘贴到 Midjourney / Flux / 即梦 / 可灵 的生图提示词。

**关键区别：**
- `director-character`（STATE 3）：产出角色身份**定义**（文本级设计文档）——定义角色是谁、长什么样
- `character-image-prompt`（本技能）：将身份定义**编译**为生图平台可执行的提示词——告诉 AI 图像生成器怎么画 Character Sheet
- `seedance-video-prompt`（STATE 6）：引用已生成的角色图作为 `@[ref]`，编译为视频平台提示词

## 编译原则

> 角色生图提示词是**结构化视觉指令**。必须简洁、精确、平台兼容——不是散文描述。

编译器将角色身份定义的各字段映射为生图提示词的标准结构：
1. **身份锁定层**（谁）→ name, age, face, skin, hair, body
2. **服装层**（穿什么）→ wardrobe, color, material, fit
3. **视图层**（怎么展示）→ 多视角列表（front/side/3/4/rear/close-up）
4. **风格层**（什么质感）→ visual style, lighting, background
5. **约束层**（不能出现什么）→ 负面约束清单

## 输入要求

编译前，验证角色身份定义包含以下字段：

- [ ] Character Name / ID
- [ ] Age / Age Range
- [ ] Face: shape, skin tone, eye shape/color, eyebrows, nose, mouth, jaw
- [ ] Hair: length, style, color, texture
- [ ] Body: height, type, build, posture
- [ ] Wardrobe: main outfit, color palette, fabric type, fit
- [ ] Props（如适用）
- [ ] Expression range（3-5种情绪）

如有字段缺失，路由回 `director-character` 补全。

## 输出结构

### 格式：Complete Character Profile + Image Prompt

按 prd2.md 的 12 段模板输出：

| 段 | 内容 | 说明 |
|----|------|------|
| [0] | Character Reference ID | 角色标识、优先级、引用标签 |
| [1] | Core Identity | 年龄、职业、性格、视觉签名、关键词 |
| [2] | Face Identity Lock | 面部全部参数（形状/肤色/五官/特征） |
| [3] | Hair Lock | 发型全部参数（长度/风格/颜色/质地/分线） |
| [4] | Body Lock | 体型全部参数（身高/体重/比例/动作签名） |
| [5] | Wardrobe Lock | 服装（主装+配色+材质），支持多Look |
| [6] | Prop Lock | 道具（如有） |
| [7] | Expression System | 表情变化列表（5种） |
| [8] | View Requirements | 必须包含的视角清单 |
| [9] | Visual Style Settings | 风格/写实度/灯光/镜头感/背景 |
| [10] | Seedance Reference Settings | 锁定开关 + 引用优先级 + 引用边界 |
| **[11]** | **Character Sheet Image Prompt** | **← 可直接粘贴到生图平台** |
| [12] | Negative Prompt | 负面约束清单 |

---

### [11] Character Sheet Image Prompt — 完整格式规范

#### 主角色设定板（标准模板）

```
Professional cinematic character sheet of [Character Name],
age [X],
[face shape], [jawline], [skin tone], [skin texture],
[eye shape], [eye color],
[eyebrow description],
[nose description], [lip description],
[hair length], [hair style], [hair color], [hair texture],
[body type], [height], [posture],

wearing [outer layer], [fabric], [fit],
[upper clothing], [fabric],
[lower clothing], [fit],
[shoes],
[accessories if any],

show front view, side view, 3/4 view, rear view,
full body standing pose, [signature pose 1], [signature pose 2], [action pose],
face close-up, hair detail,
expression sheet: [emotion 1], [emotion 2], [emotion 3], [emotion 4], [emotion 5],

professional character design sheet,
clean neutral gray studio background,
cinematic realism, photographic quality,
neutral studio lighting with subtle rim light,
high detail skin texture, visible fabric weave,
clean grid presentation layout,
consistent identity across all views
```

#### 多Look扩展板模板

当角色有多套服装时，为每套额外生成：

```
Same character identity as [Character Name] character sheet,
same face, same hair, same body, same skin,

wardrobe changed to: [outer layer], [fabric], [fit],
[upper clothing],
[lower clothing],

show front view, side view, 3/4 view, rear view,
full body standing pose, [relevant poses],

clean neutral gray studio background,
cinematic realism, consistent identity with [Character Name] character sheet
```

---

### [12] Negative Prompt — 标准清单

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
no cartoon style
no anime style
no 3D render style
no over-stylization
no watermark
no logo
no text
no poster layout
no complex background
no text-heavy layout
```

---

## 平台适配

| 平台 | 调整 |
|------|------|
| **Midjourney** | 保持英文，末尾加 `--ar 16:9 --style raw --v 6.1` |
| **Flux** | 保持英文，自然语言流，无需特殊参数 |
| **即梦** | 翻译为中文，保留多视角结构，加负面词 |
| **可灵** | 翻译为中文，强一致性强调 |

---

## 验证清单

交付前逐项验证：

- [ ] [11] Image Prompt 可直接复制粘贴使用
- [ ] 所有视角均已列出（front/side/3-4/rear/close-up）
- [ ] 面部/发型/体型/服装参数与角色身份定义一致
- [ ] 多Look扩展板声明了"same face, same hair, same body"
- [ ] [12] Negative Prompt 覆盖全部约束项
- [ ] 提示词简洁、无冗余修饰语、无散文风格
- [ ] 无"Generate a prompt"等元指令——提示词本身即是最终产物

## 集成

被 `director-core` 调用或在 STATE 3 完成后独立调用：
- 加载 `director-character` 产出的角色身份定义
- 编译为 [0]-[12] 完整 Profile + 生图提示词
- 用户确认后，去 MJ/Flux/即梦 粘贴 [11] 中的提示词生成角色参考图
- 生成的角色参考图作为 STATE 6 `seedance-video-prompt` 的 `@[character ref]` 输入
