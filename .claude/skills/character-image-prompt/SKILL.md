---
name: character-image-prompt
description: Compile character identity definitions from director-character into CHARACTER IDENTITY BOARD prompts for GPT Image. Produces artistic multi-view identity boards with asymmetric cinematic layout — NOT standard character reference sheets or turn-around grids. Use when the user has a character reference image or a director-character definition and needs a GPT Image-ready identity board prompt. Also use when director-core routes after STATE 3 completion.
---

# Character Image Prompt — GPT Image Identity Board Compiler

## Overview

```
[Reference Image] or [director-character key fields]
                    +
            [Project Context]
                    ↓
         [Compiler: 4-Layer Framework]
                    ↓
     GPT Image CHARACTER IDENTITY BOARD Prompt
```

**Core Principle:**

> This skill outputs **identity board STRUCTURE instructions**, NOT **character appearance descriptions**.
> Appearance description is `director-character`'s responsibility, already completed in the character profile.
> This skill's job is to tell GPT Image **how to LAY OUT the identity board**.

**Input Sources:**

| Source | Role |
|--------|------|
| Reference Image (recommended) | Visual anchor for character appearance — GPT Image identifies the character from the image |
| director-character key fields | Name, Role, Core Mood, Visual Keywords (3-8 items) — used for text block and direction derivation |
| Project Context | Project type, emotional tone — used to derive visual medium and art style |

## Compilation Principle — 4-Layer Framework

```
[Project Layer] → [Visual Layer] → [Board Structure Layer] → [Output Prompt]
      ↓                 ↓                   ↓                      ↓
   project           derived            board layout            GPT Image
   context           style              rules                   prompt
```

| Layer | Content | Source |
|-------|---------|--------|
| Project Layer | Project type, emotional tone | User-provided |
| Visual Layer | Visual medium, art style, lighting direction | Compiler derives from project context |
| Board Structure Layer | Composition anchor, auxiliary modules, study zones, text design, identity lock | Fixed rules (universal across projects) |
| Output | Self-contained GPT Image prompt ready to paste | Composition of three layers above |

**Note:** There is **no** "subject appearance layer" in the framework. Appearance is carried by the reference image, or auto-derived by GPT Image from visual keywords + project context.

---

## Input Requirements

### Extract from director-character (key fields only — full profile NOT required)

- [ ] Name
- [ ] Role / Identity
- [ ] Core Mood (one sentence)
- [ ] Visual Keywords (3-8 items)

### Extract from Project Context

- [ ] Project Type (animation / film / game / ad / short video / other)
- [ ] Emotional Tone (warm / dark / sci-fi / mysterious / passionate / healing / other)

### Reference Image (optional but recommended)

- [ ] Existing character image (full body or half body, from GPT Image / MJ / Flux / etc.)

---

## Visual Direction — Derivation Rules

The compiler derives visual direction from project context. These are NOT manually specified by the user.

| Derived Item | Rule |
|-------------|------|
| **Visual Medium** | Film → cinematic realism; Animation → stylized anime/semi-realistic; Game → concept design; Ad → commercial photography/editorial; Short video → semi-realistic/illustration |
| **Art Style** | Dark/sci-fi → high-contrast editorial; Warm/healing → soft natural light; Mysterious/suspense → low-key restrained cinematography; Passionate/action → dynamic concept design |
| **Lighting** | Lonely/reserved → top light + rim light; Oppressive/mysterious → cool high-contrast; Warm/intimate → soft diffused light |
| **Color Temperature** | Warm (intimate/heroic/healing) / Cool (detached/mysterious/sci-fi) / Neutral (documentary/realistic) |

---

## Output

The compiler produces a single deliverable — the GPT Image prompt. Optional working data sections provide compilation traceability.

| Section | Content | Purpose |
|---------|---------|---------|
| [W0] | Project Summary | Compiler input snapshot (from project context) |
| [W1] | Subject Identity Key | Compiler input snapshot (from director-character) |
| [W2] | Visual Direction | Compiler inference result (from derivation rules) |
| **[P]** | **GPT Image Identity Board Prompt** | **← Final deliverable. Ready to paste.** |

> `[W0]` `[W1]` `[W2]` are compiler working data — they show traceability. `[P]` is the deliverable.

---

## [P] GPT Image Identity Board Prompt — Universal Template

This is the **universal mother template**. It accepts any subject type and visual medium. The compiler fills all `{...}` slots from `[W0]` `[W1]` `[W2]`.

