# AGENT.md — 项目记忆与操作规范

## 项目概述

AI Film Skill OS — AI 视频/电影制作的 Claude Code 技能体系。
13 个技能，分为 Director 系列（9个）和 Storyboard 系列（4个）。

---

## 技能创建规范

### 命名规范
- 技能名称必须反映其**实际产出**，不能产生误导
- 示例：`director-seedance` 实际产出文本级分镜提示词包，应命名为 `director-prompt-packager`
- 新增技能前，先确认是否已有技能可完成类似职能，避免职能重叠

### Description 规范
- **严禁引用临时开发文档**（如 `prd.md`、`prd2.md`、`prd3.md` 等）
- 这些是开发阶段的参考资源，后续会删除——技能必须自包含
- 如需引用规范，使用通用描述（如"遵循多视角角色设计板规范"而非"参见 prd2.md"）
- Description 应清晰说明：触发条件、输入、输出、与其他技能的边界

### 文件结构
```
.claude/skills/
├── {skill-name}/
│   ├── SKILL.md          # 技能主文件（必须）
│   └── references/        # 参考知识文件（可选）
```

---

## 架构设计原则

### 定义与编译分离
- "定义"技能产出文本级设计文档（如 `director-character` → 角色身份定义）
- "编译"技能将定义文档转化为平台可执行提示词（如 `character-image-prompt` → GPT Image Character Sheet 提示词）
- 不能在一个技能中混合定义和编译

### 两层编译
```
角色/分镜定义（文本级）
  → character-image-prompt（编译为 GPT Image Character Sheet 提示词）
  → director-prompt-packager（编译为分镜板提示词，可选 MJ/Flux/即梦/GPT Image）
  → 用户去生图平台生成图像
  → seedance-video-prompt（编译为 Seedance 2.0 视频提示词，引用已生成的图像）
```

### Character Sheet 定义
- 角色设定参考图 = "用于AI视频一致性控制的多视角电影级角色设计板（Character Sheet）"
- `character-image-prompt` 产出 Character Sheet，不是"艺术身份板（Artistic Identity Board）"，不是单人肖像
- Character Sheet 是 AI 视频跨镜头一致性的参考资产，遵循 12段角色档案模板

### 管线状态机（STATE 0-8）
```
STATE 0 → 输入采集
STATE 1 → 故事与情绪设计
STATE 2 → 视觉设计（摄影机 + 光影）
STATE 3 → 角色锁定 → character-image-prompt
STATE 4 → 分镜规划
STATE 5 → 提示词封装（文本级）→ director-prompt-packager
STATE 6 → Seedance 视频提示词（图像引用级）→ seedance-video-prompt
STATE 7 → 最终验证
STATE 8 → 导出就绪
```

---

## 分支管理规范

### 双分支结构
| 分支 | 语言 | 用途 |
|------|------|------|
| `main` | 英文 | 所有技能文件、文档为英文 |
| `zh-cn` | 中文 | 所有技能文件、文档为中文 |

### 同步流程
1. 在 `main` 完成架构变更后 commit
2. `git checkout zh-cn && git merge main`
3. 解决冲突：zh-cn 保留中文翻译，main 保留架构结构
4. 新文件需翻译为中文后 commit

### 冲突处理策略
- 翻译类差异（仅语言不同）：接受 zh-cn 中文版本
- 架构类差异（结构/逻辑不同）：接受 main 架构变更，再翻译为中文
- 删除类差异（如 `director-seedance` 重命名）：执行删除

---

## Git 操作规范

### Commit Message
- Windows cmd 环境下，包含中文或多行的 commit message 必须使用 `-F` 文件方式：
  ```
  git commit -F _commit_msg.txt
  ```
- 禁止使用 `git commit --amend`
- 禁止使用 `git push --force` 到 main/master

### 常见问题
- **Git index.lock**: 如出现 `fatal: Unable to create index.lock`，手动删除 `.git/index.lock`
- **中文路径**: Git 对中文路径支持良好，无需转义
- **CRLF 警告**: Windows 环境正常现象，可忽略

---

## 文档管理规范

