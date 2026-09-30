"""Grade calculator used in the ICS 499 CI/CD live demo.

The grading scale lives in ONE file, site/grading_scale.json.
Both this Python code and the website (site/index.html) read it,
so the scale is never written twice (DRY).
"""

import json
from pathlib import Path

# Path to the shared grading-scale file (../site/grading_scale.json)
SCALE_FILE = Path(__file__).resolve().parent.parent / "site" / "grading_scale.json"


def load_cutoffs() -> list[tuple[float, str]]:
    """Read the grading scale and return (minimum %, letter) pairs."""
    data = json.loads(SCALE_FILE.read_text(encoding="utf-8"))
    return [(row["min"], row["letter"]) for row in data["cutoffs"]]


CUTOFFS = load_cutoffs()


def letter_grade(percent: float) -> str:
    """Return the letter grade for a percentage from 0 to 100."""
    if not 0 <= percent <= 100:  # reject bad input early
        raise ValueError("percent must be between 0 and 100")
    for minimum, letter in CUTOFFS:  # checked from highest to lowest
        if percent >= minimum:
            return letter
    return "F"  # anything below the lowest cutoff
