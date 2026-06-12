---
name: storyboard-ecommerce
description: 'Generate e-commerce/livestream/shopping storyboard prompts for AI image generators (Midjourney, Flux, Jimeng, Kling, GPT Image) — 3 formats (Social Commerce / Fashion Director / Product Showcase) auto-selected with product reference areas, creator reference areas, and subtitle-safe framing. Triggers: shopping video, 带货视频, 电商分镜, TikTok shop, 直播分镜, product showcase, 服装分镜. Note: non-commerce → `storyboard-master` or `storyboard-prompt`.'
---

# Storyboard E-Commerce

## Overview

Generate professional e-commerce and social commerce storyboard prompts for AI image generators. Unlike standard film storyboards, e-commerce boards need product reference areas, subtitle-safe framing, and commerce-oriented shot structure. Covers three commerce scenarios: host-led social selling, model fashion showcase, and pure product display.

此技能用于商业/直播/社交购物类分镜。普通电影/动画分镜请用 `storyboard-prompt`。非电商总览图请用 `storyboard-master`。Seedance I2V 规划请用 `storyboard-sketch`。

## Load Resources

- Full format specs (layout, shot breakdown, visual style, continuity) → `references/ecommerce-formats.md`
- Anti-slop replacement → `../references/anti-slop-lexicon.md`
- Cinematography quick reference → `../references/cinematography-quick-reference.md`
- Product and commerce genre recipes → `../references/seedance-genre-recipes.md`

## Context Probe (Required for Standalone Use)

After loading, probe available context to determine material sources and format selection basis:

**1. Check pipeline state:** Read `STATE.md`. If it exists, retrieve product/creator material slots.

**2. Scan project files and user assets:** Probe for available reference resources:

| If found...                           | Then...                                                              |
| ------------------------------------- | -------------------------------------------------------------------- |
| User uploaded product images          | Map to `@[image1]` (product reference area)                          |
| User uploaded creator/model images    | Map to `@[image2]` (creator reference area, Format A)                |
| User uploaded scene/background images | Map to `@[image3]` (scene reference area, Format C)                  |
| `outputs/character-sheets.md`         | If a creator character exists, extract design and map to `@[imageN]` |
| `outputs/State-4-prompt-package.md`   | Extract product info and shot design plan                            |

**3. Auto-infer format:** Infer the best commerce format (Format A/B/C) based on available assets, reducing user selection burden.

**4. No context fallback:** Select format based on user's direct product description.

---

## Sub-Mode Gate

> **This skill is NOT auto-selected.** Only execute when explicitly routed by `director-core` STATE 5 or the user explicitly requests e-commerce storyboard. Do not trigger in any default flow.

Three commerce formats, selected by scenario:

| User scenario                                          | Format                               | Characteristics                                                                                      |
| ------------------------------------------------------ | ------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Social selling, TK/Reels/Shorts, host presents product | **Format A: Social Commerce Board**  | Product ref + Creator ref + 6-shot (Hook→Problem→Reveal→Detail→Display→CTA) + subtitle line          |
| Fashion/apparel/lookbook, model showcase, no host      | **Format B: Fashion Director Board** | 12-15 shot grid + rhythm + camera + lighting modules                                                 |
| Pure product display, 3C/home/food/beauty, no people   | **Format C: Product Showcase Board** | Product ref + Scene ref + 6-shot (Showcase→Detail→Feature→Use→Atmosphere→Packshot), no subtitle line |

> Full layout structures, shot card specs, default breakdowns, continuity requirements, and visual style keywords → `references/ecommerce-formats.md`

### Format A: Social Commerce Board (Summary)

TikTok-style social selling with host/creator on camera. Dual reference area (creator + product), 6-shot Hook→Problem→Reveal→Detail→Display→CTA structure, subtitle line per shot. Aspect ratio 4:3 or 16:9.

### Format B: Fashion Director Board (Summary)

Fashion/apparel showcase with model, no host. Three-layer layout (12-15 shot grid + rhythm + camera + lighting), director notes ≤15 chars. Replaceable Zone is the only customizable area. Aspect ratio 16:9.

### Format C: Product Showcase Board (Summary)

Pure product display, no people on screen. Dual reference area (product + scene), 6-shot Showcase→Detail→Feature→Use→Atmosphere→Packshot structure, no subtitle line. For 3C/home/food/beauty and other non-apparel categories. Aspect ratio 16:9.

## Output Format

Present structured plan first, then compressed image generator prompt:

```markdown
## Storyboard Plan: [产品名称]

### Format: [Social Commerce / Fashion Director / Product Showcase]

[Complete structured breakdown matching the selected format]

## Compressed Prompt

[One complete image generator prompt with all layout instructions, style keywords, and anti-pattern checklist.]
```

## Language Rules (Hard Constraint)

> Whatever language the user speaks, the plan speaks it too. The compressed prompt can be bilingual but descriptions match the plan.

- **Plan sections**: Use the user's project language. Chinese project = Chinese plan, English project = English plan. Never mix.
- **Compressed prompt**: Use the AI image generator's preferred language (English typically gives more stable results), but shot/scene descriptions must use the plan language.
- **Style keywords**: Always English, regardless of plan language. Keywords only — nouns and adjective phrases, not full sentences.

**Wrong (Chinese project):**
```
Frame: Boy sitting on grass, golden hour lighting.
Camera: Medium shot, eye-level, static.
```

**Correct (Chinese project):**
```
镜头：男孩坐在草地上，落日逆光。
摄影机：中景，平视，固定镜头。
```

**Correct compressed prompt (Chinese project):**
```
A boy sitting on grass at golden hour, backlit by warm sunset.
男孩坐在草地上，缓慢抠开面包包装。中景，平视，固定镜头。
```

## Quality Bar

**Cross-format general rules:**

- All reference subjects (creator/model/product) must maintain strict identity consistency — never invent variants
- Shot cards must contain all required fields: number, shot size, timecode, preview, action, camera
- Visual style keywords must clearly describe board format — not video content
- Compressed prompt must include anti-pattern checklist to prevent AI image generator drift to poster/concept art style
- If user provides product/creator reference images, preserve their visual identity exactly
- **When reference images exist, do not enumerate subject appearance details (face, hairstyle, body type, wardrobe) in the Replaceable Zone or Compressed Prompt.** The reference image already locks visual identity — only slot references + 1-2 identifiers are needed. Re-enumerating details already in the image causes the generation model to reinterpret rather than directly reference.
- Reference materials use `@[imageN]` format

**Format-specific rules:**

- Format A: Subtitle-safe framing (bottom 20% reserved per frame) + creator continuity
- Format B: Rhythm module must map time segments to shot numbers and music beats
- Format C: No people on screen — if hands appear, maintain consistent skin tone/gesture style

## Save Output

After delivering the final output, prompt the user to save with a dated, topic-specific filename:

```
Save to outputs/F-[N]-[topic]-ecommerce-board.md?
Example: outputs/F-1-cyberpunk-short-seedance-prompt.md
```

If the user confirms, write the output to the specified path.
