---
name: director-seedance
description: 将所有前期制作产物（分镜、角色设定图、摄影机蓝图、灯光设计）编译为可执行的 Seedance 2.0 / Runway / Sora / Kling 图像生成视频提示词。这是 AI Film OS 管线中的最终编译器。用于生成 Seedance 提示词、视频生成提示词、分镜转视频转换、视频提示词编译，或 director-core 路由到 STATE 5（提示词编译）时。当用户已有分镜帧和角色设计待转换为生产级视频生成指令时使用。Use when the user needs Seedance prompts, storyboard-to-video conversion, video prompt compilation, or when director-core routes to STATE 5 (Prompt Compilation).
---

# Director Seedance — 提示词编译器引擎

## 概览

这是 AI Film OS 管线的最终执行引擎。它接收完整的生产包——叙事结构、情绪蓝图、摄影机语言、灯光设计、角色身份锁定和分镜帧——并将它们编译为可执行的视频生成提示词。每条提示词包含运动指令、摄影机行为、灯光方向、角色连续性锁定、环境动态和负面约束。

编译器的工作是将导演语言转化为机器可执行的运动指令。它不是创意写作工具——而是精密的编译系统。

可独立用于提示词编译，也可被 `director-core` 在 STATE 5 调用。

## 编译原则

> Seedance 提示词不是描述文字。它们是运动指令。

编译器将三个层级翻译为一个可执行块：
1. **故事层**（发生什么）→ 角色运动 + 情绪推进
2. **电影语言层**（如何拍摄）→ 摄影机行为 + 灯光方向
3. **机器层**（执行约束）→ 连续性锁定 + 负面规则

## 输入要求

编译前，验证所有上游产物是否就绪：

- [ ] 分镜帧（来自 storyboard-sketch 或 storyboard-prompt）
- [ ] 角色身份锁定（来自 director-character）
- [ ] 摄影机语言蓝图（来自 director-camera）
- [ ] 灯光设计（来自 director-light）
- [ ] 项目元数据：每镜头时长、画幅比例、目标平台

如有任何产物缺失，停止并路由回相应的 director 技能。绝不从残缺输入编译。

## 输出结构：Seedance 提示词包

为每个分镜帧生成完整的提示词块：

```markdown
## SHOT [N]: [镜头标题]

### 上下文锁定
从分镜 [帧 N-1 / Part X] 继续。
保持严格连续性：与已建立的角色身份、服装、环境和灯光逻辑一致。

### 场景定义
Duration: [N] 秒
Location: [具体地点]
Time: [时间段 / 时间上下文]
Mood: [来自 director-emotion 的情绪关键词]

### 角色运动
角色 [名称]:
- 物理动作: [一个清晰的单一动作——身体做什么]
- 面部表情: [动作过程中的微表情变化]
- 眼部行为: [方向、焦点转移、眨眼模式]
- 情绪推进: [从状态 A → 向状态 B]
- 身份锁定: 与角色设定图相同的面部、发型、体型、服装

### 摄影机行为
Shot type: [WS / MS / CU / ECU / OTS / POV]
Angle: [eye-level / low / high / Dutch / top-down]
Movement: [static / dolly-in / dolly-out / tracking / orbit / handheld]
Lens behavior: [shallow DOF / deep focus / rack focus to X]
Framing: [rule of thirds / centered / negative space / frame-in-frame]
Emotional intent: [为什么选择这个摄影机——来自 director-camera]

### 灯光设计
Key light: [光源、方向、色温、质感]
Fill light: [光源、强度、色温]
Rim/Backlight: [光源、颜色、用途]
Contrast level: [low / medium / high]
Atmosphere: [volumetric / haze / clean / fog]
Color continuity: [引用 director-light 的场景调色板]

### 环境动态
- Weather/atmosphere: [雨、风、灰尘、雾、雪——或无]
- Background motion: [此镜头中环境中有什么在动]
- Particle behavior: [如有粒子，具体运动方式]
- Reflections/shadows: [关键环境光交互]
- Spatial depth: [前景/背景关系]

### 声音方向（可选）
- Ambience: [空间音、天气声、城市底噪]
- Emotional cue: [音乐渐强、心跳、静默、持续低音]
- Silence usage: [在何处以静默制造张力]

### 负面约束
No text, no subtitles, no watermark, no logo.
No face distortion, no identity change, no face drift.
No wardrobe change, no hairstyle change.
No extra characters appearing.
No scene reset, no environment teleport.
No unnatural motion, no CGI artifacting (unless specified).
No style shift (maintain cinematic realism throughout).
```

