

---

# 🎬 Skill 3：seedance_prompt_engine（AI视频生成Prompt引擎）

---

## name

seedance_prompt_engine

---

## description

将分镜结构（Storyboard）与角色一致性系统（Character Consistency）融合，生成可直接用于AI视频生成工具（Seedance 2.0  / Kling）的高质量视频Prompt系统。该技能负责把“镜头”转化为“可执行动态影像指令”。

---

## purpose（核心用途）

* 将分镜转换为AI可执行视频指令
* 控制镜头运动、时间节奏与情绪推进
* 保持角色一致性与场景连续性
* 支持多Part长视频生成（Part 1 → Part 2 → Part 3）
* 输出生产级 video prompt（非描述性文本）

---

## input（输入类型）

支持以下输入：

* storyboard_core 输出（分镜结构）
* character_consistency_engine 输出（角色设定）
* 场景概念（scene idea）
* 参考风格（cinematic style / commercial / noir / sci-fi）
* 时长要求（duration per clip / total runtime）

---

## output（输出结构）

输出必须是 **Seedance Video Prompt Pack（视频生成提示包）**

包含三层结构：

---

# 1. Global Video Direction（全局视频导演指令）

用于整个视频统一风格：

* genre（类型）
* tone（情绪）
* visual style（视觉风格）
* camera language（摄影语言）
* lighting system（光影系统）
* color grading（调色风格）
* pacing rhythm（节奏）
* sound direction（声音方向）

---

# 2. Scene-to-Video Breakdown（分镜转视频结构）

每个 storyboard board → 转换为 video clip：

---

## 格式：

### Scene X - Video Prompt

#### Duration

* 2s–15s（根据分镜自动分配）

---

#### Video Prompt（核心生成指令）

必须包含：

* subject description（主体）
* action motion（动作变化）
* camera movement（镜头运动）
* emotional state progression（情绪变化）
* environment dynamics（环境变化）
* lighting behavior（光影变化）
* continuity lock（角色一致性锁定）

---

#### Example structure（标准结构）

> Create a cinematic 6-second video.
> A young woman stands in a rainy street under neon lights.
> She slowly turns her head toward camera with a hesitant emotional expression.
> Camera performs a slow dolly-in from medium shot to close-up.
> Rain falls continuously, reflections shimmer on wet ground.
> Lighting is cold blue with pink neon highlights.
> Maintain exact facial identity and wardrobe consistency.
> No text, no watermark, no distortion.

---

# 3. Camera Motion Engine（镜头运动系统）

必须明确使用以下摄影语言：

### Static / Controlled

* locked-off frame（静态压迫感）
* symmetrical framing（秩序感）

---

### Movement-Based

* slow dolly-in（情绪推进）
* dolly-out（情绪抽离）
* tracking shot（跟随动作）
* handheld（现实感/紧张）
* orbit shot（关系/浪漫/超现实）
* crane shot（空间揭示）

---

### Dynamic Effects

* whip pan transition（快速切换）
* rack focus（焦点转移）
* push-pull zoom（心理波动）

---

# 4. Temporal Flow System（时间流系统）

每个视频片段必须控制时间逻辑：

* 0–2s → Hook（吸引注意）
* 2–6s → Development（动作展开）
* 6–10s → Emotional shift（情绪变化）
* 10–15s → Resolution / Transition（收束或转场）

---

# 5. Character Continuity Lock（角色一致性锁定）

必须嵌入：

* face_identity_lock
* wardrobe_lock
* hairstyle_lock
* age_lock

禁止：

* 换脸
* 风格漂移
* 服装变化
* 身份重建

---

# 6. Environment Continuity System（环境一致性）

锁定：

* location consistency（地点不跳变）
* lighting continuity（光线逻辑一致）
* weather system（天气连贯）
* spatial logic（空间合理性）

---

# 7. Negative Prompt System（强制排除）

每个视频必须包含：

* no text
* no subtitles
* no watermark
* no logo
* no face distortion
* no identity shift
* no outfit change
* no extra characters
* no flickering faces
* no unnatural motion
* no CGI artifacting (unless specified)

---

# 8. Multi-Part Continuity System（多Part连续系统）

支持：

### Part 1

* 建立世界 + 角色 + 风格

### Part 2+

* 必须引用：

  * previous_video_reference
  * current_storyboard_reference
* 保持连续镜头语言
* 不允许重启叙事

---

# 9. AI Tool Compatibility Layer（AI工具兼容层）

优化输出适配：

* Seedance 2.0 (primary)
* Kling AI

---

# 10. Advanced Capabilities（高级能力）

### A. Emotion-driven Camera System

情绪驱动镜头变化：

* fear → handheld + tight framing
* romance → slow orbit + soft focus
* tension → static + slow push-in

---

### B. Micro-Movement Control

控制：

* eye movement
* breath timing
* hand gestures
* subtle facial changes

---

### C. Cinematic Transition Linking

自动生成：

* match cut
* sound bridge
* object transition
* light transition

---

# 11. Use Cases

* AI电影生成（Seedance / Sora）
* 广告视频生成
* MV制作
* 短剧生成
* 游戏过场动画
* 概念预览影片（previs）

---

# summary

seedance_prompt_engine 是一个：

> 将“分镜结构 + 角色系统”转换为“可直接驱动AI视频生成器的电影级动态影像指令系统”。

---
 