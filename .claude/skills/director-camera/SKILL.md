---
name: director-camera
description: Design the cinematography system for AI film production — camera language, shot types, movement grammar, composition rules, spatial blocking, and emotion-driven camera decisions. Use when the user needs camera design, 摄影机语言, shot planning, cinematography direction, 镜头设计, camera movement planning, or when director-core routes to STATE 2 (Visual Design). Also use when the user asks "how should this be shot" or needs to translate emotional intent into concrete camera decisions.
---

# Director Camera — Cinematography Director AI

## Overview

Design the camera system that defines *how* the film is shot — not what happens in the scene, but how the camera sees it. This skill builds a complete cinematography blueprint: shot type grammar, movement vocabulary, framing philosophy, spatial blocking, and emotional camera mapping. The output ensures every shot in the downstream storyboard and prompt systems has a grounded cinematographic reason for existing.

Works independently for camera design or is invoked by `director-core` at STATE 2.

## The Core Principle

> The camera is not a recording device. It is an emotional subject.

Every camera decision must answer three questions:
1. **What am I looking at?** (Subject)
2. **Why am I looking at it this way?** (Intent — driven by emotion)
3. **How does the camera move?** (Motion — driven by narrative rhythm)

## Output Structure

### 1. Camera Language System (摄影机语言系统)

Define the visual grammar for the entire film:

**Shot Type Grammar:**
| Type | 中文 | Narrative Function |
|------|------|-------------------|
| Wide Shot | 远景 | Establish world, show isolation, define spatial relationships |
| Medium Shot | 中景 | Carry narrative action, show behavior and interaction |
| Close-Up | 特写 | Reveal emotion, internal state, psychological detail |
| Extreme Close-Up | 超特写 | Decisive moment, emotional peak, visual anchor |
| Over-Shoulder | 过肩 | Relationship tension, dialogue structure, perspective |
| POV | 主观视角 | Immersive experience, identification with character |
| Top-Down | 鸟瞰 | Control, isolation, god-like perspective |
| Low Angle | 仰拍 | Power, threat, importance, heroism |

For the specific project, select the primary shot types and explain *why* this grammar fits the story.

**Movement Grammar:**
| Movement | 中文 | Emotional Function |
|----------|------|-------------------|
| Static | 定镜 | Oppression, observation, stillness, waiting |
| Slow Dolly-In | 缓推 | Emotional deepening, psychological pressure |
| Dolly-Out | 拉远 | Emotional withdrawal, loneliness |
| Tracking | 跟移 | Following action, participation, pursuit |
| Orbit | 环绕 | Relationship complexity, romance, surrealism |
| Handheld | 手持 | Realism, instability, tension, documentary feel |
| Crane | 升降 | Spatial revelation, epic scale |
| Whip Pan | 快速摇 | Emotional burst, rapid transition, disorientation |

**Focus Grammar:**
- **Rack Focus**: Attention transfer between subjects
- **Shallow Depth of Field**: Emotional isolation, subject emphasis
- **Deep Focus**: Environmental relationship, layered storytelling

### 2. Emotional Camera System (情绪摄影系统)

Map every primary emotion in the film to camera behavior:

| Emotion | Shot | Movement | Angle | Focus |
|---------|------|----------|-------|-------|
| Sadness / Loneliness | Wide | Static / slow push-in | Eye level | Shallow DOF |
| Fear / Tension | Close-up | Handheld micro-shake | Dutch / eye level | Tight |
| Romance / Intimacy | Close-up / OTS | Slow orbit / dolly | Eye level | Soft focus |
| Mystery | Wide / silhouette | Static / slow reveal | Low / obstructed | Deep |
| Power / Dominance | Medium / low angle | Slow controlled dolly | Low angle | Symmetrical |
| Shock | ECU | Sudden stillness | Eye level | Sharp |
| Action / Urgency | Medium | Tracking / handheld | Dynamic | Following |

This mapping table is the critical bridge — every shot in the storyboard should trace back to a row in this table.

### 3. Spatial Composition System (空间构图系统)

**Framing Rules:**
- **Rule of Thirds**: Balanced, natural composition — default for most narrative
- **Center Framing**: Ritual, power, symmetry — use for moments of significance
- **Negative Space**: Loneliness, isolation, emotional weight — subject pushed to edge
- **Foreground Obstruction**: Voyeurism, mystery, hidden observation
- **Frame Within Frame**: Layers, confinement, focus

**Depth Design:**
- Foreground → midground → background layering
- Environmental storytelling through object placement
- Spatial tension: distance between characters = emotional distance

**Blocking Design (人物调度):**
- Character position = emotional relationship
- Distance = psychological gap
- Movement direction = narrative tension
- Eye-line continuity = spatial logic

### 4. Camera Continuity System (镜头连续性)

Rules that must hold across all shots:

- **Direction consistency**: Screen direction (left-to-right / right-to-left) must not flip within a scene unless a crossing shot is explicitly designed
- **Scale progression**: Avoid jumping between extreme shot sizes without transition shots
- **Spatial geography**: The physical layout of the space must remain stable — chairs don't move, doors stay in the same place
- **Lighting direction**: Key light direction must remain consistent per scene unless a diegetic source moves
- **180-degree rule**: The camera stays on one side of the action axis within a scene unless a neutral shot breaks the line

### 5. Camera Prompt Template (摄影机提示词模板)

For every shot in the storyboard, the camera instruction must follow this template:

```
Shot type: [WS / MS / CU / ECU / OTS / POV]
Angle: [eye-level / low / high / Dutch / top-down]
Movement: [static / dolly-in / dolly-out / tracking / orbit / handheld / crane]
Lens behavior: [shallow DOF / deep focus / rack focus to X]
Framing: [rule of thirds / centered / negative space / frame-in-frame]
Emotional intent: [why this camera choice for this moment]
```

## Constraints

- No shot without an emotional reason — "it looks cool" is not a valid cinematographic decision.
- No random camera movement — every movement must serve narrative progression.
- No breaking the 180-degree rule without a deliberate crossing shot.
- Camera continuity must be verified across all shots before handing off to storyboard.
- Handheld movement must be motivated (tension, realism, chaos) — not a default.

## Integration

When invoked by `director-core`:
- Load emotional blueprint from `director-emotion` to inform the Emotional Camera System
- Produce the Cinematography Blueprint
- Feed into `director-light` for lighting alignment
- The Camera Prompt Template feeds directly into storyboard and prompt systems
