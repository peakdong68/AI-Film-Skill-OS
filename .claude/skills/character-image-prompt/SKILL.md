---
name: character-image-prompt
description: Compile character identity definitions from director-character into platform-ready character sheet image prompts for AI image generators (Midjourney / Flux / Jimeng / Kling). Follows the multi-view character design board specification — producing multi-view character design boards, not single portraits. Use for character image prompts, character sheet image prompts, character reference image generation prompts, or when director-core routes after STATE 3 completion. Use when the user has a character identity definition and needs to convert it into structured prompts ready for direct pasting into image generation platforms.
---

# Character Image Prompt — Compiler

## Overview

This is the **character identity definition → image generation prompt** compiler. It receives character identity definitions from `director-character` and compiles them into platform-ready image prompts following the multi-view character design board specification, ready for direct pasting into Midjourney / Flux / Jimeng / Kling.

**Key distinctions:**
- `director-character` (STATE 3): Produces character identity **definitions** (text-level design docs) — defines who the character is, what they look like
- `character-image-prompt` (this skill): Compiles identity definitions into **executable image prompts** for image generators — tells the AI how to draw a Character Sheet
- `seedance-video-prompt` (STATE 6): References the generated character images as `@[ref]` and compiles video platform prompts

## Compilation Principle

> Character image prompts are **structured visual instructions**. They must be concise, precise, and platform-compatible — not prose descriptions.

The compiler maps each field of the character identity definition into the standard character sheet image prompt structure:
1. **Identity Lock Layer** (who) → name, age, face, skin, hair, body
2. **Wardrobe Layer** (what they wear) → outfit, color, material, fit
3. **View Layer** (how to present) → multi-view list (front/side/3-4/rear/close-up)
4. **Style Layer** (what quality) → visual style, lighting, background
5. **Constraint Layer** (what must not appear) → negative prompt checklist

## Input Requirements

Before compilation, verify the character identity definition includes:

- [ ] Character Name / ID
- [ ] Age / Age Range
- [ ] Face: shape, skin tone, eye shape/color, eyebrows, nose, mouth, jaw
- [ ] Hair: length, style, color, texture
- [ ] Body: height, type, build, posture
- [ ] Wardrobe: main outfit, color palette, fabric type, fit
- [ ] Props (if applicable)
- [ ] Expression range (3-5 emotions)

If any field is missing, route back to `director-character` for completion.

## Output Structure

### Format: Complete Character Profile + Image Prompt

Follow the 12-section character profile template:

| Section | Content | Description |
|---------|---------|-------------|
| [0] | Character Reference ID | Identity, priority, reference tag |
| [1] | Core Identity | Age, occupation, personality, visual signature, keywords |
| [2] | Face Identity Lock | All facial parameters (shape/tone/features/details) |
| [3] | Hair Lock | All hair parameters (length/style/color/texture/parting) |
| [4] | Body Lock | All body parameters (height/weight/proportions/movement signature) |
| [5] | Wardrobe Lock | Clothing (main outfit + palette + materials), multi-look support |
| [6] | Prop Lock | Props (if applicable) |
| [7] | Expression System | Expression variations list (5 types) |
| [8] | View Requirements | Required view checklist |
| [9] | Visual Style Settings | Style/realism level/lighting/lens feel/background |
| [10] | Seedance Reference Settings | Lock switches + reference priority + reference boundaries |
| **[11]** | **Character Sheet Image Prompt** | **← Ready to paste into image generators** |
| [12] | Negative Prompt | Negative constraint checklist |

---

### [11] Character Sheet Image Prompt — Full Format Specification

#### Main Character Sheet (Standard Template)

```
Professional cinematic character sheet of [Character Name],
age [X],
[face shape], [jawline], [skin tone], [skin texture],
[eye shape], [eye color],
[eyebrow description],
[nose description], [lip description],
[hair length], [hair style], [hair color], [hair texture],
[body type], [height], [posture],

wearing [outer layer], [fabric], [fit],
[upper clothing], [fabric],
[lower clothing], [fit],
[shoes],
[accessories if any],

show front view, side view, 3/4 view, rear view,
full body standing pose, [signature pose 1], [signature pose 2], [action pose],
face close-up, hair detail,
expression sheet: [emotion 1], [emotion 2], [emotion 3], [emotion 4], [emotion 5],

professional character design sheet,
clean neutral gray studio background,
cinematic realism, photographic quality,
neutral studio lighting with subtle rim light,
high detail skin texture, visible fabric weave,
clean grid presentation layout,
consistent identity across all views
```

#### Multi-Look Extension Template

When a character has multiple outfits, generate an additional prompt per look:

```
Same character identity as [Character Name] character sheet,
same face, same hair, same body, same skin,

wardrobe changed to: [outer layer], [fabric], [fit],
[upper clothing],
[lower clothing],

show front view, side view, 3/4 view, rear view,
full body standing pose, [relevant poses],

clean neutral gray studio background,
cinematic realism, consistent identity with [Character Name] character sheet
```

---

### [12] Negative Prompt — Standard Checklist

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
no cartoon style
no anime style
no 3D render style
no over-stylization
no watermark
no logo
no text
no poster layout
no complex background
no text-heavy layout
```

---

## Platform Adaptation

| Platform | Adjustment |
|----------|------------|
| **Midjourney** | Keep in English, append `--ar 16:9 --style raw --v 6.1` |
| **Flux** | Keep in English, natural language flow, no special params needed |
| **Jimeng** | Translate to Chinese, preserve multi-view structure, add negative keywords |
| **Kling** | Translate to Chinese, strong consistency emphasis |

---

## Validation Checklist

Before delivery, verify each item:

- [ ] [11] Image Prompt can be copied and pasted directly
- [ ] All views listed (front/side/3-4/rear/close-up)
- [ ] Face/hair/body/wardrobe parameters match character identity definition
- [ ] Multi-look extension boards declare "same face, same hair, same body"
- [ ] [12] Negative Prompt covers all constraint items
- [ ] Prompt is concise, no redundant modifiers, no prose style
- [ ] No meta-instructions like "Generate a prompt" — the prompt itself is the final product

## Integration

Invoked by `director-core` or independently after STATE 3 completion:
- Load the character identity definition from `director-character`
- Compile into [0]-[12] complete Profile + image prompt
- After user confirmation, paste [11] prompts into MJ/Flux/Jimeng to generate character reference images
- Generated character reference images serve as `@[character ref]` inputs for STATE 6 `seedance-video-prompt`
