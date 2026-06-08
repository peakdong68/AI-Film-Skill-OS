---
name: seedance-20
description: "This skill should be used when directing Seedance 2.0 T2V, I2V, V2V, R2V, audio, safety, or API work."
license: MIT
user-invocable: true
tags: [seedance]
metadata:
  version: "5.4.5"
---

# seedance-20

Seedance 2.0 operating loop for agent-directed video work. Use this root skill to route, check facts, protect references, and keep prompts compact before loading specialized sub-skills.

## Operating Loop

1. Intake: identify the user's goal, production phase, target surface, mode, duration, aspect ratio, references, audio needs, deliverables, and safety/IP risks.
2. Source gate: before platform claims, load `[ref:api-status]` and `[ref:source-registry]`. For Runway or Volcengine specifics, also load `[ref:platform-surface-matrix]`.
3. Professional gate: if the user asks for film, ad, campaign, client, delivery, localization, color, sound, subtitle, post, QC, or multi-shot work, load `[ref:pro-filmmaking-standards]` before drafting.
4. Mode gate: choose T2V, I2V, V2V, R2V, FLF2V, edit, extend, or troubleshoot before writing prose.
5. Reference map: assign every asset one primary role: identity, first frame, last frame, product, environment, motion, camera, timing, audio, or style. State what must not transfer.
6. Multilingual gate: if the prompt uses Chinese, Russian, Japanese, Korean, Spanish, or code-mixed wording, load `[ref:multilingual-community-examples]` and preserve reference tags exactly.
7. Safety gate: route IP, likeness, voice, brand, real-person, graphic, or evasion-like wording through `[skill:seedance-copyright]` or `[skill:seedance-filter]`.
8. Prompt build: route to `[skill:seedance-interview]`, `[skill:seedance-prompt]`, `[skill:seedance-prompt-short]`, or a domain skill for camera, motion, audio, characters, VFX, style, recipes, or pipeline.
9. Quality pass: run anti-slop, check one visible beat, one primary camera move, physical light, sound intent, continuity anchors, constraints, delivery caveats, and source-date caveats.
10. Repair loop: if output fails, diagnose root cause before adding adjectives; use `[skill:seedance-troubleshoot]`.

## Load Map

| Situation | Load |
|---|---|
| Vague idea or missing brief | `[skill:seedance-interview]` or `[skill:seedance-interview-short]` |
| Production prompt | `[skill:seedance-prompt]`, `[ref:quick-ref]`, `[ref:prompt-examples]` |
| Professional film, commercial, campaign, or delivery workflow | `[ref:pro-filmmaking-standards]`, `[ref:shot-list-continuity]`, `[ref:delivery-qc]` |
| Compact prompt or Chinese compression | `[skill:seedance-prompt-short]`, language vocab reference |
| Camera, lens, blocking, shot contract | `[skill:seedance-camera]`, `[ref:cinematography-shot-language]` |
| Image reference / first frame | `[ref:i2v-guide]`, `[ref:reference-workflow]` |
| First and last frame | `[ref:first-last-frame-guide]` |
| API, Runway, Volcengine, workflow, pricing, model IDs | `[skill:seedance-pipeline]`, `[ref:api-workflow]`, `[ref:model-name-map]` |
| Color, ACES, HDR/SDR, aspect ratio, subtitles, audio post, or QC | `[ref:color-pipeline-aces]`, `[ref:aspect-ratio-delivery]`, `[ref:subtitles-localization]`, `[ref:audio-post-delivery]`, `[ref:delivery-qc]` |
| Genre template or examples | `[skill:seedance-recipes]`, `[ref:examples-by-mode]`, `[ref:genre-guides]` |
| Chinese/Russian/Japanese/Korean/Spanish or mixed-language examples | `[ref:multilingual-community-examples]`, language vocab reference |
| Bad result | `[skill:seedance-troubleshoot]` |

## Routing Convention

The `[ref:X]` and `[skill:Y]` markers in this skill are **plain relative-path shorthands** resolved from the skill root (the directory containing this SKILL.md). There is no special parser or tag system — treat them as short aliases for the corresponding file paths.

```
[ref:X]        →  references/X.md
[ref:X/Y]      →  references/X/Y.md        (subdirectory: vocab, migrated, etc.)
[skill:Y]      →  skills/Y/SKILL.md
```

| Marker | Resolves to |
|---|---|
| `[ref:api-status]` | `references/api-status.md` |
| `[ref:vocab/zh]` | `references/vocab/zh.md` |
| `[ref:quick-ref]` | `references/quick-ref.md` |
| `[skill:seedance-camera]` | `skills/seedance-camera/SKILL.md` |
| `[skill:seedance-prompt]` | `skills/seedance-prompt/SKILL.md` |

**Rules:**
- Every `[ref:X]` looks for `references/X.md` relative to the skill root.
- Every `[skill:Y]` looks for `skills/Y/SKILL.md` relative to the skill root.
- When creating new references or sub-skills, follow this pattern: place the file where the marker says, and the routing resolves automatically.
- Sub-skills may load their own references — those resolve relative to that sub-skill's directory (e.g., `[ref:vocab/zh]` inside `skills/seedance-vocab-zh/SKILL.md` looks for `skills/seedance-vocab-zh/references/vocab/zh.md`).

Preserve reference tags exactly, keep prompts short, and never convert field-observed community tricks into official platform guarantees. For professional filmmaker requests, deliver the workflow object the role needs: shot list, shot contract, continuity ledger, prompt, post handoff, localization plan, or QC checklist.
