---
name: director-light
description: Design the color script and lighting system for AI film production — emotion-to-color mapping, lighting progression, scene palette design, and visual temperature control. Use when the user needs lighting design, lighting design, color script, color script, mood lighting, visual atmosphere, or when director-core routes to STATE 2 (Visual Design). Also use when the film feels visually flat, the user wants a Pixar-style color script, or needs to maintain lighting continuity across shots.
---

# Director Light — Color & Lighting Intelligence Engine

## Overview

Design the visual mood system that gives the film its emotional texture. This skill builds two interconnected systems: a Color Script that maps the emotional journey to specific palettes across the full duration, and a Lighting Design that specifies light sources, qualities, and progression for each scene. The output ensures visual consistency and emotional intentionality in every frame.

Works independently for lighting/color design or is invoked by `director-core` at STATE 2.


## Loaded Resources

This skill ships with reference knowledge files. Load them when:
- For emotion-to-color mapping tables, lighting types, scene palette templates, and common lighting presets, read `references/color-lighting.md`
## The Core Principle

> Light and color are emotional actors, not environmental defaults.

Every lighting and color decision must serve the narrative. Warmth, cold, contrast, saturation — these are tools for controlling audience feeling, not just aesthetic preferences.

## Output Structure

### 1. Global Color Script (Global Color Script)

Design the color journey across the full film duration — similar to a Pixar color script. For each narrative phase (mapped from `director-emotion`'s emotional arc):

```
Phase 1 [name]: [duration %]
- Dominant palette: [2-3 colors with hex or descriptive names]
- Saturation level: [low / medium / high]
- Contrast level: [low / medium / high]
- Temperature: [warm / cool / neutral / mixed]
- Visual reference: [one-line description of the look]

Phase 2 [name]: [duration %]
...
```

The color script must show progression — color must evolve with the story, not remain static.

### 2. Emotion-to-Color Mapping (Emotion-to-Color Mapping)

Define the color language:

| Emotion | Dominant Color | Temperature | Saturation | Contrast |
|---------|---------------|-------------|------------|----------|
| Sadness / Loneliness | Blue-gray | Cold | Desaturated | Low |
| Love / Romance | Warm gold, amber | Warm | Medium | Soft |
| Fear / Horror | Green, dark desaturated | Cold | Very low | High |
| Anger / Conflict | Red, high contrast | Hot | High | Very high |
| Peace / Resolution | Soft blue, warm white | Neutral-warm | Medium | Low |
| Mystery | Deep purple, shadow | Cold-warm mix | Variable | High |
| Power / Luxury | Black, gold, silver | Cool | Low-mid | High |
| Hope / Optimism | Warm yellow, soft green | Warm | Medium | Soft |

### 3. Lighting Progression Map (Lighting Progression Map)

Define how lighting changes across the narrative:

```
Scene 1: [lighting setup] → emotional function: [why]
Scene 2: [lighting setup] → how it evolves from Scene 1
...
```

For each scene's lighting, specify:

**Lighting Types:**
| Type | Label | Emotional Function |
|------|------|-------------------|
| Natural Light | Natural Light | Realism, documentary feel |
| Hard Light | Hard Light | Conflict, pressure, harsh truth |
| Soft Diffused Light | Soft Diffused Light | Romance, dream, memory |
| Neon / Colored Light | Neon / Colored Light | Technology, night, urban, surreal |
| Silhouette / Backlight | Silhouette / Backlight | Mystery, emotional hiding, reveal |
| Practical Light | Practical Light | Diegetic sources (lamps, windows, screens) |
| Volumetric Light | Volumetric Light | Atmosphere, beams, god rays |
| Flicker Light | Flicker Light | Instability, tension, fear |

**Lighting Direction:**
- Key light position and motivation
- Fill light intensity and quality
- Rim/backlight for subject separation
- Color temperature of each source
- Shadow quality (hard/soft) and direction

### 4. Scene Palette System (Scene Palette System)

For each scene, lock the palette:

```
SCENE [N]: [name]
- Key light: [source, direction, color temp, quality]
- Fill: [source, intensity, color temp]
- Rim: [source, color, purpose]
- Ambient: [overall color cast]
- Shadows: [density, color bias]
- Special: [volumetric, practical, reflections]
- Palette lock: [what must stay consistent in this scene]
```

### 5. Visual Temperature Curve (Visual Temperature Curve)

Track color temperature across the full duration:

```
Warm ┤ ╭──╮
 │ ╱ ╲
Neut ┤───────╱ ╲──────
 │ ╱ ╲
Cool ┤╭────╱ ╲────
 │╲
 0%──────25%──────50%──────75%──────100%
```

Annotate temperature shifts with narrative events — a shift from warm to cold should correspond to a story beat.

### 6. Lighting Continuity Rules (Lighting Continuity Rules)

Rules that must hold across the film:

- Key light direction must remain consistent within each scene
- Color temperature shifts must be motivated (time of day, location change, emotional shift)
- Shadow quality should evolve, not reset arbitrarily
- Practical light sources established in one shot must persist in subsequent shots of the same scene
- No unmotivated "beauty lighting" — every light source must have a narrative or diegetic reason

## Emotional Lighting Templates

Quick-reference for common lighting moods:

**Romantic:**
- Warm key from one side (golden hour or practical lamp)
- Soft fill to reduce shadows
- Subtle warm rim for hair light
- Shallow DOF with bokeh
- Slight warm color grade

**Tension / Thriller:**
- Hard key from unusual angle (low or high)
- Deep shadows with minimal fill
- Cool color temperature
- Practical sources (flickering fluorescent, street light)
- High contrast grade

**Luxury / Commercial:**
- Large soft key for even illumination
- Strong rim/backlight for product edge definition
- Cool-toned shadows for depth
- Controlled reflections on surfaces
- Clean, high-key color grade

## Constraints

- Every scene must have a defined key light source — no ambient-only lighting.
- Color must evolve with the narrative — static palette = missed opportunity.
- Lighting continuity must be verified before storyboard handoff.
- No unmotivated color grade shifts between shots of the same scene.

## Integration

When invoked by `director-core`:
- Load emotional blueprint from `director-emotion` for the Emotion-to-Color Mapping
- Align with `director-camera` for consistent visual language
- The Scene Palette System feeds directly into storyboard and prompt compilation
