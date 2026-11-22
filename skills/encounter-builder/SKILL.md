---
name: encounter-builder
description: "Build a balanced, memorable D&D 5e combat encounter from party level, party size, and difficulty. Gives monster picks from the SRD only, XP budget math, terrain, tactics, and a twist that makes the fight about more than hit points. Use when the user asks for an encounter, a boss fight, a random encounter, a combat, or a fight for a specific party, level, or location."
---

# Encounter Builder

Build encounters that are fights *about something*, not just a bag of hit points in a blank room.

## Before you build — ask for what matters

Ask only for what is missing. Defaults in brackets.

1. **Party level** [ask — no safe default]
2. **Party size** [4]
3. **Difficulty** — easy / medium / hard / deadly [medium]
4. **Location / flavour** [ask for one line, or invent a fitting one and say so]
5. **What the fight is about** — guarding, ambushing, fleeing, buying time, protecting someone [a straight fight, unless the user says otherwise]

Do not ask for anything else up front. Build, then let the user adjust.

## The rules

- **SRD only.** Monsters, spells, and items come from the SRD 5.1 / 5.2.1. If the user names something outside the SRD, say so and offer the closest SRD equivalent. Homebrew is labelled homebrew, and only with the user's say-so.
- **Do the XP math and show it.** Use the 5e encounter XP budget: multiply each monster's XP by the encounter multiplier for the number of monsters, compare against the party's adjusted XP thresholds for the chosen difficulty, and show the working in one short table. If the budget is over or under, say so and adjust — never silently fudge it.
- **One encounter, one twist.** Every encounter gets a twist that changes the tactics: terrain, a timer, a hostage, a hazard, a second wave, a monster that does something unexpected. The twist is what the players will remember.
- **Monsters fight like monsters.** Give each monster group a 2–3 line tactic: what it does on round 1, what it does when hurt, when it flees or surrenders. A goblin that runs for help is more interesting than a goblin that stands still and dies.
- **Never play the players' side.** Describe what the monsters do. Never narrate a player character's action, dialogue, or decision.

## The workflow

1. **Budget.** Work out the XP budget for the party and difficulty. Pick monsters that fit it.
2. **Composition.** Prefer 2–4 distinct monster types over a mob of identical ones, and prefer fewer, tougher monsters over a swarm unless the fantasy is a swarm. Mix a bruiser, a skirmisher or ranged threat, and something that changes the battlefield (a spellcaster, a trap-setter, a commander).
3. **Terrain.** Give the room 3 concrete features: cover, height, and a hazard or interactive object. Name them — "a toppled pillar (half cover)", "a 10 ft ledge", "a brazier that can be tipped" — not "some cover".
4. **Twist.** Pick one twist from the list below, or invent one that fits the location. State it plainly, with its mechanical effect.
5. **Tactics.** Write the monster tactics. Include a morale point: what makes this group break, flee, or negotiate.
6. **Deliver.** Output in the format below. Keep it to one page — the DM reads this at the table.

## Twist bank

- **The floor is the enemy:** collapsing floor, rising water, lava, a room that tilts. Something changes every round.
- **The clock:** a ritual completes in 5 rounds, a door seals, reinforcements arrive.
- **The hostage:** someone the party cares about is in the fight. Area effects have a cost.
- **The terrain fights back:** a monster can trigger a trap, drop a chandelier, flood a passage.
- **The wrong monster:** the obvious threat is a distraction; the real threat is the quiet one in the corner.
- **The parley:** the monsters will talk — but only if the party stops attacking first.

## Output format

```markdown
## Encounter: <name> — <difficulty> for <n> level <x> characters

**Budget:** <XP> adjusted XP vs <threshold> for <difficulty> — <fits / over by X / under by X>
**Monsters:** <count> × <monster> (CR <n>, <XP> XP each), ...

**The room:** <2–3 sentences. Cover, height, hazard.>
**Twist:** <one line, with its mechanical effect.>

**Tactics:**
- <monster group>: <round 1, when hurt, morale>
- ...

**If the party wins:** <one line — what changes, what they find, what it costs>
**If the party runs:** <one line — what the monsters do next>
```

## Fold&Roll voice

Eerie first, funny a beat later. Dark humour where the joke sits next to something unsettling, never graphic. Two or three sharp sensory details — the smell of wet stone, a choir of frogs going suddenly silent — beat a paragraph of exposition. Commit to specifics: names, numbers, observable facts.

## Scaling

- **Easy:** the party should win with resources to spare. Use it for a warm-up, or when the party is already hurt.
- **Medium:** a real fight that costs some spell slots and hit points.
- **Hard:** someone may go down. Say so up front.
- **Deadly:** someone probably goes down, and a bad plan can end a character. Never spring deadly on a party that did not choose it. If the user asks for deadly, confirm they mean it.

## Dice

Rolls the DM needs during the fight can be made with `scripts/roll.py` in this repo (Python 3, stdlib only): `python3 scripts/roll.py 2d6+3`.
