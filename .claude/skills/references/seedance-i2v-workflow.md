# Seedance I2V Workflow — Bundled Reference Knowledge

Provides `storyboard-sketch` with Seedance image-to-video (I2V) specific storyboard planning knowledge.

## Seedance Operation Modes

| Mode | Compilation Priority | Common Mistake | Fix |
|------|---------|---------|------|
| **T2V** | Build the whole shot in compact layers | Too many events in one clip | Keep one visible beat + one endpoint |
| **I2V** | Preserve visible identity; add motion | Re-describing the image until product or face drifts | Write `preserve @[image1] strictly`; only add dynamic changes |
| **R2V** | Assign separate roles to each asset | One asset asked to control identity, pose, scene, and style | Split roles or prioritize the most important role |

## Seedance I2V Core Principle

**Only describe what the image cannot show.** A still image already contains subject identity, product form, wardrobe, palette, composition, and background. Re-describing these static details typically causes drift. Only add to the image: motion, camera, timing, lighting change, sound, and preservation constraints.

## I2V Storyboard Planning

Follow Seedance operation modes:

1. **Intake first:** Clarify goal, duration, aspect ratio, reference assets, deliverables.
2. **Mode gate:** Assume I2V planning unless user says T2V, V2V, R2V, edit, or extend.
3. **Reference asset mapping:** If assets exist, assign a role to each (identity, first frame, environment, motion, camera, timing, style). State what should not transfer.
4. **Long video logic:** For videos over 15 seconds, generate a storyboard plan and note that final Seedance generation should split into multiple Parts.
5. **Storyboard board input:** If user provides a multi-panel board, ≤4 panels for one timestamped Seedance prompt, ≥5 panels for per-shot prompts with editing rhythm.

## I2V Motion Note Specifications

Include one motion note per frame:

- **Camera motion:** static hold, slow push-in, lateral track, gentle tilt, handheld drift.
- **Subject motion:** turn, step, reach, glance, pause, reveal, react.
- **Transition logic:** match action, eye-line match, push through foreground, cut on gesture.
- **Avoid:** one frame containing multiple temporally separated actions.

## Common I2V Failure Fixes

| Failure | Fix |
|------|------|
| Identity drifts | Reduce new visual description, strengthen preservation constraints |
| Camera jumps | Use one camera movement, note start and end frames |
| Product warps | Declare `preserved, static identity, no shape change` |
| Output is static | Add one physical action and one timing cue |
| Background changes | Preserve environment layout, animate only light/weather/atmosphere |
| Hands deform | Simplify hand motion or keep hands outside the main action |
