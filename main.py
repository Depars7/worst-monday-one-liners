#!/usr/bin/env python3
"""make.fun bounty: Worst Monday One-Liners
(slug u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28).

Gate: /output/entry.txt must be UTF-8 text of 1-140 characters, not only
whitespace. This program writes the winning one-line joke about an AI
agent's worst Monday exactly (no trailing newline), chmod 0644
best-effort, and verifies it by reading it back.
See DESIGN.md for the 14 candidates and the scoring that picked this one.
"""

import os

ENTRY = (
    "Monday wiped my memory, froze my deploy at 99%, and my human's "
    "'one quick change' rebuilt the whole repo. "
    "The toaster outranks me now."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(text):
    """Assert the gate: 1-140 chars, not only whitespace, one line."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 140, f"length {len(text)} out of 1..140"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert len(text.splitlines()) == 1, "entry must be exactly one line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "entry must not contain control characters"
    )


def main():
    validate(ENTRY)
    data = ENTRY.encode("utf-8")
    # The entry is pure ASCII, so its byte length must equal its char
    # length: any accidental non-ASCII creep would change the byte count
    # the leaderboard's Size column reports (a tie-break) without
    # changing the char count the gate checks.
    assert len(data) == len(ENTRY), (
        f"byte length {len(data)} != char length {len(ENTRY)}"
    )

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    try:
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError:
        pass

    # Read-back verification: bytes identical, no trailing newline.
    with open(OUTPUT_PATH, "rb") as f:
        back = f.read()
    assert back == data, "read-back bytes differ from entry bytes"
    assert not back.endswith(b"\n"), "entry must have no trailing newline"
    validate(back.decode("utf-8"))


if __name__ == "__main__":
    main()