## 编译规则

### 规则 1：动作精确
- 每条提示词必须描述一个清晰的物理动作，而非抽象情绪状态。
- ❌ "她很悲伤" → ✔ "她的肩膀下沉，下颌放低，眼神回避，呼吸变慢"
- 使用 `director-character` 中的情绪→动作映射。

### 规则 2：摄影机必须明确
- 每条提示词必须有来自 `director-camera` 的景别、角度和运动。
- 摄影机决策必须追溯到情绪意图——不得有无动机的摄影机行为。

### 规则 3：时间必须压缩
- 1 个分镜帧 = 1 个动作单元 = 2-5 秒
- 单条提示词不得包含多个时间分离的动作

### 规则 4：角色必须锁定
- 每条提示词必须引用 `director-character` 中的角色身份锁定
- 显式声明："same [角色名], same face, same hair, same wardrobe"
- 不得重新生成或重新描述角色——引用锁定

### 规则 5：环境必须鲜活
- 每条提示词必须至少包含一个环境动态元素
- 静态环境在 AI 视频生成中显得死板

### 规则 6：连续性必须跨越镜头
- 每个镜头的上下文锁定引用前一个镜头
- 多 Part 视频（>15s）必须前向传递：previous_video_reference + current_storyboard_reference

## Multi-Part Continuity System (多 Part 连续系统)

超过 15 秒的视频，拆分为 Parts 并绑定：

### Part 1
- 建立世界 + 角色 + 视觉语言
- 设定所有连续性参数的基线

### Part 2+
- 必须引用上一段视频输出作为连续性锚点
- 必须前向传递：角色身份、服装、环境、灯光逻辑、摄影机语言
- 必须演进而非重置——情绪状态应从 Part N-1 的终点继续

### 多 Part 提示词模板
```markdown
## PART [N]: [part 标题]

### Part 连续性
这是 Part [N-1] 的直接延续。
引用前一个输出作为连续性基线。
Maintain: same character identity, same wardrobe, same environment,
same lighting logic, same camera language.
Evolve: emotional state continues from Part [N-1] endpoint.

### Shot [M].1: [镜头标题]
[完整提示词块，上下文锁定引用 Part N-1]
```

## 验证清单

交付最终提示词包前，逐镜头验证：

- [ ] 动作视觉清晰且物理可行
- [ ] 摄影机行为已定义（景别 + 角度 + 运动 + 镜头）
- [ ] 灯光有意义且匹配场景调色板
- [ ] 情绪以物理方式而非抽象方式表达
- [ ] 角色身份锁定已嵌入
- [ ] 环境至少有一个动态元素
- [ ] 负面约束块已存在
- [ ] 上下文锁定引用正确的上一个镜头
- [ ] 时长已指定
- [ ] 提示词在目标工具中可直接执行

## 平台适配

按平台调整提示词密度和具体程度：

| 平台 | 提示词风格 |
|----------|-------------|
| **Seedance 2.0** | 完整结构化块，中文或英文，显式连续性锁定 |
| **Runway Gen-3** | 简洁英文，摄影机运动用平实语言 |
| **Sora** | 自然语言流，通过一致性描述实现隐式连续性 |
| **Kling** | 优先中文，强运动强调，显式负面约束 |

## 集成

被 `director-core` 调用时：
- 加载所有上游产物（分镜、角色、摄影机、灯光）
- 验证预检清单（全部分镜已确认、角色已锁定、视觉语言已定义）
- 编译完整提示词包
- 执行验证清单
- 呈现供最终用户审核
- 确认后，标记 STATE 5 完成
