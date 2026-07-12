---
title: OpenBody Forge AI Proposal
status: concept proposal
version: 0.1.0
updated: 2026-07-12
repository: ZenKOH/OpenBody.Forge.AI
---

# Proposal: OpenBody Forge AI

## A standalone AI-driven pipeline for open 3D body modelling, rigging, motion retargeting, GLB export and browser avatar integration

## Table of contents

1. [Executive concept](#1-executive-concept)
2. [Product purpose](#2-product-purpose)
3. [Why this should be standalone and local-first](#3-why-this-should-be-standalone-and-local-first)
4. [Recommended asset strategy](#4-recommended-asset-strategy)
5. [Motion-capture and animation strategy](#5-motion-capture-and-animation-strategy)
6. [Technical architecture](#6-technical-architecture)
7. [AI modules](#7-ai-modules)
8. [User experience](#8-user-experience)
9. [Integration with Avatar Bodyweight Coach](#9-integration-with-avatar-bodyweight-coach)
10. [Minimum viable product](#10-minimum-viable-product)
11. [Development roadmap](#11-development-roadmap)
12. [Repository structure](#12-repository-structure)
13. [Key risks and controls](#13-key-risks-and-controls)
14. [Strategic recommendation](#14-strategic-recommendation)

## 1. Executive concept

**OpenBody Forge AI** would be a standalone MacBook application that converts open or licence-cleared human body models into animated, browser-ready exercise avatars.

The core pipeline is:

```text
MakeHuman / open model source
→ Blender automation
→ rigging and clean-up
→ mocap or keyframe retargeting
→ GLB export
→ browser integration with Three.js
→ AI-driven avatar exercise coach
```

The first production route should use **MakeHuman → Blender → GLB → Three.js**. MakeHuman is the most practical starting point because it is open-source and exported models from official MakeHuman versions are commonly treated as CC0 under an export exception, making them suitable for broad use, including commercial and GitHub-distributed projects, subject to verifying the exact exported assets and any clothing, hair or texture dependencies. ([Wikipedia][1])

The longer-term roadmap should also watch **Anny Body Model**, because the authors describe it as an open, differentiable, scan-free parametric human body model released under Apache 2.0. That makes Anny strategically attractive for future AI body modelling, but it should be treated as a research-forward route until tooling, examples and browser export workflows mature. ([arXiv][2])

## 2. Product purpose

The app should solve a practical gap: many avatar exercise apps either use weak cartoon avatars, closed commercial assets, or proprietary pipelines that cannot be redistributed cleanly. OpenBody Forge AI would instead make the asset pipeline transparent, local-first and auditable.

The intended user is not a professional 3D artist. The user should be able to:

1. Choose or generate an adult human model.
2. Apply clothing and safe neutral presentation.
3. Rig or validate the skeleton.
4. Import or select exercise motion clips.
5. Retarget movement to the selected avatar.
6. Review joint motion, range and safety cues.
7. Export a browser-ready `.glb`.
8. Load the avatar into a web app such as **Avatar Bodyweight Coach**.
9. Attach voice instructions, exercise metadata and licence notes.

The product should prioritise **safe movement education**, not appearance optimisation. It should not rate a user’s body, suggest body ideals, or use aesthetic scoring. Avatar controls should be framed around function, clarity, representation and rigging compatibility.

## 3. Why this should be standalone and local-first

A local Mac app is the right architecture because the workflow touches large assets, licence-sensitive files and possible future human motion data. Keeping the pipeline local reduces privacy exposure and avoids forcing users to upload models, motion clips or training assets to a cloud service.

The proposed app should therefore run as:

```text
Mac desktop shell
+ local project database
+ Blender automation layer
+ local AI assistants
+ browser-based 3D preview
+ exportable GLB package
```

The first version can be implemented as a **Tauri or Electron desktop app** with a local Python/Blender worker. Tauri is lighter, but Electron may be easier if the team wants rapid integration with web tooling. Blender should initially be detected as a local dependency rather than silently bundled, because bundling Blender increases installer size and requires careful licence/documentation handling.

## 4. Recommended asset strategy

### 4.1 Primary route: MakeHuman

MakeHuman should be the first route because it can generate adult human variants, is free/open-source, and its official exported models are commonly described as CC0 via an export exception. ([Wikipedia][1])

Recommended MakeHuman use:

```text
Use for:
- first production avatars
- adult neutral exercise models
- male/female/neutral templates
- clothed bodyweight exercise characters
- GitHub-friendly demo assets, after export and dependency review

Avoid:
- unverified third-party community clothing
- unverified hair/texture assets
- over-specific real-person likenesses
- child/minor avatars
- appearance-ranking features
```

The app should include a **MakeHuman Import Wizard**:

```text
Step 1: Select exported MakeHuman file
Step 2: Verify licence metadata
Step 3: Check mesh scale and orientation
Step 4: Validate clothing and hair assets
Step 5: Convert to Blender project
Step 6: Apply standard exercise skeleton
Step 7: Export clean GLB
```

### 4.2 Future route: Anny Body Model

Anny is promising because it is described as a differentiable, interpretable body model grounded in anthropometric knowledge, with code released under Apache 2.0. ([arXiv][2])

Recommended Anny use:

```text
Use for:
- future open parametric body modelling
- research-grade synthetic avatar generation
- controlled model diversity
- automated body-shape testing across rigs and animations

Do not rely on it for MVP:
- tooling may be less mature than MakeHuman
- Blender export workflow may require custom engineering
- asset pipeline needs validation
```

### 4.3 Research route: VALID Avatar Library

VALID is useful because it was designed as a freely available 3D avatar library with inclusion and diversity in mind; the paper describes 210 fully rigged avatars and a validation study with participants from 33 countries. ([arXiv][3])

Recommended VALID use:

```text
Use for:
- diversity/inclusion reference
- research prototypes
- perception testing
- representation benchmarks

Do not bundle until:
- package licence is reviewed
- redistribution terms are confirmed
- file formats and rig compatibility are tested
```

### 4.4 Caution route: MB-Lab

MB-Lab is powerful inside Blender and supports realistic humanoid generation, but it carries heavier GPL/AGPL-style licensing considerations. Its generated characters have been described as AGPL derivatives of AGPL data, meshes and textures, which makes it less clean for a permissively distributed GitHub demo app. ([Wikipedia][4])

Recommended MB-Lab use:

```text
Use for:
- internal experiments
- non-distributed prototypes
- Blender workflow comparison
- rigging and morphology research

Avoid for:
- first public GitHub demo
- commercial-ready bundled assets
- unclear downstream redistribution
```

### 4.5 Utility route: Mixamo

Mixamo is useful as a rigging and animation service, and it has been widely used for automatic rigging and motion clips. But it is Adobe-owned and not open-source, so it should be treated as a workflow tool rather than a source of open assets to bundle in the repository. ([Wikipedia][5])

Recommended Mixamo use:

```text
Use for:
- manual rigging experiments
- compatibility testing
- animation quality benchmarks
- non-bundled developer workflow

Do not:
- claim Mixamo is open-source
- bundle Mixamo downloads without Adobe terms review
- make Mixamo mandatory for the open-source pipeline
```

## 5. Motion-capture and animation strategy

The MVP should not begin with fully AI-generated exercise motion. It should begin with a curated library of reviewed exercise clips.

The motion pipeline should support three categories:

```text
A. Hand-authored Blender keyframe clips
B. Open or licence-cleared BVH/FBX mocap clips
C. Future AI-assisted motion synthesis and correction
```

For research datasets, **AMASS** is important because it unifies many marker-based mocap datasets into a common body representation and includes more than 40 hours of motion data. However, it should be treated as a research/reference source because underlying dataset licences vary. ([arXiv][6])

**BABEL** is also useful because it adds language labels to AMASS motion sequences, with over 28,000 sequence labels and 63,000 frame labels across more than 250 action categories. That can help the app map movement labels to exercise categories, but again it should be reviewed carefully before bundling assets. ([arXiv][7])

## 6. Technical architecture

### 6.1 Application layers

```text
Layer 1 — Desktop shell
Tauri or Electron app for MacBook, with local project files and UI.

Layer 2 — AI workflow controller
Local assistant that guides asset selection, licence checks, rigging steps, exercise mapping and export validation.

Layer 3 — Blender automation worker
Python scripts executed through Blender to import models, clean meshes, apply rigs, retarget motion and export GLB.

Layer 4 — Asset registry
Local manifest tracking source, licence, attribution, file hashes, modifications and export status.

Layer 5 — Motion and safety validator
Checks animation clips against joint limits, foot contact, spine angle, hand placement, speed and exercise-stage definitions.

Layer 6 — Browser avatar runtime
Three.js viewer that loads GLB files, selects animation clips and synchronises voice instructions with movement stages.

Layer 7 — Exercise app integration
Exports a package consumable by Avatar Bodyweight Coach or any browser app.
```

### 6.2 Why GLB is the right export format

GLB is the binary form of glTF. glTF is an open standard for 3D scenes and models, supports geometry, appearance, hierarchy and animation, and `.glb` can package the asset into a compact binary file suitable for browser delivery. ([Wikipedia][8])

This makes GLB the right app-ready format:

```text
avatar_adult_neutral.glb
avatar_adult_male.glb
avatar_adult_female.glb
exercise_squat.glb
exercise_pushup.glb
exercise_lunge.glb
```

The browser viewer should use **Three.js**, because the Three.js documentation includes animation support through `AnimationMixer` and its ecosystem supports GLTF loading. ([threejs.org][9])

## 7. AI modules

The app should be AI-driven, but the AI should assist the pipeline rather than make unsafe claims about exercise correctness.

### Module A — Licence AI

Purpose: prevent accidental redistribution of restricted assets.

Inputs:

```json
{
  "source_url": "",
  "asset_type": "model | rig | texture | motion",
  "declared_licence": "",
  "attribution_required": true,
  "redistribution_allowed": "unknown"
}
```

Outputs:

```text
- Safe to bundle
- Safe for local-only use
- Needs attribution
- Do not redistribute
- Licence review required
```

This module is critical because software licences, model licences and dataset licences can conflict. Recent research on model licensing notes that reused components from different sources may carry different rights and compliance obligations. ([arXiv][10])

### Module B — Avatar Build Assistant

Purpose: guide model selection and prepare Blender instructions.

Functions:

```text
- choose adult neutral / male / female template
- validate mesh scale
- detect missing textures
- flag unclothed or inappropriate assets
- normalise orientation
- generate Blender import script
- create project manifest
```

### Module C — Rigging Assistant

Purpose: assess and improve skeletal readiness.

Checks:

```text
- skeleton present
- humanoid bone names mapped
- shoulder, elbow, hip, knee and ankle joints identified
- mesh weights exist
- hands and feet deform acceptably
- neck and spine have safe ranges
```

Outputs:

```text
- rig status score
- missing bone list
- suggested Blender fixes
- retarget readiness
```

### Module D — Motion Retargeting Assistant

Purpose: convert source motion into avatar-specific animation.

Functions:

```text
- map source skeleton to target skeleton
- apply inverse kinematics constraints
- preserve foot contact
- reduce sliding
- smooth joint rotation
- segment movement into stages
- export named animation clips
```

Target named clips:

```text
squat
lunge
bridge
push
plank
deadbug
balance
cardio
stretch
inchworm
burpee
calf
row
```

### Module E — Exercise Safety Validator

Purpose: validate avatar motion, not the user’s body.

It should check whether the animation itself demonstrates reasonable form:

```text
- knees do not collapse inward in squat/lunge demo
- back does not hyperextend in bridge
- push-up alignment remains clear
- plank is not overarched
- movement speed is slow enough for learning
- exercise has easier option
- demo includes stop / pause / voice-off controls
```

This validator should not claim clinical correctness. It should label outputs as:

```text
Educational demo
Needs review
Unsafe-looking animation
Licence incomplete
Ready for app integration
```

### Module F — Voice and Instruction Generator

Purpose: convert exercise stages into audio-ready scripts.

Example:

```json
{
  "exercise": "Bodyweight Squat",
  "stage_1": "Stand tall with feet hip to shoulder width.",
  "stage_2": "Send the hips back and bend the knees slowly.",
  "stage_3": "Pause at a comfortable depth. Keep knees tracking over toes.",
  "stage_4": "Press through the whole foot and return to standing."
}
```

The voice engine can use browser speech synthesis for the lightweight app, with optional offline TTS later.

## 8. User experience

### 8.1 Main screens

```text
1. Project Home
Create or open avatar pipeline project.

2. Model Source
Choose MakeHuman, imported GLB/FBX/OBJ, VALID, Anny future route, or manual model.

3. Licence Check
Record source, licence, attribution, redistribution and modification status.

4. Blender Build
Run import, clean-up, rigging and export tasks through Blender.

5. Motion Library
Import, label and review exercise motion clips.

6. Retarget Studio
Apply motion to avatar and inspect stage-by-stage movement.

7. Safety Review
Check animation quality and educational clarity.

8. Browser Preview
Load GLB through Three.js and test animation playback.

9. Export Package
Generate app-ready GLB, JSON metadata, voice script and manifest.

10. Integration
Copy package into Avatar Bodyweight Coach or another browser app.
```

### 8.2 Asset manifest

Every exported avatar should include:

```json
{
  "asset_id": "adult_neutral_makehuman_v001",
  "model_source": "MakeHuman official export",
  "model_licence": "CC0 export exception - verified",
  "clothing_source": "MakeHuman default clothing",
  "texture_source": "MakeHuman default texture",
  "rig_source": "Blender generated humanoid rig",
  "motion_source": "hand-authored Blender keyframes",
  "redistribution_status": "approved",
  "review_status": "educational demo reviewed",
  "export_format": "glb",
  "animation_clips": ["squat", "lunge", "bridge"],
  "created": "YYYY-MM-DD"
}
```

## 9. Integration with Avatar Bodyweight Coach

The current Avatar Bodyweight Coach can be upgraded into a true 3D app by adding:

```text
/assets/3d/
  adult_neutral.glb
  adult_male.glb
  adult_female.glb
  exercises/
    squat.glb
    lunge.glb
    push.glb

/assets/3d/manifest.json
/js/three-avatar-viewer.js
/js/exercise-animation-map.js
```

Browser runtime:

```text
Three.js scene
→ load GLB avatar
→ read animation clips
→ map exercise card to clip name
→ play / pause / stop
→ sync voice cue timing
→ fall back to SVG avatar if GLB fails
```

The fallback matters. Even with GLB integration, the app should retain the current SVG avatar so the app still works if a 3D asset is missing, too large, corrupted or not licence-cleared.

## 10. Minimum viable product

### MVP goal

A Mac app that can take one MakeHuman adult avatar, one manually reviewed squat animation, export it as GLB, and load it in a browser viewer with voice cues.

### MVP scope

```text
- Mac desktop shell
- MakeHuman asset import
- Blender path detection
- Blender Python script runner
- licence manifest editor
- one rig validation check
- one retargeting route
- three exercise clips: squat, lunge, push-up
- GLB export
- Three.js preview
- Avatar Bodyweight Coach integration
```

### MVP exclusions

```text
- no cloud model generation
- no automatic medical assessment
- no user camera analysis
- no body scoring
- no unverified third-party bundled models
- no Mixamo asset bundling until Adobe terms are reviewed
```

## 11. Development roadmap

### Phase 1 — Research and compliance foundation, 2–3 weeks

Deliverables:

```text
- asset-source policy
- MakeHuman export workflow
- licence manifest schema
- Blender automation proof of concept
- GLB viewer prototype
- safety review checklist
```

### Phase 2 — Local Blender pipeline, 4–6 weeks

Deliverables:

```text
- Blender worker scripts
- import/clean/export pipeline
- rig validation assistant
- adult neutral / male / female MakeHuman templates
- GLB export package
```

### Phase 3 — Motion retargeting and exercise library, 6–8 weeks

Deliverables:

```text
- retargeting workflow
- first 12 exercise clips
- stage segmentation
- stop/pause/replay controls
- voice cue timing
- browser preview validation
```

### Phase 4 — AI quality layer, 6–8 weeks

Deliverables:

```text
- licence AI assistant
- rig quality assistant
- motion quality validator
- exercise cue generator
- safety flag dashboard
- export readiness score
```

### Phase 5 — Production integration, 6–10 weeks

Deliverables:

```text
- Avatar Bodyweight Coach 3D runtime
- Three.js GLB viewer
- AnimationMixer-based clip switching
- packaged 3D avatar assets with manifests
- GitHub Pages-compatible demo
- Mac installer
```

## 12. Repository structure

Recommended GitHub structure:

```text
OpenBody.Forge.AI/
  index.html
  asset-lab.html
  app.js
  demo-upgrade.js
  three-avatar-viewer.js
  styles.css
  demo-upgrade.css

  /assets/
    /3d/
      README.md
      manifest.schema.json
      adult_neutral.glb
      adult_male.glb
      adult_female.glb

  /blender/
    import_makehuman.py
    validate_rig.py
    retarget_motion.py
    export_glb.py
    batch_export.py

  /motions/
    README.md
    motion_manifest.json
    squat.bvh
    lunge.bvh

  /docs/
    OPEN_3D_ASSETS.md
    LICENCE_POLICY.md
    BLENDER_PIPELINE.md
    RETARGETING_GUIDE.md
    SAFETY_REVIEW.md

  /desktop/
    tauri_or_electron_app/
```

## GitHub implementation notes

This document is intended to live at:

```text
/docs/OPENBODY_FORGE_AI_PROPOSAL.md
```

Any future implementation should keep large or licence-sensitive third-party 3D assets out of the repository until their redistribution rights are verified. Approved assets should be accompanied by a manifest containing source URL, licence, attribution requirements, modification history, file hash and safety review status.


## 13. Key risks and controls

### Risk 1 — Licence contamination

Control:

```text
No asset enters /assets/3d/ without manifest, source URL, licence, attribution and redistribution statement.
```

### Risk 2 — Photorealistic avatar creates false authority

Control:

```text
Every demo states that it is educational, not medical advice or movement assessment.
```

### Risk 3 — Poor retargeting produces unsafe-looking movement

Control:

```text
Every exported animation must pass a movement review checklist before app integration.
```

### Risk 4 — App becomes too large

Control:

```text
Keep only approved demo GLBs in GitHub. Larger asset packs should be optional downloads.
```

### Risk 5 — AI overclaims

Control:

```text
AI is an assistant for pipeline automation, metadata, rig review and cue generation. It does not diagnose, prescribe or assess the user.
```

## 14. Strategic recommendation

The best build path is:

```text
Start with MakeHuman, not Mixamo.
Use Blender as the production engine.
Use GLB as the browser delivery format.
Use Three.js as the runtime viewer.
Use AI to manage rigging, retargeting, licence review and exercise cue generation.
Keep the current SVG avatar as a fallback.
Add true 3D only after model and motion rights are verified.
```

MakeHuman provides the cleanest early asset path. Anny is the most interesting future open body modelling direction. VALID is valuable for inclusive avatar research. MB-Lab is technically strong but licence-heavy. Mixamo is useful for workflow learning but should not be treated as open-source. Three.js and GLB are the right bridge from Blender to a browser-based exercise coach.

The final product should not simply be “an avatar app”. It should be an **open, auditable avatar production pipeline** that turns licence-cleared human models and movement clips into safe, reusable, browser-ready exercise demonstrations.


[1]: https://en.wikipedia.org/wiki/MakeHuman "MakeHuman"
[2]: https://arxiv.org/abs/2511.03589 "Human Mesh Modeling for Anny Body"
[3]: https://arxiv.org/abs/2309.10902 "VALID: A perceptually validated Virtual Avatar Library for Inclusion and Diversity"
[4]: https://en.wikipedia.org/wiki/MB-Lab "MB-Lab"
[5]: https://en.wikipedia.org/wiki/Mixamo "Mixamo"
[6]: https://arxiv.org/abs/1904.03278 "AMASS: Archive of Motion Capture as Surface Shapes"
[7]: https://arxiv.org/abs/2106.09696 "BABEL: Bodies, Action and Behavior with English Labels"
[8]: https://en.wikipedia.org/wiki/GlTF "GlTF"
[9]: https://threejs.org/docs/ "three.js docs"
[10]: https://arxiv.org/abs/2412.11483 "\"They've Stolen My GPL-Licensed Model!\": Toward Standardized and Transparent Model Licensing"
