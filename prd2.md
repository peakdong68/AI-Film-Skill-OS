
# Seedance 2.0 角色设定参考图资源文件规则（整理版）

## 一、生成时机（严格阶段锁）

角色参考图不能直接生成，必须满足流程：

1. Storyboard（分镜板）全部完成
2. 用户确认全部 Storyboard
3. Character Prompt（角色设定提示词）完成
4. 用户确认角色提示词
5. 自动进入 Character Reference Images 阶段
6. 用户确认角色参考图
7. 才允许进入 Seedance Prompt 阶段

禁止行为：

* 不允许跳过 Storyboard
* 不允许跳过角色 Prompt
* 不允许直接生成 Seedance Prompt
* 不允许默认用户已确认

---

## 二、角色参考图输出类型

默认必须输出：

Professional Character Sheet Image Prompt

不是：

* 单人肖像图
* 简短角色描述
* 普通头像 Prompt

除非用户明确要求 Portrait。

---

## 三、角色参考图资源内容结构

每个角色参考图必须包含：

### 1. Character Identity Summary

字段：

* Character label/name
* Role in story
* Age
* Emotional function
* Visual signature
* Continuity importance

---

### 2. Full Character Sheet Image Prompt

必须包含：

基础身份：

* Character name
* Age range
* Face shape
* Skin tone
* Hairstyle
* Body type

服装：

* Wardrobe
* Accessories
* Props

动作表现：

* Expression range
* Posture

多视图要求：

* Front view
* Side view
* 3/4 view
* Rear view
* Rear silhouette

细节图：

* Face close-up
* Hair detail
* Hand detail（如果重要）

人物图：

* Full body pose

表情变化：

* Emotion variations

风格：

* Visual style
* Lighting style

版式：

* Clean professional character sheet layout
* Neutral/simple background

一致性：

* Consistency notes

负面限制：

* Negative instructions

---

## 四、连续性锁（Consistency Lock）

以下元素必须在后续全部保持一致：

脸：

* 脸型
* 五官
* 年龄感
* 肤色

头发：

* 长度
* 发型
* 发色

身体：

* 身材比例
* 身高感
* 肢体特征

服装：

* 主服装
* 配件
* 鞋子

情绪：

* 性格气质
* 情绪基调

道具：

* 固定物品
* 武器
* 饰品

环境相关：

* 若有环境绑定需保持

---

## 五、负面规则（Negative Prompt）

必须加入：

* no face change
* no hairstyle change
* no wardrobe change
* no extra accessories
* no random age shift
* no body proportion change
* no extra characters
* no cartoon unless requested
* no anime unless requested
* no over-stylization
* no watermark
* no logo
* no text-heavy poster layout

---

## 六、角色参考图生成阶段规则

生成时：

保持完全一致：

* identity
* wardrobe
* hairstyle
* body type
* props
* mood
* style

禁止：

* Face morphing
* Random costume change
* Background crowd generation
* Identity drift
* Poster layout
* Text overlays

---

## 七、角色参考图确认后流程

输出：

Please confirm the character reference images.
After your confirmation, I can create the Seedance 2.0 prompts.

这份内容是根据已加载知识文件合并整理出来的，不是原文件逐字复制。对应来源主要来自角色表规则和主工作流：  


你要的是“完整角色设定模板（可直接用于 Seedance）”，属于可复用文档模板，我会输出成可直接复制到知识库/角色资产库/角色参考图工作流里的格式。
这里我补上了 Seedance 连续性字段（Identity Lock、Reference Mapping、Reference Priority、Scene Continuity 等），
让它不只是角色描述，而是能直接进入角色参考图 → Storyboard → Seedance 的完整链路。

# SEEDANCE 2.0 — COMPLETE CHARACTER PROFILE TEMPLATE

Version: Character Reference Master Template

==================================================
[0] CHARACTER REFERENCE ID
==========================

Character ID:
Character Name:
Alias/Nickname:

Story Role:
(Main Character / Supporting / Villain / Narrator / Background)

Priority:
(Primary / Secondary / Minor)

Continuity Importance:
(High / Medium / Low)

Reference Tag:
@[Character_Name]

==================================================
[1] CORE IDENTITY
=================

Age:

Age Range:

Gender:

Species:

Nationality:

Occupation:

Personality Type:

Emotional Function:

Backstory Summary:

Core Motivation:

Fear:

Goal:

Internal Conflict:

External Conflict:

Visual Signature:

Keywords:

Example:

Visual Signature:
silver earrings + short black hair + long coat

Keywords:
lonely, quiet, mysterious

==================================================
[2] FACE IDENTITY LOCK
======================

Face Shape:

Jawline:

Cheek Structure:

Forehead:

Skin Tone:

Skin Texture:

Eye Shape:

