# Seedance 2.0 Prompt Methodology — Bundled Reference

Loaded on demand by the `seedance-video-prompt` skill. Contains complete templates, failure fixes, compression rules, and scene adaptations.

---

## Full Per-Mode Templates

### I2V Minimal Preservation

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
`图片1`为产品参考；精确保留瓶身标签、Logo、瓶型、颜色不变。
仅水珠凝结并沿玻璃滑落。镜头：锁定中景产品镜头，缓慢推近。
光影：左侧暖光条扫过标签表面。音效：<清脆玻璃音>。
约束：保持无字幕、不要生成Logo。字数：96 字 ✅
```

**Example — Character:**
```
`图片1`为角色参考；精确保留面部结构、发型、外套不变。
仅眼睛缓慢眨一次，视线微微下移。镜头：锁定中近景，无重新取景。
光影：柔和的窗户自然光。<安静的房间底噪>。
```

### I2V Storyboard-Driven

```
Define the storyboard in `Image1` as motion planning reference;
do not render the storyboard itself. Ignore all borders, panels, text, labels.
Define [character traits] in `Image2` as `Subject1`.

Shot 1: [Corresponds to panel 1 — establish space and initial state]
Shot 2: [Corresponds to panel 2 — character action or environment change]
Shot 3: [Corresponds to panel 3 — continuing progression]
...

(Background plays [music style], BPM [range])

Constraints: no subtitles, no logos, no watermarks.
No facial distortion, no identity drift, no scene jumps.
```

### R2V Multi-Reference Role Mapping

```
Define [traits] in `Image1` as `Subject1`.
`Video1` controls camera rhythm only; do not transfer performer, room, brand, or costume.
`Audio1` controls tempo and energy only.

`Subject1` [action description], [scene environment].
Camera: [movement]. SFX: [cue]. Constraints: [preservation items].
```

**Example:**
```
Define the man in black trench coat with sunglasses in `Image1` as `Subject1`.
`Video1` controls side-tracking camera rhythm only;
do not transfer performer, interior layout, or brand identity.
`Audio1` controls tempo and energy only.

`Subject1` walks across a wet platform, stops under a flickering sign, turns head left.
Camera: 35mm locked medium-wide, one slow side track.
<rain sounds><footsteps>. (No music).

