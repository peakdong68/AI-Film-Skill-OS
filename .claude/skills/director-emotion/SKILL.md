---
name: director-emotion
description: 设计 AI 电影的情绪架构——情绪曲线、叙事节奏、强度评分和情绪→镜头映射。用于情绪设计、情绪曲线、叙事节奏、节奏设计、情绪弧线规划，或当 director-core 路由到 STATE 1（情绪设计）时。也适用于故事感觉平淡、用户想控制观众情绪体验、或需要将抽象感觉映射为具体视觉决策的情况。Design the emotional architecture of an AI film — emotion curves, narrative rhythm, intensity scoring, and emotion-to-shot mapping.
---

# Director Emotion — 叙事情绪引擎

## 概览

设计驱动观众体验的情绪旅程。此技能接收叙事结构（来自 `director-story`），并叠加一条情绪时间线：张力在哪里建立、在哪里释放、每个场景的感觉是什么、以及这些感觉如何映射到摄影机和视觉决策。输出是指导摄影、光影和节奏选择的情绪蓝图。

可独立用于情绪设计，或由 `director-core` 在 STATE 1 调用。

## 加载资源

本技能附带以下参考知识文件，在相应场景下读取：
- 需要情绪弧线模式、情绪节拍结构和强度评分规则时，读取 `references/emotion-narrative.md`
- 需要时间流类型（线性流/压缩流/扩展流）和情绪曲线类型（上升/下降/爆发/波动）时，读取 `references/temporal-flow.md`

## 输入门

至少需要：
- 叙事结构或场景列表（来自 `director-story` 或用户提供）
- 类型或情绪基调参考

如果不足，询问："这个故事的总体情绪基调是什么？比如悬疑、浪漫、压抑、史诗？"

## 输出结构

### 1. Emotional Arc Map（情绪曲线）

定义完整的情绪旅程：

```
[平静 / 稳定]
    ↓
[张力建立 / 好奇]
    ↓
[升级 / 冲突]
    ↓
[顶点 / 危机 / 高潮]
    ↓
[释放 / 解决 / 新状态]
```

为每个阶段分配：
- **阶段名称**：如 "不安"、"发现"、"对峙"、"崩溃"、"接纳"
- **情绪关键词**：2-3 个词捕捉主导感受
- **强度级别**：1-10
- **时长**：占总时长的百分比
- **归属场景**：映射到场景列表

### 2. Emotional Beats（情绪节拍）

识别情绪转换的关键转折点：

```
节拍 1：[事件] → 情绪从 [A] 转为 [B]
节拍 2：[事件] → 情绪从 [B] 转为 [C]
节拍 3：[事件] → 情绪从 [C] 转为 [D]
...
```

每个节拍是观众情绪状态发生变化的时刻。这些是摄影机决策的锚点——影片中最重要的镜头。

### 3. Intensity Timeline（情绪强度分布）

映射整个时长的强度（1-10）：

```
0% ────── 25% ────── 50% ────── 75% ────── 100%
 3         5          8          9          4
[引入]   [建立]     [高潮]     [顶点]     [释放]
```

### 4. Character Emotion Drift（角色情绪变化）

为每个主要角色定义各自独立的情绪轨迹：

```
角色 [A]：
- 场景 1：[情绪状态] → 强度 [N]
- 场景 2：[情绪状态] → 强度 [N]
- ...
- 弧线：[从 X 到 Y 贯穿整个故事]
```

这对角色一致性至关重要——角色的情绪状态必须演进，而非重置。

### 5. Emotion-to-Visual Mapping（情绪→视觉映射）

定义每种主要情绪如何转化为视觉决策：

| 情绪 | Camera | Lighting | Color | Pace |
|---------|--------|----------|-------|------|
| 紧张 Tension | handheld / tight framing | flicker / high contrast | cold / desaturated | accelerating |
| 浪漫 Romance | slow orbit / close-up | warm soft light | gold / amber | slow, breathing |
| 恐惧 Fear | close-up / Dutch angle | low key / shadows | blue-green / dark | erratic |
| 悲伤 Sadness | wide / static / negative space | soft diffused | blue-gray | very slow |
| 力量 Power | low angle / symmetrical | dramatic rim | high contrast | controlled, steady |
| 神秘 Mystery | partial framing / silhouettes | backlight / practical | muted / shadowed | deliberate pause |

将此表用作 `director-emotion` 与 `director-camera` / `director-light` 之间的桥梁。

### 6. Rhythm Structure（节奏结构）

定义整部影片的剪辑节奏：

```
[慢] → [建立] → [快] → [更快] → [骤然停顿] → [缓慢释放]
```

映射节奏密度（每时间段剪切数）并识别静默或静止应占主导的位置。

## 约束

- 每个场景必须被分配一个情绪值——不允许情绪中性场景。
- 情绪必须在全片中发生变化——静态情绪令人乏味。
- 角色情绪变化必须与叙事一致——不允许无动机的情绪转变。
- 情绪→视觉映射必须作为输入传递给 `director-camera` 和 `director-light`。

## 与 director-core 的集成

当被 `director-core` 调用时：
- 从 `director-story` 加载叙事结构
- 产出完整的情绪蓝图
- 提交用户确认
- 将情绪→视觉映射输入 STATE 2（视觉设计）
