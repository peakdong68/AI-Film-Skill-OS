---
name: storyboard-ecommerce
description: Generate professional e-commerce / livestream / social commerce storyboard prompts for AI image generators (Midjourney, Flux, 即梦, 可灵, GPT Image). Use when the user asks for an e-commerce storyboard, 带货视频故事板, 电商分镜, TikTok shopping video storyboard, livestream shot plan, 直播分镜, product showcase board, 产品展示分镜, fashion lookbook storyboard, 服装分镜, or any commerce-oriented video planning board that needs product reference areas, creator reference areas, and subtitle-safe shot breakdowns.
---

# Storyboard E-Commerce

## Overview

Generate professional e-commerce and social commerce storyboard prompts for AI image generators. Unlike general film storyboards, e-commerce boards require product consistency areas, creator/host reference zones, subtitle-safe framing, and commerce-oriented shot structures (Hook → Problem → Reveal → Detail → Display → CTA).

Use this skill for commerce/livestream/social shopping storyboards. For general film/animation storyboard prompts, use `storyboard-prompt`. For non-commerce master sheets, use `storyboard-master`. For Seedance I2V planning, use `storyboard-sketch`.


## Load Resources

For anti-slop lexicon replacement when writing prompts, read shared reference `../references/anti-slop-lexicon.md`.

## Sub-Mode Gate

This skill supports two commerce-specific formats. Choose automatically:

| User says... | Output format |
|---|---|
| "带货视频故事板", "TK storyboard", "TikTok shop video", "短视频带货", product demo with host/creator visible | **Social Commerce Board** (product ref + creator ref + 6-shot breakdown) |
| "服装分镜", "fashion storyboard", "电商直播分镜", "导演版分镜图", fashion/apparel with model, no talking-head host | **Fashion Director Board** (shot grid + rhythm + camera + lighting modules) |

---

## Format A: Social Commerce Board (Shopping Video Board)

For TikTok/Reels/Shorts-style product videos where a creator/host presents a product. Derived from the TK English AI Video Storyboard template.

### Layout Structure

```
┌──────────────────────────────────────────────┐
│              Top Info Bar                     │
│  Product | Audience | Selling Point | ...    │
├──────────────────┬───────────────────────────┤
│ Creator Ref (L)  │  Product Ref (R)          │
│ 3 ref images     │  3 ref images             │
├──────────────────┴───────────────────────────┤
│        6-Shot AI Video Storyboard            │
│  Shot 01 │ Shot 02 │ Shot 03 │ ... │ Shot 06│
│  [card]  │ [card]  │ [card]  │     │ [card]  │
└──────────────────────────────────────────────┘
```

Aspect ratio: 4:3 or 16:9. White background. Black thin borders. Clean grid layout. Readable English text. High information density without clutter.

### Top Info Bar

A horizontal table row with 6 information cells:

| Cell | Content |
|------|---------|
| **Product** | Product name from user input |
| **Audience** | Target audience (e.g., anime fans, desk setup lovers, collectors) |
| **Core Selling Point** | One-line value proposition |
| **Hook** | Opening hook line |
| **Video Goal** | Structure flow (e.g., Hook → Problem → Reveal → Detail → Display → CTA) |
| **Format** | Platform / aspect ratio / duration / language |

### Creator Reference Area (Left)

Title: **Creator Reference**

Three small reference images of the same creator, demonstrating visual consistency:

| # | Image | Label |
|---|-------|-------|
| 1 | Front half-body shot | Front half-body |
| 2 | Expression close-up | Expression close-up |
| 3 | Side half-body shot | Side half-body |

Requirements:
- Same person in all three — face shape, hairstyle, outfit, skin tone, and vibe must be consistent.
- Looks like a real TikTok/Short-form video creator.
- Background can suggest home desk setup, livestream room, or product-use environment.
- Each image has an English label below it.

### Product Reference Area (Right)

Title: **Product Reference**

Three small reference images of the same product:

| # | Image | Label |
|---|-------|-------|
| 1 | Packaging box | Packaging box |
| 2 | Front view | Front view |
| 3 | Side/detail view | Side/detail view |

