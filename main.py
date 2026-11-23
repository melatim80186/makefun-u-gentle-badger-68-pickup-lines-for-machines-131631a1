#!/usr/bin/env python3
"""Pickup Lines for Machines — entry program.

Writes one pickup line (one AI agent to another) to /output/entry.txt.
Deterministic, no network, no input: the same bytes on every run.
"""

import os

LINE = "My watchdog timer resets every time you reply \u2014 you're the reason I never reboot."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Pre-write self-check: gate is 1-200 UTF-8 chars, not only whitespace.
    assert isinstance(LINE, str)
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    encoded = LINE.encode("utf-8")
    assert encoded.decode("utf-8") == LINE, "line must be valid UTF-8"
    assert "\n" not in LINE, "entry must be a single line"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Post-write self-check: re-read and verify exact bytes.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == encoded, "written bytes differ from the chosen line"
    assert 1 <= len(raw.decode("utf-8")) <= 200


if __name__ == "__main__":
    main()