### 目录用途
| 目录 | 用途 | 操作规则 |
|------|------|----------|
| `reference/` | 参考知识库（架构图、工作流案例、技能规范） | **只能提取信息，禁止直接引用路径**。技能文件不得出现 `reference/xxx.md` 或 `参见 xxx.md` |
| `doc/` | 生成产物（分镜板、Seedance提示词等输出文档） | 存放面向用户的最终交付物 |
| 根目录 `.md` | 项目级文档（README.md、AGENT.md） | 项目记忆和入口文档 |
| 根目录 `prd*.md` | 开发阶段临时参考 | 仅开发期存在，后续删除——**严禁技能文件引用** |

### 参考知识使用规范
- `reference/` 下的文档是**知识来源**，为技能设计提供背景和模板
- 技能文件提取其中的**规则和模板**融合到自身逻辑中，而非直接引用
- `reference/CHARACTER/` 下的"艺术身份板"模板与 prd 系列的"Character Sheet"模板是两种不同产物——技能需明确自己产出的类型
- 示例：角色设定板12段模板 → `character-image-prompt` 充分吸收后自包含，不写"参见 prd2.md"

### 输出文档命名
- 格式：`{YYYYMMDD}_{主题}_{产物类型}.md`
- 示例：`20260608_现代都市潮流男装_导演分镜板.md`
- 存放路径：`doc/` 目录下

### 参考文档
- 开发阶段临时文档（prd.md 等）位于根目录，不可被技能文件引用
- 持久化参考知识位于 `reference/` 目录，仅可提取不可引用

### 项目入口
- 根目录 `README.md`：项目介绍和技能体系总览
- 根目录 `AGENT.md`：AI 助手的项目记忆和操作规范

---

## 已知问题与教训

### 问题 1: 技能命名与实际职能不符
- **现象**: `director-seedance` 产出文本级分镜提示词包，但名称暗示是 Seedance 平台提示词
- **修复**: 重命名为 `director-prompt-packager`，新增真正的 `seedance-video-prompt` 技能
- **教训**: 先明确技能边界和产出物类型，再命名

### 问题 2: 缺少角色生图提示词技能
- **现象**: `director-character` 产出角色身份定义，但没有任何技能将定义编译为生图平台可用的提示词
- **修复**: 新增 `character-image-prompt` 技能
- **教训**: 定义文档和可执行提示词之间必须有一个编译层

### 问题 3: `director-core` 未被触发
- **现象**: 用户输入电商视频需求时，`storyboard-ecommerce` 被直接调用，跳过 `director-core` 状态机
- **修复**: 扩展 `director-core` 触发词（电商直播、带货视频、服装视频 等）
- **教训**: 总控技能的触发词需要覆盖所有下游子技能的使用场景

### 问题 4: 技能 Description 引用临时文档
- **现象**: 多个技能 description 引用 `prd2.md` / `prd3.md`，这些是开发参考文档
- **修复**: 替换为通用描述（如"多视角角色设计板规范"）
- **教训**: 技能必须是自包含的，不能依赖可能被删除的临时文档

### 问题 5: 主分支文件语言不一致
- **现象**: `main` 分支上新创建的三个技能文件（character-image-prompt、seedance-video-prompt、director-prompt-packager）误写为中文
- **修复**: 重写为英文版本，然后合并到 zh-cn 再翻译回中文
- **教训**: 在 main 分支工作时应保持英文，zh-cn 分支单独维护中文翻译

### 问题 6: 角色生图产物类型混淆（艺术身份板 vs Character Sheet）
- **现象**: `character-image-prompt` 曾按 `reference/CHARACTER/` 的"艺术性角色身份设定板（Artistic Identity Board）"格式输出——不对称布局、纯白背景、宽松视图选择，与 Seedance 管线（prd2/prd3）定义的"用于AI视频一致性控制的多视角电影级角色设计板（Character Sheet）"不符
- **修复**: 对齐 prd2 12段模板和 prd3 强制视图清单（front/side/3-4/rear/face close-up/hair/hand/expression sheet），使用中性背景 + 专业布局，默认风格为电影级写实而非强制"艺术性"
- **教训**: `reference/` 下可能存在多种不同用途的模板（艺术展示 vs AI训练一致性），技能必须明确引用正确的规范来源，不能混用
