"""
OpenBody Forge AI GLB export template.

Run with Blender:
  blender --background --python blender/export_glb.py -- --project PROJECT_NAME --output assets/3d/adult_neutral.glb
"""
import argparse
import json
import sys


def parse_args():
    argv = sys.argv
    argv = argv[argv.index("--") + 1:] if "--" in argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--output", default="assets/3d/adult_neutral.glb")
    return parser.parse_args(argv)


def main():
    args = parse_args()
    result = {
        "project": args.project,
        "stage": "export_glb",
        "output": args.output,
        "status": "template_ready",
        "next_step": "Run inside Blender after model, rig and animation clips exist. Extend with bpy.ops.export_scene.gltf(...)."
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
