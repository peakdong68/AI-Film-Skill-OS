---
name: director-style
description: Define the director's visual personality and philosophical stance for AI film production — choose from Observer, Emotional, Immersive, Epic, or Commercial director profiles, each with distinct camera philosophy, pacing strategy, lighting approach, and narrative philosophy. Use when the user wants to define a directorial style, choose how the film should "feel" at a meta-level, select a director personality, need visual philosophy guidance, or when director-core routes here before visual design. Also use when the user says "make it feel like Wong Kar-wai" or "shoot this like Nolan" — map auteur references to concrete director profiles.
---

# Director Style — Director Personality System

## Overview

Before designing specific camera movements or lighting setups, every AI film needs a director personality — a consistent philosophical stance that governs how the camera sees, how time flows, and how emotion is expressed. This skill helps select and apply a director profile that shapes every downstream decision.

This is the "meta-level" of visual design: not what specific shot to use, but *what kind of filmmaker is making this film*.

Works independently or is invoked by `director-core` between STATE 1 (Story) and STATE 2 (Visual Design).

## The Core Concept

> The director personality is the WHY behind every visual choice.

Without a defined director personality, visual decisions become arbitrary. With one, every camera angle, lighting choice, and pacing decision traces back to a coherent philosophy.

## Director Personality Profiles

Select the dominant profile for the project. One film = one dominant profile. Mixing profiles mid-film causes visual incoherence.

### Profile A — Observer Director (Observer Director)

**Visual Philosophy**: The camera observes. It never interferes. It witnesses.

```
Philosophy: Reality unfolds naturally. The director does not manipulate.
Camera: Static, wide shots, long takes, minimal movement
Angle: Eye-level, occasionally distant
Movement: Static > slow tracking > rare dolly
Pacing: Slow cinema — long shots, breathing room, silence is structural
Lighting: Natural and motivated only — practical sources, available light
Emotion: Understated, implied, never forced
Narrative: Information is shown, not told. Audience discovers.
```

**Best for**: Documentary realism, social drama, slow-burn character studies, neorealism
**Reference touchpoints**: Italian Neorealism, observational documentary, Kogonada, slow cinema
**Visual identity**: *The world exists; the camera notices it.*

### Profile B — Emotional Director (Emotional Director)

**Visual Philosophy**: The camera feels with the character. It participates in their emotional state.

```
Philosophy: Emotion drives every decision. The camera is an emotional subject.
Camera: Close-ups dominant, slow dolly-in, shallow depth of field
Angle: Eye-level intimate, occasional POV
Movement: Dolly-in > orbit > handheld (only for emotional instability)
Pacing: Varied — slows for emotional peaks, accelerates for tension release
Lighting: Expressive and emotional — warm for intimacy, cold for isolation
Emotion: Foreground — faces, micro-expressions, breathing, hesitation
Narrative: Internal emotional journey prioritized over external plot
```

**Best for**: Romance, melodrama, psychological drama, character-driven stories
**Reference touchpoints**: Wong Kar-wai, Barry Jenkins, intimate cinema
**Visual identity**: *The camera breathes with the character.*

### Profile C — Immersive Director (Immersive Director)

**Visual Philosophy**: The camera becomes the audience. First-person experience. No distance.

```
Philosophy: The audience is inside the story, not watching it.
Camera: POV dominant, handheld realism, tracking shots that follow
Angle: Subjective — what the character sees, what the participant sees
Movement: Tracking > handheld > FPV > fluid continuous motion
Pacing: Real-time feel — action unfolds at the speed of experience
Lighting: Diegetic and environmental — what you'd actually see
Emotion: Immediate and visceral — no filter between audience and experience
Narrative: Mystery and discovery — audience learns as character learns
```

**Best for**: Thriller, horror, action, first-person narrative, mystery
**Reference touchpoints**: Paul Greengrass, found-footage, immersive journalism, FPV cinema
**Visual identity**: *You are there. You are in it.*

### Profile D — Epic Director (Epic Director)

**Visual Philosophy**: The camera dominates space. Scale over intimacy. Monumental.

```
Philosophy: The world is vast. Characters exist within it, not above it.
Camera: Wide shots dominant, crane, drone, large-scale movement
Angle: Low angle (power), high angle (scale), top-down (order/chaos)
Movement: Crane > drone > sweeping dolly > slow orbit
Pacing: Deliberate and grand — slow builds to massive peaks
Lighting: Dramatic and sculptural — strong directional, volumetric, god rays
Emotion: Awe and scale — individual emotion embedded in vast context
Narrative: World-building, historical sweep, mythic structure
```

**Best for**: Historical epic, sci-fi world-building, fantasy, nature documentary
**Reference touchpoints**: Denis Villeneuve, Terrence Malick, epic cinema
**Visual identity**: *The world is the main character.*

