---
name: director-emotion
description: 设计 AI 电影的情绪架构——情绪曲线、叙事节奏、强度评分和情绪到镜头的映射。当用户需要情绪设计、情绪曲线、叙事节奏、节奏设计、情绪弧线规划时使用，或在 director-core 路由到 STATE 1（情绪设计）时使用。也可在故事感觉平淡、用户想控制观众情绪体验、或需要将抽象感受映射为具体视觉决策时使用。Design the emotional architecture of an AI film — emotion curves, narrative rhythm, intensity scoring, and emotion-to-shot mapping.
---

# Director Emotion — 叙事情绪引擎

## 概览

设计驱动观众穿越整部电影的情绪旅程。此技能接收一个叙事结构（来自 `director-story`），叠加一条情绪时间轴：紧张在哪里建立、在哪里释放、每场戏感觉如何，以及那些感受如何映射为摄影机和视觉决策。产出是指引 cinematography、lighting 和节奏选择的情绪蓝图。

此技能可独立用于情绪设计，或由 `director-core` 在 STATE 1 调用。

## 输入门

至少需要：
- 一个叙事结构或场景列表（来自 `director-story` 或用户提供）
- 一个类型或情绪基调参考

如果不够，追问："这个故事的总体情绪基调是什么？比如悬疑、浪漫、压抑、史诗？"

## 输出结构

### 1. 情绪弧线图

定义完整的情绪旅程：

```
[平静 / 稳定]
    ↓
[建立紧张 / 好奇]
    ↓
[升级 / 冲突]
    ↓
[顶点 / 危机 / 高潮]
    ↓
[释放 / 解决 / 新状态]
```

为每个阶段指定：
- **阶段名称**: 如"不安"、"发现"、"对抗"、"崩溃"、"接受"
- **情绪关键词**: 2-3 个词捕捉主导感受
- **强度等级**: 1-10
- **时长**: 总时长的百分比
- **哪些场景属于这里**: 映射到场景列表

### 2. 情绪节拍

识别情绪转变的关键转折点：

```
Beat 1: [事件] → 情绪从 [A] 转变为 [B]
Beat 2: [事件] → 情绪从 [B] 转变为 [C]
Beat 3: [事件] → 情绪从 [C] 转变为 [D]
...
```

每个节拍是观众情绪状态发生变化的时刻。这些是摄影机决策的锚点——电影中最重要的镜头。

### 3. 强度时间轴

在完整时长上映射强度（1-10）：

```
0% ────── 25% ────── 50% ────── 75% ────── 100%
 3         5          8          9          4
[引入]    [建立]    [高潮段]   [顶点]     [释放]
```

### 4. 角色情绪漂移

为每个主要角色定义其个人的情绪轨迹：

```
角色 [A]:
- 场景 1: [情绪状态] → 强度 [N]
- 场景 2: [情绪状态] → 强度 [N]
- ...
- 弧线: [从 X 到 Y，贯穿整个故事]
```

这对角色一致性至关重要——角色的情绪状态必须演进，而非重置。

### 5. 情绪→视觉映射

定义每种主要情绪如何转化为视觉决策：

| 情绪 | 摄影机 | 灯光 | 色彩 | 节奏 |
|------|--------|------|------|------|
| 紧张 | handheld / tight framing | flicker / high contrast | cold / desaturated | 加速 |
| 浪漫 | slow orbit / close-up | warm soft light | gold / amber | 缓慢、呼吸感 |
| 恐惧 | close-up / Dutch angle | low key / shadows | blue-green / dark | 不稳定 |
| 悲伤 | wide / static / negative space | soft diffused | blue-gray | 极慢 |
| 力量 | low angle / symmetrical | dramatic rim | high contrast | 克制、稳定 |
| 神秘 | partial framing / silhouettes | backlight / practical | muted / shadowed | 刻意停顿 |

将此作为 `director-emotion` 与 `director-camera` / `director-light` 之间的桥梁。

### 6. 节奏结构

定义整部电影的剪辑节奏：

```
[缓慢] → [建立] → [快速] → [更快] → [骤然停顿] → [缓慢释放]
```

映射节奏密度（每时间段内的剪辑次数），并确定沉默或静止应占主导的位置。

## 约束

- 每场戏必须被赋予情绪值——没有情绪中立的场景。
- 情绪必须在时长内变化——静态情绪是无聊的。
- 角色情绪漂移必须与叙事一致——没有无动机的情绪转变。
- 情绪→视觉映射必须作为输入移交给 `director-camera` 和 `director-light`。

## 与 director-core 的集成

当被 `director-core` 调用时：
- 加载来自 `director-story` 的叙事结构
- 产出完整的情绪蓝图
- 呈现给用户确认
- 将情绪→视觉映射输入到 STATE 2（视觉设计）
