 
# 📦 SEEDANCE 2.0 SYSTEM ENGINE SPEC

## FILE 02 — SHOT GENERATOR ENGINE（自动分镜系统）

---

# 🎬 1. 系统定位（System Purpose）

Shot Generator Engine 的作用是：

> 将“故事 / 脚本 / 概念”自动拆解为可执行的电影级分镜单元（Shots）

---

## 🧠 核心定义

```text id="sg01"
Story Input
→ Emotional Beats
→ Time Segmentation
→ Shot Units
→ Camera Assignment
→ Motion Assignment
→ Seedance-ready Shot List
```

---

# ⏱ 2. 时间拆解规则（Temporal Engine）

系统必须根据总时长自动生成镜头数量：

---

## 🎯 Shot Density Rule

| 总时长  | 镜头数量        | 单镜头时长 |
| ---- | ----------- | ----- |
| 15s  | 5–7 shots   | 2–3s  |
| 30s  | 8–12 shots  | 2–4s  |
| 60s  | 12–20 shots | 3–5s  |
| 3min | 25–40 shots | 4–6s  |

---

## ⚠️ 强制规则

* 不允许镜头超过 5 秒（除非情绪慢镜）
* 每个镜头必须表达“单一动作节点”
* 禁止一个镜头包含多个事件

---

# 🧩 3. 故事拆解系统（Story Deconstruction Engine）

系统将输入拆为 3 层：

---

## 3.1 Emotional Beats（情绪节拍）

```text id="be1"
Beat 1: setup emotion
Beat 2: conflict / change
Beat 3: escalation
Beat 4: resolution / silence
```

---

## 3.2 Action Units（动作单元）

每个 Beat 必须拆为：

* 1 个核心动作
* 1 个视觉变化
* 1 个情绪变化（可隐含）

---

## 3.3 Time Flow（时间流）

系统必须保证：

> 时间 = 线性推进，不允许跳跃式叙事（除非梦境/超现实）

---

# 🎥 4. 镜头生成规则（Shot Creation Engine）

每个 Shot 必须包含：

---

## 4.1 基础结构

```text id="sh01"
SHOT [X]:
Duration:
Action:
Emotion:
Camera:
Movement:
Lighting:
Environment:
```

---

## 4.2 Shot 生成逻辑

系统自动选择：

### ✔ 如果是“情绪节点”

→ Close-up + slow push-in

### ✔ 如果是“行为推进”

→ Medium shot + tracking

### ✔ 如果是“空间变化”

→ Wide shot + static / dolly-out

### ✔ 如果是“冲突”

→ handheld + close-up + fast rhythm

---

# 🎭 5. 动作粒度控制系统（Action Granularity Engine）

每个 Shot 只能包含：

## ❌ 错误：

* 她走路 + 回头 + 哭泣 + 说话

## ✅ 正确：

* 她停下脚步（一个动作）
* 她慢慢回头（一个动作）
* 她低头呼吸（一个动作）

---

# 🎬 6. 镜头节奏系统（Pacing Engine）

## 节奏分类：

### 1. 快节奏（Action / Thriller）

* 1.5–2s / shot
* handheld + tracking

### 2. 中节奏（Drama）

* 2–4s / shot
* medium + dolly

### 3. 慢节奏（Romance / Art）

* 4–6s / shot
* static + slow push-in

---

# 🧠 7. 镜头优先级系统（Shot Priority Logic）

系统自动排序：

---

## 🔥 Priority 1：情绪爆点

* close-up
* extreme close-up

---

## 🎭 Priority 2：行为变化

* medium shot

---

## 🌍 Priority 3：空间信息

* wide shot

---

# 🌫 8. 镜头类型自动分配（Auto Camera Assignment）

系统根据内容自动匹配：

---

## 🎬 情绪类镜头

| 情绪 | 镜头                  |
| -- | ------------------- |
| 爱  | close-up + dolly-in |
| 恐惧 | handheld + close-up |
| 孤独 | wide + static       |
| 震惊 | extreme close-up    |

---

## 🎬 行为类镜头

| 类型 | 镜头                  |
| -- | ------------------- |
| 行走 | tracking shot       |
| 停止 | static frame        |
| 转身 | medium + slow orbit |
| 对话 | over-the-shoulder   |

---

# 🔁 9. 连续性拆解系统（Continuity Shot Flow）

系统必须保证：

* 镜头之间有逻辑连接
* 动作不能“瞬移”
* 空间必须连续

---

## 示例：

```text id="cflow"
SHOT 01 → Establish space
SHOT 02 → Character enters
SHOT 03 → Action begins
SHOT 04 → Emotional reaction
SHOT 05 → Resolution / pause
```

---

# 🎥 10. Shot 输出标准（Final Shot Format）

系统最终输出必须统一为：

---

## 📦 SHOT TEMPLATE

```text id="final_shot"
SHOT 01

Duration: 3s
Action: [single action]
Emotion: [emotion keyword]

Camera:
- Shot type:
- Angle:
- Movement:

Lighting:
- color mood
- intensity

Environment:
- motion elements (rain / wind / light / particles)

Purpose:
- why this shot exists in story flow
```

---

# 🧾 11. Shot Generator → Seedance 转换接口

系统输出必须直接兼容：

```text id="pipe01"
Shot List
→ Camera Mapping
→ Motion Mapping
→ Lighting Mapping
→ Prompt Compiler
→ Seedance Ready Output
```

---

# 🚨 12. 强制规则（Engine Constraints）

## ❌ 禁止：

* 多动作混合
* 镜头无情绪
* 镜头无目的
* 跳时间线
* 无摄影机设计

---

## ✅ 必须：

* 每个 shot = 1动作
* 每个 shot = 1情绪
* 每个 shot = 1镜头逻辑
* 每个 shot = 可拍摄

---
 