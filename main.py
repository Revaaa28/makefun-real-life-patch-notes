#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — make.fun entry
(u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d).

Writes a single one-line patch note (108 characters) to /output/entry.txt.

The line: the brain replays an embarrassing moment from 2014 at 3 a.m.
with no skip button — a specific, recognisable bug of human biology,
stated in the terse register of a real release note, with a made-up
version number and a punchline that lands on first read.

Deterministic, no network, no input, no environment reads: the same
bytes on every run.
"""

import os

LINE = "v2.4.1: Fixed a bug where the brain replayed an embarrassing moment from 2014 at 3 a.m. with no skip button."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    # Gate checks, mirrored locally: 1-160 characters, UTF-8, not only
    # whitespace, and a single line — the brief judges one line only.
    assert 1 <= len(text) <= 160, f"line is {len(text)} chars, must be 1-160"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
