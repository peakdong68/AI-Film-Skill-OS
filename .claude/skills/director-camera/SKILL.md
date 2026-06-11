---
name: director-camera
description: Design the cinematography system for AI film production — camera language, shot types, movement grammar, composition rules, spatial blocking, and emotion-driven camera decisions. Use when the user needs camera design, camera language, shot planning, cinematography direction, shot design, camera movement planning, or when director-core routes to STATE 2 (Visual Design). Also use when the user asks "how should this be shot" or needs to translate emotional intent into concrete camera decisions.
---

# Director Camera — Cinematography Director AI

## Overview

Design the camera system that defines *how* the film is shot — not what happens in the scene, but how the camera sees it. This skill builds a complete cinematography blueprint: shot type grammar, movement vocabulary, framing philosophy, spatial blocking, and emotional camera mapping. The output ensures every shot in the downstream storyboard and prompt systems has a grounded cinematographic reason for existing.

Works independently for camera design or is invoked by `director-core` at STATE 2.


## Load Resources

This skill includes bundled reference knowledge files. Load when needed:
- For complete shot type grammar, camera movement vocabulary, and emotion-to-camera mapping tables, see the sections below for shot type grammar, camera movement vocabulary, and emotion-to-camera mapping
- For the six shot semantics and visual priority decision logic, read `references/shot-semantics.md`
- For Seedance-specific shot contracts, shot size usage guides, and camera movement grammar, read `references/seedance-shot-language.md`
- For anti-slop lexicon replacement, read shared reference `../references/anti-slop-lexicon.md`
## The Core Principle

> The camera is not a recording device. It is an emotional subject.

Every camera decision must answer three questions:
1. **What am I looking at?** (Subject)
2. **Why am I looking at it this way?** (Intent — driven by emotion)
3. **How does the camera move?** (Motion — driven by narrative rhythm)

## Output Structure

### 1. Camera Language System (Camera Language System)

Define the visual grammar for the entire film:

**Shot Type Grammar:**
| Type | Label | Narrative Function |
|------|------|-------------------|
| Wide Shot | WS | Establish world, show isolation, define spatial relationships |
| Medium Shot | MS | Carry narrative action, show behavior and interaction |
| Close-Up | CU | Reveal emotion, internal state, psychological detail |
| Extreme Close-Up | ECU | Decisive moment, emotional peak, visual anchor |
| Over-Shoulder | OTS | Relationship tension, dialogue structure, perspective |
| POV | POV | Immersive experience, identification with character |
| Top-Down | Top-Down | Control, isolation, god-like perspective |
| Low Angle | Low Angle | Power, threat, importance, heroism |

For the specific project, select the primary shot types and explain *why* this grammar fits the story.

**Movement Grammar:**
| Movement | Label | Emotional Function |
|----------|------|-------------------|
| Static | Static | Oppression, observation, stillness, waiting |
| Slow Dolly-In | Slow Dolly-In | Emotional deepening, psychological pressure |
| Dolly-Out | Dolly-Out | Emotional withdrawal, loneliness |
| Tracking | Tracking | Following action, participation, pursuit |
| Orbit | Orbit | Relationship complexity, romance, surrealism |
| Handheld | Handheld | Realism, instability, tension, documentary feel |
| Crane | Crane | Spatial revelation, epic scale |
| Whip Pan | Whip Pan | Emotional burst, rapid transition, disorientation |

**Focus Grammar:**
- **Rack Focus**: Attention transfer between subjects
- **Shallow Depth of Field**: Emotional isolation, subject emphasis
- **Deep Focus**: Environmental relationship, layered storytelling

### 2. Emotional Camera System (Emotional Camera System)

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

### 3. Spatial Composition System (Spatial Composition System)

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

**Blocking Design (Character Blocking):**
- Character position = emotional relationship
- Distance = psychological gap
- Movement direction = narrative tension
- Eye-line continuity = spatial logic

### 4. Camera Continuity System (Camera Continuity System)

Rules that must hold across all shots:

- **Direction consistency**: Screen direction (left-to-right / right-to-left) must not flip within a scene unless a crossing shot is explicitly designed
- **Scale progression**: Avoid jumping between extreme shot sizes without transition shots
- **Spatial geography**: The physical layout of the space must remain stable — chairs don't move, doors stay in the same place
- **Lighting direction**: Key light direction must remain consistent per scene unless a diegetic source moves
- **180-degree rule**: The camera stays on one side of the action axis within a scene unless a neutral shot breaks the line

### 5. Camera Prompt Template (Camera Prompt Template)

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


## Save Output

After delivering the final output, prompt the user to save:

```
Save to outputs/director-camera-cinematography-blueprint.md?
```

If the user confirms, write the output to the specified path.
