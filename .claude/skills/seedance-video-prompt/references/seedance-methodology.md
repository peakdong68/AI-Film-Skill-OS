# Seedance 2.0 Prompt Methodology — Bundled Reference

Load-on-demand reference for the `seedance-video-prompt` skill. Contains complete templates, failure fixes, compression rules, and scene adaptations.

---

## Complete Per-Mode Templates

### I2V Preservation

**Chinese:**
```
`图片1`为参考；精确保留[身份/产品/场景]。仅[运动]发生变化。
镜头：[单一运镜]。光影：[光源或过渡]。音效：[提示音]。约束：[不变项]。
```

**English:**
```
`Image1` as reference, strictly preserve [identity/product/scene].
Only [motion] changes. Camera: [one movement]. Light: [source or transition].
Sound: [cue]. Constraints: [what must not change].
```

**Example — Product:**
```
`Image1` as product reference; strictly preserve bottle label, logo, shape, color.
Only condensation beads form and slide down the glass. Camera: locked medium product shot, slow push-in.
Light: warm strip light sweeps left across the label. Sound: <crisp glass tick>.
Constraints: keep subtitle-free, no logos. Word count: 96 chars ✅
```

**Example — Character:**
```
`Image1` as character reference; strictly preserve facial structure, hairstyle, jacket.
Only eyes blink once slowly, gaze drops slightly. Camera: locked medium close-up, no reframing.
Light: soft window natural light. <quiet room tone>.
```

### I2V Storyboard-Driven

```
Use the storyboard in `Image1` as motion planning reference; do not render the storyboard itself.
Ignore all borders, panel frames, text, labels.
Define [character features] in `Image2` as `Subject1`.

Shot 1: [Panel 1 — establish space and initial state]
Shot 2: [Panel 2 — character action or environment change]
Shot 3: [Panel 3 — continuing progression]
...

(Play [music style] in background, BPM [range])

Constraints: keep subtitle-free, no logos, no watermarks.
No facial distortion, no identity drift, no scene jumps.
```

### R2V Multi-Reference Role Mapping

```
Define [features] in `Image1` as `Subject1`.
`Video1` controls camera rhythm only; do not transfer performer, room, brand, or costume.
`Audio1` controls tempo and energy only.

`Subject1` [action], [scene environment].
Camera: [movement]. Sound: [SFX]. Constraints: [what must not change].
```

**Example:**
```
Define the man in `Image1` wearing a black trench coat and sunglasses as `Subject1`.
`Video1` controls lateral tracking camera rhythm only; do not transfer performer, interior layout, or brand identity.
`Audio1` controls tempo and energy only.

`Subject1` walks across a wet train platform, stops under a flickering sign, and turns left on the final beat.
Camera: 35mm locked medium-wide, one slow side track.
<rain><footsteps>. (No music).

Constraints: keep subtitle-free, no logos, no watermarks.
```

### FLF2V First/Last Frame

```
`Image1` is the first frame. `Image2` is the last frame.
Preserve the same subject's facial structure, hairstyle, outfit, and scene layout.
Generate a continuous transition from [starting state] to [ending state].
Motion: [one physical action path]. Camera: [locked medium or one slow push-in].
Light: [source and continuity]. Sound: [ambience]. Constraints: [what must not change].
```

**Example:**
```
`Image1` is the first frame. `Image2` is the last frame.
Preserve `Subject1`'s facial structure, hairstyle, jacket, and room layout.
Generate a continuous transition from sitting to standing: `Subject1` slowly rises from the chair, walks to the window, and stops in the final pose.
Camera: locked medium shot, slight push-in. Light: same cool window light, warm lamp glow at end.
<quiet room tone><soft floor creak>.
```

### T2V Text-to-Video

```
[Subject] [action] in [scene]. Camera: [one primary movement].
Light: [source and quality]. Style: [tone]. Constraints: [exclusions].
```

### V2V Edit

```
Edit `Video1`, change [original feature] to [new feature].
Elements not mentioned remain unchanged by default.
Constraints: keep subtitle-free, no logos.
```

### V2V Extend

```
Extend `Video1` forward, [subject] continues [action].
Audio-visual style, subject, and narrative remain consistent.
Constraints: keep subtitle-free, no logos, no watermarks.
```

---

## Role Mapping

| Asset Type | Recommended Role | Avoid |
|---|---|---|
| Image | identity, product, pose, costume, environment, first frame, last frame | Asking it to define unseen motion |
| Video | motion, camera, pacing, blocking, timing | Copying protected identity, logo, or scenes |
| Audio | rhythm, tempo, mood, timbre, music texture | Assuming voice/song/likeness authorization |

**Core Rules:**
- Assign one primary role per reference; no stacking additional style descriptions
- Explicitly declare "what to preserve" and "what must not transfer"
- When authorization is unclear, transfer only broad motion/rhythm/mood, not protected identity
- Audio/video conflict: mute video or declare video controls camera/motion only

---

## I2V Failure Fixes

| Failure | Fix |
|---|---|
| Identity drift | Reduce new visual description, strengthen preservation constraints; place face ref first |
| Camera jumps | Use one camera movement, note start and end frames |
| Product deformation | Declare preserved static identity, no shape change |
| Output is static | Add one physical action and one temporal cue |
| Background changes | Preserve environment layout, animate only light/weather/atmosphere |
| Hand deformation | Simplify hand motion or exclude hands from main action |
| ID drift / face-swap | Use separate face close-up (headshot) + full-body reference; prohibit three-view sheets |
| Twin problem | Define subjects explicitly with binding relationships; add global constraint prohibiting identical duplicates |

---

## Compression Rules

When prompts are too long, trim in this order:

**Delete:** duplicate style adjectives → generic quality words → background details visible in refs → secondary camera moves → secondary actions → speculative emotion labels

**Preserve:** reference tags and roles → subject/product identity → action verb + visible endpoint → one camera move → physical light source or atmosphere → sound cue → safety/continuity constraints

**Compact Chinese I2V template:**
```
`图片1`为参考，严格保持[主体]不变；仅加入[动作/光线/镜头]。音效：[提示]。约束：[不变项]。
```

---

## Common Scene Adaptations

### Fashion / Apparel Videos
- Role mapping mandatory: `` `Image1` `` locks color/print/fit
- Fabric dynamics (folds, sway) must be described
- Back constraint: solid color, no print, no text
- Music: lo-fi hip-hop / chill trap, BPM 90-110
- Prioritize Chinese compression, within 500 characters

### Product Showcase Videos
- Product image locks appearance, background image locks environment
- Camera: push-in / orbit / detail, one primary movement
- **Let light/particles/camera move around the product — do not deform the product itself**

### Narrative Short Films
- Character image locks identity, storyboard image (if used) locks narrative pacing
- Emotion evolves, never resets
- One segment = one beat = one emotional turn

### Multi-Character Scenes
- Each character independently defined + reference-bound (`` Define [features] in `ImageN` as `SubjectN` ``)
- Declare spatial relationships remain unchanged
- Add constraint at end: `Prohibit figures with identical appearance, clothing, or accessories; prohibit duplicate clones or twin effects`
- Over 4 reference characters: generate in groups (group images first, then feed into video)

---

## Asset Configuration Strategy

Recommended total: 4-5 assets — 1-2 character images (separate face close-up + full-body) + 1 scene image + 1 camera reference video + 1 audio clip. Avoid maxing out asset slots; too many assets cause feature priority confusion.
