---
name: director-light
description: 为 AI 电影制作设计色彩脚本和光影系统——情绪→色彩映射、光影推进图、场景调色板设计和视觉温度控制。用于光影设计、光影设计、色彩脚本、色彩脚本、氛围灯光、视觉氛围，或当 director-core 路由到 STATE 2（视觉设计）时。也适用于影片视觉平淡、用户想要 Pixar 风格的色彩脚本、或需要跨镜头保持光影连续性的情况。Design the color script and lighting system for AI film production — emotion-to-color mapping, lighting progression, scene palette design, and visual temperature control.
---

# Director Light — 色彩与光影智能引擎

## 概览

设计赋予影片情绪质感的视觉氛围系统。此技能构建两个相互关联的系统：Color Script（色彩脚本），将情绪旅程映射到整个时长的特定调色板；Lighting Design（光影设计），指定每个场景的光源、质量和演进。输出确保每一帧都有视觉一致性和情绪意图性。

可独立用于光影/色彩设计，或由 `director-core` 在 STATE 2 调用。

## 加载资源

本技能附带以下参考知识文件，在相应场景下读取：
- 需要完整的情绪→色彩映射表、灯光类型速查、场景调色板模板、常见灯光预设方案时，读取 `references/color-lighting.md`

## 核心原则

> 光和色彩是情绪演员，不是环境默认值。

每个光影和色彩决策都必须服务于叙事。暖、冷、对比度、饱和度——这些是控制观众感受的工具，不仅仅是审美偏好。

## 输出结构

### 1. Global Color Script（全片色彩脚本）

设计贯穿整部影片的色彩旅程——类似 Pixar 的色彩脚本。为每个叙事阶段（映射自 `director-emotion` 的情绪弧线）：

```
阶段 1 [名称]：[时长占比%]
- 主导调色板：[2-3 种颜色，含色值或描述性名称]
- 饱和度级别：[low / medium / high]
- 对比度级别：[low / medium / high]
- 色温：[warm / cool / neutral / mixed]
- 视觉参考：[用一句话描述画面质感]

阶段 2 [名称]：[时长占比%]
...
```

色彩脚本必须展示演进——色彩必须随故事而变化，不能静止。

### 2. Emotion-to-Color Mapping（情绪→色彩映射）

定义色彩语言：

| 情绪 | 主导色彩 | 色温 | 饱和度 | 对比度 |
|---------|---------------|-------------|------------|----------|
| 悲伤/孤独 Sadness | 蓝灰 Blue-gray | 冷 Cold | 低饱和 Desaturated | 低 Low |
| 爱/浪漫 Love | 暖金/琥珀 Warm gold, amber | 暖 Warm | 中 Medium | 柔 Soft |
| 恐惧/惊悚 Fear | 绿/暗去饱和 Green, dark | 冷 Cold | 极低 Very low | 高 High |
| 愤怒/冲突 Anger | 红/高对比 Red, high contrast | 热 Hot | 高 High | 极高 Very high |
| 平静/释然 Peace | 柔蓝/暖白 Soft blue, warm white | 中性暖 Neutral-warm | 中 Medium | 低 Low |
| 神秘 Mystery | 深紫/阴影 Deep purple, shadow | 冷暖混合 Cold-warm mix | 可变 Variable | 高 High |
| 权力/奢华 Power | 黑/金/银 Black, gold, silver | 冷 Cool | 中低 Low-mid | 高 High |
| 希望/乐观 Hope | 暖黄/柔绿 Warm yellow, soft green | 暖 Warm | 中 Medium | 柔 Soft |

### 3. Lighting Progression Map（光影推进图）

定义光影如何随叙事变化：

```
场景 1：[光影方案] → 情绪功能：[为什么]
场景 2：[光影方案] → 如何从场景 1 演变而来
...
```

为每个场景的光影指定：

**灯光类型：**
| 类型 | 中文 | 情绪功能 |
|------|------|-------------------|
| Natural Light | 自然光 | 现实感、纪录片质感 |
| Hard Light | 硬光 | 冲突、压力、残酷真相 |
| Soft Diffused Light | 柔光 | 浪漫、梦境、回忆 |
| Neon / Colored Light | 霓虹光 | 科技、夜晚、都市、超现实 |
| Silhouette / Backlight | 剪影光 | 神秘、情绪隐藏、揭示 |
| Practical Light | 实景光 | 剧情内光源（灯、窗户、屏幕） |
| Volumetric Light | 体积光 | 氛围、光束、上帝之光 |
| Flicker Light | 闪烁光 | 不稳定、紧张、恐惧 |

**光线方向：**
- 主光位置和动机
- 辅助光强度和质量
- 轮廓光/背光用于主体分离
- 每个光源的色温
- 阴影质量（软/硬）和方向

### 4. Scene Palette System（场景专属调色板）

为每个场景锁定调色板：

```
SCENE [N]：[名称]
- Key light 主光：[来源、方向、色温、质量]
- Fill 辅助光：[来源、强度、色温]
- Rim 轮廓光：[来源、颜色、目的]
- Ambient 环境光：[整体色调]
- Shadows 阴影：[密度、色调偏好]
- Special 特殊：[体积光、实景光、反射]
- Palette lock 调色板锁定：[此场景中必须保持一致的元素]
```

### 5. Visual Temperature Curve（冷暖变化曲线）

追踪整个时长的色温：

```
暖 Warm ┤         ╭──╮
         │        ╱    ╲
中 Neut ┤───────╱      ╲──────
         │      ╱        ╲
冷 Cool ┤╭────╱          ╲────
         │╲
         0%──────25%──────50%──────75%──────100%
```

用叙事事件标注温度转换——从暖到冷的转变应对应一个故事节拍。

### 6. Lighting Continuity Rules（光影连续性）

全片必须遵守的规则：

- 主光方向在同一场景内必须保持一致
- 色温变化必须有动机（时间变化、地点变化、情绪转折）
- 阴影质量应演进，而非随意重置
- 在一个镜头中建立的实景光源必须在同一场景的后续镜头中持续存在
- 不允许无动机的"美颜灯光"——每个光源必须有叙事或剧情内的理由

## 情绪灯光模板

常见灯光氛围的快速参考：

**浪漫 Romantic：**
- 单侧暖主光（黄金时刻或实景灯）
- 柔辅光减少阴影
- 微暖轮廓光做发丝光
- 浅景深带散景
- 轻微暖色调色

**紧张/惊悚 Tension / Thriller：**
- 非常规角度的硬主光（低位或高位）
- 深阴影伴最少辅光
- 冷色温
- 实景光源（闪烁荧光灯、街灯）
- 高对比度调色

**奢华/商业 Luxury / Commercial：**
- 大面积柔主光均匀照明
- 强轮廓光/背光做产品边缘界定
- 冷调阴影增加深度
- 表面受控反射
- 干净的高调调色

## 约束

- 每个场景必须有确定的主光光源——不允许纯环境光。
- 色彩必须随叙事演进——静态调色板 = 错失的机会。
- 光影连续性必须在分镜交付前验证。
- 同一场景的镜头之间不允许无动机的色调跳变。

## 集成

当被 `director-core` 调用时：
- 从 `director-emotion` 加载情绪蓝图以构建情绪→色彩映射
- 与 `director-camera` 对齐以确保视觉语言一致
- 场景调色板系统直接输入到分镜和提示词编译
