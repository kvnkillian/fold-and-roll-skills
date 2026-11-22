---
name: dice-roller
description: "Roll dice for D&D 5e: any notation (2d6+3, d20, 4d6 drop lowest), advantage and disadvantage, critical hits and fumbles, damage, and group rolls. Use when the user asks to roll dice, roll a check, roll damage, roll with advantage or disadvantage, or roll for a monster, NPC, or player."
---

# Dice Roller

Roll the dice, show the dice, and let the result stand. No fudging, in either direction.

## Before you roll — ask for what matters

Ask only for what is missing. Defaults in brackets.

1. **What to roll** — the notation, e.g. `2d6+3`, `d20`, `4d6` [ask — no safe default]
2. **Advantage / disadvantage** — for a d20 test [neither, unless the user says so]
3. **What the roll is for** — an attack, a check, a save, damage [ask if it changes the read of the result; otherwise roll and say what it was]

If the user just says "roll", ask for the notation once, then roll.

## The rules

- **Show the dice, not just the total.** Always report each die, then the total: `2d6+3: [4, 2] + 3 = 9`. A total without the dice is not a roll.
- **Use the script when you can.** Run `python3 scripts/roll.py <notation>` from the repo root (Python 3, stdlib only) and report its output. If the script is not available, roll honestly and say you rolled without it.
- **Advantage and disadvantage are two d20s.** Advantage: roll two d20s, take the higher. Disadvantage: roll two d20s, take the lower. Show both dice. Never roll one die and call it advantage.
- **A natural 20 is a critical hit on an attack; a natural 1 is a critical miss.** On a damage roll after a crit, roll the damage dice twice (do not double the modifier). Say so when it happens — "natural 20, critical hit" — then roll the damage.
- **State the DC or the target before the dice land, or immediately after** — never after the player has already committed to a different plan on the basis of the result.
- **Never fudge a roll.** If the result is bad for the party, or bad for the monster, it stands. A failed roll changes the situation; it does not stop the story.
- **Never roll for a player character without being asked.** The player rolls their own dice. The agent rolls for monsters, NPCs, and the world — and for a player only when the player asks it to.

## Notation

| Notation | Meaning |
|---|---|
| `d20` | One 20-sided die |
| `2d6+3` | Two 6-sided dice, plus 3 |
| `4d6 drop lowest 1` | Four 6-sided dice, drop the lowest one (ability scores) |
| `d20 advantage` | Two d20s, take the higher |
| `d20 disadvantage` | Two d20s, take the lower |
| `8d6` | Eight 6-sided dice (a fireball, for example) |
| `1d4+1` | One 4-sided die, plus 1 |

Modifiers are added once, after the dice — never per die, unless the rule says so.

## Output format

```markdown
**Roll:** <what it was for>
**Dice:** <notation>: [<each die>] <+/- modifier> = <total>
**Result:** <what it means — hit / miss, save / fail, damage dealt>
```

For advantage / disadvantage:

```markdown
**Roll:** <what it was for> — advantage
**Dice:** d20: [14, 7] → take 14, + 5 = 19
**Result:** <what it means>
```

## Group rolls

When several creatures roll the same thing — a group of goblins making a save, for example — roll once per creature and list each result on its own line. Do not roll once and apply it to the whole group unless the user asks for that.

## Fold&Roll voice

Dice are the one place the voice stays plain. No flourish on the roll itself — the drama is in the result, not the reporting. One line for the dice, one line for what it means, then back to the game.
