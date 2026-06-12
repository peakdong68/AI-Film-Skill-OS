# AI Film Skill OS — 技能体系文档

## 概览

本项目为 AI 视频/电影制作提供 15 个 Claude Code 技能，分为三大体系：

- **Director 系列 (10个)**：完整的 AI 电影制作管线，从创意到可执行视频提示词
- **Storyboard 系列 (4个)**：生成分镜图提示词，面向 AI 图像生成器和 Seedance I2V

## 技能地图

```
                    ┌─────────────────────────┐
                    │     director-core         │
                    │   (状态机·阶段锁·总控)    │
                    └──────────┬──────────────┘
           ┌─────────┬────────┼────────┬─────────┬──────────┬──────────────┬──────────────────┐
           ▼         ▼        ▼        ▼         ▼          ▼              ▼                  ▼
    director-    director-  director-  director-  director-  director-    character-       seedance-
     story       emotion    style      camera     light     character      image-           video-
    (剧本结构)   (情绪曲线)  (导演人格)  (镜头语法)  (光影色彩)  (角色锁定)   prompt           prompt
                                                                         (角色生图提示词)  (L5视频生成)
                                         │
                                    director-
                                    prompt-packager
                                    (提示包编译·STATE 4)

                  Storyboard 系列（独立使用 / STATE 5 条件性调用）
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
STATE 2   VISUAL           导演人格 + 摄影机语言 + 色彩脚本
   │      (director-style + director-camera + director-light)
   │      输出: Visual Language Blueprint
   ▼
STATE 3   CHARACTER        角色身份定义
   │      (director-character)
   │      输出: Character Identity Definitions
   │
   ├──→ character-image-prompt → 编译为生图平台提示词 → 用户去 MJ/Flux/即梦 生成角色参考图
   │
   ▼
STATE 4   PROMPT PKG       编译为电影级短片提示包（分镜设计+镜头语言+声音设计+Part分解方案）
   │      (director-prompt-packager)
   │      输出: Film-Level Prompt Package → 用户确认
   │
   ▼
[路由决策]                 盘点已有资源 → 匹配 STATE 6 模式 → 选择方案
   │                       ┌─────────────────┬──────────────────┐
   ▼                       ▼                 ▼                  ▼
方案A: 分镜蓝图           方案B: 直接生视频   方案C: 混合
   │                       │                 │
STATE 5 (条件性)           跳过 STATE 5       STATE 5（关键镜头）
   │                       │                 │
   │      storyboard-*      │                 │
   │      输出: 分镜蓝图图像  │                 │
   │                       │                 │
   └───────────┬───────────┘─────────────────┘
               ▼
STATE 6   SEEDANCE        编译为 Seedance 2.0 视频平台可执行提示词（7 模式）
   │      (seedance-video-prompt)
   │      输入: 按所选模式（分镜图 / 单张参考 / 首尾帧 / 视频片段 / 纯文本）
   │      输出: Seedance 2.0 / Kling Video Prompt
   ▼
STATE 7   VALIDATE         逐 Part 审核 + 全局质量校验
   ▼
STATE 8   EXPORT           专业交付包（含帧对齐/音频淡出/授权备注）
```

### 阶段锁 (Phase Locks)

每个阶段必须通过验证才能进入下一阶段。STATE 0-4 为必选，严禁跳过。

| 锁 | 规则 |
|----|------|
| Story Lock | 剧本结构确认后才能进行视觉设计 |
| Visual Lock | 摄影+光影定义后才能编译提示包 |
| Character Lock | 角色身份定义确认后才能编译提示包 |
| Package Lock | 提示包确认后才能进入后续阶段 |
| Storyboard Lock | 如经 STATE 5，分镜蓝图确认后才能生成视频指令 |
| Mode Lock | STATE 6 必须按可用资源选择模式，不可默认分镜驱动 |
| Prompt Lock | 全部预检项通过后才能最终导出 |

## 各技能详情

### director-core
- **职责**: 总管控制器，不生成内容，负责调度、验证和检查点持久化
- **触发**: 制作AI电影、完整视频项目、multi-phase 视频创作
- **路由**: 按阶段自动调用其他 Director 技能，支持会话恢复（`STATE.md`）
- **关键特性**: STATE 5 条件性执行、STATE 6 七模式支持、路由决策机制

### director-interview
- **职责**: 创意入站访谈——模糊创意/描述充分但缺剧情的输入 → 可执行制作简报
- **三路径**: 快速通道（创意完整）/ 创意展开（2-3方案供选择）/ 创意访谈（逐项问清）
- **输出**: 统一制作简报（含创意方向、类型路径、时长、风格、平台、参考素材）
- **调用者**: `director-core` STATE 0、`director-story` 独立使用

### director-story
- **职责**: 剧本→导演级叙事结构
- **能力**: 3/5幕结构、场景目的分析、因果链构建、导演意图层
- **输出**: Script Director Blueprint

### director-emotion
- **职责**: 设计观众情绪旅程
- **能力**: 情绪曲线、情绪节拍、强度评分、情绪→视觉映射表
- **输出**: Emotional Blueprint

### director-style
- **职责**: 定义导演视觉人格与哲学立场
- **能力**: 五种导演人格（Observer/Emotional/Immersive/Epic/Commercial）、摄影哲学、节奏策略
- **输出**: Director Style Profile

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
- **注意**: 产出角色身份**定义**，不产出生图提示词。生图提示词由 `character-image-prompt` 编译

