# AI Film Skill OS — 技能体系文档

## 概览

本项目为 AI 视频/电影制作提供 13 个 Claude Code 技能，分为两大体系：

- **Storyboard 系列 (4个)**：生成分镜图提示词，面向 AI 图像生成器和 Seedance I2V
- **Director 系列 (9个)**：完整的 AI 电影制作管线，从创意到可执行视频提示词

## 技能地图

```
                    ┌─────────────────────────┐
                    │     director-core         │
                    │   (状态机·阶段锁·总控)    │
                    └──────────┬──────────────┘
           ┌─────────┬────────┼────────┬─────────┬──────────┬──────────────┬──────────────────┐
           ▼         ▼        ▼        ▼         ▼          ▼              ▼                  ▼
    director-    director-  director-  director-  director-  director-    character-       seedance-
     story       emotion    camera     light     character   prompt-       image-           video-
    (剧本结构)   (情绪曲线)  (镜头语法)  (光影色彩)  (角色锁定)  packager      prompt           prompt
                                                          (文本编译)   (角色生图提示词)  (L5视频生成)
                                                              │
                                             调用 Storyboard 技能
                                                │    │    │
                                                ▼    ▼    ▼
                                         sketch prompt master ecommerce

                  Storyboard 系列（独立使用）
                  ┌─────────────────────────────┐
                  │ storyboard-sketch            │
                  │ Seedance I2V 分镜草图规划    │
                  ├─────────────────────────────┤
                  │ storyboard-prompt            │
                  │ 单帧分镜提示词 → MJ/Flux/即梦 │
                  ├─────────────────────────────┤
                  │ storyboard-master            │
                  │ 分镜总览图 → 导演提案板       │
                  ├─────────────────────────────┤
                  │ storyboard-ecommerce         │
                  │ 电商带货/直播/服装分镜        │
                  └─────────────────────────────┘
```

## Director 管线 (AI 电影制作流程)

```
STATE 0   INPUT            收集创意、时长、风格、参考图
   │
STATE 1   STORY            剧本结构 + 情绪曲线
   │      (director-story + director-emotion)
   │      输出: Script Blueprint + Emotional Timeline
   ▼
STATE 2   VISUAL           摄影机语言 + 色彩脚本
   │      (director-camera + director-light)
   │      输出: Visual Language Blueprint
   ▼
STATE 3   CHARACTER        角色身份定义
   │      (director-character)
   │      输出: Character Identity Definitions
   │
   ├──→ character-image-prompt  → 编译为生图平台提示词 → 用户去 MJ/Flux/即梦 生成角色参考图
   │
   ▼
STATE 4   STORYBOARD       分镜帧生成（可与角色生图并行）
   │      (storyboard-sketch / storyboard-prompt / storyboard-master / storyboard-ecommerce)
   │      输出: Storyboard Boards + Shot Plan
   ▼
STATE 5   PROMPT PKG       编译为文本级图像生成提示词包
   │      (director-prompt-packager)
   │      输出: Storyboard Prompt Package → 用户拿去 MJ/Flux/即梦 生图
   ▼
STATE 6   SEEDANCE         编译为 Seedance 2.0 视频平台可执行提示词
   │      (seedance-video-prompt)
   │      输入: 已生成的分镜图 + 角色参考图 + 产品图
   │      输出: Seedance 2.0 / Runway / Sora / Kling Video Prompt
   ▼
STATE 7   VALIDATE         质量校验
   ▼
STATE 8   EXPORT           打包交付
```

### 阶段锁 (Phase Locks)

每个阶段必须通过验证才能进入下一阶段，严禁跳步：

| 锁 | 规则 |
|----|------|
| Story Lock | 剧本结构确认后才能进行视觉设计 |
| Visual Lock | 摄影+光影定义后才能生成分镜 |
| Character Lock | 角色身份定义确认后才能生成角色生图提示词 |
| Storyboard Lock | 全部分镜确认后才能生成视频指令 |
| Prompt Lock | 全部预检项通过后才能最终导出 |

## 各技能详情

### director-core
- **职责**: 总管控制器，不生成内容，负责调度和验证
- **触发**: 制作AI电影、完整视频项目、multi-phase 视频创作
- **路由**: 按阶段自动调用其他 Director 技能

### director-story
- **职责**: 剧本→导演级叙事结构
- **能力**: 3/5幕结构、场景目的分析、因果链构建、导演意图层
- **输出**: Script Director Blueprint

### director-emotion
- **职责**: 设计观众情绪旅程
- **能力**: 情绪曲线、情绪节拍、强度评分、情绪→视觉映射表
- **输出**: Emotional Blueprint

### director-camera
- **职责**: 摄影机语言系统设计
- **能力**: 镜头类型语法、运动语法、情绪→摄影机映射、构图规则
- **输出**: Cinematography Blueprint

### director-light
- **职责**: 色彩脚本与光影设计
- **能力**: Color Script、情绪→色彩映射、灯光推进图、场景专属调色板
- **输出**: Color & Lighting Blueprint

