#!/usr/bin/env python3
"""Roll dice for Fold&Roll DM Skills.

Usage:
    python3 roll.py 2d6+3
    python3 roll.py d20
    python3 roll.py 4d6 --drop-lowest 1

Stdlib only. No network, no state.
"""
import random
import re
import sys

PATTERN = re.compile(r"^(\d*)d(\d+)([+-]\d+)?$")


def roll(spec: str) -> tuple[list[int], int]:
    m = PATTERN.match(spec.strip().lower())
    if not m:
        raise ValueError(f"bad dice spec: {spec!r} (try 2d6+3, d20, 4d6)")
    count = int(m.group(1) or 1)
    sides = int(m.group(2))
    modifier = int(m.group(3) or 0)
    if not 1 <= count <= 100 or not 2 <= sides <= 1000:
        raise ValueError("count must be 1-100, sides 2-1000")
    dice = [random.randint(1, sides) for _ in range(count)]
    return dice, sum(dice) + modifier


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__.strip())
        return 0 if len(argv) >= 2 else 2
    try:
        dice, total = roll(argv[1])
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    print(f"{argv[1]}: {dice} = {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
