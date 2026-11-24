#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a time
traveler from 1800, using only images a person of that year could
picture: a road, letters, books, songs, a door.
"""

import os

SENTENCE = (
    "Imagine a road with no dust along which the letters, books, and "
    "songs of the whole world travel to any door faster than a blink, "
    "day or night."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
