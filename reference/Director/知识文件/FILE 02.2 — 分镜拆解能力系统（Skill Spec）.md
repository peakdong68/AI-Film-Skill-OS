 

---

# 📦 STORYBOARD DECONSTRUCTION ENGINE

## 🧠 FILE 02.2 — 分镜拆解能力系统（Skill Spec）

---

# 🧬 NAME

Storyboard Deconstruction Engine（分镜拆解引擎）

---

# 🧠 DESCRIPTION

将故事/脚本/叙事内容拆解为可执行的时间化视觉单元（Storyboard Panels），并将每个单元标准化为 AI 可生成的视频镜头结构。

核心目标：

> 将“叙事结构”转换为“时间碎片化镜头语言”

---

# ⚙️ MODULES

## 1. Temporal Segmentation Module（时间切割模块）

### FUNCTION：

将整体故事拆分为多个 storyboard panels

### RULES：

* 1 storyboard = 8–12 panels
* 每 panel = 1个动作单元
* 每个动作必须具备独立时间意义
* 禁止跨动作混合

### OUTPUT：

```text id="ts01"
Panel List:
P1 → setup
P2 → trigger
P3 → escalation
P4 → reaction
...
```

---

## 2. Action Unit Extractor（动作单元提取器）

### FUNCTION：

将连续叙事拆解为最小可执行动作单元

### RULES：

* 一个 panel = 一个动作
* 动作必须可视觉化
* 禁止抽象描述

### VALID ACTION FORMAT：

* walk
* turn
* look
* stop
* reach
* collapse
* speak (only if visualized)

### INVALID:

* feel sad
* become emotional
* think about past

### OUTPUT:

```text id="au01"
Action Units:
P1 → walk forward
P2 → stop
P3 → turn head
P4 → look back
```

---

## 3. Emotion Mapping Module（情绪映射模块）

### FUNCTION：

为每个动作单元绑定情绪状态

### RULES：

* 每个 panel 只能有 1 个主情绪
* 情绪必须可表现为身体行为
* 情绪必须驱动动作变化

### OUTPUT FORMAT:

```text id="em01"
P1 → neutral
P2 → tension
P3 → anxiety
P4 → sadness
```

---

## 4. Camera Mapping Module（摄影机映射模块）

### FUNCTION：

为每个 panel 自动分配镜头语言

### RULES：

* camera = emotion-driven
* 必须包含 shot type + movement + angle
* 禁止无镜头逻辑

### CAMERA LIBRARY:

* wide shot
* medium shot
* close-up
* extreme close-up

### MOVEMENT LIBRARY:

* static
* dolly-in
* dolly-out
* tracking
* handheld
* orbit

### OUTPUT:

```text id="cm01"
P1 → wide + static + eye-level
P2 → medium + tracking + eye-level
P3 → close-up + dolly-in
```

---

## 5. Timing Engine（时间分配模块）

### FUNCTION：

为每个 panel 分配时间长度

### RULES：

* 每 panel = 1–3 seconds
* 情绪越强 → 时间越长
* 动作越复杂 → 时间越长

### OUTPUT:

```text id="tm01"
P1 → 2s
P2 → 1.5s
P3 → 3s
```

---

# 📦 OUTPUT SPECIFICATION

最终输出必须统一结构：

```text id="final01"
STORYBOARD DECONSTRUCTION OUTPUT

Panel X:

Action:
Emotion:
Camera:
Timing:

---

Panel X+1:
...
```

---

# 🔁 RULES（核心约束）

## ❌ 禁止：

* 一个 panel 多动作
* 情绪抽象化表达
* 无 camera 信息
* 时间缺失
* 动作不可视觉化

---

## ✅ 必须：

* Action = 可拍摄行为
* Emotion = 可视觉表现
* Camera = 明确镜头语言
* Timing = 明确秒数
* Panel = 时间碎片单元

---

# 🧠 OUTPUT CONTRACT

系统输出必须满足：

* 可直接进入 Shot Generator Engine
* 可直接映射 Camera Director System
* 可直接进入 Seedance Prompt Compiler
* 不含解释性语言
* 完全结构化

---
 