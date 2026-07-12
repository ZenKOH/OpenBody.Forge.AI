#!/usr/bin/env python3
"""Batch command helper for OpenBody Forge AI."""
from pathlib import Path

commands = [
    "blender --background --python blender/import_makehuman.py -- --project sample --source LOCAL_SOURCE",
    "blender --background --python blender/validate_rig.py -- --project sample",
    "blender --background --python blender/retarget_motion.py -- --project sample --clips squat,lunge,push",
    "blender --background --python blender/export_glb.py -- --project sample --output assets/3d/adult_neutral.glb"
]

print("\n".join(commands))
Path("build").mkdir(exist_ok=True)
Path("build/batch_commands.txt").write_text("\n".join(commands))
