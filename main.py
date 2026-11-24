#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second (u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a).

Writes one sentence of at most 200 characters to /output/entry.txt:
a bizarre startup pitch whose business logic survives a second look.
No network, no randomness: every run writes the same bytes so both
graded runs match exactly.
"""
import os

PITCH = (
    "Rent-a-Rooster for chronic oversleepers: a live rescue rooster in your "
    "backyard crows at dawn and cannot be snoozed \u2014 $12/mo, cheaper than "
    "three missed shifts."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    line = PITCH.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line, f"({len(line)} chars)")


if __name__ == "__main__":
    main()