Eye Color:

Eyebrows:

Nose Shape:

Lips:

Teeth:

Ears:

Special Face Features:

Freckles:

Scars:

Moles:

Wrinkles:

Beauty Marks:

Makeup Style:

Expression Default:

Eye Direction Habit:

Example:

Face Shape:
soft oval

Eye Shape:
slightly narrow almond eyes

Expression Default:
emotionally restrained

Eye Direction Habit:
looks away before making eye contact

==================================================
[3] HAIR LOCK
=============

Hair Length:

Hair Style:

Hair Color:

Hair Texture:

Hair Parting:

Hair Movement:

Special Hair Features:

Example:

Hair Length:
shoulder length

Hair Style:
slightly messy layered cut

Hair Color:
dark brown

Hair Texture:
soft natural wave

==================================================
[4] BODY LOCK
=============

Height:

Weight:

Body Type:

Body Proportion:

Shoulders:

Arms:

Hands:

Legs:

Movement Style:

Posture:

Walking Style:

Signature Gesture:

Example:

Movement Style:
slow controlled movement

Walking Style:
slightly cautious steps

Signature Gesture:
touches necklace while thinking

==================================================
[5] WARDROBE LOCK
=================

Main Outfit:

Upper Clothing:

Lower Clothing:

Outer Layer:

Shoes:

Accessories:

Jewelry:

Watch:

Gloves:

Bags:

Color Palette:

Fabric Type:

Weather Variant:

Alternative Outfit:

Forbidden Clothing:

Example:

Main Outfit:
long black trench coat

Shoes:
dark leather boots

Color Palette:
black + gray + silver

Forbidden Clothing:
bright colors

==================================================
[6] PROP LOCK
=============

Primary Prop:

Secondary Prop:

Signature Item:

Weapon:

Technology Device:

Vehicle:

Interaction Style:

Example:

Primary Prop:
old camera

Signature Item:
silver lighter

Interaction Style:
always holds camera close to chest

==================================================
[7] EXPRESSION SYSTEM
=====================

Neutral:

Happy:

Sad:

Angry:

Fear:

Surprised:

Thinking:

Confused:

Confident:

Romantic:

Embarrassed:

Crying:

Laughing:

Extreme Emotion:

==================================================
[8] CHARACTER SHEET VIEW REQUIREMENTS
=====================================

Required Views:

✓ Front View

✓ Side View

✓ 3/4 View

✓ Rear View

✓ Rear Silhouette

✓ Face Close-up

✓ Hair Detail

✓ Hand Detail

✓ Accessory Detail

✓ Full Body

✓ Walking Pose

✓ Action Pose

✓ Relaxed Pose

✓ Expression Sheet

==================================================
[9] VISUAL STYLE SETTINGS
=========================

Visual Style:

Realism Level:

Lighting Style:

Color Mood:

Lens Feel:

Texture Style:

Background:

Layout Style:

Example:

Visual Style:
cinematic realism

Lighting Style:
soft studio lighting with subtle rim light

Lens Feel:
50mm portrait

Texture Style:
high skin detail

==================================================
[10] SEEDANCE REFERENCE SETTINGS
================================

Identity Lock:

ON

Face Lock:

ON

Hair Lock:

ON

Body Lock:

ON

Wardrobe Lock:

ON

Prop Lock:

ON

Style Lock:

ON

Continuity Lock:

ON

Reference Priority:

1. Character Identity
2. Face
3. Hair
4. Outfit
5. Props
6. Mood
7. Style

Reference Use:

Character reference only controls:

* identity
* face
* hair
* body
* wardrobe

Character reference does NOT control:

* camera
* action
* scene composition

==================================================
[11] CHARACTER SHEET IMAGE PROMPT
=================================

Professional cinematic character sheet of
[Character Name],

age [X],

[face description],

[skin description],

[hair description],

[body description],

wearing [wardrobe],

holding [props],

show front view,
side view,
3/4 view,
rear view,
full body pose,
walking pose,
expression sheet,
face close-up,
hair detail,
hand detail,
accessory detail,

professional character design sheet,
neutral background,
cinematic realism,
high detail skin texture,
clean presentation layout,
consistent identity

==================================================
[12] NEGATIVE PROMPT
====================

no face change

no hairstyle change

no body proportion change

no random age shift

no wardrobe change

no extra accessories

no extra characters

no duplicate characters

no distorted face

no bad anatomy

no extra fingers

no identity drift

no inconsistent skin tone

no random props

no cartoon style unless requested

no anime unless requested

no watermark

no logo

no text

no poster layout

==================================================
END
===

这版已经是“Seedance 可直接用角色主档（Master Character Asset）”，后续只要填角色信息，就能直接衔接：角色参考图 → Storyboard → Part1 → Part2+ 连续视频。