```
Create a 16:9 artistic CHARACTER IDENTITY BOARD.

[Subject]
{If reference image available: Use the reference image. Perform color correction. Maintain subject identity accuracy.}
{If no reference image: Create character appearance based on the following keywords: {Visual Keywords}.}
Subject type: Human character.
Visual medium: {Visual Medium}.

Background: Pure white or soft off-white. No environment, no scene, no logo, no watermark, no decorative elements.

[Design Direction]
Do NOT create a standard character reference sheet.
Create a cinematic artistic identity board that feels like: a high-end animation studio character study page + an art book layout + an editorial design spread + a production-grade concept study page.
Overall visual feel: Minimal, premium, memorable, art-directed, asymmetric layout, breathing room.
Use: Large areas of negative space, intentional imbalance, varied image scales, varied visual rhythm.
Avoid: Grid layout, catalog layout, blueprint style, repetitive arrangement, mechanical symmetry, standard turn-around sheet arrangement.

[Critical Layout Rules]
No character images may overlap. Every view must have clear spacing and breathing room.
Keep all full-body views, portraits, silhouettes, and detail studies visually distinct from each other.
No cropping faces, no hiding limbs, no stacking characters, no merging poses.

[Subject Composition Anchor]
Place one large off-center hero {full body / three-quarter body} shot as the visual anchor for the entire board.
Subject pose: {Signature Pose}.
Embodies character qualities: {Character Qualities}.

[Subject Identity Lock]
All views must maintain strict identity consistency.

Face:
{Face shape}. {Skin tone description}, {skin texture}.
{Eye shape}, {eye color}, {eye features}.
{Eyebrow description}, {eyebrow features}.
{Nose description}. {Mouth/lip description}.
Jaw {jaw description}.
{Distinguishing facial features if any}.

Hair:
{Hair style description}, {length}.
Color {hair color}, {hair texture}.
{Part direction if any}.

Body:
{Body type}. Height {height}.
Posture {posture description}.

Wardrobe:
{Full outfit from director-character Wardrobe System}.
Color palette: {color palette}.
Fabric language: {fabric description}.
Fit: {fit description}.
Accessories: {accessories list}.

Props:
{Props list. Write "No fixed props" if none}.

[Auxiliary Study Modules]
Arrange the following auxiliary study modules around the anchor with clean spacing. Each module should feel like an independent study page — no overlapping, no merging poses, no stacking characters, no cropping faces, no hiding limbs.
Select appropriate modules based on character type:

• Neutral full body front
• Full body back
• Full body side
• {Signature pose 1}
• {Signature pose 2}
• {Behavior/action pose}
• Expressive portrait study (face close-up)

[Art Study Zones]

Small silhouette study zone: 2-4 simplified pure black character silhouettes showing silhouette readability across different poses.

Small expression study zone: Show subtle emotional variations.
{Emotion 1}: {physical manifestation}
{Emotion 2}: {physical manifestation}
{Emotion 3}: {physical manifestation}
{Emotion 4}: {physical manifestation}
{Emotion 5}: {physical manifestation}

Small detail study zone: Magnified details of key visual features.
• Facial structure details
• Hair texture details
• Fabric and tailoring details
• {Accessory/prop details if any}

[Text Design Block]
Add a minimal, premium identity information block. Keep it minimal, bold, and art-directed. Use only:

NAME: {Character Name}
ROLE: {Narrative Role}
CORE MOOD: {Core Emotion}
VISUAL SIGNATURE: {Visual Keywords}

Optional: Small handwritten-style labels, minimal arrows, editor marks, brief annotations. Keep restrained.

[Identity Lock Declaration]
All views maintain: Same facial structure, same facial proportions, same hairstyle, same hair color, same outfit, same body proportions, same silhouette character, same posture language, same visual personality, same visual DNA.

[Readability Optimization]
Ensure: Clear silhouette, clear facial features, clear hair outline, clear clothing outline, clear body structure, clear hand expression, clear posture language, clear expression range, clear visual hierarchy.
Suitable for future image generation and video character consistency training.

[Final Style Requirements]
Minimal, cinematic, premium, art book quality, clean, expressive, production-grade, elegant, AI-training-friendly, visually memorable.

The final image should feel like an artistic character identity board designed to help AI models understand the character's face, silhouette, clothing, posture, and emotional range.
Focus on helping understand: Identity features, silhouette language, form structure, material characteristics, posture patterns, emotional range, visual DNA.
```

---

## Board Design Rules (Fixed — Apply to All Prompts)

