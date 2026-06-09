# AGENT.md — Project Memory & Operational Conventions

## Project Overview

AI Film Skill OS — Claude Code skill system for AI video/film production.
13 skills, organized into Director Series (9) and Storyboard Series (4).

---

## Skill Creation Conventions

### Naming Conventions
- Skill names must reflect their **actual output**; must not be misleading
- Example: `director-seedance` actually produced text-level storyboard prompt packages — was renamed to `director-prompt-packager`
- Before creating a new skill, verify whether an existing skill already covers similar functionality to avoid overlap

### Description Conventions
- **Strictly forbid referencing temporary development documents** (e.g., `prd.md`, `prd2.md`, `prd3.md`, etc.)
- These are development-phase reference resources that will be deleted — skills must be self-contained
- When referencing specifications, use generic descriptions (e.g., "follows multi-view character design board specification" rather than "see prd2.md")
- Description should clearly state: trigger conditions, inputs, outputs, and boundaries with other skills

### File Structure
```
.claude/skills/
├── {skill-name}/
│   ├── SKILL.md          # Skill main file (required)
│   └── references/        # Reference knowledge files (optional)
```

---

## Architecture Design Principles

### Definition/Compilation Separation
- "Definition" skills produce text-level design documents (e.g., `director-character` → character identity definitions)
- "Compilation" skills convert definition documents into platform-executable prompts (e.g., `character-image-prompt` → AI image platform Character Sheet prompts)
- Definition and compilation must not be mixed within a single skill

### Two-Tier Compilation
```
Character/Story Definitions (text-level, STATE 1-3)
  → character-image-prompt (compile to Character Sheet image generation prompts, for MJ/Flux/Jimeng/GPT Image)
  → director-prompt-packager (compile to film-level prompt package: storyboard design + camera language + sound design + Seedance decomposition plan)
  → User confirms prompt package
  → storyboard-* series (generate storyboard blueprint images, STATE 5)
  → seedance-video-prompt (compile to Seedance 2.0 video prompts, referencing generated images, STATE 6)
```

### Character Sheet Definition
- Character reference sheet = "Multi-view cinematic character design board for AI video consistency control (Character Sheet)"
- `character-image-prompt` produces Character Sheets, not "Artistic Identity Boards", not single portraits
- Character Sheets are reference assets for AI video cross-shot consistency, following the 12-section character profile template

### Pipeline State Machine (STATE 0-8)
```
STATE 0 → Input Collection
STATE 1 → Story & Emotion Design
STATE 2 → Visual Design (Camera + Lighting)
STATE 3 → Character Lock → character-image-prompt
STATE 4 → Prompt Packaging (Film-Level Short Film Prompt Package) → director-prompt-packager
STATE 5 → Storyboard Blueprint Generation (Image Level) → storyboard-* series
STATE 6 → Seedance Video Prompt (Image Reference Level) → seedance-video-prompt
STATE 7 → Final Validation
STATE 8 → Export Ready
```

---

## Branch Management Conventions

### Dual Branch Structure
| Branch | Language | Purpose |
|--------|----------|---------|
| `main` | English | All skill files and documentation in English |
| `zh-cn` | Chinese | All skill files and documentation in Chinese |

### Sync Flow
1. Complete architecture changes on `main`, then commit
2. `git checkout zh-cn && git merge main`
3. Resolve conflicts: zh-cn keeps Chinese translations, main keeps architecture structure
4. New files translated to Chinese before commit

### Conflict Resolution Strategy
- Translation differences (language only): accept zh-cn Chinese version
- Architecture differences (structure/logic changes): accept main architecture changes, then translate to Chinese
- Deletion differences (e.g., `director-seedance` rename): execute deletion

---

## Git Operation Conventions

### Commit Message
- On Windows cmd, commit messages containing Chinese or multiple lines must use `-F` file method:
  ```
  git commit -F _commit_msg.txt
  ```
- Forbidden: `git commit --amend`
- Forbidden: `git push --force` to main/master

### Common Issues
- **Git index.lock**: If `fatal: Unable to create index.lock` appears, manually delete `.git/index.lock`
- **Chinese paths**: Git handles Chinese paths well; no escaping needed
- **CRLF warnings**: Normal on Windows, can be ignored

---

## Document Management Conventions