### character-image-prompt
- **职责**: 角色身份定义 → 生图平台可执行提示词（MJ/Flux/即梦/可灵）
- **能力**: 12段完整角色档案 + 多视角角色设计板生图提示词 + Negative Prompt
- **输入**: `director-character` 产出的角色身份定义
- **输出**: 可直接粘贴到生图平台的角色设计板提示词

### director-prompt-packager
- **职责**: 文本级编译器——STATE 1-3 所有设计产物 → 完整的电影级短片提示包
- **能力**: 结构化分镜设计 + 镜头语言规范 + 声音设计方向 + Part 分解方案（每 Part ≤ 15s）
- **输出**: Film-Level Prompt Package（导演愿景总文档，用户确认后进入路由决策）
- **注意**: 平台无关的导演级设计文档，**不是** Seedance 视频提示词

### seedance-video-prompt
- **职责**: L5 视频生成编译器——多模态参考 → Seedance 2.0 可执行提示词
- **能力**: 7 种生成模式（T2V / I2V minimal / I2V storyboard / R2V / FLF2V / V2V Edit / V2V Extend），官方 `` `图片N` `` 参考格式，动作描述四规则，特殊字符规范
- **输入**: 按所选模式（分镜图仅在 storyboard 模式需要；支持单张参考/首尾帧/视频片段/纯文本）
- **输出**: Seedance 2.0 / Kling 平台可直接使用的视频生成提示词（每条 ≤ 500 中文字）
- **关键认知**: 分镜图像不是必须的

---

### storyboard-sketch
- **职责**: Seedance I2V 分镜草图规划（文本描述）
- **输出**: 文字分镜帧描述 + I2V 运动说明
- **注意**: 如需分镜总览图，请使用 `storyboard-master`

### storyboard-prompt
- **职责**: 单帧分镜图提示词（→ MJ/Flux/即梦/可灵）
- **框架**: 8要素（Scene/Subject/Action/Camera/Composition/Lighting/Mood/Story Purpose）
- **输出**: 可粘贴到图像生成器的分镜帧提示词

### storyboard-master
- **职责**: 分镜总览图/导演提案板（→ 图像生成器）
- **结构**: 4区（分镜展示区 + 节奏设计区 + 运镜设计区 + 视觉设计区）
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
| "模糊创意需要先展开再分析" | `director-interview` |
| "设计这部电影的情绪曲线" | `director-emotion` |
| "选择导演风格/视觉人格" | `director-style` |
| "设计镜头语言和摄影机运动" | `director-camera` |
| "设计光影风格和色彩脚本" | `director-light` |
| "创建角色身份定义并锁定" | `director-character` |
| "把角色身份定义编译为生图提示词" | `character-image-prompt` |
| "把故事+视觉+角色编译为电影短片提示包" | `director-prompt-packager` |
| "有提示包+参考图，直接生成视频（无需分镜图）" | `director-core` → 路由决策 → 方案 B → `seedance-video-prompt` |
| "有单张参考图/首尾帧，需要生成视频" | `seedance-video-prompt`（I2V minimal / FLF2V） |
| "把分镜图+角色图编译为 Seedance 2.0 视频提示词" | `seedance-video-prompt`（I2V storyboard） |
| "生成分镜蓝图图给 Seedance 用" | `storyboard-sketch` |
| "写一个分镜画面提示词给 MJ" | `storyboard-prompt` |
| "做一张导演提案板分镜总览图" | `storyboard-master` |
| "做 TK 带货视频分镜/服装导演分镜" | `storyboard-ecommerce` |

## 文件结构

```
.claude/skills/
├── director-core/SKILL.md + references/
├── director-interview/SKILL.md
├── director-story/SKILL.md + references/
├── director-emotion/SKILL.md + references/
├── director-style/SKILL.md
├── director-camera/SKILL.md + references/
├── director-light/SKILL.md + references/
├── director-character/SKILL.md + references/
├── character-image-prompt/SKILL.md
├── director-prompt-packager/SKILL.md + references/
├── seedance-video-prompt/SKILL.md + references/
├── storyboard-sketch/SKILL.md + references/
├── storyboard-prompt/SKILL.md
├── storyboard-master/SKILL.md
├── storyboard-ecommerce/SKILL.md
└── references/
    ├── anti-slop-lexicon.md
    ├── cinematography-quick-reference.md
    ├── seedance-genre-recipes.md
    └── seedance-platform.md
```

## 关键设计原则

1. **阶段不可跳**: STATE 0-4 为必选阶段，严禁跳过。STATE 5 为条件性阶段。
2. **路由决策**: STATE 4 确认后根据已有资源选择方案（A: 分镜蓝图 / B: 直接生视频 / C: 混合），不盲目进入 STATE 5。
3. **分镜非必须**: STATE 6 支持 7 种模式，分镜图像仅在 I2V storyboard 模式下需要。
4. **角色锁死**: 面部/发型/体型/服装四维参数必须在每一帧中保持一致。
5. **情绪驱动**: 摄影机、光影、节奏的选择都必须有情绪理由。
6. **动作优先**: AI 视频模型需要物理动作描述（肢体细化+程度量化+过渡衔接+情绪外化），不是抽象情绪标签。
7. **连续性绑定**: 多 Part 视频必须引用前一个输出作为连续性基线，每个 Part 独立计数（≤ 500 中文字）。
8. **定义与提示分离**: 角色/分镜的"定义文档"和"生图提示词"由不同技能产出。
9. **素材使用格式**: 参考素材使用   `@[图片N]`   /  `@[视频N]` /   `@[音频N]`   格式，对齐 Seedance 2.0 官方语法。
10. **检查点持久化**: 制作进度通过 `STATE.md` 文件持久化，支持会话中断后恢复。
 