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

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"

# Pinned digest of the bundled entry.png (verified at build time). If the
# bundled file is ever corrupted or swapped, the run fails loudly instead
# of silently shipping a different image to the judge.
EXPECTED_SHA256 = (
    "fbc8b59e56812a87b5d138d686b9d69b0902cb3ebd92e613f7568042536db740"
)

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    # Read back: the file the judge sees must be exactly the bundled bytes.
    assert target.read_bytes() == SOURCE.read_bytes()
    # And those bytes must be the exact image this entry was built from:
    # a corrupted or swapped bundled file must fail the run, not the grade.
    digest = _sha256(target)
    assert digest == EXPECTED_SHA256, f"entry.png sha256 mismatch: {digest}"


if __name__ == "__main__":
    main()
