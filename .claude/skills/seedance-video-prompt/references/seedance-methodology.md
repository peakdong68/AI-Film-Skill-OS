# Seedance 2.0 Prompt Methodology — Bundled Reference

Knowledge extracted and adapted for the `seedance-video-prompt` skill.

---

## Director Formula

```
Subject + Action + Scene + Camera + Lighting/Style + Audio + Constraints
```

Put the subject and primary action first — early clauses set the shot hierarchy. Do not force every slot if a reference asset already shows the information. For I2V, describe only the motion, camera, timing, transformation, audio, and preservation constraints that the still image cannot show.

| Slot | Use for | Prompt-ready pattern |
|---|---|---|
| Subject | The anchor the model must track. | `Original ceramic perfume bottle on black acrylic, label preserved exactly` |
| Action | The visible change. | `condensation beads form and slide down the glass over five seconds` |
| Scene | Only what is not already in references. | `quiet rain-lit kitchen counter, shallow depth of field` |
| Camera | One primary move with endpoint. | `slow dolly-in from medium product shot to macro label detail` |
| Light and style | Physical light plus safe visual language. | `warm practical key from frame left, cool blue rim, clean commercial realism` |
| Audio | Ambient bed, SFX, dialogue, or silence. | `Sound: low room tone, soft glass chime on final frame` |
| Constraints | Preservation and exclusions. | `do not alter logo, shape, label, or cap geometry` |

## Mode Gates

| Mode | Drafting priority | Common mistake | Repair |
|---|---|---|---|
| T2V | Build the whole shot in compact layers. | Too many events in one clip. | Keep one visible beat and one endpoint. |
| I2V | Preserve visible identity; add motion. | Re-describing the image until product/face drifts. | Say `preserve [Image1] exactly`; add only dynamic changes. |
| V2V | Transfer motion, camera, or timing. | Copying unauthorized likeness or scene details. | Use owned/licensed/authorized references and restrict transfer role. |
| R2V | Assign separate roles to each asset. | One reference asked to control identity, pose, scene, and style. | Split roles or prioritize the most important role. |
| FLF2V | Move from first frame to last frame. | Treating the last frame as vague mood instead of endpoint. | State `[Image2]` is the final visual target. |
| Edit | Preserve the source clip while changing one layer. | Rewriting the whole scene and losing continuity. | Say `[Video1] is the source clip; change only...` |
| Extend | Continue from the existing final state. | Starting a new scene after the clip. | Use last frame as continuity anchor, change one variable. |

## @[ref] Role Mapping

Before writing prompt prose, assign every uploaded asset a primary role. This prevents accidental transfer of identity, logos, scene ownership, or incompatible camera/motion instructions.

| Asset | Good Roles | Avoid |
|---|---|---|
| Image | identity, product, pose, costume, environment, first frame, last frame | Asking it to define unseen motion |
| Video | motion, camera, pacing, blocking, timing, gesture rhythm | Copying protected identity, logo, or scene ownership |
| Audio | rhythm, tempo, mood, ambience, delivery tone, music texture | Assuming voice, song, or likeness authorization |

**Core rules:**
- Preserve reference tags exactly.
- Give every reference one primary role before writing style language.
- Write what should transfer and what should not transfer.
- When authorization is unclear, transfer broad motion, tempo, mood, or production function rather than protected identity.

**Role mapping declaration template (Chinese):**

```
@[产品图片1] 控制产品身份——严格锁定颜色、印花图案、印花颜色、大小、位置、版型。
@[角色图片1] 控制角色身份——严格保持同一位模特的主体特征，面部自然。
@[分镜图片1] 控制动作节奏——用作动作规划参考，不渲染分镜表本身。
@[背景图片1] 控制环境——严格保持空间结构、光线、色调和陈列稳定。
@[音频1] 仅控制节奏和能量——不复制受保护的声音、歌曲或表演者身份。
```

## I2V Core Principles

**Only prompt what the image cannot show.** A still image already contains subject identity, product form, wardrobe, palette, composition, and background. Re-describing those static details often causes drift. Add only: motion, camera, timing, transformation, lighting change, audio, and preservation constraints.

**Minimal I2V template:**
```
[Image1] is the reference; preserve [identity/product/scene] exactly.
Only [motion] changes. Camera: [one move]. Lighting: [source or transition].
Sound: [cue]. Constraint: [what must not change].
```

### Good I2V Additions

| Add | Example |
|---|---|
| Micro-expression | `subject blinks once and lowers their eyes` |
| Product light sweep | `thin highlight travels across the label` |
| Weather | `rain streaks behind the subject; droplets bead on the surface` |
| Camera | `slow dolly-in from current composition to tighter detail` |
| Atmosphere | `dust catches the doorway beam and settles` |
| Audio | `soft room tone, one key click at the endpoint` |

### Common I2V Failure Fixes

| Failure | Fix |
|---|---|
| Identity drifts | Reduce new visual description, strengthen preservation constraints |
| Camera jumps | Use one camera move with start and endpoint |
| Product warps | Say `preserved, static identity, no shape change` |
| Output is still | Add one physical action and one time cue |
| Background changes | Preserve environment layout, animate only light/weather/atmosphere |
| Hands deform | Simplify hand motion or keep hands outside the main action |

## Compression Rules

When the prompt is too long, **delete in this order:**

1. Duplicate style adjectives
2. Generic quality words
3. Background details visible in references
4. Secondary camera moves
5. Secondary actions
6. Speculative emotional labels

**Preserve at all costs:**
1. Reference tags and their role
2. Subject or product identity
3. Action verb and visible endpoint
4. One camera move
5. Physical light source or atmosphere
6. Audio cue or silence instruction
7. Safety, IP, or continuity constraint

**Compact Chinese I2V template:**
```
@[图1]为参考，严格保持[主体]不变；仅加入[动作/光线/镜头]。声音：[提示]。约束：[不变项]。
```

## Anti-Slop Lexicon

Replace empty evaluation language with observable production language. Rule: **If a camera, microphone, light meter, or stopwatch cannot detect it — rewrite it.**

| Weak phrase | Replace with |
|---|---|
| cinematic | shot scale, camera move, lighting, grade |
| epic | physical scale, stakes, crowd size, lens distance |
| beautiful | color, texture, composition, material, light behavior |
| stunning | visible contrast, reveal, movement, or detail |
| dynamic | specific movement, speed, and endpoint |
| dramatic | blocking, shadow, silence, or camera pressure |
| ultra-realistic | material behavior, skin texture, lens artifacts, natural motion |
| cool transition | match cut, whip pan, dissolve, hard cut, object wipe |
| magical | particle behavior, glow source, motion path, interaction |
| professional | product lighting setup, clean background, controlled camera |
