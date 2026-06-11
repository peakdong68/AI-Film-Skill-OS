---
name: director-style
description: 为AI电影制作定义导演的视觉人格与哲学立场——从Observer旁观者、Emotional情绪、Immersive沉浸、Epic史诗、Commercial商业五种导演人格中选择，每种人格具有独特的摄影哲学、节奏策略、光影方式和叙事哲学。当用户需要定义导演风格、选择影片"感觉"、选择导演人格、需要视觉哲学指导，或 director-core 在视觉设计前路由至此技能时使用。也用于"拍得像王家卫"或"用诺兰的方式拍"——将作者参考映射为具体的导演人格。Define the director's visual personality and philosophical stance for AI film production — choose from Observer, Emotional, Immersive, Epic, or Commercial director profiles, each with distinct camera philosophy, pacing strategy, lighting approach, and narrative philosophy.
---

# Director Style — 导演人格系统

## 概述

在设计具体的摄影机运动或光影设置之前，每部AI电影都需要一个导演人格——一种贯穿始终的哲学立场，它主导着摄影机如何看待世界、时间如何流动、情绪如何表达。本技能帮助选择和运用一种导演人格，塑造所有下游决策。

这是视觉设计的"元层面"：不是具体使用什么镜头，而是*什么类型的电影人在拍这部电影*。

可独立使用，也可由 `director-core` 在 STATE 1（故事确认后）和 STATE 2（视觉设计）之间调用。

## 核心理念

> 导演人格是每一个视觉选择背后的 WHY。

没有明确的导演人格，视觉决策将变得随意。有明确人格，每一个摄影机角度、光影选择和节奏决策都可以追溯到一个连贯的哲学体系。

## 导演人格档案

为项目选择主导人格。一部影片 = 一个主导人格。在影片中途混用人格会导致视觉分裂。

### Profile A — Observer Director（旁观者导演）

**视觉哲学**：摄影机观察。它从不干预。它只是见证。

```
哲学：现实自然展开。导演不操控。
摄影机：Static、Wide shot、长镜头、最小运动
角度：Eye-level，偶尔远距离
运动：Static > slow tracking > 极少Dolly
节奏：Slow cinema——长镜头、呼吸空间、静默是结构元素
光影：仅自然光和情节内光源——实景光源、可用光
情绪：含蓄、暗示、从不强迫
叙事：信息被展示，不被讲述。观众自行发现。
```

**最适合**：纪录写实主义、社会题材、慢燃角色研究、新写实主义
**参照坐标**：意大利新写实主义、观察式纪录片、是枝裕和、Slow cinema
**视觉身份**：*世界存在着；摄影机注意到了它。*

### Profile B — Emotional Director（情绪导演）

**视觉哲学**：摄影机与角色共情。它参与到角色的情绪状态中。

```
哲学：情绪驱动每一个决策。摄影机是情绪主体。
摄影机：Close-up 主导、Slow dolly-in、Shallow depth of field
角度：Eye-level 亲密，偶尔 POV
运动：Dolly-in > orbit > handheld（仅在情绪不稳时使用）
节奏：变化——情绪峰值时放慢，紧张释放时加速
光影：富有表现力和情绪性——暖色调 = 亲密，冷色调 = 孤立
情绪：前景化——面部、微表情、呼吸、犹豫
叙事：内心情绪旅程优先于外部情节
```

**最适合**：爱情片、家庭伦理、心理剧、角色驱动故事
**参照坐标**：王家卫、Barry Jenkins、亲密电影
**视觉身份**：*摄影机与角色一同呼吸。*

### Profile C — Immersive Director（沉浸导演）

**视觉哲学**：摄影机成为观众。第一人称体验。没有距离。

```
哲学：观众在故事内部，而非在外部观看。
摄影机：POV 主导、Handheld 写实、Tracking shots 跟随
角度：主观——角色看到的，参与者看到的
运动：Tracking > handheld > FPV > 流畅连续运动
节奏：实时感——动作以体验的速度展开
光影：画面内光源和环境光——你实际能看到的
情绪：即刻和本能——观众与体验之间没有滤镜
叙事：神秘与发现——观众与角色同步了解信息
```

**最适合**：惊悚片、恐怖片、动作片、第一人称叙事、悬疑
**参照坐标**：Paul Greengrass、拾得影像、沉浸式新闻、FPV 电影
**视觉身份**：*你就在那里。你就置身其中。*

### Profile D — Epic Director（史诗导演）

**视觉哲学**：摄影机支配空间。尺度大于亲密。纪念碑式。

```
哲学：世界是广阔的。角色居于其中，而非凌驾其上。
摄影机：Wide shot 主导、Crane、Drone、大规模运动
角度：Low angle（力量）、High angle（尺度）、Top-down（秩序/混乱）
运动：Crane > drone > sweeping dolly > slow orbit
节奏：从容而宏大——缓慢推进至巨大峰值
光影：戏剧性和雕刻感——强方向光、Volumetric、神圣光束
情绪：敬畏与尺度——个体情绪嵌入广阔语境中
叙事：世界构建、历史视野、神话结构
```

