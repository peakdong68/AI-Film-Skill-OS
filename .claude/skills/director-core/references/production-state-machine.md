# Production State Machine — Core Knowledge

## State Flow

```
STATE 0 → Input Collection   (Gather brief, ask key questions)
STATE 1 → Story & Emotion    (Narrative structure + emotional arc)
STATE 2 → Visual Design      (Camera grammar + lighting + color)
STATE 3 → Character Lock     (Character sheets + identity locking)
STATE 4 → Prompt Packaging   (Film-level short film prompt package: storyboard design + camera language + sound design + Part decomposition plan)
    ↓
[Routing Decision: inventory resources → match STATE 6 mode → select route]
    ↓                        ↓
STATE 5 (conditional)    Direct to STATE 6
Storyboard Blueprint     (skip STATE 5)
Generation
    ↓                        ↓
    └────────┬───────────────┘
             ↓
STATE 6 → Seedance Video Prompt (multi-mode, image reference level, platform executable)
STATE 7 → Final Validation   (Quality audit of all deliverables)
STATE 8 → Export Ready       (Package deliverables)
```

STATE 0-4 are mandatory, must not be skipped. STATE 5 is conditional — only executed when routing decision selects the storyboard blueprint route (Route A/C). STATE 6-8 are mandatory.

## Absolute Workflow Locks

1. Story structure and emotional arc must be confirmed before visual design
2. Camera language and lighting system must be defined before prompt package compilation
3. Character identity must be confirmed before prompt package compilation
4. Prompt package must be user-confirmed before entering subsequent stages
5. If going through STATE 5, storyboard blueprint images must be confirmed before Seedance prompts
6. Do not assume confirmation — wait for explicit user approval
7. Prompt package unconfirmed → downstream stages forbidden
8. Character unconfirmed → Seedance prompt creation forbidden
9. STATE 4 output must never mention Seedance/Kling video platforms
10. STATE 6 must select the correct mode based on available resources — do not default to storyboard-driven mode

## Phase Lock Enforcement

| Lock | Condition | Consequence of Violation |
|------|-----------|---------------------------|
| Story Lock | Story structure must be confirmed before visual design | Incoherent visual language |
| Visual Lock | Camera + lighting must be defined before prompt package compilation | Arbitrary camera decisions |
| Character Lock | Character sheets must be confirmed before prompt package compilation | Character drift, face-swap |
| Package Lock | Prompt package must be user-confirmed before entering subsequent stages | Wrong downstream direction |
| Storyboard Lock | If going through STATE 5, storyboard images must be confirmed before Seedance prompts | Missing narrative visual reference |
| Output Boundary Lock | STATE 4 output must not mention video platforms | User misinputs text prompts into video platform |
| Prompt Lock | All pre-flight items must pass before final export | Continuity breakdown |
| Mode Lock | STATE 6 must select mode based on available resources, not default to storyboard-driven | Prompt-input mismatch, generation failure |

## Routing Decision Rules (After STATE 4 Confirmation)

After prompt package confirmation, do NOT proceed directly to STATE 5. Execute a three-step routing decision:

### Step 1: Inventory available resources
Ask the user what multimodal resources they have (character images, product images, background images, first/last frames, video clips, audio clips).

### Step 2: Match STATE 6 modes
| Available resources | Eligible modes |
|---|---|
| No reference assets | T2V |
| Single reference image (product/character/scene) | I2V (minimal) |
| First + last frame | FLF2V |
| Multiple different ref types | R2V |
| Video source clip | V2V Edit / V2V Extend |
| Need storyboard boards for multi-shot continuous camera | I2V (storyboard) → requires STATE 5 first |

### Step 3: Present 2-3 route options
| Route | Path | Best for |
|---|---|---|
| A: Storyboard Blueprint | STATE 4 → STATE 5 → STATE 6 (I2V storyboard) | Narrative films, complex multi-shot, precise storyboard control |
| B: Direct to Video | STATE 4 → STATE 6 (I2V minimal / FLF2V / T2V / R2V) | Existing ref images, product demos, first/last frame transitions, text-only |
| C: Hybrid | STATE 4 → STATE 5 (key shots) + STATE 6 (non-key in parallel) | Mix of storyboard-needed and direct-reference shots |

## STATE 4 vs STATE 5/6 — Separation of Concerns

**STATE 4 (director-prompt-packager)**: Text-level compiler
- Compiles all STATE 1-3 design outputs into a film-level short film prompt package
- Contains: structured storyboard design + camera language + sound design + Part decomposition plan
- For user confirmation, serves as design foundation for subsequent stages
- **Must never mention Seedance/Kling video platforms in output**
- Output is a platform-agnostic director-level design document

**STATE 5 (conditional, storyboard-sketch/storyboard-prompt/storyboard-master/storyboard-ecommerce)**: Image-level generation
- Only executed when routing decision selects Route A or C
- Uses the confirmed prompt package to generate storyboard blueprint images
- In production, only storyboard blueprint boards (overview images) are needed, not per-frame individual images
- Blueprint images serve as @[ref] inputs for STATE 6 I2V storyboard mode

**STATE 6 (seedance-video-prompt)**: Video prompt compiler
- Supports 7 modes, selected automatically based on available resources
- Storyboard images are only required for I2V storyboard mode
- Each prompt corresponds to one Part (≤ 15s), counted independently

## Multi-Part Structure Rules

- Each Part = one Seedance 2.0 call = one video segment (max 15 seconds)
- Each Part gets its own prompt, independently subject to word count limits (Chinese ≤ 500 chars / English ≤ 1000 words)
- Total duration = number of Parts × seconds per Part
- Part 1: driven by the selected mode (storyboard / ref image / first-last frame / text-only)
- Part 2+: must reference the previous Part's output video as a continuity baseline (`@[Video1] is previous Part output`)
- Multi-Part projects compile prompts Part-by-Part in STATE 6, not all at once

## Pre-Flight Checklist (Before STATE 4 Prompt Package Compilation)

All must be YES:
- [ ] Story structure confirmed?
- [ ] Emotional arc confirmed?
- [ ] Visual language (camera + lighting) defined?
- [ ] Character identities locked and confirmed?
- [ ] Duration and aspect ratio locked?
- [ ] Part decomposition plan determined (each Part ≤ 15s)?

## Pre-Flight Checklist (Before STATE 6 Seedance Prompt Generation — Mode-Aware)

- [ ] Routing decision completed, route selected?
- [ ] Required inputs for selected mode ready?
- [ ] If Route A/C: storyboard blueprint images generated and confirmed?
- [ ] If Route B: reference images (single/first-last frames/video clips) ready?
- [ ] Character reference images available? (or user explicitly chose to skip)
- [ ] Product images locked (if applicable)?
- [ ] Background images locked (if applicable)?
- [ ] Music style and BPM determined?
- [ ] Each prompt word count compliant (Chinese ≤ 500 chars per Part)?
