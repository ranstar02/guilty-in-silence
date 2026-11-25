"""Guilty in Silence — One-Line Laugh-Off entry.

Writes a single fixed one-line joke to /output/entry.txt.
Fully deterministic: no randomness, no network, no environment reads,
no dependencies.
"""

import os

JOKE = "My meditation app costs $15 a month, and the only thing it taught me is how to feel guilty in silence — more efficiently."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    joke = JOKE
    assert 1 <= len(joke) <= 200, "joke must be 1-200 characters"
    assert joke.strip(), "joke must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(joke)
    # Verify the write: read back and confirm byte-identical content.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        assert f.read() == joke, "written entry does not match JOKE"


if __name__ == "__main__":
    main()
