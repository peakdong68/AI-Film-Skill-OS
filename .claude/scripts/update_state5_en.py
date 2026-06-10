import sys

filepath = '.claude/skills/director-core/SKILL.md'

with open(filepath, 'r', encoding='utf-8') as f:
    c = f.read()

changes = 0

# 1. Diagram already done
# 2. Key distinction already done
# 3. Lock rules already done
# 4. STATE 4 boundary already done

# 5. STATE 4 end → routing decision → STATE 5
i = c.find('**State 4 output**')
j = c.find('**Pre-flight Checklist (all must be YES):**', i)
old = c[i:j]
new = """**State 4 output**: Film-level short film prompt package (text-level director's vision document). Proceed to routing decision.

**User next step**: Confirm the prompt package content. After confirmation, do NOT proceed directly to STATE 5 — first execute the routing decision to determine the best path forward.

### After STATE 4: Routing Decision

After the prompt package is confirmed, **do NOT proceed directly to STATE 5.** First determine the best path based on project needs, available resources, and the target STATE 6 mode.

**Step 1: Inventory available resources**

Ask the user what multimodal resources they currently have (multi-select):

```
Which visual/multimodal resources do you currently have?
- [ ] Character reference images (from STATE 3 character generation or user-provided)
- [ ] Product reference images
- [ ] Background/environment reference images
- [ ] First/last frame images
- [ ] Video reference clips
- [ ] Audio reference clips
- [ ] None of the above — start from text only
```

**Step 2: Match STATE 6 modes**

Based on available resources, match against the STATE 6 mode selection table:

| Available resources | Eligible modes |
|---|---|
| None of the above | T2V |
| Single reference image (product/character/scene) | I2V (minimal) |
| First + last frame images | FLF2V |
| Multiple different ref types (product+video+audio etc.) | R2V |
| Video source clip | V2V Edit / V2V Extend |
| Need storyboard boards for multi-shot continuous camera | I2V (storyboard) → requires STATE 5 first |

**Step 3: Present 2-3 route options**

Recommend the most suitable route based on project characteristics, with alternatives:

| Route | Path | Best for | User needs to provide |
|---|---|---|---|
| **A: Storyboard Blueprint** | STATE 4 → STATE 5 → STATE 6 (I2V storyboard) | Narrative short films, complex multi-shot sequences, precise storyboard-controlled camera movement | Nothing extra (STATE 5 generates storyboard images) |
| **B: Direct to Video** | STATE 4 → STATE 6 (I2V minimal / FLF2V / T2V / R2V) | Existing reference images, product showcases, simple actions, first/last frame transitions, text-only generation | Single/multiple reference images / first-last frames / video-audio clips |
| **C: Hybrid** | STATE 4 → STATE 5 (key shots) + STATE 6 (non-key shots in parallel) | Some shots need storyboard control, others can use direct references | Reference images for non-key shots |

After user selects a route, proceed accordingly. Route A enters STATE 5; Route B skips STATE 5 directly to STATE 6; Route C partially executes STATE 5 as needed.

### STATE 5 — Storyboard Blueprint Generation (Image Level, Conditional)

**This stage is only executed when Route A or C is selected in the routing decision.** If the user selects Route B (direct to video), skip STATE 5 and proceed directly to STATE 6.

Route to `storyboard-sketch` (for Seedance I2V rough sketches) or `storyboard-prompt` / `storyboard-master` / `storyboard-ecommerce` (for generating complete storyboard blueprint images).

"""
c = c.replace(old, new)
changes += 1

# 6. Dependency graph
i = c.find('director-prompt-packager [STATE 4: Film-Level Short Film Prompt Package]')
j = c.find('[Final Validation → Export]', i) + len('[Final Validation → Export]')
old = c[i:j]
new = """director-prompt-packager [STATE 4: Film-Level Short Film Prompt Package]
                │
                ↓ (User confirms prompt package)
                │
         [Routing Decision: inventory → match → route]
                │                    │
        Route A: Storyboard    Route B: Direct to Video
                │                    │
         storyboard-sketch /         │
         storyboard-prompt /         │
         storyboard-master /         │
         storyboard-ecommerce        │
         [STATE 5: Conditional]      │
                │                    │
                └────────┬───────────┘
                         ↓
         seedance-video-prompt [STATE 6: Image-ref video prompts → Seedance 2.0]
                │
                ↓
         [Final Validation → Export]"""
c = c.replace(old, new)
changes += 1

# 7. Routing guide
i = c.find('I have a creative idea')
j = c.find('E-commerce/livestream/fashion video storyboards', i)
old = c[i:j]
new = """I have a creative idea, help me make it into a film"                              | Stay in director-core, start from STATE 0                                                          |
| "I already have a script, need visual design"                                      | Enter from STATE 2                                                                                 |
| "I have character identity definitions, need image generation prompts"             | Route to `character-image-prompt`                                                                  |
| "I have story + visual + character design, need to compile a prompt package"       | Enter from STATE 4                                                                                 |
| "I have a prompt package (text), need to generate storyboard blueprint images"     | Enter from STATE 5                                                                                 |
| "I have a prompt package + ref images, need video directly (no storyboard needed)" | Enter from STATE 4 routing → Route B → skip to STATE 6                                             |
| "I have storyboard blueprint images + character images, need Seedance 2.0 prompts" | Enter from STATE 6                                                                                 |
| "I have single ref image / first-last frames, need to generate video"              | Enter from STATE 4 routing → Route B → STATE 6 (I2V minimal / FLF2V)                              |
| "I just want character identity definitions"                                       | Route directly to `director-character`                                                             |
| "Fix my broken AI video, characters keep changing faces"                           | Enter from STATE 3 (re-lock characters), then STATE 6                                              |
| """
c = c.replace(old, new)
changes += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(c)

print(f'OK - {changes} changes applied')