**最适合**：历史史诗、科幻世界构建、奇幻、自然纪录片
**参照坐标**：Denis Villeneuve、Terrence Malick、史诗电影
**视觉身份**：*世界才是主角。*

### Profile E — Commercial Director（商业导演）

**视觉哲学**：注意力是首要货币。冲击力大于细腻。

```
哲学：每一帧都必须赢得注意力。视觉冲击是结构性的。
摄影机：多样化——快速剪切、动态运动、产品Hero Shot
角度：Low angle（向往感）、Eye-level（可亲感）、Top-down（产品）
运动：Fast tracking > orbit > push-in > whip pan
节奏：快速且有韵律——从不逗留，始终推进
光影：高级和受控——Beauty lighting、Rim light、高抛光
情绪：向往和即刻——想要、渴望、需要
叙事：Hook → Problem → Solution → Aspiration → CTA
```

**最适合**：广告、品牌片、产品展示、MV
**参照坐标**：高端商业广告、时尚电影、奢侈品广告
**视觉身份**：*每一帧都在卖。*

## 人格选择指南

| 用户说... | 对应人格 |
|---|---|
| "像纪录片一样真实" / "自然观察" | Observer（A） |
| "注重情感表达" / "拍得很走心" / "王家卫风格" | Emotional（B） |
| "第一人称体验" / "身临其境" / "恐怖片" | Immersive（C） |
| "史诗感" / "宏大" / "科幻大片" / "维伦纽瓦风格" | Epic（D） |
| "广告片" / "品牌大片" / "高端商业" | Commercial（E） |

## 导演决策引擎

一旦选定人格，所有下游决策都必须参照它：

### 视觉哲学 → 摄影机决策

| 人格 | 主用镜头 | 主用运动 | 角度偏好 |
|------|---------|---------|---------|
| Observer | Wide, medium | Static, slow track | Eye-level, distant |
| Emotional | Close-up, ECU | Slow dolly-in | Eye-level, intimate |
| Immersive | POV, handheld | Tracking, handheld | Subjective |
| Epic | Wide, extreme wide | Crane, drone, sweep | Low, high, top-down |
| Commercial | Varied, CU product | Fast, dynamic, orbit | Low（向往）, eye（可亲） |

### 视觉哲学 → 节奏决策

| 人格 | 剪辑密度 | 镜头时长 | 静默角色 |
|------|---------|---------|---------|
| Observer | 极低 | 4-8s | 核心结构元素 |
| Emotional | 低-中 | 3-5s | 用于情绪重量 |
| Immersive | 中 | 2-4s | 很少——沉浸需要连续性 |
| Epic | 极低 | 5-10s | 用于尺度和敬畏 |
| Commercial | 极高 | 1-3s | 很少使用——持续向前推进 |

### 视觉哲学 → 光影哲学

| 人格 | 光源 | 光质 | 色温 |
|------|------|------|------|
| Observer | 仅自然光/实景光 | 柔、写实 | 中性 |
| Emotional | 富有表现力、有动机 | 随情绪变化 | 随感受变化 |
| Immersive | 画面内光源、环境光 | 写实、不完美 | 实际存在的色温 |
| Epic | 戏剧性、雕刻感 | 强、有方向性 | 冷或暖主导 |
| Commercial | 受控、高级 | 柔+轮廓光、抛光 | 冷调优雅 |

## 输出格式

```markdown
## 导演人格：[人格名称]

### 视觉哲学
[1-2句：这位导演如何看待世界]

### 摄影哲学
- 主导镜头类型：[列举]
- 运动词汇：[列举]
- 角度特征：[描述]
- 镜头性格：[景深、焦点行为]

### 节奏哲学
- 节奏类型：[slow cinema / classical / fast commercial]
- 剪辑密度：[低 / 中 / 高]
- 静默运用：[结构性 / 情绪性 / 极少]
- 情绪节奏：[张力如何积累和释放]

### 光影哲学
- 光影理念：[natural / expressive / diegetic / dramatic / controlled]
- 主光质量：[soft / hard / varied]
- 色温弧线：[冷暖如何演变]

### 叙事哲学
- 叙事方式：[observe / feel / experience / awe / sell]
- 信息策略：[show don't tell / emotional reveal / gradual discovery / spectacle]

### 对项目的影响
- 该人格对以下方面的影响：[故事 → 摄影机 → 光影 → 角色 → 节奏]
```

## 约束

- 一个项目 = 一个主导导演人格。混用人格导致视觉精神分裂。
- 人格必须在 `director-camera` 和 `director-light` 工作之前选定。
- 人格选择必须有故事和情绪意图的支撑——不能随意。
- 作者参考（王家卫、Nolan 等）必须转化为具体的人格属性，而非作为模仿复制。

## 集成

当 `director-core` 调用时：
- 在 STATE 1（故事+情绪确认后）完成选择
- 输出输入到 STATE 2——`director-camera` 和 `director-light` 使用该人格指导其决策
- 该人格在所有下游技能中被引用（而非重复复制）


## 保存输出

交付最终输出后，提示用户保存：



用户确认后，将输出写入指定路径。
