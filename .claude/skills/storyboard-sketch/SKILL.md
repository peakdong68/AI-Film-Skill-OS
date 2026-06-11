---
name: storyboard-sketch
description: "Generate text-level per-frame I2V storyboard sketch descriptions for Seedance — no images, only motion/camera/lighting/sound text per frame. Use for I2V frame planning, per-frame motion descriptions, animatic sketches, or script-to-frame-sequence breakdown. Triggers: I2V storyboard, per-frame motion, animatic sketch, first-frame prompt. Note: for multi-shot image boards use `storyboard-master`; for single-frame image prompts use `storyboard-prompt`; for commerce boards use `storyboard-ecommerce`."
---

# Seedance Storyboard Sketch

## Overview

Turn a scene idea, script, or concept into a storyboard plan for Seedance image-to-video. This skill supports two output modes, selected automatically by the Mode Gate below:

- **Compact Frame Prompts** (default): 3-8 concise rough-sketch frame prompts optimized for Seedance I2V seed images.
- **Storyboard Master Sheet** (on request): For 4-section overview boards (Shot Grid + Rhythm + Camera + Visual Language), use `storyboard-master` skill.

Favor clarity, continuity, and sketchability over polished cinematic prose in both modes.

## Mode Selection Gate

Before generating output, decide which mode to use:

| If the user says... | Use this mode |
|---|---|
| "storyboard sketch", "keyframe prompts", "rough frame prompts", "I2V storyboard", "shot-by-shot prompts", "quick preview board", "rough visual frames", or any Seedance-focused prompt request | **Compact Frame Prompts** |
| "storyboard master sheet", "Master Sheet", "director storyboard board", "shot list board", "director treatment board", "storyboard planning board", "complete storyboard plan", or explicitly asks for a full visual planning layout | **Storyboard Master Sheet** |

When the user provides a multi-panel board image: identify whether it's ≤4 panels (treat as Compact Frame Prompts) or ≥5 panels (treat as source for Master Sheet structure).

When uncertain, default to Compact Frame Prompts but mention the Master Sheet option briefly.

---

# Mode A: Compact Frame Prompts

## Workflow

1. Run the Input Gate before writing any frame prompts.
2. Identify the scene goal, characters, location, emotional beat, references, target mode, aspect ratio, and intended output length.
3. Convert the idea or script into a compact storyboard plan: 3-8 frames unless the user specifies a count.
4. For each frame, define one readable visual moment including: subject, action, composition, camera angle, lighting mood, story purpose, and continuity notes.
5. Write each frame as a rough sketch prompt, not a final video prompt.
6. Add a short Seedance I2V note for how the frame should animate into the next moment.

Ask one concise question only when missing information would materially change the board, such as the target aspect ratio, number of frames, or whether the board should be realistic, anime, ad-like, or cinematic.

## Input Gate

Before generating storyboard sketch prompts, decide whether the user has already provided enough scene material to convert into a compact storyboard plan.

Treat the input as sufficient when it includes at least:

- A core scene idea, script, beat list, or image/video reference.
- A subject or character.
- A situation, location, or action.
- A desired use, such as Seedance I2V, preview board, animatic, or shot planning.

If sufficient, proceed directly and state any light assumptions inside "Storyboard Setup".

If insufficient, infer a draft brief from available context before asking the user. Use conversation context, provided files, project names, existing prompt text, uploaded images, or nearby project materials when available. Then ask the user to confirm or correct the brief before generating frame prompts.

Use this confirmation format:

```markdown
Let me first confirm the storyboard basics:
- Core scene: [inferred or missing]
- Subject/Character: [inferred or missing]
- Location/Situation: [inferred or missing]
- Output target: Seedance image-to-video storyboard sketch
- Suggested specs: [aspect ratio, frame count, style]

Can you confirm this direction? Or adjust one line and I will generate the storyboard sketch prompts.
```

If the request is urgent or the user explicitly says proceed directly without confirmation, proceed with reasonable assumptions and mark them clearly.

## Output Format

Use this structure by default:

```markdown
**Storyboard Setup**
- Aspect ratio:
- Visual style:
- Scene context: [one-line scene description — time, location, environment]
- Continuity anchors: [character wardrobe, key props, geography, screen direction]

**Frame 1 - [short beat name]**
Sketch prompt: [one clean prompt for a rough storyboard image]
Scene: [time · location · environment context for this beat]
Composition: [shot size, camera angle, framing]
Lighting & Mood: [key light, atmosphere]
I2V motion note: [one sentence describing the motion into or within this beat]
Story purpose: [what this shot communicates — reveal, tension, transition, establish, etc.]
Continuity: [what must remain consistent]

**Frame 2 - [short beat name]**
...
```

Repeat the frame block for each shot. End with a compact "Board Notes" section only when useful.

### Field Guide

