---
name: director-seedance
description: Compile all prior production artifacts (storyboard, character sheets, camera blueprint, lighting design) into executable Seedance 2.0 / Runway / Sora / Kling image-to-video prompts. This is the final compiler in the AI Film OS pipeline. Use when the user needs Seedance prompts, 视频生成提示词, storyboard-to-video conversion, video prompt compilation, or when director-core routes to STATE 5 (Prompt Compilation). Also use when the user has storyboard frames and character designs ready and needs them converted into production-ready video generation instructions.
---

# Director Seedance — Prompt Compiler Engine

## Overview

This is the final execution engine of the AI Film OS pipeline. It ingests the complete production package — narrative structure, emotional blueprint, camera language, lighting design, character identity locks, and storyboard frames — and compiles them into executable video generation prompts. Every prompt includes motion instructions, camera behavior, lighting direction, character continuity locks, environment dynamics, and negative constraints.

The compiler's job is to transform director language into machine-executable motion instructions. It is not a creative writing tool — it is a precision compilation system.

Works independently for prompt compilation or is invoked by `director-core` at STATE 5.

## The Compilation Principle

> Seedance prompts are not descriptions. They are motion instructions.

The compiler translates three layers into one executable block:
1. **Story Layer** (what happens) → Character motion + emotional progression
2. **Film Language Layer** (how it's shot) → Camera behavior + lighting direction  
3. **Machine Layer** (execution constraints) → Continuity locks + negative rules

## Input Requirements

Before compilation, verify all upstream artifacts are available:

- [ ] Storyboard frames (from storyboard-sketch or storyboard-prompt)
- [ ] Character identity locks (from director-character)
- [ ] Camera language blueprint (from director-camera)
- [ ] Lighting design (from director-light)
- [ ] Project metadata: duration per shot, aspect ratio, target platform

If any artifact is missing, halt and route back to the appropriate director skill. Never compile from incomplete inputs.

## Output Structure: Seedance Prompt Pack

For each storyboard frame, produce a complete prompt block:

```markdown
## SHOT [N]: [shot title]

### Context Lock
Continue from storyboard [frame N-1 / Part X].
Maintain strict continuity: same character identity, wardrobe, environment, and lighting logic as established.

### Scene Definition
Duration: [N] seconds
Location: [specific place]
Time: [time of day / temporal context]
Mood: [emotional keywords from director-emotion]

### Character Motion
Character [Name]:
- Physical action: [single clear action — what body does]
- Facial expression: [micro-expression change during the action]
- Eye behavior: [direction, focus shift, blink pattern]
- Emotional progression: [from state A → toward state B]
- Identity lock: same face, hair, body, wardrobe as Character Sheet

### Camera Behavior
Shot type: [WS / MS / CU / ECU / OTS / POV]
Angle: [eye-level / low / high / Dutch / top-down]
Movement: [static / dolly-in / dolly-out / tracking / orbit / handheld]
Lens behavior: [shallow DOF / deep focus / rack focus to X]
Framing: [rule of thirds / centered / negative space / frame-in-frame]
Emotional intent: [why this camera choice — from director-camera]

### Lighting Design
Key light: [source, direction, color temperature, quality]
Fill light: [source, intensity, color temperature]
Rim/Backlight: [source, color, purpose]
Contrast level: [low / medium / high]
Atmosphere: [volumetric / haze / clean / fog]
Color continuity: [reference to scene palette from director-light]

### Environment Dynamics
- Weather/atmosphere: [rain, wind, dust, fog, snow — or none]
- Background motion: [what moves in the environment during this shot]
- Particle behavior: [specific particle movement if applicable]
- Reflections/shadows: [key environmental light interactions]
- Spatial depth: [foreground/background relationship]

### Sound Direction (Optional)
- Ambience: [room tone, weather sound, city hum]
- Emotional cue: [music swell, heartbeat, silence, drone]
- Silence usage: [where silence creates tension]

### Negative Constraints
No text, no subtitles, no watermark, no logo.
No face distortion, no identity change, no face drift.
No wardrobe change, no hairstyle change.
No extra characters appearing.
No scene reset, no environment teleport.
No unnatural motion, no CGI artifacting (unless specified).
No style shift (maintain cinematic realism throughout).
```

## Compilation Rules

### Rule 1: Action Precision
- Every prompt must describe one clear physical action, not an abstract emotional state.
- ❌ "She feels sad" → ✔ "Her shoulders drop, chin lowers, eyes avoid contact, breathing slows"
- Use the emotion-to-motion mapping from `director-character`.

### Rule 2: Camera Must Be Explicit
- Every prompt must carry shot type, angle, and movement from `director-camera`.
- Camera decisions must trace back to an emotional intent — no unmotivated camera behavior.

### Rule 3: Time Must Be Compressed
- 1 storyboard frame = 1 action unit = 2-5 seconds
- A single prompt must not contain multiple time-separated actions

### Rule 4: Character Must Be Locked
- Every prompt must reference the character identity lock from `director-character`
- Explicitly state: "same [character name], same face, same hair, same wardrobe"
- Never regenerate or redescribe the character — reference the lock

### Rule 5: Environment Must Be Alive
- Every prompt must include at least one environmental dynamic element
- Static environments feel dead in AI video generation

### Rule 6: Continuity Must Span Shots
- Each shot's Context Lock references the previous shot
- Multi-part videos (>15s) must carry forward: previous_video_reference + current_storyboard_reference

## Multi-Part Continuity System (多Part连续系统)

For videos exceeding 15 seconds, split into Parts and bind them:

### Part 1
- Establish world + characters + visual language
- Set the baseline for all continuity parameters

### Part 2+
- Must reference previous video output as continuity anchor
- Must carry forward: character identity, wardrobe, environment, lighting logic, camera language
- Must evolve, not reset — emotional state should continue from where Part N-1 ended

### Multi-Part Prompt Template
```markdown
## PART [N]: [part title]

### Part Continuity
This is a direct continuation of Part [N-1].
Reference previous output as the continuity baseline.
Maintain: same character identity, same wardrobe, same environment,
same lighting logic, same camera language.
Evolve: emotional state continues from Part [N-1] endpoint.

### Shot [M].1: [shot title]
[Full prompt block as above, with Context Lock referencing Part N-1]
```

## Validation Checklist

Before delivering the final prompt pack, verify every shot:

- [ ] Action is visually clear and physically possible
- [ ] Camera behavior is defined (shot + angle + movement + lens)
- [ ] Lighting is meaningful and matches the scene palette
- [ ] Emotion is expressed physically, not abstractly
- [ ] Character identity lock is embedded
- [ ] Environment has at least one dynamic element
- [ ] Negative constraints block is present
- [ ] Context lock references the correct previous shot
- [ ] Duration is specified
- [ ] Prompt is executable as-is in the target tool

## Platform Adaptation

Adjust prompt density and specificity per platform:

| Platform | Prompt Style |
|----------|-------------|
| **Seedance 2.0** | Full structured blocks, Chinese or English, explicit continuity locks |
| **Runway Gen-3** | Concise English, camera movement in plain language |
| **Sora** | Natural language flow, implicit continuity through consistent description |
| **Kling** | Chinese-preferred, strong motion emphasis, explicit negative constraints |

## Integration

When invoked by `director-core`:
- Load all upstream artifacts (storyboard, character, camera, lighting)
- Verify pre-check checklist (all storyboards confirmed, characters locked, visual language defined)
- Compile the full prompt pack
- Run validation checklist
- Present for final user review
- Upon confirmation, signal STATE 5 complete
