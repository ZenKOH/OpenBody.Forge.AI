"""
OpenBody Forge AI Blender automation template.

Run with Blender:
  blender --background --python blender/import_makehuman.py -- --project PROJECT_NAME --source SOURCE_NOTE

This script does not download assets or assume redistribution rights.
"""
import argparse
import json
import sys
from pathlib import Path


def parse_args():
    argv = sys.argv
    argv = argv[argv.index("--") + 1:] if "--" in argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--source", default="")
    return parser.parse_args(argv)


def main():
    args = parse_args()
    project_dir = Path("build") / args.project
    project_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "project": args.project,
        "source": args.source,
        "stage": "import",
        "notes": [
            "Import MakeHuman/OBJ/FBX/GLB manually or extend this script with bpy import operators.",
            "Verify clothing, hair and texture licences before redistribution."
        ]
    }
    (project_dir / "import_manifest.json").write_text(json.dumps(manifest, indent=2))
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