- **Sketch prompt**: The primary image-generation prompt. 25-60 words. Include subject, action, camera, composition, lighting cues, and rough-board style keywords. This is what gets fed to an image generator to produce the storyboard panel.
- **Scene**: Time, location, and environment context specific to this beat. Keeps the sketch prompt from needing to re-explain the setting.
- **Composition**: Shot size (see Quick Reference), camera angle, framing approach. Use plain terms like "wide shot", "over-shoulder", "low angle", "centered", "rule of thirds".
- **Lighting & Mood**: Key light direction and quality, color temperature, atmosphere. E.g. "warm rim light from window, soft fill, tense atmosphere".
- **I2V motion note**: How the Seedance image-to-video should animate this frame. Camera movement + subject movement + transition logic. One sentence.
- **Story purpose**: What narrative function this shot serves — e.g. "establish spatial environment", "reveal character emotional shift", "emphasize product texture", "build suspense for the next shot". This is the single most important addition from professional storyboard practice: every shot must have a clear narrative reason to exist.
- **Continuity**: What must remain identical to other frames — character identity, wardrobe, props, lighting direction, screen geography.

## Prompt Style

- Keep sketch prompts short: usually 25-60 words per frame.
- Use simple physical language: "wide shot", "over-shoulder", "low angle", "profile", "center frame", "foreground silhouette".
- Specify rough-board aesthetics: pencil sketch, grayscale marker, loose storyboard lines, clean thumbnail composition, no finished rendering.
- Include only the objects and expressions needed to understand the beat.
- Preserve character identity, wardrobe, props, geography, and screen direction across frames.
- Prefer visible action over abstract mood words.
- Use plain composition cues instead of bloated cinematic adjectives.

## Seedance Workflow Alignment

Follow the Seedance operating pattern without becoming a full production prompt skill:

- Intake first: clarify goal, duration, aspect ratio, references, deliverable, and safety/IP risks when relevant.
- Mode gate: assume this skill serves I2V planning unless the user says T2V, V2V, R2V, edit, or extend.
- Reference map: if assets exist, assign each one a role such as identity, first frame, environment, motion, camera, timing, or style. State what should not transfer.
- Long-form logic: for videos over 15 seconds, produce a storyboard plan and note that final Seedance generation should be split into shots or segments.
- Storyboard-board input: if the user provides a multi-panel board, first identify whether it is ≤4 panels for one timestamped Seedance prompt or ≥5 panels for separate per-shot prompts plus editing rhythm.
- Quality pass: check every frame has one visible beat, one primary camera setup, continuity anchors, and an I2V motion note.

## Seedance I2V Notes

For each frame, include a motion note that helps a still storyboard become a Seedance image-to-video seed:

- Camera movement: static hold, slow push-in, lateral track, gentle tilt, handheld drift.
- Subject movement: turn, step, reach, glance, pause, reveal, react.
- Transition logic: match action, eye-line match, push through foreground, cut on gesture.
- Avoid asking one frame to contain multiple time-separated actions.

## Example — Compact Frame Prompts

User idea: "A courier discovers the package is ticking in a rainy alley."

```markdown
**Storyboard Setup**
- Aspect ratio: 16:9
- Visual style: rough grayscale storyboard sketch, clean readable thumbnails
- Scene context: Midnight, narrow back alley, heavy rain, wet brick walls
- Continuity anchors: red courier jacket, wet alley bricks, small black package

**Frame 1 - Alley Arrival**
Sketch prompt: Wide shot, rainy narrow alley at night, courier in a red jacket enters from screen left holding a small black package, wet brick walls, simple pencil lines, clear silhouette.
Scene: Midnight · narrow alley · rain on brick
Composition: Wide shot, eye level, leading lines from alley walls
Lighting & Mood: Street lamp top light, blue ambient, tense
I2V motion note: Slow lateral track follows the courier walking deeper into the alley.
Story purpose: Establish spatial environment and character entrance state
Continuity: Courier keeps the package in the right hand.

**Frame 2 - The Sound**
Sketch prompt: Medium close shot, courier stops under a dim wall lamp and tilts the package toward one ear, rain streaks behind, anxious face, loose storyboard shading.
Scene: Same alley · under wall lamp
Composition: Medium close-up, eye level, centered on face and package
Lighting & Mood: Overhead lamp as key, rain reflections on face, suspenseful
I2V motion note: Static hold with a small head turn as the courier hears the ticking.
Story purpose: Reveal crisis signal, establish suspense turning point
Continuity: Same red jacket, same package size and orientation.
```

---
## Load Resources

This skill includes bundled reference knowledge. Load when needed:

- For Seedance I2V workflow, operating modes, and motion note specifications, read `references/seedance-i2v-workflow.md`
- For anti-slop lexicon replacement when writing prompts, read shared reference `../references/anti-slop-lexicon.md`
- For bilingual shot size, camera movement, angle, composition, lighting, and narrative purpose quick reference tables, read `../references/cinematography-quick-reference.md`
- For Seedance platform constraints (word limits, @[ref] format), read shared reference `../references/seedance-platform.md`

---

## Quality Bar

- The reader should understand the entire scene by scanning frame titles and sketch prompts.
- Every prompt should be drawable as a single storyboard panel.
- Every frame must have a clear story purpose — answering "why does this shot exist."
- The planning board should be usable before writing final Seedance prompts.
- If user requests Chinese output, write all prompts in concise Chinese with the same structure.
- For Master Sheet mode, the four zones (Shot Grid, Rhythm, Camera, Visual Language) should form a coherent planning document, not just a shot list.


## Save Output

After delivering the final output, prompt the user to save:

outputs/storyboard-sketch-i2v-frames.mdoutputs/storyboard-sketch-i2v-frames-example.md

If the user confirms, write the output to the specified path.
