#!/usr/bin/env python3
"""Write one short two-line micro poem about light and morning to entry.txt."""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "The cat has not moved since six.\n"
    "The square of light has, and takes her with it."
)


def output_dir() -> Path:
    """Return the output folder.

    MAKEFUN_OUTPUT_DIR wins when set, then OUTPUT_DIR, then /output.
    """
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    directory = output_dir()
    directory.mkdir(parents=True, exist_ok=True)

    destination = directory / "entry.txt"
    destination.write_bytes(TEXT.encode("utf-8"))

    print(f"wrote {destination} ({len(TEXT)} characters)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
