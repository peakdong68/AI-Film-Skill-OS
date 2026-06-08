 
# 📦 SEEDANCE 2.0 SYSTEM ENGINE SPEC

## FILE 04 — MOTION TRANSLATION ENGINE（动作翻译系统）

---

# 🎬 1. 系统定位（System Purpose）

Motion Translation Engine 是 Seedance 2.0 的“人体语言编译器”。

> 它负责将“语言/情绪描述”转换为“可被AI视频执行的身体动作 + 微表情 + 节奏运动”。

---

## 🧠 核心定义

```text id="mt01"
Emotion / Text
→ Physical Behavior Decomposition
→ Micro Motion Units
→ Facial Expression Mapping
→ Body Kinetics
→ Camera-Sync Motion Output
```

---

# 🧍 2. 动作最小单位系统（Micro Motion Units）

系统禁止“模糊动作”，必须拆解为最小单元：

---

## 📦 Micro Unit Library

### ✔ Head (头部)

* slow turn（缓慢转头）
* downward tilt（低头）
* slight shake（轻微摇头）
* freeze (静止凝视)

---

### ✔ Eyes (眼睛)

* eye dart（快速移动视线）
* long stare（持续凝视）
* avoid gaze（回避视线）
* blink delay（延迟眨眼）

---

### ✔ Mouth (嘴部)

* lips part slightly（微微张嘴）
* tighten lips（嘴唇紧绷）
* silent breath（无声呼吸）

---

### ✔ Shoulders (肩部)

* drop shoulders（肩膀下沉）
* tense shoulders（肩部紧绷）
* release tension（放松）

---

### ✔ Hands (手部)

* finger curl（手指收紧）
* hand tremble（轻微颤抖）
* hand relax（自然放松）

---

### ✔ Body (身体整体)

* step forward（向前一步）
* step back（后退）
* freeze posture（静止姿态）
* slow collapse（缓慢下沉）

---

# 🎭 3. 情绪 → 动作映射系统（Emotion Motion Engine）

---

## ❤️ 爱 / 情感

* gaze softens（眼神柔化）
* slow lean forward（身体微倾）
* breath slows（呼吸变慢）
* hands relax

---

## 😨 恐惧 / 压迫

* shoulders tighten
* eyes widen slightly
* body pulls backward
* breathing shallow

---

## 🧍 孤独 / 空虚

* body becomes still
* gaze fixed but unfocused
* shoulders drop
* minimal movement

---

## ⚡ 紧张 / 冲突

* finger tension
* quick eye movement
* unstable breathing
* micro head movement

---

## 💔 悲伤 / 失落

* head lowers
* shoulders sink
* slow breathing
* gaze avoids others

---

# 🎬 4. 动作时间系统（Motion Timing Engine）

所有动作必须绑定时间逻辑：

---

## ⏱ Timing Rules

| 动作类型 | 时长     |
| ---- | ------ |
| 微动作  | 0.2–1s |
| 情绪动作 | 1–3s   |
| 行为动作 | 2–5s   |
| 转折动作 | 3–6s   |

---

## ❗规则

* 不允许“瞬间完成复杂动作”
* 所有动作必须“分阶段发生”
* 情绪必须有延迟（emotional lag）

---

# 🧠 5. 动作拆解规则（Action Decomposition Engine）

---

## ❌ 错误：

“她哭了”

---

## ✅ 正确拆解：

* eyes become glossy
* lower lip trembles
* breath pauses
* tears slowly form
* head lowers slightly

---

# 🎥 6. 摄影机同步动作系统（Camera-Motion Sync）

动作必须与镜头联动：

---

## 📷 Sync Rules

### ✔ camera push-in

→ emotion intensifies
→ micro facial tension increases

---

### ✔ camera pull-out

→ emotional distancing
→ body becomes still

---

### ✔ handheld movement

→ body instability must match

---

### ✔ static shot

→ internal emotion must increase (not external motion)

---

# 🌫 7. 微表情系统（Micro Expression Engine）

---

## 📦 Face Micro-Units

* eyebrow tighten（眉毛紧缩）
* eyelid tension（眼睑紧张）
* nostril flare（鼻翼扩张）
* jaw tighten（下颚紧绷）
* lip compression（嘴唇压紧）

---

## 🎭 情绪映射：

| 情绪 | 微表情组合                       |
| -- | --------------------------- |
| 恐惧 | eyes widen + jaw tense      |
| 悲伤 | eyelids lower + lip tremble |
| 爱  | soft eyes + relaxed jaw     |
| 愤怒 | eyebrow down + jaw tight    |

---

# 🧍 8. 身体叙事系统（Body Narrative Engine）

身体必须表达“心理状态”：

---

## 📈 状态映射：

### ✔ Confidence

* upright posture
* open chest
* steady movement

---

### ✔ Anxiety

* unstable posture
* shifting weight
* restless hands

---

### ✔ Depression

* collapsed shoulders
* slow movement
* minimal gestures

---

# 🔁 9. 动作连续性系统（Motion Continuity Engine）

系统必须保证：

---

## ❗连续性规则：

* 动作不能“跳帧式变化”
* 情绪必须渐进
* 身体状态必须延续
* 前一个动作影响下一个动作

---

## 📦 Example Flow:

```text id="mc01"
Step 1: eyes shift
Step 2: head follows
Step 3: body reacts
Step 4: emotion escalates
```

---

# 🎬 10. Motion → Seedance 输出格式

---

## 📦 MOTION BLOCK OUTPUT

```text id="mo_out"
Character Motion:
- head movement:
- eye behavior:
- mouth micro expression:
- shoulder/body state:
- hand movement:

Emotional Progression:
- initial state → transition → peak emotion

Timing:
- micro timing breakdown per action

Camera Sync:
- how motion aligns with camera movement
```

---

# 🚨 11. 禁止规则（Hard Constraints）

❌ 禁止：

* “模糊动作词”（如：表现悲伤）
* 一句话多动作未拆解
* 无时间结构动作
* 动作与情绪不匹配
* 缺少微表情层

---

# ✅ 必须：

✔ 所有情绪必须“身体化”
✔ 所有动作必须“可拍摄”
✔ 所有表情必须“可分解”
✔ 所有动作必须“有时间结构”

---
 