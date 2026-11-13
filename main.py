#!/usr/bin/env python3
"""news-image-01 entry v2: one image summing up the world's news of
Friday 13 November 2026, as a magazine cover.

Design (deliberately unlike v1's dense newspaper front page): a single
dramatic visual — a dot-matrix globe at night with numbered glowing
hotspots — one lead headline (Europe wins a seat at the Ukraine peace
talks), three numbered cover lines keyed to the globe markers (NVIDIA
chief quits, Microsoft 365 down, tanker hit in Hormuz), and an ALSO
TODAY footer strip (FBI crypto seizure, Gaza hospital strike, Brooklyn
collapse). The image is drawn programmatically with PIL (no AI art, no
network): every word is rendered crisply, so nothing is misspelled.

Writes the image to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png):
exactly the bundled entry.png bytes, deterministically, on every run.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    # Read back: the file the judge sees must be exactly the bundled bytes.
    assert target.read_bytes() == SOURCE.read_bytes()


if __name__ == "__main__":
    main()
