# Seedance 2.0 Platform Constraints — Shared Reference Knowledge

## Prompt Word Count Limits

| Language | Limit | Rationale |
|------|------|------|
| **Chinese** | ≤ 500 characters | Excessive word count scatters information; model ignores details |
| **English** | ≤ 1000 words | Same as above |
| **Total characters** | ≤ 2000 characters | seedance-prompt platform budget |

**Violating this constraint causes missing elements, character drift, and incomplete motion.** Always count and annotate word count after compilation.

## @[ref] Reference Format

All uploaded image/video/audio assets use the `@[description]` format:

| Reference Example | Purpose |
|---------|------|
| `@[storyboard image 1]` | Storyboard blueprint — motion planning reference |
| `@[character image 1]` | Character identity lock — face, hairstyle, body type |
| `@[product image 1]` | Product lock — color, print pattern, silhouette |
| `@[background image 1]` | Environment lock — spatial structure, light, color tone |
| `@[audio 1]` | Rhythm and energy — do not copy protected sounds/songs |

## Stability Constraints

- Different Seedance 2.0 surfaces may have different capabilities; do not assume uniformity.
- Do not assume API access, pricing, model IDs, region restrictions, upload limits, duration, or likeness authorization from memory.
- Do not infer permission from unauthorized uploaded images/voice/video.
- Do not provide instructions for protected characters, celebrities, brand logos, song reproductions, exact scene replicas, or voice imitation.
- Each Part ≤ 15 seconds (Seedance single-generation maximum).
- Part 2+ must use the previous video output as a continuity anchor.

## Surface-Specific Constraints

When users mention specific platforms (Jimeng, Kling, Volcengine Ark, Runway, etc.), annotate the response with platform name and date. Label community/unofficial tools explicitly.
