# Seedance Genre Recipes — 捆绑参考

标准化的视频类型模式与提示词骨架。用作起始模板，非僵化规则。选择匹配产出的配方，然后自定义主体、动作、镜头、光影、音频和约束。

## 配方家族

| 家族 | 最佳用途 | 核心模式 |
|---|---|---|
| Product / 产品 | 广告、电商、英雄镜头、材质展示。 | `产品锚点 + 一次材质变化 + 受控镜头 + Logo 保留` |
| Lifestyle / 生活方式 | 人物使用、美食、旅行、社交片段。 | `简单动作 + 生活化环境 + 手持或自然光 + 环境声` |
| Drama / 剧情 | 情绪、对白、短叙事节拍。 | `角色标签 + 手势 + 动机驱动的镜头 + 静默或稀疏音效` |
| Music video / 音乐视频 | 节拍同步、舞蹈、风格化剪辑。 | `节奏参考 + 可见节拍变化 + 灯光脉冲 + 清晰的角色调度` |
| Landscape / 风景 | 定场镜头、自然、氛围。 | `缓慢运镜 + 天气运动 + 层次深度 + 自然音效` |
| Commercial / 商业 | 品牌安全的精致感和功能性。 | `问题/使用/结果节拍 + 精确产品约束 + 干净光线` |
| Animation / 动画 | 原创角色和风格化运动。 | `媒介 + 造型语言 + 调色板 + 弹性质感或重量感运动` |
| VFX / 视效 | 变形、粒子、天气、能量特效。 | `源 + 材质行为 + 交互 + 消散终点` |
| First/last frame / 首帧尾帧 | 帧间过渡、产品状态变化、角色姿势目标。 | `首帧 + 尾帧 + 连续过渡 + 身份锁定` |
| Commercial campaign / 商业广告系列 | 6/10/15/30s 变体、竖屏/社交裁剪版、无字/本地化母版。 | `Hook + 产品验证 + 结束状态 + 裁剪矩阵 + 交付备注` |

## 提示词骨架

**产品 I2V：**
```
[Image1] is the product reference; preserve logo, label, shape, and materials exactly.
[One material or light change]. Camera: [single move]. Lighting: [physical source].
Sound: [ambient/SFX].
```

**剧情 T2V：**
```
Character A [visible emotional action] in [specific setting].
Camera: [motivated framing]. Lighting: [motivated source].
Sound: [ambient or short dialogue]. End state: [changed expression/action].
```

**参考运动：**
```
[Video1] provides only [camera/action/timing] reference; do not transfer identity,
costume, logo, or environment. New subject: [authorized/original subject].
[Action and endpoint].
```

**首帧/尾帧：**
```
[Image1] is the first frame. [Image2] is the last frame.
Preserve [identity/product/scene anchors]. Generate a continuous transition from
[start state] to [end state]. Camera: [locked or one controlled move].
Sound: [ambient/SFX].
```

**动画：**
```
Original [character archetype] [action] in [environment].
Style: [medium, line quality, texture, palette]. Motion: [rhythm].
Camera and sound: [simple support].
```

## 选择规则

当多个目标冲突时，优先选择保护最脆弱需求的配方：

产品身份 > 镜头奇观。
口型同步 > 大幅头部运动。
角色一致性 > 复杂编舞。
首帧/尾帧目标精度 > 额外风格变化。
安全与授权 > 风格模仿。
