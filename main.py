"""The Long Roast — one line roasting my own AI agent.

Writes the roast to /output/entry.txt. Standard library only,
deterministic: two runs write the same bytes. The output path is
fixed by the competition, so it never depends on the working
directory; the roast text lives in this file, next to the code.
"""

import os

ROAST = (
    "My agent burned 40,000 tokens reading my own notes, spawned "
    "three subagents to think about them, then asked me to confirm "
    "what I'd already confirmed twice."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    assert text.strip(), "roast must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
