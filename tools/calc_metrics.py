#!/usr/bin/env python3
"""Keep the original calculator CLI available from the repository."""

from pathlib import Path
import runpy


if __name__ == "__main__":
    script = (
        Path(__file__).resolve().parents[1]
        / "skills" / "boji-diagnosis" / "scripts" / "calc_metrics.py"
    )
    runpy.run_path(str(script), run_name="__main__")
