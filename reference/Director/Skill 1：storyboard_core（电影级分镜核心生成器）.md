 
# 🎬 Skill 1：storyboard_core（电影级分镜核心生成器）

---

## name

storyboard_core

---

## description

根据用户输入的故事创意、剧本片段、视觉概念或情绪描述，自动生成电影级分镜结构（Storyboard）。输出内容包含镜头拆分、镜头语言、节奏设计、情绪推进与AI可执行的画面提示词。适用于短片、广告、MV、AI视频生成（Seedance / Runway / Sora / Kling）。

---

## purpose（核心用途）

* 将“抽象故事”转换为“可拍摄分镜结构”
* 将剧本拆成可执行镜头序列
* 为AI视频生成提供结构化视觉脚本
* 统一角色、场景、情绪与镜头语言

---

## input（输入类型）

支持以下输入：

* 故事概念（story idea）
* 剧本片段（script）
* 情绪描述（mood board text）
* 场景设定（location + action）
* AI视频创意（prompt-like input）
* 图片参考（reference frame）

---

## output（输出结构）

输出必须包含以下模块：

### 1. Cinematic Direction Analysis（电影导演分析）

* 影片类型（genre）
* 情绪基调（tone）
* 视觉世界（visual world）
* 摄影语言（camera language）
* 光影风格（lighting）
* 节奏结构（pacing）
* 声音设计（sound design）
* 推荐电影语言类型（cinematic reference category）

---

### 2. Storyboard Structure（分镜结构）

自动拆分为：

* Scene / Board 01, 02, 03...
* 每个Board = 5–15秒
* 每个Board = 8–12个镜头单元（panels）

---

### 3. Panel System（镜头系统）

每个panel必须包含：

* shot type（wide / medium / close-up / POV / overhead）
* camera movement（static / dolly / handheld / orbit / tracking）
* subject action（角色行为）
* emotion state（情绪状态）
* eye direction（眼神逻辑）
* lighting cue（光影变化）
* sound cue（环境/音乐/音效）

---

### 4. AI Prompt Layer（AI可执行提示词）

每个镜头必须生成：

#### Image Prompt

结构：

* 主体描述
* 场景
* 动作
* 镜头
* 光影
* 情绪
* 色彩
* 风格（cinematic realistic）
* negative prompt（无文字/无水印/无崩脸）

#### Image-to-Video Prompt

结构：

* 时间长度（2–5s）
* 摄影机运动
* 角色动作变化
* 环境变化（风/雨/光）
* 情绪推进
* 禁止项（no distortion / no text / no identity change）

---

## rules（核心规则）

### 1. 镜头逻辑规则

* 每个镜头必须有“情绪目的”
* 不能出现无意义过场镜头
* 镜头之间必须有“视觉连续性”

---

### 2. 节奏规则

* 15秒 = 5–10镜头
* 30秒 = 6–12镜头
* 1分钟 = 10–20镜头
* 节奏必须遵循：建立 → 冲突 → 情绪 → 收束

---

### 3. 摄影语言规则

必须使用明确摄影术语：

* wide shot（建立世界）
* close-up（情绪爆发）
* dolly-in（心理压迫）
* handheld（现实感/混乱）
* orbit shot（关系/浪漫/超现实）

---

### 4. 情绪驱动规则

所有分镜必须绑定情绪变化：

* calm → tension → reveal → release
* love → hesitation → conflict → acceptance
* fear → discovery → panic → silence

---

### 5. 连贯性规则

* 角色必须保持一致（脸/服装/年龄）
* 场景必须逻辑一致
* 光影必须符合时间变化
* 不允许随机跳场景

---

## constraints（限制）

* 不生成无结构描述
* 不输出纯文学文本
* 不允许没有镜头语言的描述
* 不允许跳过分析直接生成分镜
* 不允许角色不一致

---

## advanced capabilities（高级能力）

### A. Multi-Part Storyboard System

支持：

* Part 1 / Part 2 / Part 3 连续叙事
* 自动延续上一段镜头语言
* 保持视觉连续性

---

### B. Cinematic Style Mapping

可自动匹配风格：

* luxury commercial cinema
* documentary realism
* neo-noir thriller
* surreal fantasy
* emotional poetic realism
* action handheld cinema

---

### C. AI Production Readiness

输出可直接用于：

* Seedance 2.0
* Runway Gen-3
* Sora
* Kling AI
* Pika Labs

---

## typical use cases

* AI短片制作
* 广告分镜设计
* MV视觉规划
* 概念电影预演
* 游戏过场动画设计
* 视觉叙事设计

---

## example behavior

用户输入：
“一个男人在雨夜等待失踪的恋人”

输出：

* 6–10个分镜板
* 每个板包含镜头拆分
* 雨夜灯光设计
* 情绪从期待 → 不安 → 崩溃
* 最终生成AI可用prompt

---

## summary

storyboard_core 是一个：

> 将“文字故事”转化为“电影级可执行视觉分镜系统”的核心引擎

---
 