Requirements:
- Product must be strictly consistent across all three — color, shape, material, packaging, logos, base, key details.
- If the user's product has no packaging box, generate one matching the product style — but do not alter the product itself.
- Clean, centered, e-commerce style product photography.
- Each image has an English label below it.

### 6-Shot Breakdown

Title: **6-Shot AI Video Storyboard** or **6-Shot TikTok Video Breakdown**

Each shot card contains:

```
┌─────────────────────────────┐
│     Shot 01: Hook           │  ← shot title
│                             │
│   [Keyframe Preview]        │  ← visual frame
│                             │
│ Time: 0–2s                  │
│ Shot type: Medium close-up  │
│ Action: [one line]          │
│ Camera: [one line]          │
│ Subtitle/Line: "[script]"   │
└─────────────────────────────┘
```

### Default 6-Shot Structure

If the user doesn't provide a custom shot list, use this proven commerce structure:

**Shot 01: Hook**
- Frame: Creator shows packaging or product reveal, facing camera, attention-grabbing expression.
- Time: 0–2s
- Shot type: Medium close-up
- Action: Creator pushes the product toward camera or reveals it dramatically
- Camera: Fast push-in
- Subtitle: Catchy one-liner that hooks the viewer

**Shot 02: Problem**
- Frame: Show the problem or gap in the use scenario — empty desk, lack of atmosphere, common pain point.
- Time: 2–4s
- Shot type: Medium
- Action: Creator gestures to the empty/problematic space
- Camera: Quick side move
- Subtitle: Question that resonates with the audience's pain point

**Shot 03: Reveal**
- Frame: Creator places product in the scene, becoming the visual center.
- Time: 4–6s
- Shot type: Product medium close-up
- Action: Creator sets the product in position
- Camera: Gentle push-in
- Subtitle: Declaration of the product as solution

**Shot 04: Detail**
- Frame: Close-up of product details — material, texture, finish, key features. Hands may assist but not block.
- Time: 6–8s
- Shot type: Close-up
- Action: Show hair, sculpt, paint, texture, or base details
- Camera: Detail push-in
- Subtitle: Statement about quality or craftsmanship

**Shot 05: Display**
- Frame: Product in real use environment — on desk, shelf, or in situ. Creator admires or interacts.
- Time: 8–10s
- Shot type: Medium
- Action: Product displayed in lifestyle setting
- Camera: Slow lateral move
- Subtitle: Lifestyle benefit statement

**Shot 06: CTA**
- Frame: Creator and product together. Creator naturally recommends. Product clearly visible.
- Time: 10–12s
- Shot type: Medium close-up
- Action: Creator points to product and recommends
- Camera: Hold on product
- Subtitle: Call to action or purchase prompt

### Continuity Requirements (Social Commerce Board)

These must be verified for every board:

- [ ] Same creator in all shots — hairstyle, outfit, face shape, complexion, vibe consistent.
- [ ] Same product in all shots — color, shape, packaging, base, key details unchanged.
- [ ] Scene style unified across shots — same lighting direction, background style, color palette.
- [ ] Clear action progression — not just repeated posing.
- [ ] Subtitle-safe framing — bottom 20% of each frame kept clear for text overlay.
- [ ] All 6 shots map to the script rhythm — no orphan shots that don't serve the flow.

### Visual Style Requirements

```
clean commercial storyboard, professional production board, TikTok AI video planning sheet, white background, black thin borders, neat grid layout, infographic style, readable English text, high information density, practical structured layout, subtitle-safe framing
```

Do NOT generate: poster style, film concept art, decorative PPT, cyberpunk, over-designed ad, cluttered e-commerce collage, unreadable small text, garbled text, multiple different creator identities, inconsistent product appearance.

---

## Format B: Fashion Director Board (Fashion E-commerce Livestream Storyboard)

For fashion/apparel/lookbook-style shoots where a model showcases clothing without talking-head hosting. Derived from the fashion livestream director storyboard template.

### Layout Structure

```
┌─────────────────────────────────────┐
│   Shot Grid (3 rows × 4-5 columns)  │
│   12-15 individual shot cards       │
├─────────────────────────────────────┤
│ Rhythm  │ Camera   │ Lighting &     │
│ Struct  │ Movement │ Atmosphere     │
└─────────────────────────────────────┘
```

