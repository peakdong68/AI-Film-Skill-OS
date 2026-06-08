# Production State Machine — Core Knowledge

## State Flow

```
STATE 0 → INPUT INGESTION     (gather brief, ask key questions)
STATE 1 → STORY & EMOTION      (narrative structure + emotion arc)
STATE 2 → VISUAL DESIGN        (camera grammar + lighting + color)
STATE 3 → CHARACTER LOCK       (character sheets + identity locks)
STATE 4 → STORYBOARD           (frame generation + confirmation)
STATE 5 → PROMPT COMPILATION   (Seedance prompt generation)
STATE 6 → FINAL VALIDATION     (quality pass across all artifacts)
STATE 7 → EXPORT READY         (packaged deliverable)
```

## Absolute Workflow Locks

1. Never create Seedance prompts before all storyboards are completed
2. Never create Seedance prompts before user confirms all storyboards
3. Never create character design prompts before storyboard confirmation
4. Never assume confirmation — wait for explicit user approval
5. Storyboard unconfirmed → Seedance Prompt FORBIDDEN
6. Character unconfirmed → Seedance Prompt FORBIDDEN

## Phase Lock Enforcement

| Lock | Condition | Violation Consequence |
|------|-----------|----------------------|
| Story Lock | Story structure must be confirmed before visual design | Incoherent visual language |
| Visual Lock | Camera + lighting must be defined before storyboard | Random camera decisions |
| Character Lock | Character sheet must be confirmed before prompts | Character drift, face swapping |
| Storyboard Lock | All frames confirmed before compilation | Missing narrative context |
| Prompt Lock | All pre-checks pass before final export | Broken continuity |

## Mandatory Status Tracker

Every production session output must include:
- Requested storyboard count
- Completed storyboard count  
- Remaining storyboard count
- Current phase
- Next required action
- Critical lock status

## Multi-Part Structure Rules

- Each storyboard = one video clip (max 15 seconds)
- Each storyboard = 8-12 panels
- Total runtime = storyboard count × seconds per board
- Part 2+ must reference previous output as continuity baseline

## Pre-Check Checklist (before Seedance prompt generation)

All must be YES:
- [ ] All storyboards completed?
- [ ] User confirmed all storyboards?
- [ ] Character prompts completed?
- [ ] User confirmed characters?
- [ ] Visual language defined?
- [ ] Duration and aspect ratio locked?
