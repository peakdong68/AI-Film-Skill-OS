# Seedance 提示词模板——核心知识

## 转换公式

```
分镜面板
  → STEP 1: 提取（时间、动作、情绪、角色、环境）
  → STEP 2: 转换为电影语法（景别、摄影机、角度、灯光）
  → STEP 3: 添加运动层（身体、面部、环境、摄影机）
  → STEP 4: 添加连续性锁定（相同角色、服装、地点）
  → STEP 5: 压缩为 AI 提示词语言
  = Seedance 提示词
```

## 标准 Seedance 2.0 提示词结构

### 1. Context Lock 上下文锁定
```
从分镜 Part X 继续。
保持相同角色身份、服装、环境和灯光连续性。
```

### 2. Scene Definition 场景定义
时长、地点、时间、情绪

### 3. Character Motion 角色运动
身份描述、身体运动、面部表情变化、眼神方向

### 4. Camera Behavior 摄影机行为
景别、角度、运动、镜头行为、构图、情绪意图

### 5. Lighting Design 灯光设计
色调、强度、方向、情绪映射

### 6. Environment Motion 环境运动
天气、粒子、光行为、背景运动、空间深度

### 7. Sound Direction 声音方向（可选）
氛围声、情绪音效提示、静默的运用

### 8. Negative Constraints 负面约束
```
No text, no subtitles, no watermark, no logo.
No face distortion, no identity change, no face drift.
No wardrobe change, no hairstyle change.
No extra characters appearing.
No scene reset, no environment teleport.
No unnatural motion, no CGI artifacting.
```

## 镜头时长规则

| 总时长 | 镜头数量 | 每镜头时长 |
|---------------|------------|-------------------|
| 15s | 5–7 shots | 2–3s |
| 30s | 8–12 shots | 2–4s |
| 60s | 12–20 shots | 3–5s |
| 3 min | 25–40 shots | 4–6s |

规则：
- 单镜头不超过 5 秒（除非情绪慢镜）
- 每个镜头 = 一个动作单元
- 一个镜头不得包含多个事件

## 6 条核心规则

1. **动作优先**: 描述物理运动，而非情绪标签
2. **摄影机明确**: 每条提示词必须有景别 + 运动 + 角度
3. **时间压缩**: 一个镜头 = 一个动作单元 (2-3s)
4. **角色锁定**: 每条提示词必须有"same character identity"
5. **环境鲜活**: 每个镜头必须有雨/风/光/粒子
6. **摄影机有因**: 每个运动都有情绪动机

## 表演翻译

❌ "她很悲伤"
✔ "她低下头，肩膀下沉，呼吸变慢，眼神回避"

❌ "他很紧张"
✔ "他的手指敲击桌面，反复瞟向门口，下颚紧绷"

AI 视频模型需要物理动作，而非情绪标签。

## 多 Part 生成规则

超过 15 秒的视频，拆分为 Parts：

### Part 1
- previous_video_reference: 无
- 建立世界 + 角色 + 视觉语言

### Part N (N > 1)
- previous_video_reference: Part N-1 的输出
- 保持: character, wardrobe, environment, lighting logic, camera language
- 演进: emotional state continues from Part N-1 endpoint
- 永不重启或重置——连续电影流

## 平台适配

| Platform | Prompt Density | Language | Key Adaptation |
|----------|---------------|----------|----------------|
| Seedance 2.0 | 完整结构化块 | 中文或英文 | 显式连续性锁定 |
| Runway Gen-3 | 简洁 | 优先英文 | 平实语言摄影机 |
| Sora | 自然流 | 英文 | 隐式连续性 |
| Kling | 强运动强调 | 优先中文 | 显式负面约束 |

## 编译工作流

```
镜头数据 (storyboard + character + camera + lighting)
  → 标准化（全部视觉化，无抽象）
  → 冲突解析（修正矛盾）
  → 提示词结构化（8 段格式）
  → 压缩（最少字数，最大可执行性）
  → Seedance 最终提示词
```

## 验证清单（逐镜头）

- [ ] 运动是否视觉清晰？
- [ ] 摄影机行为是否已定义？
- [ ] 灯光是否有意义？
- [ ] 情绪是否以物理方式表达？
- [ ] 连续性是否保持？
- [ ] 提示词是否可直接执行？