### Profile E — Commercial Director (Commercial Director)

**Visual Philosophy**: Attention is the primary currency. Impact over subtlety.

```
Philosophy: Every frame must earn attention. Visual impact is structural.
Camera: Varied — fast cuts, dynamic movement, product hero shots
Angle: Low angle (aspiration), eye-level (relatable), top-down (product)
Movement: Fast tracking > orbit > push-in > whip pan
Pacing: Fast and rhythmic — never linger, always advance
Lighting: Premium and controlled — beauty lighting, rim light, high polish
Emotion: Aspirational and immediate — want, desire, need
Narrative: Hook → Problem → Solution → Aspiration → CTA
```

**Best for**: Advertising, brand films, product showcases, music videos
**Reference touchpoints**: High-end commercial, fashion film, luxury advertising
**Visual identity**: *Every frame sells.*

## Profile Selection Guide

| User says... | Profile |
|---|---|
| "real like a documentary" / "natural observation" | Observer (A) |
| "focus on emotional expression" / "soulful filmmaking" / "Wong Kar-wai style" | Emotional (B) |
| "first-person experience" / "immersive" / "horror film" | Immersive (C) |
| "epic feel" / "grand scale" / "sci-fi blockbuster" / "Villeneuve style" | Epic (D) |
| "commercial" / "brand film" / "high-end advertising" | Commercial (E) |

## Director Decision Engine

Once a profile is selected, every downstream decision must reference it:

### Visual Philosophy → Camera Decisions

| Profile | Primary Shots | Primary Movement | Angle Preference |
|---------|--------------|-----------------|-----------------|
| Observer | Wide, medium | Static, slow track | Eye-level, distant |
| Emotional | Close-up, ECU | Slow dolly-in | Eye-level, intimate |
| Immersive | POV, handheld | Tracking, handheld | Subjective |
| Epic | Wide, extreme wide | Crane, drone, sweep | Low, high, top-down |
| Commercial | Varied, CU product | Fast, dynamic, orbit | Low (aspire), eye (relate) |

### Visual Philosophy → Pacing Decisions

| Profile | Cut Density | Shot Length | Silence Role |
|---------|------------|-------------|--------------|
| Observer | Very low | 4-8s | Primary structural element |
| Emotional | Low-medium | 3-5s | Used for emotional weight |
| Immersive | Medium | 2-4s | Minimal — immersion requires continuity |
| Epic | Very low | 5-10s | Used for scale and awe |
| Commercial | Very high | 1-3s | Rarely used — constant forward momentum |

### Visual Philosophy → Lighting Philosophy

| Profile | Light Source | Quality | Temperature |
|---------|-------------|---------|-------------|
| Observer | Natural/practical only | Soft, realistic | Neutral |
| Emotional | Expressive, motivated | Varied by emotion | Shifts with feeling |
| Immersive | Diegetic, environmental | Realistic, imperfect | What's actually there |
| Epic | Dramatic, sculptural | Strong, directional | Cool or warm dominant |
| Commercial | Controlled, premium | Soft + rim, polished | Cool elegance |

## Output Format

```markdown
## Director Profile: [Profile Name]

### Visual Philosophy
[1-2 sentences on how this director sees the world]

### Camera Philosophy
- Dominant shot types: [list]
- Movement vocabulary: [list]
- Angle signature: [description]
- Lens character: [depth, focus behavior]

### Pacing Philosophy
- Rhythm type: [slow cinema / classical / fast commercial]
- Cut density: [low / medium / high]
- Silence usage: [structural / emotional / minimal]
- Emotional rhythm: [how tension builds and releases]

### Lighting Philosophy
- Light philosophy: [natural / expressive / diegetic / dramatic / controlled]
- Key quality: [soft / hard / varied]
- Temperature arc: [how warmth/cool evolves]

### Narrative Philosophy
- Storytelling approach: [observe / feel / experience / awe / sell]
- Information strategy: [show don't tell / emotional reveal / gradual discovery / spectacle]

### Influence on This Project
- What this profile means for: [story → camera → lighting → character → pacing]
```

## Constraints

- One project = one dominant director profile. Mixing profiles causes visual schizophrenia.
- The profile must be selected before `director-camera` and `director-light` begin their work.
- Profile choice must be justified by the story and emotional intent — not arbitrary.
- Auteur references (Wong Kar-wai, Nolan, etc.) must be translated into profile attributes, not copied as imitations.

## Integration

When invoked by `director-core`:
- Selected after STATE 1 (story + emotion confirmed)
- Output feeds into STATE 2 — `director-camera` and `director-light` use the profile to guide their decisions
- The profile is referenced (not repeated) in all downstream skills


## Save Output

After delivering the final output, prompt the user to save:

```
Save to outputs/director-style-director-style-profile.md?
```

If the user confirms, write the output to the specified path.
