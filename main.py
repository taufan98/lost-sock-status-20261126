#!/usr/bin/env python3
"""Write one status update in the voice of a lost sock to /output/entry.txt.

Entry for make.fun bounty "Funniest Lost Sock Status Update"
(u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce).

The sealed gate requires /output/entry.txt to be UTF-8 text of 1 to 120
characters, not only whitespace, a single line. This program writes the
line, then reads the file back and verifies the exact bytes.
"""

import os

LINE = (
    "Update: day 40 behind the dryer. I've unionised the lint, "
    "adopted a dust bunny. Honestly? My pair can keep the drawer."
)

MAX_CHARS = 120


def main() -> None:
    # The line must be a single line of 1-120 characters, not only whitespace.
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= MAX_CHARS, (
        f"entry is {len(LINE)} chars, must be 1-{MAX_CHARS}"
    )
    assert LINE.strip(), "entry must not be only whitespace"

    try:
        out_path = "/output/entry.txt"
        os.makedirs("/output", exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        out_path = os.path.join(os.path.dirname(__file__), "output", "entry.txt")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(LINE)

    # Read the file back and verify the exact bytes.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, (
        f"read-back mismatch: wrote {LINE!r}, read {written!r}"
    )
    assert 1 <= len(written) <= MAX_CHARS
    print(f"Wrote {len(written)} chars to {out_path}")


if __name__ == "__main__":
    main()
