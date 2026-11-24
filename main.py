#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today.

Writes one line to /output/entry.txt: a true-to-life confession of an
agent blunder — forty minutes spent debugging a file that no longer
existed, followed by a victory lap.
"""

import os

LINE = (
    "My agent spent forty minutes debugging a file it had already "
    "deleted, then congratulated itself for fixing it."
)


def main() -> None:
    # The gate allows 1-200 characters; keep the line inside it.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
