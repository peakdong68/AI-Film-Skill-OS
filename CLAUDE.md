# AGENT.md — 项目记忆与操作规范

**素材使用格式**: 参考素材使用   `@[图片N]`   /  `@[视频N]` /   `@[音频N]`   格式，对齐 Seedance 2.0 官方语法。

## Description 规范
- **严禁引用临时开发文档**（如 `prd.md`、`prd2.md`、`prd3.md` 等）
- 这些是开发阶段的参考资源，后续会删除——技能必须自包含
- 如需引用规范，使用通用描述（如"遵循多视角角色设计板规范"而非"参见 prd2.md"）
- Description 应清晰说明：触发条件、输入、输出、与其他技能的边界

## 文件结构
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
- "编译"技能将定义文档转化为平台可执行提示词（如 `character-image-prompt` → AI 生图平台 Character Sheet 提示词）
- 不能在一个技能中混合定义和编译

### Character Sheet 定义
- 角色设定参考图 = "用于AI视频一致性控制的多视角电影级角色设计板（Character Sheet）"
- `character-image-prompt` 产出 Character Sheet，不是"艺术身份板（Artistic Identity Board）"，不是单人肖像
- Character Sheet 是 AI 视频跨镜头一致性的参考资产，遵循 12段角色档案模板

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
