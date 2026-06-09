# Seedance 2.0 提示词方法论 — 内置参考知识

供 `seedance-video-prompt` 技能使用。

---

## Director Formula（导演公式）

```
Subject + Action + Scene + Camera + Lighting/Style + Audio + Constraints
```

将主体和主要动作放在最前面——早期子句设定镜头层次。如果参考资产已显示信息，不强制填充每个槽位。对于 I2V，只描述静态图像无法呈现的内容：运动、摄影机、时间推进、变换、音频和保留约束。

| 槽位 | 用途 | Prompt 就绪模式 |
|---|---|---|
| Subject | 模型必须追踪的锚点。 | `Original ceramic perfume bottle on black acrylic, label preserved exactly` |
| Action | 可见的变化。 | `condensation beads form and slide down the glass over five seconds` |
| Scene | 仅描述参考中未显示的内容。 | `quiet rain-lit kitchen counter, shallow depth of field` |
| Camera | 一个带终点的主要运动。 | `slow dolly-in from medium product shot to macro label detail` |
| Light and style | 物理光源加上安全的视觉语言。 | `warm practical key from frame left, cool blue rim, clean commercial realism` |
| Audio | 环境音、音效、对白或静默。 | `Sound: low room tone, soft glass chime on final frame` |
| Constraints | 保留项和排除项。 | `do not alter logo, shape, label, or cap geometry` |

## 模式门（Mode Gates）

| 模式 | 编译优先级 | 常见错误 | 修复 |
|---|---|---|---|
| T2V | 用紧凑层构建完整镜头。 | 一个片段事件过多。 | 保持一个可见节拍和一个终点。 |
| I2V | 保留可见身份；添加运动。 | 重新描述图像直至产品或面部漂移。 | 写 `preserve [Image1] exactly`；仅添加动态变化。 |
| V2V | 传递运动、摄影机或节奏。 | 复制未经授权的肖像或场景细节。 | 使用自有/已授权/已许可的参考并限制传递角色。 |
| R2V | 为每个资产分配独立角色。 | 一个参考被要求同时控制身份、姿势、场景和风格。 | 拆分角色或优先最重要的角色。 |
| FLF2V | 从首帧移动到末帧。 | 将末帧视为模糊情绪而非终点。 | 声明 `[Image2]` 是最终视觉目标。 |
| Edit | 保留源片段，仅更改一个层。 | 重写整个场景并丢失连续性。 | 写 `[Video1] is the source clip; change only...` |
| Extend | 从现有最终状态继续。 | 在片段之后开始全新场景。 | 使用最后一帧作为连续性锚点，更改一个变量。 |

## @[ref] 角色映射

在撰写提示词之前，为每个上传资产分配主角色。角色映射防止身份、logo、场景所有权或摄影机/运动指令之间的意外互串。

| 资产 | 推荐角色 | 避免 |
|---|---|---|
| Image | identity, product, pose, costume, environment, first frame, last frame | 要求它定义未见的运动 |
| Video | motion, camera, pacing, blocking, timing, gesture rhythm | 复制受保护的身份、logo 或场景所有权 |
| Audio | rhythm, tempo, mood, ambience, delivery tone, music texture | 假定语音/歌曲/肖像已授权 |

**核心规则：**
- 精确保留参考标签。
- 在写风格语言之前，给每个参考分配一个主角色。
- 写清楚什么应该传递、什么不应该传递。
- 当授权不明确时，传递广义的运动/节奏/情绪/制作功能，而非受保护的身份。

**角色映射声明模板：**

```
@[产品图片1] 控制产品身份——严格锁定颜色、印花图案、印花颜色、大小、位置、版型。
@[角色图片1] 控制角色身份——严格保持同一位模特的主体特征，面部自然。
@[分镜图片1] 控制动作节奏——用作动作规划参考，不渲染分镜表本身。
@[背景图片1] 控制环境——严格保持空间结构、光线、色调和陈列稳定。
@[音频1] 仅控制节奏和能量——不复制受保护的声音、歌曲或表演者身份。
```

## I2V 核心原则

**只描述图像无法呈现的内容。** 静态图像已包含主体身份、产品形态、服装、调色板、构图和背景。重新描述这些静态细节通常导致漂移。仅添加：运动、摄影机、时间推进、变换、光线变化、音频和保留约束。

**最小 I2V 模板：**
```
[Image1] is the reference; preserve [identity/product/scene] exactly.
Only [motion] changes. Camera: [one move]. Lighting: [source or transition].
Sound: [cue]. Constraint: [what must not change].
```

### I2V 优质添加项

| 添加 | 示例 |
|---|---|
| 微表情 | `subject blinks once and lowers their eyes` |
| 产品光线扫过 | `thin highlight travels across the label` |
| 天气 | `rain streaks behind the subject; droplets bead on the surface` |
| 摄影机 | `slow dolly-in from current composition to tighter detail` |
| 氛围 | `dust catches the doorway beam and settles` |
| 音频 | `soft room tone, one key click at the endpoint` |

### 常见 I2V 失败修复

| 失败 | 修复 |
|---|---|
| 身份漂移 | 减少新视觉描述，加强保留约束 |
| 摄影机跳变 | 使用一个摄影机运动，注明起止点 |
| 产品变形 | 声明 `preserved, static identity, no shape change` |
| 画面静止 | 添加一个物理动作和一条时间提示 |
| 背景变化 | 保留环境布局，仅动画化光线/天气/氛围 |
| 手部变形 | 简化手部动作或将手部排除在主动作之外 |

## 压缩规则

提示词过长时，**按此顺序删除：**

1. 重复的风格形容词
2. 泛化质量词
3. 参考中已可见的背景细节
4. 次要摄影机运动
5. 次要动作
6. 推测性情绪标签

**不惜一切代价保留：**
1. 参考标签及其角色
2. 主体或产品身份
3. 动作动词和可见终点
4. 一个摄影机运动
5. 物理光源或氛围
6. 音频提示或静默指令
7. 安全/IP/连续性约束

**紧凑中文 I2V 模板：**
```
@[图1]为参考，严格保持[主体]不变；仅加入[动作/光线/镜头]。声音：[提示]。约束：[不变项]。
```

## Anti-Slop 去水词库

将空洞评价词替换为可观察的生产语言。规则：**若无法被相机、麦克风、测光表或秒表检测到——重写。**

| 空洞词 | 替换为 |
|---|---|
| cinematic | shot scale, camera move, lighting, grade |
| epic | physical scale, stakes, crowd size, lens distance |
| beautiful | color, texture, composition, material, light behavior |
| stunning | visible contrast, reveal, movement, or detail |
| dynamic | specific movement, speed, and endpoint |
| dramatic | blocking, shadow, silence, or camera pressure |
| ultra-realistic | material behavior, skin texture, lens artifacts, natural motion |
| cool transition | match cut, whip pan, dissolve, hard cut, object wipe |
| magical | particle behavior, glow source, motion path, interaction |
| professional | product lighting setup, clean background, controlled camera |
