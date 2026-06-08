---
name: storyboard-sketch
description: Create concise, clean rough-sketch storyboard prompts from scene ideas, scripts, beats, or visual concepts for Seedance image-to-video workflows. Use when the user asks for a storyboard, preview board, animatic planning, animation shot plan, keyframe board, rough visual frames, first-frame prompts, shot-by-shot sketch prompts, or a quick board to guide Seedance I2V generation.
---

# Seedance Storyboard Sketch

## Overview

Turn a scene idea or script into a compact storyboard plan whose frames can be drawn or generated as simple preview images before Seedance image-to-video. Favor clarity, continuity, and sketchability over polished cinematic prose.

## Workflow

1. Run the Input Gate before writing any frame prompts.
2. Identify the scene goal, characters, location, emotional beat, references, target mode, aspect ratio, and intended output length.
3. Convert the idea or script into a compact storyboard plan: 3-8 frames unless the user specifies a count.
4. For each frame, define one readable visual moment: subject, action, composition, camera angle, and continuity notes.
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
我先确认一下分镜基础：
- 场景核心：[inferred or missing]
- 主体/角色：[inferred or missing]
- 地点/情境：[inferred or missing]
- 输出目标：Seedance image-to-video storyboard sketch
- 建议规格：[aspect ratio, frame count, style]

确认这些方向吗？也可以直接改一句，我再生成分镜草图提示词。
```

If the request is urgent or the user explicitly says "直接生成", proceed with reasonable assumptions and mark them clearly.

## Output Format

Use this structure by default:

```markdown
**Storyboard Setup**
- Aspect ratio:
- Visual style:
- Continuity anchors:

**Frame 1 - [short beat name]**
Sketch prompt: [one clean prompt for a rough storyboard image]
I2V motion note: [one sentence describing the motion into or within this beat]
Continuity: [what must remain consistent]
```

Repeat the frame block for each shot. End with a compact "Board Notes" section only when useful.

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
- Storyboard-board input: if the user provides a multi-panel board, first identify whether it is <=4 panels for one timestamped Seedance prompt or >=5 panels for separate per-shot prompts plus editing rhythm.
- Quality pass: check every frame has one visible beat, one primary camera setup, continuity anchors, and an I2V motion note.
## Seedance I2V Notes

For each frame, include a motion note that helps a still storyboard become a Seedance image-to-video seed:

- Camera movement: static hold, slow push-in, lateral track, gentle tilt, handheld drift.
- Subject movement: turn, step, reach, glance, pause, reveal, react.
- Transition logic: match action, eye-line match, push through foreground, cut on gesture.
- Avoid asking one frame to contain multiple time-separated actions.

## Example

User idea: "A courier discovers the package is ticking in a rainy alley."

```markdown
**Storyboard Setup**
- Aspect ratio: 16:9
- Visual style: rough grayscale storyboard sketch, clean readable thumbnails
- Continuity anchors: red courier jacket, wet alley bricks, small black package

**Frame 1 - Alley Arrival**
Sketch prompt: Wide shot, rainy narrow alley, courier in a red jacket enters from screen left holding a small black package, wet brick walls, simple pencil lines, clear silhouette.
I2V motion note: Slow lateral track follows the courier walking deeper into the alley.
Continuity: Courier keeps the package in the right hand.

**Frame 2 - The Sound**
Sketch prompt: Medium close shot, courier stops under a dim wall lamp and tilts the package toward one ear, rain streaks behind, anxious face, loose storyboard shading.
I2V motion note: Static hold with a small head turn as the courier hears the ticking.
Continuity: Same red jacket, same package size and orientation.
```

## Quality Bar

- A reader should understand the whole scene by scanning frame titles and sketch prompts.
- Each prompt should be drawable as one storyboard panel.
- The board should be useful even before final Seedance prompt writing.
- If the user asks for Chinese output, write all prompts in concise Chinese with the same structure.

