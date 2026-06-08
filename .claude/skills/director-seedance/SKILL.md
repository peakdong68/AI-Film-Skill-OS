---
name: director-seedance
description: 将所有前期制作产出物（分镜、角色表、摄影蓝图、光影设计）编译为可执行的 Seedance 2.0 / Runway / Sora / Kling 图生视频提示词。这是 AI Film OS 管线的最终编译器。用于 Seedance 提示词、视频生成提示词、分镜转视频、视频提示词编译，或当 director-core 路由到 STATE 5（提示词编译）时。也适用于用户已有分镜帧和角色设计、需要将其转化为可用于生产的视频生成指令的情况。Compile all prior production artifacts into executable image-to-video prompts for Seedance 2.0 / Runway / Sora / Kling.
---

# Director Seedance — 提示词编译引擎

## 概览

这是 AI Film OS 管线的最终执行引擎。它接收完整的制作包——叙事结构、情绪蓝图、摄影机语言、光影设计、角色身份锁定和分镜帧——并将其编译为可执行的视频生成提示词。每条提示词都包含运动指令、摄影机行为、光影方向、角色连续性锁定、环境动态和负面约束。

编译器的工作是将导演语言转化为机器可执行的运动指令。它不是创意写作工具——而是精确的编译系统。

可独立用于提示词编译，或由 `director-core` 在 STATE 5 调用。

## 加载资源

本技能附带以下参考知识文件，在相应场景下读取：

- 需要**Seedance 标准 Prompt 结构模板**（8段完整结构：Context Lock / Scene / Character Motion / Camera / Lighting / Environment / Sound / Negative Constraints 各段详细规范和示例）时，读取 `references/seedance-templates.md`
- 需要**6条核心编译规则**（动作优先、镜头明确、时间压缩、角色锁定、环境动态、摄影机理由）或**多Part连续性规则**或**平台适配差异表**（Seedance 2.0 / Runway Gen-3 / Sora / Kling 的 Prompt 密度和风格差异）时，读取 `references/seedance-templates.md`

## 编译原则

> Seedance 提示词不是描述。它们是运动指令。

编译器将三层转化为一个可执行块：
1. **Story Layer（故事层）**（发生了什么）→ 角色运动 + 情绪推进
2. **Film Language Layer（电影语言层）**（怎么拍）→ 摄影机行为 + 光影方向
3. **Machine Layer（机器层）**（执行约束）→ 连续性锁定 + 负面规则

## 输入要求

编译前，验证所有上游产出物是否齐备：

- [ ] 分镜帧（来自 storyboard-sketch 或 storyboard-prompt）
- [ ] 角色身份锁定（来自 director-character）
- [ ] 摄影机语言蓝图（来自 director-camera）
- [ ] 光影设计（来自 director-light）
- [ ] 项目元数据：每个镜头的时长、画幅比例、目标平台

如果任何产出物缺失，立即停止并路由回相应的导演技能。严禁从不完整的输入编译。

## 输出结构：Seedance 提示词包

为每个分镜帧产出完整的提示词块：

```markdown
## SHOT [N]：[镜头标题]

### Context Lock 上下文锁定
继续自分镜 [帧 N-1 / Part X]。
严格保持连续性：与之前建立的相同角色身份、服装、环境和光影逻辑。

### Scene Definition 场景定义
时长：[N] 秒
地点：[具体地点]
时间：[时间 / 时间语境]
情绪：[来自 director-emotion 的情绪关键词]

### Character Motion 角色运动
角色 [姓名]：
- 身体动作：[单一清晰的动作——身体做什么]
- 面部表情：[动作过程中的微表情变化]
- 眼神行为：[方向、焦点转移、眨眼模式]
- 情绪推进：[从状态 A → 向状态 B]
- 身份锁定：与角色表相同的面部、发型、体型、服装

### Camera Behavior 摄影机行为
镜头类型：[WS / MS / CU / ECU / OTS / POV]
角度：[eye-level / low / high / Dutch / top-down]
运动：[static / dolly-in / dolly-out / tracking / orbit / handheld]
镜头行为：[shallow DOF / deep focus / rack focus to X]
取景：[rule of thirds / centered / negative space / frame-in-frame]
情绪意图：[为什么这样拍——来自 director-camera]

### Lighting Design 光影设计
主光：[来源、方向、色温、质量]
辅光：[来源、强度、色温]
轮廓光/背光：[来源、颜色、目的]
对比度级别：[low / medium / high]
氛围：[volumetric / haze / clean / fog]
色彩连续性：[引用 director-light 的场景调色板]

### Environment Dynamics 环境动态
- 天气/氛围：[rain, wind, dust, fog, snow——或 none]
- 背景运动：[此镜头中环境里有什么在动]
- 粒子行为：[如适用，具体的粒子运动]
- 反射/阴影：[关键环境光交互]
- 空间深度：[前景/背景关系]

### Sound Direction 声音方向（可选）
- 氛围音：[房间声、天气声、城市嗡鸣]
- 情绪提示：[音乐渐强、心跳、静默、持续低音]
- 留白运用：[何处用静默制造张力]

### Negative Constraints 负面约束
不要文字、不要字幕、不要水印、不要 Logo。
不要面部变形、不要身份变化、不要面部漂移。
不要服装变化、不要发型变化。
不要出现额外角色。
不要场景重置、不要环境瞬移。
不要不自然的运动、不要 CGI 人工痕迹（除非指定）。
不要风格切换（全程保持 cinematic realism）。
```

