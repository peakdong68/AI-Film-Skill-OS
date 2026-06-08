# 📦 SEEDANCE 2.0 SYSTEM ENGINE SPEC

## 🧠 FILE 02.4 — EMOTION-TO-PANEL AUTO GENERATOR（情绪驱动分镜生成器）

---

# 🎬 1. 系统定位（System Purpose）

Emotion-to-Panel Auto Generator 是 Seedance 2.0 的“故事自动分镜核心”。

> 它负责将“一句话/概念/脚本”自动转换为结构化 storyboard panels，并直接进入时间流与镜头系统。

---

## 🧠 核心定义

```text id="ep01"
Text / Idea Input
→ Emotion Extraction
→ Narrative Decomposition
→ Temporal Flow Mapping
→ Panel Generation
→ Camera + Motion + Timing Assignment
→ Seedance Ready Storyboard
```

---

# 🧩 2. 输入结构（Input Schema）

系统支持以下输入类型：

---

## 📦 INPUT TYPES

### 1. SINGLE SENTENCE

* “A girl sees her past lover in the rain.”

---

### 2. SHORT SCRIPT

* 2–5 sentences narrative

---

### 3. SCENE IDEA

* abstract concept (e.g. “loneliness in a futuristic city”)

---

# 🧠 3. 情绪提取系统（Emotion Extraction Engine）

---

## 📌 RULES:

* 每个输入必须拆为 1–3 个核心情绪
* 情绪必须驱动动作，而不是描述状态
* 禁止抽象情绪未结构化

---

## 📦 EMOTION LIBRARY:

* love
* fear
* sadness
* tension
* loneliness
* surprise
* nostalgia
* hope

---

## 📦 OUTPUT:

```text id="em01"
Input Emotion Map:
- primary emotion: sadness
- secondary emotion: nostalgia
- latent emotion: tension
```

---

# 🎭 4. 故事拆解系统（Narrative Decomposition Engine）

---

## 📌 RULES:

* 输入必须拆为 3–8 narrative beats
* 每个 beat = 一个动作变化点
* 每个 beat = 一个情绪变化点

---

## 📦 EXAMPLE:

Input:
“A girl sees her past lover in the rain.”

Output:

```text id="nd01"
Beat 1: establish loneliness
Beat 2: girl walks in rain
Beat 3: emotional recognition
Beat 4: hesitation
Beat 5: turn back
Beat 6: emotional collision
```

---

# 🎬 5. 自动 Panel 生成系统（Panel Generation Engine）

---

## 📌 RULES:

* 1 beat = 1–2 panels
* 1 panel = 1 action unit
* 每个 panel 必须可视觉化

---

## 📦 PANEL STRUCTURE:

```text id="pg01"
Panel X:
- Action:
- Emotion:
- Camera:
- Motion:
- Timing:
```

---

## 📦 EXAMPLE:

```text id="ex01"
P1:
Action: girl walks alone in rain
Emotion: loneliness
Camera: wide shot, static
Motion: slow tracking
Timing: 3s

P2:
Action: girl slows down
Emotion: tension
Camera: medium shot
Motion: slow dolly-in
Timing: 2s
```

---

# 🧠 6. 自动镜头绑定系统（Auto Camera Binding）

---

## 📌 RULES:

系统自动绑定：

* Emotion → Camera type
* Action → Shot scale
* Intensity → Motion speed

---

## 📦 MAPPING TABLE:

| Emotion | Camera                   |
| ------- | ------------------------ |
| sadness | wide / static            |
| love    | close-up / slow dolly-in |
| fear    | handheld / close-up      |
| tension | dutch angle / tracking   |

---

# ⏱ 7. 自动时间分配系统（Auto Timing Engine）

---

## 📌 RULES:

* emotional peak = longer duration
* transition = shorter duration
* silence = expanded time

---

## 📦 EXAMPLE:

```text id="tm01"
P1 → 3s
P2 → 2s
P3 → 4s (emotional peak)
P4 → 2.5s
```

---

# 🎥 8. 自动摄影机运动生成（Motion Auto Engine）

---

## 📌 RULES:

* emotion intensity → camera motion intensity
* calm → static
* tension → handheld
* emotional rise → dolly-in

---

## 📦 EXAMPLE:

```text id="mo01"
P1 → static
P2 → slow tracking
P3 → slow dolly-in
P4 → handheld subtle shake
```

---

# 🌫 9. 情绪→视觉一致性系统（Emotion Visual Consistency Engine）

---

## 📌 RULES:

* emotion must remain visually traceable
* no emotional reset between panels
* emotion must evolve, not restart

---

## 📦 FLOW:

```text id="flow01"
loneliness → tension → recognition → emotional collapse
```

---

# 🔁 10. 完整输出系统（Final Generator Output）

---

## 📦 STORYBOARD OUTPUT FORMAT

```text id="final01"
AUTO GENERATED STORYBOARD

Emotion Core:
- primary:
- secondary:

Temporal Flow:
- emotional progression curve:

Panels:

P1:
Action:
Emotion:
Camera:
Motion:
Timing:

P2:
...

Final Output Type:
- Seedance ready storyboard
```

---

# 🚨 11. 禁止规则（Hard Constraints）

❌ 禁止：

* 情绪不绑定动作
* panel 无镜头
* 时间缺失
* 多动作混合
* 情绪跳跃重置

---

# ✅ 必须：

✔ emotion → action → camera → time 全链路
✔ 每个 panel 可拍摄
✔ 情绪必须连续变化
✔ 自动生成可进入 Seedance pipeline

---

# 🎬 FILE 02.4 END

---

# 🚀 🎉 到这里你已经完成：

## 📦 Seedance 2.0 “分镜智能生成核心层”

你现在拥有：

* 情绪自动解析系统
* 分镜自动生成系统
* 时间流叙事系统
* 摄影机自动绑定系统
* 可直接进入 Prompt Compiler 的结构

---
 