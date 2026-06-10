---
name: director-story
description: Deconstruct a story idea, script, or concept into a director-grade narrative structure with scene breakdown, causal chain analysis, and director intent. Use when the user needs script analysis, story structure design, script breakdown, scene decomposition, narrative architecture, 3-act or 5-act structure, or when director-core routes to STATE 1 (Story Design). Also use when the user has a vague story idea and needs it turned into a structured scene sequence before proceeding to storyboard.
---

# Director Story — Script Director Engine

## Overview

Transform a story idea or script into a professional narrative blueprint. This skill applies director-level analysis: breaking the story into acts, extracting scene purpose, building the causal chain, and defining what each scene must achieve narratively. The output is the structural foundation that all downstream systems (emotion, camera, storyboard, prompt) build upon.

This skill works independently for script analysis or is invoked by `director-core` at STATE 1.


## Loaded Resources

This skill ships with reference knowledge files. Load them when:
- For the scene purpose taxonomy and complete narrative structure templates, read `references/script-breakdown.md`
## Input Gate

Accept any of the following as starting material:
- A story concept (one sentence to one paragraph)
- A script or script excerpt
- A beat outline or director's treatment
- A scene list
- A thematic concept with character descriptions

**For vague or descriptive-but-no-plot inputs, route to  for creative intake.** The skill auto-selects the best path:

| Input quality | Path |
|---|---|
| Creative complete | Fast track, analyze directly |
| Descriptive but no plot | 2-3 options, then analyze |
| Vague creative | Clarifying interview, then analyze |

If the user explicitly requests "just analyze it" and refuses interview, expand from available material and annotate assumptions.

## Output Structure

Every analysis must produce a Script Director Blueprint with these 5 sections:

### 1. Narrative Structure Map (Narrative Structure)

Select and populate one structure:

**3-Act Structure:**
```
Act 1: Setup — [world, character, status quo]
  Turning Point 1: [inciting incident]
Act 2: Confrontation — [rising obstacles, complications]
  Midpoint Shift: [irreversible change]
  Turning Point 2: [darkest moment / crisis]
Act 3: Resolution — [climax, new equilibrium]
```

**5-Act Structure:**
```
Act 1: Exposition — [world and character established]
Act 2: Rising Action — [complications accumulate]
Act 3: Climax — [peak conflict, decisive moment]
Act 4: Falling Action — [consequences unfold]
Act 5: Denouement — [resolution, new state]
```

For short-form content (≤30s), default to 3-act. For long-form (>60s), consider 5-act.

### 2. Scene Breakdown Map (Scene Breakdown)

For each scene, define:

```
SCENE [N]: [scene title]
- Scene purpose: [why this scene exists in the narrative]
- Emotional function: [what emotion does the audience feel?]
- Narrative function: [advance plot / reveal character / build world / create tension / resolve]
- Characters involved: [who appears]
- Conflict type: [internal / interpersonal / external / environmental]
- Entry state → Exit state: [what changes by scene end?]
```

### 3. Causal Chain (Causal Chain)

Define the chain of causation that drives the narrative forward:

```
Event A → triggers → Event B → consequence → Event C
```

Map dependencies:
```
[Scene 1 event] → causes → [Scene 2 situation] → forces → [Scene 3 decision] → results in → [Climax]
```

For each link, verify: "If I remove this event, does the next scene still make sense?" If yes, the causal link is weak.

### 4. Director Intent Layer (Director Intent Layer)

For every scene, answer three director questions:

| Question | What it reveals |
|---|---|
| Why does this scene exist? | Narrative justification — if you can cut it without losing anything, it shouldn't exist |
| What changes after this scene? | The delta — audience knowledge, character state, tension level |
| What emotion does the audience leave with? | Emotional residual — what feeling carries into the next scene |

### 5. Storyboard Readiness Check (Storyboard Readiness)

Assess whether the narrative structure is ready for storyboard:

- [ ] Every scene has a clear purpose
- [ ] Causal chain has no gaps
- [ ] Emotional arc covers the full duration
- [ ] Character motivations drive plot, not coincidence
- [ ] Director intent is clear for every scene

If any item is unchecked, note what's missing before handing off to storyboard.

## Scene Purpose Taxonomy

Use these categories to classify scene purpose. Every scene must fall into at least one:

| Category | Chinese | Signal |
|---|---|---|
| Establish | 建立 | Introduce world, character, or status quo |
| Advance | 推进 | Move plot forward through action or decision |
| Reveal | 揭示 | Expose information, character truth, or stakes |
| Escalate | 升级 | Increase tension, stakes, or conflict |
| Contrast | 对比 | Juxtapose two states, characters, or ideas |
| Transition | 过渡 | Bridge between major narrative blocks |
| Resolve | 收束 | Conclude an arc, answer a question, reach closure |

## Constraints

- No scene without a purpose — if a scene exists only for aesthetic reasons, mark it and ask the user to confirm.
- No orphaned events — every event must connect to the causal chain.
- No unexamined director intent — every scene must pass the three questions.
- No handoff to storyboard until the Readiness Check passes.

## Integration with director-core

When invoked by `director-core` at STATE 1:
- Produce the full Script Director Blueprint
- Present for user confirmation
- Upon confirmation, signal STATE 1 complete
- The blueprint feeds into `director-emotion` for the emotional timeline