Constraints: no subtitles, no logos, no watermarks.
```

### FLF2V First/Last Frame

```
`Image1` is the first frame. `Image2` is the last frame.
Preserve the same subject's facial structure, hairstyle, outfit, and scene layout.
Generate a continuous transition from [start state] to [end state].
Motion: [one physical action path]. Camera: [locked medium or one slow push-in].
Lighting: [source and continuity]. Sound: [ambience]. Constraints: [preservation items].
```

**Example:**
```
`Image1` is the first frame. `Image2` is the last frame.
Preserve `Subject1`'s facial structure, hairstyle, jacket, and room layout.
Generate a continuous transition from sitting to standing:
`Subject1` slowly rises from the chair, walks to the window, stops in the final pose.
Camera: locked medium shot, slight push-in. Lighting: same cool window light, warm lamp at end.
<quiet room tone><soft floor creak>.
```

### T2V Text-to-Video

```
[Subject] [action] in [scene]. Camera: [one primary movement].
Lighting: [source and quality]. Style: [tone]. Constraints: [exclusions].
```

### V2V Edit

```
Edit `Video1`, change [original feature] to [new feature].
Unmentioned elements remain unchanged by default.
Constraints: no subtitles, no logos.
```

### V2V Extend

```
Extend `Video1` backward/forward, [subject] continues [action].
Audio-visual style, subject, and narrative remain consistent.
Constraints: no subtitles, no logos, no watermarks.
```

---

## Role Mapping Patterns

| Asset Type | Recommended Roles | Avoid |
|---|---|---|
| Image | identity, product, pose, costume, environment, first frame, last frame | Asking it to define unseen motion |
| Video | motion, camera, rhythm, blocking, timing | Copying protected identity, logo, or scene |
| Audio | tempo, pacing, atmosphere, tone, music texture | Assuming voice/song/portrait authorization |

**Core rules:**
- Each reference asset gets one primary role; do not layer additional style descriptions
- Explicitly declare "what must preserve" and "what must not transfer"
- When authorization is unclear, only transfer generalized motion/rhythm/atmosphere, not protected identity
- When audio and video conflict: mute the video or declare video controls camera/motion only

---

## I2V Failure Fixes

| Failure | Fix |
|---|---|
| Identity drift | Reduce new visual descriptions, strengthen preservation constraints; place face reference early |
| Camera jumps | Use one camera movement, note start and end frames |
| Product deformation | Declare preserved static identity, no shape change |
| Static image | Add one physical action and one time cue |
| Background change | Preserve environment layout, only animate lighting/weather/atmosphere |
| Hand deformation | Simplify hand motion or exclude hands from main action |
| ID drift / face-swap | Use separate face close-up + full-body reference images |
| Twin/duplicate problem | Define subjects clearly with binding, add global constraint prohibiting identical duplicates |

---

## Compression Rules

When prompts are too long, trim in this order:

**Delete:** repeated style adjectives → generic quality words → background details visible in references → secondary camera moves → secondary actions → speculative emotion labels

**Keep:** reference tags and roles → subject/product identity → action verb + visible endpoint → one camera movement → physical light source or atmosphere → sound cue → safety/continuity constraints

**Compact Chinese I2V template:**
```
`图片1`为参考，严格保持[主体]不变；仅加入[动作/光线/镜头]。音效：[提示]。约束：[不变项]。
```

---

## Common Scene Adaptations

### Fashion / Apparel Videos
- Role mapping is mandatory: `` `Image1` `` locks color/print/fit
- Fabric dynamics (folds, sway) must be described
- Back constraint: solid color, no print, no text
- Music: lo-fi hip-hop / chill trap, BPM 90-110
- Prioritize Chinese compression, within 500 characters

### Product Showcase Videos
- Product image locks appearance, background image locks environment
- Camera: push-in / orbit / detail, one primary movement
- **Let light/particles/camera move around the product, not deform the product itself**

### Narrative Short Films
- Character image locks identity, storyboard image (if used) locks narrative pacing
- Emotion evolves, never resets
- One segment = one beat = one emotional turn

### Multi-Character Scenes
- Each character independently defined with reference binding (`` Define [traits] in `ImageN` as `SubjectN` ``)
- Declare spatial relationships remain unchanged
- Add end constraint: `prohibit characters with identical appearance, outfit, or accessories; prohibit duplicate/twin effects`
- When reference characters exceed 4: generate in groups (split into images, then combine for video)

---

## Asset Configuration Strategy

Recommended total of 4-5 assets: 1-2 character images (face close-up + full-body separate) + 1 scene image + 1 camera reference video + 1 audio clip. Do not max out the asset limit — too many assets confuse feature priority.

---

## Troubleshoot Diagnostic

Diagnose the failure cause before rewriting. Do not simply add more adjectives. Identify whether the failure comes from mode mismatch, overload, ambiguity, fragile identity lock, unsafe wording, unsupported operation, or missing preservation constraints.

| Symptom | Root cause | First repair |
|---|---|---|
| Product/face changes | I2V prompt re-described visible identity or overloaded motion | Add preservation constraints (`strictly preserve [subject] unchanged`); remove duplicate static detail |
| Camera jumps | Multiple incompatible moves specified, or no clear endpoint | Choose one camera movement, specify start and end points |
| Static image / motion ignored | Prompt too static, no visible consequence | Add subject, verb, time cue, and changed end state |
| Lip-sync misaligned | Camera movement, dialogue too long, speaker not specified | Lock framing, shorten line, explicitly assign speaker |
| VFX noisy | Effect has no source, physics, or dissipation | Add source, material, path, interaction, and endpoint |
| Prompt blocked | Protected IP, real-person, graphic, or evasion wording | Rewrite intent in safe production language without circumvention |
| Extension quality degrades | No last-frame anchor, too many new variables across continuations | Use returned last frame as new first frame, change only one variable |
| Audio reference ignored | Competing video sound, no visual beat mapping | Mute competing video, map one visible event to the beat |
| Text/logo breaks | Small text asked to move or be redrawn | Keep text static, centered, protected; animate light around it |
| Generic / style-less output | Hollow style words, weak action description | Replace with physical action, light source, material, and sound |

**Conservative retry template:**
```
[Reference role if applicable]. Strictly preserve [identity/product/environment].
One visible action: [specific verb + consequence]. Camera: [single movement].
Lighting: [physical source]. Sound: [ambience/SFX/dialogue]. Constraints: [preservation items].
```

**Escalation rules:** If the same error repeats → split into shorter clips, reduce character count, simplify hand/face motion, strengthen role mapping, or switch mode. For edit/extend failures, preserve the source clip first and change only the failing layer. If the platform returns last frames, use that still as the next extension's first-frame anchor.

---

## Camera Selection Guide

Use one clear camera idea. The best camera direction has a start frame, movement, speed, subject relationship, and endpoint. Avoid stacking contradictory moves in a single 5-second shot.

**Move matching table:**

| Need | Recommended move | Example |
|---|---|---|
| Lip-sync / product identity / delicate VFX | Locked-off | `locked medium shot, focus stays on product label` |
| Discovery / emotional realization | Dolly-in | `slow dolly-in from medium close-up to facial close-up as Character A lowers the envelope` |
| Travel / pursuit / product motion | Tracking | `smooth lateral track, following subject through scene` |
| Scale / arrival / reveal | Crane / drone | `low-angle crane up from boots to skyline, ending behind character's shoulder` |
| Realism (precision secondary) | Handheld | `subtle handheld breathing sway, subject kept centered` |
| Subject clear from all angles | Orbit | `slow orbit halfway around subject, from front to back` |

