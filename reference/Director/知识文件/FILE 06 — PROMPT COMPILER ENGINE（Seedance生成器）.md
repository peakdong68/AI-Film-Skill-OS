# 📦 SEEDANCE 2.0 SYSTEM ENGINE SPEC

## FILE 06 — PROMPT COMPILER ENGINE（Seedance生成器）

---

# 🎬 1. 系统定位（System Purpose）

Prompt Compiler Engine 是 Seedance 2.0 的“最终执行大脑”。

> 它负责将所有子系统输出（镜头 / 动作 / 光影 / 摄影机 / 连续性）压缩为**可直接用于 Image-to-Video 模型的执行级 Prompt**。

---

## 🧠 核心定义

```text id="pc01"
Shot Data (Multi-System Inputs)
→ Standardization Layer
→ Conflict Resolution
→ Prompt Structuring
→ Compression Engine
→ Seedance 2.0 Final Prompt
```

---

# 🧩 2. 输入结构（Compiler Input Schema）

系统必须接收以下模块输入：

---

## 📦 INPUT PACK

### 🎥 Shot Engine

* duration
* action
* shot type

### 🎭 Motion Engine

* body movement
* micro expression
* emotional progression

### 🎬 Camera Engine

* angle
* movement
* framing
* lens logic

### 🌫 Lighting Engine

* color temperature
* contrast
* light sources
* atmosphere

### 🔁 Continuity Engine

* identity lock
* wardrobe lock
* environment lock

---

# ⚙️ 3. 标准化系统（Normalization Layer）

系统必须统一所有输入为“可执行结构”。

---

## ❗规则：

* 所有描述必须“视觉化”
* 禁止抽象词（如“感觉很好”）
* 所有信息必须可拍摄 / 可渲染

---

## 🔄 标准化示例：

❌ input:
“她很悲伤”

✔ normalized:

* head lowered
* eyes avoid contact
* shoulders dropped
* slow breathing

---

# 🧠 4. 冲突解析系统（Conflict Resolution Engine）

当系统检测冲突时必须修正：

---

## ⚠️ 常见冲突：

### ❌ Camera conflict

* static shot + fast motion

✔ 修正：
→ slow motion or reduce action intensity

---

### ❌ Lighting conflict

* warm romantic + horror action

✔ 修正：
→ choose dominant emotional layer

---

### ❌ Motion conflict

* multiple unrelated actions

✔ 修正：
→ split into multiple shots

---

# 🎬 5. Prompt结构生成系统（Prompt Structuring Engine）

---

## 📦 SEEDANCE PROMPT STRUCTURE

必须按以下顺序：

---

### 1. CONTEXT LOCK

```text id="ctx01"
Continue from storyboard Part [X].
Maintain strict continuity: same character identity, wardrobe, environment, lighting logic.
```

---

### 2. SCENE CORE

```text id="sc01"
Duration: X seconds
Location: X
Time: X
Mood: X
```

---

### 3. CHARACTER MOTION BLOCK

```text id="ch01"
Character:
- head movement:
- eye behavior:
- facial micro expressions:
- body posture:
- hand motion:
- emotional progression:
```

---

### 4. CAMERA BLOCK

```text id="cm01"
Camera:
- shot type:
- angle:
- movement:
- lens behavior:
- framing logic:
```

---

### 5. LIGHTING BLOCK

```text id="lt01"
Lighting:
- key light:
- fill light:
- rim light:
- color temperature:
- contrast level:
- atmosphere:
```

---

### 6. ENVIRONMENT BLOCK

```text id="env01"
Environment:
- weather:
- particles:
- background motion:
- spatial depth behavior:
```

---

### 7. SOUND (optional layer)

```text id="sd01"
Sound:
- ambient tone:
- emotional cue:
- silence usage:
```

---

### 8. NEGATIVE CONSTRAINTS

```text id="ng01"
No text, no subtitles, no watermark, no identity change, no face drift, no wardrobe change, no extra characters, no scene reset.
```

---

# 🧬 6. 压缩引擎（Compression Engine）

系统必须将结构压缩为：

> 🎯 “最小信息密度 + 最大视觉可执行性”

---

## 📉 压缩规则：

* 删除解释性语言
* 保留动作词
* 保留摄影机词
* 保留光影词
* 保留连续性锁定

---

## 📦 示例：

### Before:

“She slowly feels emotional sadness and turns away while camera moves gently”

### After:

* slow head turn away
* shoulders drop
* camera: slow dolly-in
* lighting: cold soft fade

---

# 🎥 7. Seedance 输出标准（Final Output Contract）

最终 Prompt 必须满足：

---

## ✔ EXECUTION REQUIREMENTS

* 可直接用于 image-to-video
* 无解释语言
* 完全视觉化
* 每一行都可渲染
* 动作 + 镜头 + 光影完整

---

## ✔ STRUCTURE REQUIREMENTS

每个 Prompt 必须包含：

* context lock
* motion
* camera
* lighting
* environment
* negative constraints

---

# 🔁 8. 连续性绑定系统（Continuity Binding Engine）

系统必须强制绑定：

---

## ❗LOCK RULES:

* identity locked
* wardrobe locked
* environment locked
* lighting logic continuous
* no sudden resets

---

## 📦 continuity example:

```text id="cb01"
same character identity as previous shot
same rainy night street environment
continuing emotional state
```

---

# 🧠 9. Prompt质量验证系统（Validation Engine）

系统必须检查：

---

## ✔ VALIDATION CHECKLIST

* Is motion visually clear?
* Is camera behavior defined?
* Is lighting meaningful?
* Is emotion physically expressed?
* Is continuity preserved?
* Is prompt executable?

---

# 🚨 10. 禁止规则（Hard Constraints）

❌ 禁止：

* 抽象情绪词
* 无摄影机信息
* 无光影结构
* 无动作拆解
* 重复描述
* 风格混乱

---

# ✅ 必须：

✔ 每个元素可视化
✔ 每个动作可拍摄
✔ 每个光影有意义
✔ 每个镜头可执行

---
 