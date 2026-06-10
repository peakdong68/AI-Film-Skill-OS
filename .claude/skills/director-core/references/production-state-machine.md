# Production State Machine — Core Knowledge

## State Flow

```
STATE 0 → Input Collection   (Gather brief, ask key questions)
STATE 1 → Story & Emotion    (Narrative structure + emotional arc)
STATE 2 → Visual Design      (Camera grammar + lighting + color)
STATE 3 → Character Lock     (Character sheets + identity locking)
STATE 4 → Prompt Packaging   (Film-level short film prompt package: storyboard design + camera language + sound design + Seedance decomposition plan)
STATE 5 → Storyboard Blueprint Generation  (Generate storyboard blueprint images for @[ref] reference)
STATE 6 → Seedance Video Prompt  (Image reference level, platform executable)
STATE 7 → Final Validation   (Quality audit of all deliverables)
STATE 8 → Export Ready       (Package deliverables)
```

## Absolute Workflow Locks

1. Story structure and emotional arc must be confirmed before visual design
2. Camera language and lighting system must be defined before prompt package compilation
3. Character identity must be confirmed before prompt package compilation
4. Prompt package must be user-confirmed before entering storyboard blueprint generation
5. Storyboard blueprint images must be confirmed before Seedance prompt creation
6. Do not assume confirmation — wait for explicit user approval
7. Prompt package unconfirmed → storyboard blueprint generation forbidden
8. Storyboard blueprint unconfirmed → Seedance prompt creation forbidden
9. Character unconfirmed → Seedance prompt creation forbidden
10. STATE 4 output must never mention Seedance /Kling video platforms

## Phase Lock Enforcement

| Lock | Condition | Consequence of Violation |
|------|-----------|---------------------------|
| Story Lock | Story structure must be confirmed before visual design | Incoherent visual language |
| Visual Lock | Camera + lighting must be defined before prompt package compilation | Arbitrary camera decisions |
| Character Lock | Character sheets must be confirmed before prompt package compilation | Character drift, face-swap |
| Package Lock | Prompt package must be user-confirmed before entering storyboard blueprint | Wrong storyboard direction |
| Storyboard Lock | Storyboard blueprint images must be confirmed before Seedance prompts | Missing narrative visual reference |
| Output Boundary Lock | STATE 4 output must not mention video platforms | User misinputs text prompts into video platform |
| Prompt Lock | All pre-flight items must pass before final export | Continuity breakdown |

## Mandatory Status Tracker

Every production session output must include:
- Current phase
- Completed states
- Pending states
- Active locks
- Next required action
- Critical lock status

## STATE 4 vs STATE 5 — Separation of Concerns

**STATE 4 (director-prompt-packager)**: Text-level compiler
- Compiles all STATE 1-3 design outputs into a film-level short film prompt package
- Contains: structured storyboard design + camera language + sound design + Seedance decomposition plan
- For user confirmation, serves as input foundation for STATE 5 storyboard blueprint generation
- **Must never mention Seedance/Kling video platforms in output**

**STATE 5 (storyboard-sketch/storyboard-prompt/storyboard-master/storyboard-ecommerce)**: Image-level generation
- Uses the confirmed prompt package to generate storyboard blueprint images
- In production, only storyboard blueprint boards (overview images) are needed, not per-frame individual images
- Blueprint images serve as @[ref] inputs for STATE 6

## Multi-Part Structure Rules

- Each Part = one video segment (max 15 seconds)
- Total duration = number of Parts × seconds per Part
- Part 2 and beyond must reference the previous output as a continuity baseline

## Pre-Flight Checklist (Before STATE 4 Prompt Package Compilation)

All must be YES:
- [ ] Story structure confirmed?
- [ ] Emotional arc confirmed?
- [ ] Visual language (camera + lighting) defined?
- [ ] Character identities locked and confirmed?
- [ ] Duration and aspect ratio locked?

## Pre-Flight Checklist (Before STATE 6 Seedance Prompt Generation)

All must be YES:
- [ ] Storyboard blueprint images generated?
- [ ] User confirmed storyboard blueprints?
- [ ] Character reference images available?
- [ ] Product images locked (if applicable)?
- [ ] Background images locked (if applicable)?
- [ ] Music style and BPM determined?
