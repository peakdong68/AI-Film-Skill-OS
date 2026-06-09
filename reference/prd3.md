下面是**“角色设定参考图（Character Sheet Image Prompt）资源文件规则”**的完整结构整理（基于你上传的知识文件内容提炼），并按“可直接用于制作/生成角色图”的方式输出。

🎭 角色设定参考图资源文件规则（Character Sheet Image Prompt Rules）
一、核心原则（必须遵守）
必须生成“角色设定表（Character Sheet）”，而不是单张人物图
❌ 不允许：单一头像 / 单一半身像描述
✅ 必须：多视角、多状态、完整设定板
必须包含4大模块
角色身份摘要（Identity Summary）
完整角色设定图Prompt（Full Character Sheet Prompt）
一致性规则（Consistency Notes）
负面约束（Negative Prompt）
用途优先级
用于：Storyboard / Seedance 2.0 / AI视频角色锁定
核心目标：保证“跨镜头角色一致性”
二、标准资源文件结构（必须按此输出）
📁 CHARACTER SHEET IMAGE PROMPT STRUCTURE
1️⃣ Character Identity Summary（角色身份摘要）1️⃣ 角色身份摘要

必须包含：

Character Name / Label（角色名或代号）
Role in Story（故事角色）
Age / Age Range（年龄）年龄 / 年龄范围
Emotional Function（情绪功能）情绪功能
Visual Signature（视觉识别点）
Continuity Importance（镜头一致性关键点）

👉 示例结构：

Character Name: Aiden / Guard-01
Role: Night shift security guard in luxury mall
Age: 28–35
Emotional Function: Calm observer slowly losing trust in reality
Visual Signature: Dark uniform, tired eyes, subtle facial fatigue
Continuity Importance: Must remain identical across all storyboard boards
2️⃣ Full Character Sheet Image Prompt（完整角色设定图提示词）

必须生成“多视角角色板”，包含：

📌 必须结构内容：
A. 基础信息
年龄
脸型
肤色
身体类型
气质关键词
B. 外观细节
发型（必须稳定）
眼睛特征
面部细节（痣/皱纹/疲惫感等）
C. 服装系统（必须固定）
主服装
配色方案
材质（布料/皮革/制服等）
D. 动作与姿态
站姿
行走姿态
情绪姿态（紧张/冷静/疲惫）
📌 必须包含的视角（强制）

角色设定图必须包含：

Front view（正面）正面视角
Side view（侧面）侧面视图
3/4 view（三分之四角度）
Back view / silhouette（背面或轮廓）
Close-up face detail（面部特写）脸部细节特写（脸部亮点）
Full body pose（全身动态姿势）
Expression range（表情变化：3–5种）
📌 光影与风格要求

必须写清：

Lighting（光线类型）
cinematic soft light / studio neutral light / dramatic rim light电影级柔光 / 影棚中性光 / 戏剧性轮廓光
Style风格
cinematic realistic（默认）电影级写实（默认）
或用户指定风格
Background背景
必须干净（neutral / studio background）
不允许复杂场景干扰角色识别
📌 Prompt结构模板（标准格式）
A professional cinematic character sheet showing [CHARACTER NAME],
featuring front view, side view, 3/4 view, back view, close-up face detail,
full body pose and expression variations.

The character is a [age] year old [role description],
with [face shape], [skin tone], [hair style], [body type].

Wardrobe: [fixed clothing description, color, material].
Expression range: calm, tense, fearful, focused, emotional.

Lighting: neutral studio lighting with subtle cinematic contrast.
Style: cinematic realistic, ultra-detailed, film character design sheet.
Background: clean neutral grey or soft gradient studio backdrop.

Must maintain strict identity consistency across all views.
No change in face, hair, wardrobe, or body proportions.
No text, no watermark, no logo.
3️⃣ Consistency Notes（一致性规则）

必须明确写：

面部必须固定（no face drift）
发型必须固定（no hairstyle change）
服装必须固定（no wardrobe variation）
身材比例必须固定
情绪基调必须一致
不能出现“随机新配件”

👉 示例：

Consistency Rules:
- Face must remain identical across all scenes
- Hair style must not change under any condition
- Uniform must remain unchanged across storyboard sequences
- Body proportions must remain consistent
- No additional accessories allowed unless specified in story
4️⃣ Negative Prompt（负面约束）4️⃣ 负面约束

必须包含以下限制：

no face change无面部变化
no hairstyle change无发型改变
no wardrobe change无服装更换
no extra accessories无额外配件
no age shift无年龄变化
no body distortion无身体扭曲
no cartoon/anime style unless requested除非要求，否则不使用卡通/动漫风格
no watermark无水印
no text无文字
no logo无标志
no extra characters无额外角色
no style drift无风格漂移
三、关键规则总结（最重要）
🚨 强制规则
❗必须是“角色设定板”，不是单图
❗必须包含 4–8个视角
❗必须用于“跨镜头一致性”
❗必须提供完整负面约束
❗必须保证可用于 AI视频生成（Seedance / Kling / Sora）
四、一句话标准定义

👉 角色设定参考图 =
“用于AI视频一致性控制的多视角电影级角色设计板（Character Sheet）”