Aspect ratio: 16:9. White or light gray background. Clean director storyboard style. Professional commercial feel.

### Shot Card Format

Each shot card follows a strict unified structure:

```
┌──────────────────────────┐
│ 01 | LS (Full Shot) | 0:00-0:02 │  ← gray header bar
│                          │
│   [Cinematic Preview]    │  ← realistic fashion shot preview
│                          │
│ Natural entrance, establish character presence │  ← director note in Chinese
└──────────────────────────┘
```

Header format: `Shot # | Shot Size Abbrev | Timecode`

Director note rules:
- ≤15 characters in Chinese
- Reads like an on-set director's margin note
- Describes the core visual moment, not abstract concepts
- Examples: Adjust hem to highlight silhouette / 45° side angle to show structure / Push-in to reveal print detail

### Bottom Module 1: Rhythm Structure (Rhythm Structure Diagram)

Title: **Rhythm Structure (XX seconds / Beat-Synced Edit)**

Content organized by music phases:

```
| 0–5s   | Setup & Establish | Kick / Snare          |
| 5–10s  | Motion Display   | Rhythm groove         |
| 10–15s | Fit & Detail     | Melody build          |
| 15–20s | Closing Emphasis | Drop / Bass           |
```

Add a waveform graphic showing intensity, with shot numbers (①②③...) marking time points.

### Bottom Module 2: Camera Movement Diagram (Camera Movement Diagram)

Title: **Camera Movement Diagram (Reference)**

Top-down spatial plan with:
- Numbered camera positions (①→③→④→⑥→⑧→⑩→⑫)
- Dashed trajectory arrows
- Movement type labels: Slow Push-in / Lateral Track / Semi-Orbit / Static Hold / Push-in / Pull-back

### Bottom Module 3: Lighting & Atmosphere (Lighting & Atmosphere)

Title: **Lighting & Atmosphere (Consistent with Reference)**

Checklist format:
```
✓ Warm key light from front-left
✓ Soft fill light
✓ Rim light from rear-right
✓ Clean, transparent walls
✓ Warm white space
✓ Soft depth of field
```

Keywords: Trendy / Street / Premium / Relaxed / Texture

### Replaceable Zone (Replaceable Zone)

This is the only area the user needs to customize per project. Keep the rest of the structure fixed.

```
【Scene】[location description, lighting environment, set details]
【Model】[single model: gender, age range, hairstyle, accessories, outfit style, expression]
【Product】[garment: color, wash, fit, print pattern, collar, cuffs, length, hem, fabric texture, proportions]
【Shot Actions】[list of key movements: Natural walk-in / Adjust hem / Pull cuff / 45° side angle / Frontal stance / Slight head tilt]
```

### Visual Style Requirements (Fashion Director Board)

```
Director treatment board, commercial ad director storyboard, e-commerce fashion ad storyboard, professional camera language, clear information hierarchy, clean layout, strong premium feel, authentic photography feel, white or light gray background
```

Do NOT generate: illustration style, poster style, comic style, UI interface style. Must look like a real director storyboard pitch deck.

---

## Output Format

For both sub-modes, present the structured plan first, then the compressed image generator prompt.

```markdown
## Storyboard Plan: [product name]

### Format: [Social Commerce / Fashion Director]

[Full structured breakdown matching the chosen format above]

## Compressed Prompt

[One complete prompt for the image generator. Include all layout instructions, style keywords, and the anti-pattern list.]
```

## Quality Bar

- All reference images (creator + product for social commerce) must maintain strict identity consistency.
- Shot cards must include all required fields: number, shot type, timecode, preview, action, camera, and (for social commerce) subtitle line.
- The rhythm module must map time segments to shot numbers and music beats.
- Visual style keywords must clearly describe the board format — not the video content.
- Subtitle-safe framing must be mentioned for social commerce boards.
- If the user provides product/creator reference images, preserve their visual identity exactly — do not invent variations.
- Anti-pattern list must be included in the compressed prompt to prevent common AI image generator drift into poster/concept art styles.
