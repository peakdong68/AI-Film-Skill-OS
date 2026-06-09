# Prompt Packager Templates — Core Knowledge

## The Conversion Formula

```
Storyboard Panel
  → STEP 1: Extract (time, action, emotion, character, environment)
  → STEP 2: Convert to Film Grammar (shot type, camera, angle, lighting)
  → STEP 3: Add Motion Layer (body, facial, environmental, camera)
  → STEP 4: Add Continuity Lock (same character, wardrobe, location)
  → STEP 5: Compress into AI Image Prompt Language
  = Storyboard Image Prompt
```

## Standard Image Prompt Structure

### 1. Context Lock
```
Continue from storyboard Part X.
Maintain same character identity, wardrobe, environment, and lighting continuity.
```

### 2. Scene Definition
Duration, location, time, mood

### 3. Character Motion
Identity description, body movement, facial expression change, eye direction

### 4. Camera Behavior
Shot type, angle, movement, lens behavior, framing, emotional intent

### 5. Lighting Design
Color tone, intensity, direction, emotional mapping

### 6. Environment Motion
Weather, particles, light behavior, background movement, spatial depth

### 7. Sound Direction (optional)
Ambience, emotional sound cue, silence usage

### 8. Negative Constraints
```
No text, no subtitles, no watermark, no logo.
No face distortion, no identity change, no face drift.
No wardrobe change, no hairstyle change.
No extra characters appearing.
No scene reset, no environment teleport.
No unnatural motion, no CGI artifacting.
```

## Shot Duration Rules

| Total Duration | Shot Count | Per-Shot Duration |
|---------------|------------|-------------------|
| 15s | 5–7 shots | 2–3s |
| 30s | 8–12 shots | 2–4s |
| 60s | 12–20 shots | 3–5s |
| 3 min | 25–40 shots | 4–6s |

Rules:
- No shot exceeds 5 seconds (unless emotional slow cinema)
- Each shot = one action unit
- No multiple events in one shot

## The 6 Core Rules

1. **Action-first**: Describe physical movement, not emotional labels
2. **Camera explicit**: shot type + movement + angle in every prompt
3. **Time compressed**: one shot = one action unit (2-3s)
4. **Character locked**: "same character identity" in every prompt
5. **Environment alive**: rain/wind/light/particles in every shot
6. **Camera with reason**: every movement has an emotional motivation

## Performance Translation

❌ "She is sad"
✔ "She lowers her head, shoulders drop, breathing slows, eyes avoid contact"

❌ "He is nervous"
✔ "His fingers tap the table, he glances at the door repeatedly, jaw tightens"

The AI image model needs physical actions, not emotional labels.

## Multi-Part Generation Rules

For videos > 15 seconds, split into Parts:

### Part 1
- Previous_video_reference: none
- Establishes world + characters + visual language

### Part N (N > 1)
- previous_video_reference: output of Part N-1
- Maintains: character, wardrobe, environment, lighting logic, camera language
- Evolves: emotional state continues from Part N-1 endpoint
- Never restarts or resets — continuous cinematic flow

## Platform-Specific Adaptation

| Platform | Prompt Density | Language | Key Adaptation |
|----------|---------------|----------|----------------|
| Midjourney | Concise keywords | EN | Visual-first, style tokens |
| Flux | Natural language | EN | Detailed descriptions |
| 即梦/可灵 | Rich detail | CN preferred | Strong visual sense |

## Compilation Workflow

```
Shot Data (storyboard + character + camera + lighting)
  → Standardization (all visual, no abstract)
  → Conflict Resolution (fix contradictions)
  → Prompt Structuring (8-section format)
  → Compression (minimum words, maximum executability)
  → Storyboard Image Prompt
```

## Validation Checklist (per shot)

- [ ] Motion is visually clear?
- [ ] Camera behavior defined?
- [ ] Lighting is meaningful?
- [ ] Emotion is physically expressed?
- [ ] Continuity preserved?
- [ ] Prompt is executable as-is?
