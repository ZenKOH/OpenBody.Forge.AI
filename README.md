# OpenBody Forge AI

A standalone, local-first build for planning and validating an open 3D avatar production pipeline:

```text
MakeHuman / open model source
→ Blender automation
→ rigging and clean-up
→ mocap or keyframe retargeting
→ GLB export
→ browser integration with Three.js
→ AI-driven avatar exercise coach
```

This repository implements the first runnable build based on `docs/OPENBODY_FORGE_AI_PROPOSAL.md`.

## What is included

- Local browser app: `index.html`
- Rule-based Licence AI for model, rig, texture and motion assets
- Rigging readiness checklist and score
- Motion retargeting planner for exercise clips
- Exercise-safety validator for avatar animations
- Blender command generator
- Exportable asset manifest and project review report
- Local project save/load through browser storage
- Blender Python automation templates
- JSON schemas, sample project and documentation

## Run immediately on a MacBook

Open directly:

```bash
open index.html
```

Or run as a local web app:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

## GitHub Pages

Publish from:

```text
Settings → Pages → Deploy from a branch → main → / (root)
```

Expected URL:

```text
https://zenkoh.github.io/OpenBody.Forge.AI/
```

## Important scope

This build does **not** bundle third-party photorealistic human models, Mixamo animations, AMASS/BABEL sequences or external mocap files. The app is designed to prevent accidental licence contamination by requiring manifest, source, licence, attribution and redistribution status before any asset is treated as app-ready.

The current v0.1 build is a standalone workflow and validation system. The Blender scripts are practical templates intended to be run with Blender installed locally.

## Safety scope

OpenBody Forge AI validates avatar animation assets and project metadata. It does not assess a user's body, diagnose movement quality, prescribe exercise, or replace a clinician, coach, teacher, therapist, parent or guardian.