**Lens focal length anchors:** `24mm wide spatial energy`, `35mm natural street perspective`, `50mm portrait compression`, `85mm shallow close-up`, `macro lens material detail`. Pair lens words with subject distance and motion; do not stack lens numbers as decoration.

**Conflict rule:** If user gives multiple incompatible moves → choose one primary move, put the rest in optional variants. Multi-beat needs → split into separate clips or time-segmented prompts.

**Multi-character camera anchoring:** `Camera holds Character A in foreground while Character B crosses behind`. For I2V, preserve image composition unless user explicitly wants reframing. For video reference, declare: `` `Video1` controls camera rhythm only; do not transfer performer, room, logo, or identity ``.

---

## Character Contract

Character prompts must remove ambiguity before adding style.

### Character Tags

Assign each character a stable tag: `Character A`, `Character B`, `Subject1`. After more than one character appears, do not use ambiguous pronouns.

| Field | Prompt usage |
|---|---|
| Tag | `Character A` or `Subject1` |
| Identity anchor | Age range, silhouette, hair, outfit, authorized reference role |
| Position | Foreground/background, left/right, seated/standing |
| Action | One assigned verb and endpoint |
| Expression | Observable behavior: blink, glance, smile, grip, pause |
| Constraint | What must stay unchanged |

### Multi-Character Blocking

Assign actions separately:
- ✅ `Character A lowers the envelope; Character B remains in the doorway`
- ❌ `They argue intensely` — the model needs to know who does what

Contact scenes: describe contact point and endpoint. Crowd scenes: identify the hero subject, keep background motion simple.

### Hand and Face Stability

- Keep hands visible but simple
- Avoid rapid finger actions
- Avoid face-touching during dialogue
- Lock camera for lip-sync or portrait preservation
- Use props to convey emotion when facial precision is fragile

### Likeness Rule

Do not infer consent from an uploaded asset for real-person likeness. When authorization is unclear → rewrite to an original character archetype while preserving the scene function.
