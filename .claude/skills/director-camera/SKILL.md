---
name: director-camera
description: 为AI电影制作设计摄影机语言系统——镜头类型、运动语法、构图规则、空间调度、情绪驱动的摄影机决策。当用户需要摄影机设计、镜头规划、摄影指导方向、Camera Movement Planning，或 director-core 路由至 STATE 2 时使用。也用于"这个场景怎么拍"或需要将情绪意图转化为具体摄影机决策的场景。Design the cinematography system for AI film production — camera language, shot types, movement grammar, composition rules, spatial blocking, and emotion-driven camera decisions.
---

# Director Camera — 摄影机导演系统

## 概述

设计定义影片*如何被拍摄*的摄影机系统——不是场景里发生了什么，而是摄影机如何看待它。本技能构建完整的摄影蓝图：镜头类型语法、运动词汇、构图哲学、空间调度以及情绪驱动的摄影机映射。输出成果确保下游分镜和提示词系统中的每一个镜头都有扎实的摄影依据。

可独立使用，也可由 `director-core` 在 STATE 2 调用。

## 核心原则

> 摄影机不是记录工具，它是情绪主体。

每一个摄影机决策必须回答三个问题：
1. **我在看什么？**（主体）
2. **为什么这样看？**（意图——由情绪驱动）
3. **摄影机如何运动？**（运动——由叙事节奏驱动）

## 输出结构

### 1. Camera Language System（摄影机语言系统）

为全片定义视觉语法：

**Shot Type Grammar（镜头类型语法）：**
| Type | 中文 | 叙事功能 |
|------|------|---------|
| Wide Shot | 远景 | 建立世界、表现孤立感、定义空间关系 |
| Medium Shot | 中景 | 承载叙事动作、表现行为与互动 |
| Close-Up | 特写 | 揭示情绪、内在状态、心理细节 |
| Extreme Close-Up | 超特写 | 决定性瞬间、情绪峰值、视觉锚点 |
| Over-Shoulder | 过肩 | 关系张力、对话结构、视角 |
| POV | 主观视角 | 沉浸式体验、角色认同 |
| Top-Down | 鸟瞰 | 控制感、孤立感、上帝视角 |
| Low Angle | 仰拍 | 力量感、威胁感、重要性、英雄主义 |

针对具体项目，选出主要镜头类型并解释*为什么*这套语法契合故事。

**Movement Grammar（运动语法）：**
| Movement | 中文 | 情绪功能 |
|----------|------|---------|
| Static | 定镜 | 压迫、观察、静止、等待 |
| Slow Dolly-In | 缓推 | 情绪加深、心理压迫 |
| Dolly-Out | 拉远 | 情绪抽离、孤独感 |
| Tracking | 跟移 | 跟随动作、参与感、追逐 |
| Orbit | 环绕 | 关系复杂化、浪漫、超现实 |
| Handheld | 手持 | 真实感、不稳定、紧张、纪录风格 |
| Crane | 升降 | 空间揭示、史诗感 |
| Whip Pan | 快速摇 | 情绪爆发、快速转场、迷失感 |

**Focus Grammar（焦点语法）：**
- **Rack Focus（焦点转移）**：注意力在主体间转移
- **Shallow Depth of Field（浅景深）**：情绪隔离、主体强调
- **Deep Focus（深焦）**：环境关系、层次叙事

### 2. Emotional Camera System（情绪摄影系统）

将影片中每种核心情绪映射到摄影机行为：

| 情绪 | 镜头 | 运动 | 角度 | 焦点 |
|------|------|------|------|------|
| 悲伤 / 孤独 | Wide | Static / slow push-in | Eye level | Shallow DOF |
| 恐惧 / 紧张 | Close-up | Handheld micro-shake | Dutch / eye level | Tight |
| 浪漫 / 亲密 | Close-up / OTS | Slow orbit / dolly | Eye level | Soft focus |
| 神秘 | Wide / silhouette | Static / slow reveal | Low / obstructed | Deep |
| 力量 / 支配 | Medium / low angle | Slow controlled dolly | Low angle | Symmetrical |
| 震惊 | ECU | Sudden stillness | Eye level | Sharp |
| 动作 / 紧迫 | Medium | Tracking / handheld | Dynamic | Following |

这张映射表是关键的桥梁——分镜中的每一个镜头都应该能追溯到这张表中的某一行。

### 3. Spatial Composition System（空间构图系统）

**Framing Rules（构图规则）：**
- **Rule of Thirds（三分法）**：均衡、自然的构图——大多数叙事的默认选择
- **Center Framing（中心构图）**：仪式感、力量、对称——用于重要时刻
- **Negative Space（负空间）**：孤独、孤立、情绪重量——主体被推到画面边缘
- **Foreground Obstruction（前景遮挡）**：偷窥感、神秘感、隐蔽观察
- **Frame Within Frame（框中框）**：层次感、局限感、聚焦

**Depth Design（景深设计）：**
- 前景 → 中景 → 背景的分层关系
- 通过物体布置进行环境叙事
- 空间张力：角色之间的距离 = 情感距离

**Blocking Design（人物调度）：**
- 角色站位 = 情感关系
- 距离 = 心理间隙
- 运动方向 = 叙事张力
- 视线连续性 = 空间逻辑

### 4. Camera Continuity System（镜头连续性）

贯穿所有镜头的硬性规则：

- **方向一致性**：同场景内屏幕方向（左→右 / 右→左）不得翻转，除非设计了明确的越轴镜头
- **景别递进**：避免在极端景别之间跳跃，需要过渡镜头
- **空间地理**：空间的物理布局必须保持稳定——椅子不移动，门保持在原位
- **光源方向**：同场景内主光方向必须一致，除非情节内的光源发生了移动
- **180度规则**：同场景内摄影机保持在动作轴同一侧，除非用中性镜头打破轴线

### 5. Camera Prompt Template（摄影机提示词模板）

分镜中每个镜头的摄影机指令必须遵循此模板：

```
Shot type: [WS / MS / CU / ECU / OTS / POV]
Angle: [eye-level / low / high / Dutch / top-down]
Movement: [static / dolly-in / dolly-out / tracking / orbit / handheld / crane]
Lens behavior: [shallow DOF / deep focus / rack focus to X]
Framing: [rule of thirds / centered / negative space / frame-in-frame]
Emotional intent: [为什么在这个时刻选择这个镜头]
```

## 约束

- 禁止没有情绪理由的镜头——"看起来酷"不是有效的摄影决策。
- 禁止随机的摄影机运动——每一次运动必须服务于叙事推进。
- 禁止未经刻意设计越轴镜头的情况下打破180度规则。
- 镜头连续性必须在交付分镜前验证通过。
- 手持运动必须有动机（紧张、真实感、混乱）——不能作为默认选项。

## 集成

当 `director-core` 调用时：
- 加载 `director-emotion` 的情绪蓝图，用于填充情绪摄影系统
- 产出摄影蓝图
- 输入到 `director-light` 进行光影对齐
- 摄影机提示词模板直接输入到分镜和提示词系统