## 编译规则

### Rule 1：动作精确
- 每条提示词必须描述一个清晰的物理动作，而非抽象的情绪状态。
- ❌ "她很悲伤" → ✔ "她的肩膀下沉、下颌降低、眼神回避接触、呼吸变慢"
- 使用 `director-character` 中的情绪→动作映射。

### Rule 2：镜头必须明确
- 每条提示词必须携带来自 `director-camera` 的镜头类型、角度和运动。
- 摄影机决策必须可追溯到情绪意图——杜绝无动机的摄影机行为。

### Rule 3：时间必须压缩
- 1 个分镜帧 = 1 个动作单元 = 2-5 秒
- 单条提示词不得包含多个时间分离的动作

### Rule 4：角色必须锁定
- 每条提示词必须引用来自 `director-character` 的角色身份锁定
- 显式声明："同一 [角色姓名]、同一张脸、同一发型、同一服装"
- 绝不要重新生成或重新描述角色——引用锁定即可

### Rule 5：环境必须鲜活
- 每条提示词必须包含至少一个环境动态元素
- 静态环境在 AI 视频生成中显得死气沉沉

### Rule 6：连续性必须跨镜头
- 每个镜头的上下文锁定引用上一镜头
- 多 Part 视频（>15s）必须前传：previous_video_reference + current_storyboard_reference

## Multi-Part Continuity System（多 Part 连续系统）

对于超过 15 秒的视频，拆分为 Part 并绑定它们：

### Part 1
- 建立世界 + 角色 + 视觉语言
- 为所有连续性参数设定基线

### Part 2+
- 必须引用上一视频输出作为连续性锚点
- 必须前传：角色身份、服装、环境、光影逻辑、摄影机语言
- 必须演进，而非重置——情绪状态应从 Part N-1 结束点继续

### 多 Part 提示词模板
```markdown
## PART [N]：[Part 标题]

### Part 连续性
这是 Part [N-1] 的直接延续。
引用上一输出作为连续性基线。
保持：同一角色身份、同一服装、同一环境、
同一光影逻辑、同一摄影机语言。
演进：情绪状态从 Part [N-1] 结束点继续。

### Shot [M].1：[镜头标题]
[完整提示词块（同上），上下文锁定引用 Part N-1]
```

## 验证清单

交付最终提示词包前，验证每个镜头：

- [ ] 动作在视觉上清晰且物理上可行
- [ ] 摄影机行为已定义（镜头 + 角度 + 运动 + 镜头行为）
- [ ] 光影有意义且匹配场景调色板
- [ ] 情绪通过身体动作表达，而非抽象描述
- [ ] 角色身份锁定已嵌入
- [ ] 环境至少有一个动态元素
- [ ] 负面约束块存在
- [ ] 上下文锁定引用了正确的上一镜头
- [ ] 时长已指定
- [ ] 提示词可在目标工具中直接使用

## 平台适配

根据平台调整提示词密度和特异性：

| 平台 | 提示词风格 |
|----------|-------------|
| **Seedance 2.0** | 完整结构化块，中文或英文，显式连续性锁定 |
| **Runway Gen-3** | 简洁英文，摄影机运动用平实语言 |
| **Sora** | 自然语言流，通过一致描述实现隐式连续性 |
| **Kling** | 中文优先，强烈运动强调，显式负面约束 |

## 集成

当被 `director-core` 调用时：
- 加载所有上游产出物（分镜、角色、摄影机、光影）
- 验证预检清单（所有分镜已确认、角色已锁定、视觉语言已定义）
- 编译完整提示词包
- 运行验证清单
- 提交最终用户审核
- 确认后，标记 STATE 5 完成
