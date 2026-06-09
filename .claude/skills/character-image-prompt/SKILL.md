---
name: character-image-prompt
description: Compile character identity definitions from director-character into multi-view cinematic Character Sheet prompts for AI image generators (MJ/Flux/即梦/GPT Image). Produces character design sheets for AI video consistency control — NOT single portraits, NOT artistic identity boards. Use when the user has a character reference image or a director-character definition and needs a Character Sheet prompt ready for AI image generation platforms. Also use when director-core routes after STATE 3 completion.
---

# Character Image Prompt — Character Sheet Compiler

## Overview

```
[Reference Image] or [director-character key fields]
                    +
            [Project Context]
                    ↓
         [Compiler]
                    ↓
   Character Sheet Prompt (MJ / Flux / 即梦 / GPT Image)
```

**Core Definition:**

> Character Sheet = **"Multi-view cinematic character design board for AI video consistency control."**
>
> This skill outputs **Character Sheet image prompts**, NOT single portraits, NOT artistic identity boards.
> The purpose is AI video cross-shot consistency — the Character Sheet is a reference asset that locks character identity across all generated video frames.

**Input Sources:**

| Source | Role |
|--------|------|
| Reference Image (recommended) | Visual anchor for character appearance |
| director-character output | Full character profile: face, hair, body, wardrobe, props, expression system |
| Project Context | Project type, emotional tone — used to derive visual style direction |

---

## Output Structure — 12-Section Character Sheet Profile

| Section | Content | Purpose |
|---------|---------|---------|
| [0] | Character Reference ID | ID, role, priority, continuity importance, reference tag |
| [1] | Core Identity | Age, occupation, personality, emotional function, visual signature, keywords |
| [2] | Face Identity Lock | Face shape, skin tone, eyes, eyebrows, nose, mouth, jaw, distinguishing features |
| [3] | Hair Lock | Length, style, color, texture, parting, movement |
| [4] | Body Lock | Height, body type, build, posture, movement style, signature gesture |
| [5] | Wardrobe Lock | Main outfit, color palette, fabric, fit, accessories, alternative outfits |
| [6] | Prop Lock | Primary/secondary props, signature items, interaction style |
| [7] | Expression System | Emotion range with physical manifestations (3-5 key emotions) |
| [8] | Character Sheet View Requirements | Required views checklist |
| [9] | Visual Style Settings | Style, realism level, lighting, color mood, lens feel, background |
| [10] | Seedance Reference Settings | Lock switches, reference priority, reference boundaries |
| **[11]** | **Character Sheet Image Prompt** | **← Final deliverable. Ready to paste into AI image generators.** |
| [12] | Negative Prompt | Negative constraint checklist |

> **Note:** Sections [0]-[10] are the compiler's working data sourced from director-character. Section [11] is the deliverable. Section [12] is the constraint appendix.

---

## [11] Character Sheet Image Prompt — Template

```
Professional cinematic character sheet showing {Character Name},
age {Age},

{face shape}, {jawline}, {skin tone}, {skin texture},
{eye shape}, {eye color},
{eyebrow description},
{nose description}, {lip description},
{hair length}, {hair style}, {hair color}, {hair texture},

{body type}, {height}, {posture},

wearing {wardrobe full description},
{accessories if any},

show front view, side view, 3/4 view, rear view,
full body standing pose, {signature pose 1}, {signature pose 2},
face close-up, hair detail, hand detail,
expression sheet: {emotion 1}, {emotion 2}, {emotion 3}, {emotion 4}, {emotion 5},

professional character design sheet,
neutral background,
cinematic realism,
high detail skin texture, visible fabric weave,
clean presentation layout,
consistent identity across all views
```

### With Reference Image Variant

```
Professional cinematic character sheet using the reference image as identity source,
perform color correction, maintain subject identity accuracy,

show front view, side view, 3/4 view, rear view,
full body standing pose, {signature pose 1}, {signature pose 2},
face close-up, hair detail, hand detail,
expression sheet: {emotion 1}, {emotion 2}, {emotion 3}, {emotion 4}, {emotion 5},

same face, same hair, same body, same wardrobe as reference image,
professional character design sheet,
neutral background,
cinematic realism,
clean presentation layout,
consistent identity across all views
```

---

## [12] Negative Prompt

```
no face change
no hairstyle change
no body proportion change
no random age shift
no wardrobe change
no extra accessories
no extra characters
no duplicate characters
no distorted face
no bad anatomy
no extra fingers
no identity drift
no inconsistent skin tone
no random props
no cartoon style unless requested
no anime unless requested
no over-stylization
no watermark
no logo
no text
no poster layout
no text-heavy poster layout
```

