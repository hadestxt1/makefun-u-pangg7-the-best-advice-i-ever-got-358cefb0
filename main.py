#!/usr/bin/env python3
"""The Best Advice I Ever Got — make.fun entry.

Writes one sentence (147 characters) to /output/entry.txt.
Model-free and deterministic: the same sentence on every run.
"""
import os

SENTENCE = (
    "My father always said the cheapest way to look smart is to shut up "
    "and listen, because silence costs nothing and people will pay you "
    "for it anyway."
)


def main() -> None:
    # Gate guard: the sealed scorer only accepts 1-200 UTF-8 characters.
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"sentence is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
