---
name: storyboard-ecommerce
description: "Generate e-commerce/livestream/shopping storyboard prompts for AI image generators (Midjourney, Flux, Jimeng, Kling, GPT Image) — 3 formats (Social Commerce / Fashion Director / Product Showcase) auto-selected with product reference areas, creator reference areas, and subtitle-safe framing. Triggers: shopping video, 带货视频, 电商分镜, TikTok shop, 直播分镜, product showcase, 服装分镜. Note: non-commerce → `storyboard-master` or `storyboard-prompt`."
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

## Sub-Mode Gate

> **This skill is NOT auto-selected.** Only execute when explicitly routed by `director-core` STATE 5 or the user explicitly requests e-commerce storyboard. Do not trigger in any default flow.

Three commerce formats, selected by scenario:

| User scenario | Format | Characteristics |
|---|---|---|
| Social selling, TK/Reels/Shorts, host presents product | **Format A: Social Commerce Board** | Product ref + Creator ref + 6-shot (Hook→Problem→Reveal→Detail→Display→CTA) + subtitle line |
| Fashion/apparel/lookbook, model showcase, no host | **Format B: Fashion Director Board** | 12-15 shot grid + rhythm + camera + lighting modules |
| Pure product display, 3C/home/food/beauty, no people | **Format C: Product Showcase Board** | Product ref + Scene ref + 6-shot (Showcase→Detail→Feature→Use→Atmosphere→Packshot), no subtitle line |

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

## Quality Bar

**Cross-format general rules:**

- All reference subjects (creator/model/product) must maintain strict identity consistency — never invent variants
- Shot cards must contain all required fields: number, shot size, timecode, preview, action, camera
- Visual style keywords must clearly describe board format — not video content
- Compressed prompt must include anti-pattern checklist to prevent AI image generator drift to poster/concept art style
- If user provides product/creator reference images, preserve their visual identity exactly

**Format-specific rules:**

- Format A: Subtitle-safe framing (bottom 20% reserved per frame) + creator continuity
- Format B: Rhythm module must map time segments to shot numbers and music beats
- Format C: No people on screen — if hands appear, maintain consistent skin tone/gesture style


## Save Output

After delivering the final output, prompt the user to save with a dated, topic-specific filename:

```
Save to outputs/YYYY-MM-DD-[topic]-ecommerce-board.md?
Example: outputs/2026-06-10-cyberpunk-short-seedance-prompt.md
```

If the user confirms, write the output to the specified path.