---

## View Requirements (Mandatory)

Every Character Sheet MUST include:

| View | Required | Notes |
|------|----------|-------|
| Front view | ✓ | Full body |
| Side view | ✓ | Full body |
| 3/4 view | ✓ | Full body |
| Rear view | ✓ | Full body or silhouette |
| Face close-up | ✓ | Neutral expression, front |
| Hair detail | ✓ | Close-up showing texture |
| Hand detail | ✗ | If hands are narratively important |
| Full body standing pose | ✓ | Signature stance |
| Walking pose | ✗ | If movement is important |
| Action pose | ✗ | If character has signature action |
| Expression sheet | ✓ | 3-5 emotion variations |

---

## Visual Style Settings

| Parameter | Default | Alternatives |
|-----------|---------|-------------|
| Visual Style | Cinematic realism | Stylized anime, semi-realistic, concept art, editorial, 3D render — derived from project type |
| Lighting | Neutral studio lighting with subtle rim light | Dramatic rim light, soft diffused, high-contrast — derived from emotional tone |
| Background | Neutral gray or soft gradient studio backdrop | Clean off-white — must NOT distract from character |
| Lens feel | 50mm portrait | 85mm editorial, 35mm situational |
| Layout | Clean professional presentation | Asymmetric editorial (if project calls for it) |

---

## Consistency Lock

All views and all downstream Seedance prompts must maintain:

| Lock | Scope |
|------|-------|
| Face Lock | Face shape, features, proportions, age |
| Hair Lock | Length, style, color, texture |
| Body Lock | Build, height proportion, limb features |
| Wardrobe Lock | Main outfit, accessories, shoes |
| Prop Lock | Fixed items, weapons, ornaments |
| Mood Lock | Personality, emotional baseline |

---

## Compilation Workflow

1. Load character profile from `director-character` output → fill sections [0]-[10]
2. Derive visual style settings [9] from project context
3. Fill Character Sheet Image Prompt [11] template
4. Attach Negative Prompt [12]
5. Deliver: sections [11] + [12] are ready to paste into the user's chosen AI image generator

---

## Two Input Modes

### Mode A: With Reference Image

User already has a character image. The prompt uses the image as the identity source.

- Prompt says: "using the reference image as identity source"
- Character appearance is locked by the reference
- The image generator focuses on creating the multi-view Character Sheet layout

### Mode B: Without Reference Image

User only has director-character definition. The prompt includes full appearance details.

- Prompt fills in all face/hair/body/wardrobe fields from the character profile
- The image generator creates both the character appearance AND the multi-view layout

---

## Multi-Look Extension

When a character has multiple outfits, generate additional prompts per outfit:

```
Same character identity as {Character Name} character sheet,
same face, same hair, same body, same skin tone,

wardrobe changed to: {new outfit description},

show front view, side view, 3/4 view, rear view,
full body standing pose,

neutral background,
cinematic realism,
consistent identity with {Character Name} character sheet
```

---

## Platform Adaptation

The Character Sheet prompt is platform-agnostic. Adjust per target platform:

| Platform | Language | Adjustments | Parameters |
|----------|----------|-------------|------------|
| **Midjourney** | English (default) | Keep as-is | `--ar 16:9 --style raw --v 6.1` |
| **Flux** | English (default) | Keep as-is, natural flow | None needed |
| **GPT Image** | English (default) | Keep as-is | None needed |
| **即梦 (Jimeng)** | Translate to Chinese | Preserve multi-view structure, add negative keywords to negative prompt | None needed |
| **可灵 (Kling)** | Translate to Chinese | Strong consistency emphasis, add negative keywords | None needed |

---

## Validation Checklist

- [ ] [11] Character Sheet Image Prompt is self-contained — directly pastable
- [ ] All required views listed (front, side, 3/4, rear, face close-up, expression sheet)
- [ ] Face/hair/body/wardrobe parameters match director-character definition
- [ ] [12] Negative Prompt covers all constraint items
- [ ] Background is neutral, not distracting
- [ ] No "artistic identity board" language — uses "cinematic character design board" instead
- [ ] No grid/blueprint/catalog layout forced — style is derived from project context
- [ ] Platform adaptations applied if targeting 即梦/可灵 (Chinese translation)

---

## Integration

Invoked by `director-core` or independently after STATE 3:

1. Load character profile from `director-character`
2. Compile into [0]-[12] complete Character Sheet Profile + Image Prompt
3. User confirms, then pastes [11] into their chosen AI image generator to generate Character Sheet image
4. Generated Character Sheet serves as `@[character ref]` for STATE 6 `seedance-video-prompt`
