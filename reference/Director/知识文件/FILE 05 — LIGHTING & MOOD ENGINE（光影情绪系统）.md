 
# 📦 SEEDANCE 2.0 SYSTEM ENGINE SPEC

## FILE 05 — LIGHTING & MOOD ENGINE（光影情绪系统）

---

# 🎬 1. 系统定位（System Purpose）

Lighting & Mood Engine 是 Seedance 2.0 的“情绪视觉调色系统”。

> 它负责将“情绪 + 场景 + 叙事意图”转换为可执行的电影级光影结构。

---

## 🧠 核心定义

```text id="lm01"
Emotion State
→ Mood Mapping
→ Light Source Logic
→ Color Temperature System
→ Shadow Design
→ Atmospheric Rendering
→ Seedance Lighting Output
```

---

# 🌈 2. 情绪 → 光影映射系统（Emotion Light Engine）

系统必须将情绪转换为“可视光结构”。

---

## ❤️ 爱 / 温柔 / 亲密

* color temperature: warm gold / soft amber
* light type: diffused soft light
* shadow: minimal / soft edges
* contrast: low
* mood effect: emotional openness

---

## 😨 恐惧 / 压迫

* color temperature: cold blue / green tint
* light type: flickering or unstable light
* shadow: hard deep shadows
* contrast: high
* mood effect: psychological tension

---

## 🧍 孤独 / 空虚

* color temperature: desaturated cold tones
* light type: distant ambient light
* shadow: long shadows
* contrast: medium-high
* mood effect: emotional distance

---

## ⚡ 紧张 / 冲突

* color temperature: mixed warm/cold clash
* light type: directional sharp light
* shadow: fragmented shadows
* contrast: very high
* mood effect: instability

---

## 🌌 神秘 / 未知

* color temperature: deep blue / purple
* light type: backlight / silhouette lighting
* shadow: dominant silhouettes
* contrast: controlled low visibility
* mood effect: concealment

---

# 💡 3. 光源结构系统（Lighting Source Engine）

每个场景必须定义光源逻辑：

---

## 📦 Light Types

### 1. Key Light（主光）

* 主情绪来源
* 决定角色面部可见性

### 2. Fill Light（补光）

* 控制阴影柔和程度

### 3. Rim Light（轮廓光）

* 用于人物分离背景

### 4. Ambient Light（环境光）

* 决定整体空间情绪

---

## 🎯 规则：

* Key Light = 情绪主导
* Fill Light = 情绪修饰
* Rim Light = 人物强调
* Ambient Light = 场景氛围

---

# 🌫 4. 氛围系统（Atmosphere Engine）

环境必须“可呼吸”，不能静态。

---

## 📦 Atmosphere Elements

* fog density（雾气浓度）
* particle motion（粒子运动）
* air humidity effect（空气湿度）
* dust floating (灰尘漂浮)
* rain / snow / wind

---

## 🎬 示例映射：

| 情绪 | 氛围                            |
| -- | ----------------------------- |
| 爱  | soft air, warm haze           |
| 恐惧 | dense fog, unstable particles |
| 孤独 | empty air, still atmosphere   |
| 紧张 | fast-moving particles         |

---

# 🎨 5. 色彩系统（Color Grading Engine）

系统必须定义“情绪调色板”。

---

## 🎨 Color Logic Rules

* warm tones → 情绪靠近
* cold tones → 情绪疏离
* desaturated → 情绪低落
* high saturation → 情绪爆发

---

## 📦 情绪色板：

### ❤️ Romantic Palette

* gold / pink / soft orange

### 😨 Horror Palette

* cyan / deep green / dark blue

### 🧍 Lonely Palette

* gray / faded blue / muted tones

### ⚡ Tension Palette

* red / blue contrast / neon clash

---

# 🧠 6. 光影叙事逻辑（Lighting Narrative Engine）

光影不是装饰，而是“叙事结构”。

---

## 📈 Lighting Story Rules

* 光变强 → 情绪升级
* 光变弱 → 情绪崩塌
* 阴影扩展 → 未知增强
* 光源移动 → 情绪变化

---

## 🎬 示例：

```text id="ln01"
Scene begins: soft ambient light
→ character emotion rises
→ key light intensifies
→ shadows deepen
→ climax = harsh contrast lighting
```

---

# 🎥 7. 摄影机-光影联动系统（Camera-Light Sync）

---

## 📷 联动规则：

### ✔ camera push-in

→ light intensity increases

### ✔ camera pull-out

→ ambient light dominates

### ✔ handheld motion

→ flickering or unstable lighting

### ✔ static shot

→ controlled stable lighting

---

# 🌑 8. 阴影系统（Shadow Engine）

阴影 = 心理结构表达。

---

## 📦 Shadow Types

* soft shadow → 安全 / 温柔
* hard shadow → 冲突 / 压迫
* broken shadow → 混乱 / 分裂
* long shadow → 孤独 / 时间延伸

---

# 🔁 9. 连续性光影系统（Lighting Continuity Engine）

系统必须保证：

---

## ❗规则：

* 光源方向一致
* 时间变化必须合理（不能瞬间白天/夜晚）
* 色温变化必须渐进
* 阴影结构必须连续

---

# 🎬 10. Lighting → Seedance 输出格式

---

## 📦 LIGHTING BLOCK OUTPUT

```text id="lt_out"
Lighting:
- key light:
- fill light:
- rim light:
- ambient light:

Color Temperature:
- warm / cold / mixed

Contrast Level:
- low / medium / high

Atmosphere:
- fog / particles / air behavior

Shadow Design:
- type and emotional meaning

Mood Function:
- how lighting drives emotion
```

---

# 🚨 11. 禁止规则（Hard Constraints）

❌ 禁止：

* 无光影逻辑
* 光影与情绪无关
* 色彩随机
* 光源不明确
* 阴影缺失

---

# ✅ 必须：

✔ 光 = 情绪载体
✔ 阴影 = 心理结构
✔ 色彩 = 情绪温度
✔ 环境 = 情绪延伸

---
 