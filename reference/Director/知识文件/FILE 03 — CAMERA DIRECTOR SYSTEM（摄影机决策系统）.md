 
# 📦 SEEDANCE 2.0 SYSTEM ENGINE SPEC

## FILE 03 — CAMERA DIRECTOR SYSTEM（摄影机决策系统）

---

# 🎬 1. 系统定位（System Purpose）

Camera Director System 是 Seedance 2.0 的“视觉决策大脑”。

> 它负责把“镜头内容”转化为“摄影机如何看这个世界”。

---

## 🧠 核心定义

```text id="cd01"
Shot Intent
→ Emotional State
→ Visual Priority
→ Camera Decision
→ Lens + Movement + Angle
→ Executable Camera Language
```

---

# 🎥 2. 摄影机决策三层结构（Camera Decision Stack）

系统必须在每个镜头中同时决策三件事：

---

## 🧩 Layer 1：视觉优先级（Visual Priority）

判断当前镜头“看什么最重要”

### 优先级规则：

1. Emotion（情绪）→ 必须优先展示脸/身体
2. Action（动作）→ 展示行为过程
3. Environment（环境）→ 展示空间关系

---

## 🧠 Layer 2：镜头语义选择（Shot Semantics）

系统自动选择镜头语义：

| 语义类型     | 含义   |
| -------- | ---- |
| Observe  | 客观观察 |
| Immerse  | 沉浸体验 |
| Reveal   | 信息揭示 |
| Confront | 情绪冲突 |
| Isolate  | 孤立人物 |
| Expand   | 空间扩展 |

---

## 🎬 Layer 3：摄影机执行层（Camera Execution Layer）

最终输出必须包含：

* shot type
* angle
* movement
* lens behavior

---

# 🎭 3. 情绪 → 摄影机决策系统（Emotion Camera Engine）

---

## ❤️ 情绪映射规则

### 💞 爱 / 浪漫

* Camera: slow dolly-in
* Angle: eye-level
* Lens: shallow depth
* Motion intent: emotional convergence

---

### 😨 恐惧 / 压迫

* Camera: handheld / jitter
* Angle: low + close-up
* Lens: tight framing
* Motion intent: instability

---

### 🧍 孤独 / 空虚

* Camera: wide static shot
* Angle: high or distant
* Lens: deep focus
* Motion intent: emotional distance

---

### ⚡ 紧张 / 冲突

* Camera: fast tracking / cut rhythm
* Angle: Dutch angle
* Lens: partial focus
* Motion intent: instability + tension

---

### 🌌 神秘 / 未知

* Camera: slow orbit or static silhouette
* Angle: backlight framing
* Lens: silhouette focus
* Motion intent: concealment

---

# 🎥 4. 镜头运动生成系统（Camera Motion Engine）

系统必须从以下库中选择：

---

## 📦 Motion Library

### 1. Static Frame

* 用于压迫 / 观察 / 情绪停顿

### 2. Slow Dolly-In

* 情绪逐渐增强
* 关系靠近

### 3. Dolly-Out

* 情绪抽离
* 孤独感增强

### 4. Tracking Shot

* 跟随动作
* 行为推进

### 5. Orbit Shot

* 情绪包围
* 关系复杂

### 6. Handheld

* 现实感
* 不稳定心理

### 7. Crane / Drone

* 空间扩展
* 史诗感

---

# 🎯 5. 镜头角度决策系统（Angle Engine）

---

## 📐 Angle Logic Rules

| Angle         | Meaning | Usage   |
| ------------- | ------- | ------- |
| Eye-level     | 平衡      | 对话 / 现实 |
| Low angle     | 压迫      | 权力 / 威胁 |
| High angle    | 脆弱      | 孤立 / 失控 |
| Dutch angle   | 混乱      | 紧张 / 崩溃 |
| Over-shoulder | 关系      | 对话冲突    |
| POV           | 沉浸      | 第一视角体验  |

---

# 🎬 6. 镜头构图系统（Framing Engine）

---

## 🧩 构图规则：

### ✔ Rule 1：情绪中心优先

* 人脸 > 动作 > 环境

---

### ✔ Rule 2：空间关系表达情绪

* 空旷 = 孤独
* 紧缩 = 压迫
* 对称 = 控制感
* 不对称 = 不安

---

### ✔ Rule 3：前景/背景层级

* 前景遮挡 = 心理障碍
* 背景模糊 = 情绪隔离

---

# 🌫 7. 光影 + 摄影机联动系统

摄影机必须“理解光”：

---

## 🔆 光影驱动镜头行为：

* 强背光 → silhouette shot
* 低光 → close-up + noise texture
* 柔光 → slow motion + dolly-in
* 闪烁光 → handheld instability

---

# 🧠 8. 摄影机叙事逻辑（Narrative Camera System）

摄影机必须有“情绪轨迹”：

---

## 📈 情绪轨迹模型：

```text id="camflow"
Distance:
far → medium → close → extreme close

Emotion:
neutral → tension → breakdown → climax

Motion:
static → slow → unstable → chaotic
```

---

# 🔁 9. 摄影机连续性系统（Camera Continuity Engine）

系统必须保持：

---

## ❗连续性规则：

* 镜头运动逻辑连续
* 不允许镜头突然跳变风格
* 不允许焦段突变（除非剧情转折）
* 光线方向必须一致

---

# 🎥 10. Camera → Seedance 转换输出格式

最终必须输出：

---

## 📦 CAMERA EXECUTION BLOCK

```text id="cam_out"
Camera:
- Shot type:
- Angle:
- Movement:
- Lens:
- Framing logic:

Intent:
- why this camera exists emotionally

Continuity:
- locked visual conditions
```

---

# 🚨 11. 禁止规则（Hard Constraints）

❌ 禁止：

* 无意义镜头运动
* 镜头与情绪不匹配
* 摄影机“只是记录”
* 风格跳跃
* 镜头无意图

---

# ✅ 必须：

✔ 摄影机必须“表达情绪”
✔ 每个镜头必须有“视觉意图”
✔ 每个运动必须有“心理原因”
✔ 镜头必须服务叙事推进

---
 