### Directory Purposes
| Directory | Purpose | Operating Rules |
|-----------|---------|-----------------|
| `reference/` | Reference knowledge base (architecture diagrams, workflow cases, skill specifications) | **Extract information only; direct path references forbidden**. Skill files must not contain `reference/xxx.md` or "see xxx.md" |
| `doc/` | Generated outputs (storyboard boards, Seedance prompts, etc.) | Store user-facing final deliverables |
| Root `.md` | Project-level documentation (README.md, AGENT.md) | Project memory and entry documents |
| Root `prd*.md` | Development-phase temporary references | Only present during development, to be deleted — **strictly forbidden as skill file references** |

### Reference Knowledge Usage Conventions
- Documents under `reference/` are **knowledge sources**, providing background and templates for skill design
- Skill files extract their **rules and templates** and integrate them into their own logic, rather than directly referencing
- The "Artistic Identity Board" template under `reference/CHARACTER/` and the "Character Sheet" template from prd series are two different output types — skills must clearly identify which type they produce
- Example: 12-section character design board template → `character-image-prompt` fully absorbs it and becomes self-contained; does not write "see prd2.md"

### Output Document Naming
- Format: `{YYYYMMDD}_{Topic}_{Output Type}.md`
- Example: `20260608_Modern_Urban_Menswear_Director_Storyboard.md`
- Storage path: under `doc/` directory

### Reference Documents
- Development-phase temporary documents (prd.md, etc.) reside in root and must not be referenced by skill files
- Persistent reference knowledge resides under `reference/` directory; extraction only, no direct references

### Project Entry Points
- Root `README.md`: Project introduction and skill system overview
- Root `AGENT.md`: AI assistant's project memory and operational conventions

---

## Known Issues & Lessons Learned

### Issue 1: Skill Name Mismatch with Actual Function ✅ Fixed
- **Symptom**: `director-seedance` produced text-level storyboard prompt packages, but the name implied Seedance platform prompts
- **Fix**: Renamed to `director-prompt-packager`, added true `seedance-video-prompt` skill; swapped STATE 4/5 order — prompt package compilation now precedes storyboard image generation
- **Lesson**: Clarify skill boundaries and output types before naming; text-level design documents should come before image generation

### Issue 2: Missing Character Image Prompt Skill
- **Symptom**: `director-character` produced character identity definitions, but no skill compiled definitions into image-platform-usable prompts
- **Fix**: Added `character-image-prompt` skill
- **Lesson**: A compilation layer must exist between definition documents and executable prompts

### Issue 3: `director-core` Not Triggered
- **Symptom**: When user entered e-commerce video requirements, `storyboard-ecommerce` was called directly, bypassing the `director-core` state machine
- **Fix**: Expanded `director-core` trigger phrases (e-commerce livestream, commerce video, fashion video, etc.)
- **Lesson**: Master controller trigger phrases must cover all downstream sub-skill usage scenarios

### Issue 4: Skill Description References Temporary Documents
- **Symptom**: Multiple skill descriptions referenced `prd2.md` / `prd3.md`, which are development reference documents
- **Fix**: Replaced with generic descriptions (e.g., "multi-view character design board specifications")
- **Lesson**: Skills must be self-contained; cannot depend on temporary documents that may be deleted

### Issue 5: Main Branch File Language Inconsistency
- **Symptom**: Three newly created skill files on `main` branch (character-image-prompt, seedance-video-prompt, director-prompt-packager) were written in Chinese by mistake
- **Fix**: Rewrote as English versions, then merged to zh-cn and translated back to Chinese
- **Lesson**: Maintain English on main branch; zh-cn branch separately maintains Chinese translations

### Issue 6: Character Image Output Type Confusion (Artistic Identity Board vs. Character Sheet)
- **Symptom**: `character-image-prompt` once output in the `reference/CHARACTER/` "Artistic Identity Board" format — asymmetrical layout, pure white background, loose view selection — inconsistent with the Seedance pipeline (prd2/prd3) defined "Multi-view cinematic character design board for AI video consistency control (Character Sheet)"
- **Fix**: Aligned with prd2 12-section template and prd3 mandatory view checklist (front/side/3-4/rear/face close-up/hair/hand/expression sheet), used neutral background + professional layout, default style cinematic realistic rather than forced "artistic"
- **Lesson**: `reference/` may contain multiple templates serving different purposes (artistic display vs. AI training consistency); skills must explicitly reference the correct specification source, not mix them
