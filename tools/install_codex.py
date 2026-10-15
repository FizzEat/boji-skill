#!/usr/bin/env python3
"""Copy the complete skill suite into a Codex skill discovery directory."""

import argparse
from pathlib import Path
import shutil


REPO_ROOT = Path(__file__).resolve().parents[1]


def install_skills(destination):
    source_root = REPO_ROOT / "skills"
    destination = Path(destination).expanduser().resolve()
    if destination == source_root or source_root in destination.parents:
        raise ValueError("The destination must be outside the source skills directory.")

    skills = sorted(path.parent for path in source_root.glob("*/SKILL.md"))
    if not skills:
        raise ValueError("No skills found next to this installer.")

    conflicts = [
        destination / skill.name
        for skill in skills
        if (destination / skill.name).exists()
        or (destination / skill.name).is_symlink()
    ]
    if conflicts:
        raise FileExistsError(
            "No skills were copied. These destinations already exist; choose another "
            "--dest or move the previous installations before retrying:\n"
            + "\n".join(str(path) for path in conflicts)
        )

    destination.mkdir(parents=True, exist_ok=True)
    for skill in skills:
        shutil.copytree(
            skill,
            destination / skill.name,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.pyo"),
        )
    return [destination / skill.name for skill in skills]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dest",
        type=Path,
        default=REPO_ROOT / ".agents" / "skills",
        help="Skill discovery directory (default: this repository's .agents/skills).",
    )
    args = parser.parse_args()
    try:
        installed = install_skills(args.dest)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Installation failed: {error}\n")
    print(f"Installed {len(installed)} skills in {installed[0].parent}")
    print("In Codex, type $ and select boji from the skill list, then enter: 新手入门")


if __name__ == "__main__":
    main()
