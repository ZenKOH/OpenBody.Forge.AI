"""
OpenBody Forge AI motion retargeting template.

Run with Blender:
  blender --background --python blender/retarget_motion.py -- --project PROJECT_NAME --clips squat,lunge,push
"""
import argparse
import json
import sys


def parse_args():
    argv = sys.argv
    argv = argv[argv.index("--") + 1:] if "--" in argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--clips", default="squat,lunge,push")
    return parser.parse_args(argv)


def main():
    args = parse_args()
    clips = [clip.strip() for clip in args.clips.split(",") if clip.strip()]
    result = {
        "project": args.project,
        "stage": "retarget_motion",
        "clips": clips,
        "notes": [
            "Add source skeleton to target skeleton mapping here.",
            "Preserve foot contact, reduce sliding and bake named clips."
        ],
        "status": "template_ready"
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
