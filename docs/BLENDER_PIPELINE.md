# Blender Pipeline

## Goal

Convert a licence-cleared human model into an app-ready GLB avatar with named exercise animation clips.

## Command flow

```bash
blender --background --python blender/import_makehuman.py -- --project sample --source LOCAL_SOURCE
blender --background --python blender/validate_rig.py -- --project sample
blender --background --python blender/retarget_motion.py -- --project sample --clips squat,lunge,push
blender --background --python blender/export_glb.py -- --project sample --output assets/3d/adult_neutral.glb
```

## Manual Blender steps still required in v0.1

- Import the MakeHuman/GLB/FBX/OBJ source model.
- Confirm clothing and texture licences.
- Confirm skeleton and mesh weights.
- Retarget or keyframe exercise clips.
- Export as binary GLB.

## Future automation

The next build should extend the scripts with `bpy` import operators, armature checks, retarget maps, GLB export settings and manifest writing.