### director-character
- **职责**: 角色身份定义与锁定（防崩脸/换衣）
- **能力**: 面部/发型/体型/服装四维锁定、情绪→动作映射、多层锁定系统
- **输出**: Character Identity Definitions（文本级设计文档）
- **注意**: 此技能产出角色身份**定义**，不产出生图提示词。生图提示词由 `character-image-prompt` 编译

### character-image-prompt (NEW)
- **职责**: 角色身份定义 → 生图平台可执行提示词（MJ/Flux/即梦/可灵）
- **能力**: 12段完整角色档案 + 多视角Character Sheet生图提示词 + Negative Prompt
- **输入**: `director-character` 产出的角色身份定义
- **输出**: 可直接粘贴到生图平台的角色设定板提示词

### director-prompt-packager
- **职责**: 文本级编译器——所有前期制作产物 → 结构化分镜图像提示词包
- **能力**: 8段 Prompt 结构、连续性绑定、多 Part 系统
- **输出**: Storyboard Prompt Package（供 MJ/Flux/即梦 生成分镜图）

### seedance-video-prompt
- **职责**: L5 视频生成编译器——分镜图像 + 角色参考图 → Seedance 2.0 可执行提示词
- **能力**: @[ref] 图像引用语法、连续长镜头运动描述、音乐节奏指定、负面约束
- **输入**: 已生成的分镜图像 + 角色参考图 + 产品图
- **输出**: Seedance 2.0 / Runway / Sora / Kling 平台可直接使用的视频生成提示词

---

### storyboard-sketch
- **职责**: Seedance I2V 分镜草图规划（文本描述）
- **双模式**: Compact Frame Prompts + Storyboard Master Sheet
- **输出**: 文字分镜帧描述 + I2V 运动说明

### storyboard-prompt
- **职责**: 单帧分镜图提示词（→ MJ/Flux/即梦/可灵）
- **框架**: 8要素（Scene/Subject/Action/Camera/Composition/Lighting/Mood/Story Purpose）
- **输出**: 可粘贴到图像生成器的分镜帧提示词

### storyboard-master
- **职责**: 分镜总览图/导演提案板（→ 图像生成器）
- **结构**: 4区（Shot Grid + Rhythm + Camera Movement + Visual Language）
- **输出**: 完整导演提案板提示词

### storyboard-ecommerce
- **职责**: 电商带货/直播/服装分镜
- **子模式**: Social Commerce Board + Fashion Director Board
- **输出**: 含产品参考区+人物参考区的电商分镜提示词

## 使用场景路由

| 你想做什么 | 加载哪个技能 |
|-----------|------------|
| "我有一个故事创意，帮我拍成AI电影" | `director-core`（自动调度全部流程） |
| "分析这个剧本的结构" | `director-story` |
| "设计这部电影的情绪曲线" | `director-emotion` |
| "设计镜头语言和摄影机运动" | `director-camera` |
| "设计光影风格和色彩脚本" | `director-light` |
| "创建角色身份定义并锁定" | `director-character` |
| "把角色身份定义编译为生图提示词" | `character-image-prompt` |
| "把这些分镜文本编译为图像提示词包" | `director-prompt-packager` |
| "把分镜图+角色图编译为 Seedance 2.0 视频提示词" | `seedance-video-prompt` |
| "生成分镜草图给Seedance用" | `storyboard-sketch` |
| "写一个分镜画面提示词给MJ" | `storyboard-prompt` |
| "做一张导演提案板分镜总览图" | `storyboard-master` |
| "做TK带货视频分镜/服装导演分镜" | `storyboard-ecommerce` |

## 文件结构

```
.claude/skills/
├── director-core/SKILL.md + references/
├── director-story/SKILL.md + references/
├── director-emotion/SKILL.md + references/
├── director-camera/SKILL.md + references/
├── director-light/SKILL.md + references/
├── director-character/SKILL.md + references/
├── character-image-prompt/SKILL.md
├── director-prompt-packager/SKILL.md + references/
├── seedance-video-prompt/SKILL.md
├── storyboard-sketch/SKILL.md
├── storyboard-prompt/SKILL.md
├── storyboard-master/SKILL.md
└── storyboard-ecommerce/SKILL.md
```

## 关键设计原则

1. **阶段不可跳**: 禁止从创意直接跳到 Seedance 提示词——必须逐阶段验证
2. **角色锁死**: 面部/发型/体型/服装四维参数必须在每一帧中保持一致
3. **情绪驱动**: 摄影机、光影、节奏的选择都必须有情绪理由
4. **动作优先**: AI 视频模型需要物理动作描述，不是情绪标签
5. **连续性绑定**: 多 Part 视频必须引用前一个输出作为连续性基线
6. **三层编译**: director-character(定义) → character-image-prompt(生图) → seedance-video-prompt(视频)
7. **定义与提示分离**: 角色/分镜的"定义文档"和"生图提示词"由不同技能产出

## 知识来源

- `reference/Director/` — AI Film OS 完整架构、核心技能系统、引擎规格、模块化规则
- `reference/Storyboard/` — 分镜提示词规范、总览图设计框架、电商分镜模板
- `reference/seedance-20/` — Seedance 2.0 操作系统技能包（参考）
