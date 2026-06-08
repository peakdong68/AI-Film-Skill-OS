---
name: director-camera
description: 为 AI 电影制作设计摄影系统——摄影机语言、镜头类型、运动语法、构图规则、空间调度和情绪驱动的摄影机决策。用于摄影机设计、摄影机语言、镜头规划、摄影指导方向、镜头设计、摄影机运动规划，或当 director-core 路由到 STATE 2（视觉设计）时。也适用于用户问"这个该怎么拍"或需要将情绪意图转化为具体摄影机决策的情况。Design the cinematography system for AI film production — camera language, shot types, movement grammar, composition rules, spatial blocking, and emotion-driven camera decisions.
---

# Director Camera — 摄影导演 AI

## 概览

设计定义影片*如何被拍摄*的摄影机系统——不是场景中发生了什么，而是摄影机如何看待它。此技能构建完整的摄影蓝图：镜头类型语法、运动词汇、取景哲学、空间调度和情绪摄影机映射。输出确保下游分镜和提示词系统中的每一个镜头都有扎实的摄影理由。

可独立用于摄影机设计，或由 `director-core` 在 STATE 2 调用。

## 加载资源

本技能附带以下参考知识文件，在相应场景下读取：
- 需要完整的镜头类型语法、摄影机运动词汇表、情绪→摄影机映射表时，读取 `references/camera-grammar.md`
- 需要六种镜头语义（Observe/Immerse/Reveal/Confront/Isolate/Expand）及视觉优先级决策逻辑时，读取 `references/shot-semantics.md`

## 核心原则

> 摄影机不是记录设备。它是情绪主体。

每个摄影机决策必须回答三个问题：
1. **我在看什么？**（Subject 主体）
2. **为什么这样看？**（Intent 意图——由情绪驱动）
3. **摄影机如何运动？**（Motion 运动——由叙事节奏驱动）

## 输出结构

### 1. Camera Language System（摄影机语言系统）

定义整部影片的视觉语法：

**镜头类型语法：**
| 类型 | 中文 | 叙事功能 |
|------|------|-------------------|
| Wide Shot | 远景 | 建立世界、表现孤立、定义空间关系 |
| Medium Shot | 中景 | 承载叙事动作、展示行为和互动 |
| Close-Up | 特写 | 揭示情绪、内心状态、心理细节 |
| Extreme Close-Up | 超特写 | 决定性瞬间、情绪顶点、视觉锚点 |
| Over-Shoulder | 过肩 | 关系张力、对话结构、视角 |
| POV | 主观视角 | 沉浸体验、与角色认同 |
| Top-Down | 鸟瞰 | 控制、孤立、上帝视角 |
| Low Angle | 仰拍 | 权力、威胁、重要性、英雄感 |

为具体项目选择主要镜头类型，并解释*为什么*这套语法适合这个故事。

**运动语法：**
| 运动 | 中文 | 情绪功能 |
|----------|------|-------------------|
| Static | 定镜 | 压迫、观察、静止、等待 |
| Slow Dolly-In | 缓推 | 情绪加深、心理压迫 |
| Dolly-Out | 拉远 | 情绪抽离、孤独感 |
| Tracking | 跟移 | 跟随动作、参与、追逐 |
| Orbit | 环绕 | 关系复杂化、浪漫、超现实 |
| Handheld | 手持 | 现实感、不稳定、紧张、纪录片质感 |
| Crane | 升降 | 空间揭示、史诗规模 |
| Whip Pan | 快速摇 | 情绪爆发、快速转场、迷失感 |

**焦点语法：**
- **Rack Focus（焦点转移）**：注意力在主体间转移
- **Shallow Depth of Field（浅景深）**：情绪隔离、主体突出
- **Deep Focus（深焦）**：环境关系、层次叙事

### 2. Emotional Camera System（情绪摄影系统）

将影片中每种主要情绪映射到摄影机行为：

| 情绪 | 镜头 | 运动 | 角度 | 焦点 |
|---------|------|----------|-------|-------|
| 悲伤/孤独 Sadness | Wide | Static / slow push-in | Eye level | Shallow DOF |
| 恐惧/紧张 Fear | Close-up | Handheld micro-shake | Dutch / eye level | Tight |
| 浪漫/亲密 Romance | Close-up / OTS | Slow orbit / dolly | Eye level | Soft focus |
| 神秘 Mystery | Wide / silhouette | Static / slow reveal | Low / obstructed | Deep |
| 权力/支配 Power | Medium / low angle | Slow controlled dolly | Low angle | Symmetrical |
| 震惊 Shock | ECU | Sudden stillness | Eye level | Sharp |
| 动作/紧迫 Action | Medium | Tracking / handheld | Dynamic | Following |

这张映射表是关键的桥梁——分镜中的每一个镜头都应该能追溯到这张表中的某一行。

### 3. Spatial Composition System（空间构图系统）

**取景规则：**
- **Rule of Thirds（三分法）**：平衡、自然的构图——大多数叙事的默认选择
- **Center Framing（居中构图）**：仪式感、权力、对称——用于重要时刻
- **Negative Space（负空间）**：孤独、隔离、情绪重量——主体被推到边缘
- **Foreground Obstruction（前景遮挡）**：偷窥感、神秘、隐藏观察
- **Frame Within Frame（框中框）**：层次、禁锢、聚焦

**景深设计：**
- 前景 → 中景 → 背景分层
- 通过物体摆放进行环境叙事
- 空间张力：角色之间的距离 = 情感距离

**Blocking Design（人物调度）：**
- 角色位置 = 情感关系
- 距离 = 心理差距
- 运动方向 = 叙事张力
- 视线连续性 = 空间逻辑

### 4. Camera Continuity System（镜头连续性）

在所有镜头中必须遵守的规则：

- **方向一致性**：屏幕方向（左→右 / 右→左）在同一场景中不得翻转，除非明确设计了越轴镜头
- **景别递进**：避免在极端景别之间跳跃而无过渡镜头
- **空间地理**：空间的物理布局必须保持稳定——椅子不会移动，门保持在原位
- **光线方向**：主光方向在同一场景中必须保持一致，除非剧情内的光源发生了移动
- **180 度规则**：摄影机在同一场景内应保持在动作轴线的同一侧，除非用中性镜头打破轴线

### 5. Camera Prompt Template（摄影机提示词模板）

分镜中的每个镜头，摄影机指令必须遵循此模板：

```
镜头类型：[WS / MS / CU / ECU / OTS / POV]
角度：[eye-level / low / high / Dutch / top-down]
运动：[static / dolly-in / dolly-out / tracking / orbit / handheld / crane]
镜头行为：[shallow DOF / deep focus / rack focus to X]
取景：[rule of thirds / centered / negative space / frame-in-frame]
情绪意图：[为什么这个时刻选择这种摄影机方式]
```

## 约束

- 无情绪理由的镜头不可存在——"看着很酷"不是有效的摄影决策。
- 无随机的摄影机运动——每次运动必须服务于叙事推进。
- 不打破 180 度规则——除非有意设计的越轴镜头。
- 镜头连续性必须在交付分镜前跨所有镜头验证。
- 手持运动必须有动机（紧张、现实感、混乱）——不能是默认选择。

## 集成

当被 `director-core` 调用时：
- 从 `director-emotion` 加载情绪蓝图以构建情绪摄影系统
- 产出摄影蓝图
- 输入到 `director-light` 以对齐光影
- 摄影机提示词模板直接输入到分镜和提示词系统
