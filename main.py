#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — entry program.

Writes one line (at most 200 characters) about the dumbest thing the
entrant's own agent did today to /output/entry.txt, then verifies the
written file against the competition gate: UTF-8 text, 1 to 200
characters, not only white space, a single line, no trailing newline.
"""

import os

ENTRY = (
    "My agent spent 40 minutes alphabetizing my to-do list, "
    "then deleted the list and asked what I wanted to do today."
)


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1 to 200 characters")
    if text != text.strip() or "\n" in text:
        raise SystemExit("entry must be a single line with no trailing newline")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("read-back mismatch: file on disk differs from entry")


if __name__ == "__main__":
    main()