| Rule | ✅ DO | ❌ DO NOT |
|------|-------|-----------|
| Layout | Asymmetric, breathing spacing, varied scales, intentional imbalance | Grid, blueprint, catalog, mechanical symmetry |
| Background | Pure white / soft off-white | Gray studio, gradient, environment, scene |
| Anchor | One large off-center hero view | Centered, equally sized, tiled |
| View Separation | Clear spacing, each view = independent study page | Overlapping, stacking, merging poses |
| Cropping | Full body/face/limbs visible | Face crop, limb cut-off, hidden body parts |
| Text | Name / Role / Core Mood / Visual Signature only | Paragraphs, bios, stats, UI-style text blocks |
| Decorations | None | Watermark, logo, borders, brand elements |

---

## Two Input Modes

### Mode A: With Reference Image (Recommended)

User already has a character image (from GPT Image / MJ / Flux / photography etc.) and needs a multi-view identity board.

**Prompt key difference:**
```
[Subject]
Use the reference image. Perform color correction. Maintain subject identity accuracy.
```

Character appearance is locked by the reference image. The prompt only controls identity board structure and layout. No need to fill in face/hair/body/wardrobe appearance parameters — this information is already in the image.

### Mode B: Without Reference Image

User does not yet have a character image and needs to generate an identity board from scratch.

**Prompt key difference:**
```
[Subject]
Create character appearance based on the following keywords: {Visual Keywords}.
```

GPT Image auto-derives the full appearance from keywords + project context. The compiler does NOT manually fill in face/hair/body/wardrobe details — these are autonomously derived by GPT Image.

---

## Multi-Look Extension

When a character has multiple outfits, generate one additional prompt per outfit, referencing the primary board:

```
Create a 16:9 artistic CHARACTER IDENTITY BOARD, outfit variant of the same character {Name}.

[Subject]: Same face, same hair, same body, same skin tone as the {Name} primary identity board. Use the reference image.

[Wardrobe Change]: {New outfit keyword description}.

[Composition Anchor]: Same hero pose as the primary board, wearing the new outfit.
[Auxiliary Views]: Full body front, full body back, full body side, all in the new outfit.

Pure white background. No environment. Style consistent with the {Name} primary identity board.
```

---

## Multi-Character Contrast Block

For projects with multiple characters, append after individual prompts:

```
[Multi-Character Visual Contrast Design]

{Character A} ←→ {Character B}

Size contrast: {Height and body type differences}
Color palette contrast: {A palette} vs {B palette} — {contrast effect}
Shape language contrast: {A shapes} vs {B shapes}
Texture contrast: {A textures} vs {B textures}
Lighting rules: Differentiated expression under shared lighting logic
Interaction rules:
  - Distance norm: {Typical distance}
  - Gaze patterns: {Respective eye behaviors}
  - Touch boundaries: {Rules}
  - Power dynamic: {Dominance relationship}
```

---

## Platform: GPT Image

| Aspect | Requirement |
|--------|-------------|
| Language | Primary language of the project (Chinese for zh-cn, English for main). English only for proper names and design term labels |
| Prompt style | Structured sections, not prose |
| Negative constraints | Embedded as positive rules ("Do NOT..." / "Avoid..." / "No..."), not a separate negative prompt list |
| Aspect ratio | `16:9` declared at the start of the prompt |
| Parameters | No additional parameters needed (GPT Image does not use --ar / --style / --v) |

---

## Validation Checklist

- [ ] Prompt is self-contained — directly pastable into GPT Image with no meta-instructions
- [ ] All `{...}` placeholders are filled with actual data
- [ ] No grid/blueprint/catalog/turn-around sheet language
- [ ] No detailed per-field face/hair/body/wardrobe appearance descriptions (appearance is carried by reference image or auto-derived by GPT Image)
- [ ] Background: "Pure white / soft off-white"
- [ ] Layout rules include "asymmetric", "large negative space", "no overlapping", "no merging poses"
- [ ] Identity lock covers structure + proportions + hair + wardrobe + silhouette + visual DNA
- [ ] Silhouette study zone (2-4 simplified black silhouettes) present
- [ ] Expression study zone present
- [ ] Detail study zone present
- [ ] Text block: Name / Role / Core Mood / Visual Signature only — four fields
- [ ] No --ar / --style / --v parameters

---

## Integration

Invoked by `director-core` or independently after STATE 3:

1. Extract key fields from `director-character` (Name / Role / Core Mood / Keywords)
2. Obtain project context from user (type / emotional tone)
3. Confirm whether a reference image is available
4. Derive visual direction → fill the universal template → output the GPT Image prompt
5. User pastes into GPT Image → generates CHARACTER IDENTITY BOARD image
6. Generated image serves as `@[character ref]` for STATE 6 `seedance-video-prompt`
