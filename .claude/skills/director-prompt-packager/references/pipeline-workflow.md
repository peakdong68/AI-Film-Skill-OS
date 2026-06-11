# Seedance Production Pipeline Workflow — Bundled Reference Knowledge

Provides `director-prompt-packager` with Seedance production pipeline knowledge.

## Professional Production Workflow

1. **Brief:** Define client/creative goals, audience, region, duration, aspect ratio, deliverables, reference assets, rights, approval owner, and hard constraints.
2. **Pre-production:** Create treatment, reference mapping, shot list, continuity ledger, color/audio/localization intent, and risk log.
3. **Generation plan:** Break into stable clips. Each Seedance clip gets one visible beat, one camera concept, and one endpoint.
4. **Review loop:** Evaluate identity, product, motion, camera, continuity, audio sync, text, safety, and rights before extending or editing.
5. **Post plan:** Edit, composite, stabilize, sound, color, captions, versioning, textless, and archive metadata.
6. **Delivery/QC:** Check spec, naming, frame rate, resolution, color pipeline, loudness, captions, safe areas, rights notes, and human review.

## Workflow Split

| Workflow | Description |
|--------|------|
| Web workflow | Jimeng/Kling frontend, upload references, enter prompts, review output |
| API workflow | Volcengine/BytePlus/Runway, model ID, auth, file handling, task lifecycle |
| Professional production | Treatment, shot list, continuity ledger, reference rights map, review loop, post handoff |
| Post workflow | Edit, composite, stitch, stabilize, audio cleanup, captions, color, localization, versioning |
| First/last-frame | Map first frame, last frame, transition action, identity locks, ending target |
| Extend workflow | Continue from existing final state, using last frame as continuity anchor |

## Continuity Rules

- Each Part ≤ 15 seconds (Seedance single-generation maximum).
- Part 1 establishes world baseline: character identity, wardrobe, environment, lighting logic, camera language.
- Part 2+ must reference the previous video output as a continuity anchor.
- Forward pass: character identity, wardrobe, environment, lighting logic, camera language.
- Emotion evolves, never resets — continue from the previous Part's endpoint.

## Multi-Part Continuity Template

```
Part 1: Establish world baseline + character + visual language
Part 2: Reference Part 1 video → continue same character/wardrobe/space/lighting/camera → emotion continues from endpoint
Part N: Reference Part N-1 video → narrative advance → resolution
```

## Deliverable Packaging Checklist

- Complete Seedance 2.0 prompts (in execution order)
- Image reference-to-role mapping (which reference asset corresponds to which image)
- Multi-Part generation context continuity notes
- Delivery format notes (duration, aspect ratio, platform)
