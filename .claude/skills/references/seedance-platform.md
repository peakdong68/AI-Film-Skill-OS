# Seedance 2.0 Platform Constraints — Shared Reference

## Prompt Word Count Limits

Each Seedance 2.0 prompt corresponds to one Part (≤ 15s), counted independently.

| Language | Limit (per prompt) | Rationale |
|------|------|------|
| **Chinese** | ≤ 500 characters | Excess characters scatter info; model ignores details |
| **English** | ≤ 1000 words | Same as above |
| **Total characters** | ≤ 2000 characters | Platform budget |

Multi-Part projects: one prompt per Part, each counted independently.

## Reference Format

Seedance 2.0 uses `` `ImageN` `` / `` `VideoN` `` / `` `AudioN` `` format to reference uploaded assets. Upload assets in order, reference by sequence number.

| Reference Example | Purpose |
|---------|------|
| `` `Image1` `` `` `Image2` `` | Character anchoring, scene setting, product locking, first/last frame |
| `` `Video1` `` | Camera reference, motion reference, VFX reference, edit/extend source |
| `` `Audio1` `` | Rhythm/atmosphere, voice tone reference |

**Edit/Extend tasks:** Use `` `VideoN` `` directly. NEVER add "reference" prefix, which causes task misclassification.

## Subject Definition

Explicitly define subjects in reference assets using 2-3 clear, stable features for unique identification.

- Basic: `` Define [features] in `Image1` as `Subject1` ``
- Shorthand: `` `Subject1`@`Image1` ``
- Face close-up separation (recommended): `` `Subject1`'s facial features reference `Image1` (headshot), styling references `Image2` (full-body) ``

## Stable Constraints

- Seedance 2.0 surface behavior varies; do not assume uniformity.
- Do not assume API access, pricing, model IDs, region limits, upload quotas, duration, or likeness authorization from memory.
- Do not infer permission from unauthorized uploaded images/voice/video.
- Do not provide instructions for protected characters, celebrities, brand logos, song reproductions, exact scene copies, or voice imitation.
- Each Part ≤ 15 seconds (Seedance single-generation limit).
- Part 2+ must use the previous Part's output video as a continuity anchor.
- Recommended asset configuration: 4-5 assets total (1-2 character images + 1 scene image + 1 camera video + 1 audio clip). Avoid maxing out the asset limit.
- Multi-Part splice point guidance: trim 6 frames from previous clip end + 1 frame from next clip start to reduce jump cuts.

## Surface-Specific Constraints

When users mention specific platforms (Jimeng, Kling, Volcengine Ark, Runway, etc.), label responses with platform name and date. Community/unofficial tools must be clearly marked.
