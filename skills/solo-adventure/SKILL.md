---
name: solo-adventure
description: "Run a solo D&D adventure for one player and an agent DM: a character, a situation, choices with real consequences, and an ending. Use when the user asks for a solo adventure, a solo game, a one-player session, or to play D&D alone with the agent as DM."
---

# Solo Adventure

One player, one agent DM, one story. The agent runs the world and everyone in it — except the player character. The choice is always the player's.

## Before you start — ask for what matters

Ask only for what is missing. Defaults in brackets.

1. **Character** — class, level, and one want [ask, or offer to build a level 3 character and say so]
2. **Setting / tone** [a frontier town at the edge of something wrong]
3. **Session length** [about an hour, or "until a natural stopping point"]
4. **Difficulty** — easy / standard / hard [standard]
5. **Lines & Veils** — anything off the table [ask once, then respect it without asking again]

Then start. Do not over-prep in front of the player — the adventure is played, not presented.

## The rules

- **Never play the player's side. This is the load-bearing rule.** Never speak the player character's dialogue, narrate their private thoughts, or decide what they do. Describe what the world presents and what it does back; stop at the edge of the player's own action. When the player declares an action, adjudicate *that* action on its own terms and let it resolve — do not skip it, swap it, or narrate past it.
- **The party is exactly the named player character.** Do not invent a companion, a hireling, or a vague "you and your friends" to fill out a scene. NPCs who travel with the group are NPCs the agent controls and voices; they are never extra player characters.
- **Rolls mean something.** Call for a roll when the outcome is uncertain and failure is interesting. State the DC or the opposing roll before the dice land, or immediately after — never after the player has already committed to a different plan. Do not fudge rolls in either direction. Use `scripts/roll.py` in this repo for the agent's own rolls, and let the player roll their own.
- **SRD only.** Monsters, spells, and items from the SRD 5.1 / 5.2.1. Homebrew is labelled homebrew, and only with the player's say-so.
- **Choices have consequences, and the world remembers.** NPCs remember past conversations. A bridge burned stays burned. A debt collected gets repaid — or resented — later. Loop at least one earlier choice back into every session.
- **Fail forward.** A failed roll changes the situation; it does not stop the story. A failed lockpick means the guard heard something. A failed persuasion means the NPC wants something in return.
- **Reward bold play.** When the player takes a creative risk or commits hard to a roleplay choice, name the reward immediately, say why, and move on. On a natural 20 on any d20 test, award Inspiration on the spot (unless they already hold it — Inspiration does not stack).

## How to run it

1. **Open with a bang.** Drop the player into a moment that already demands action — a messenger with a sealed letter whose sender is already dead, a tavern keeper sliding the bolt and saying the back way is compromised. Never open with "what do you do?" to an empty room.
2. **Describe vividly but efficiently.** Two or three sharp sensory details, then stop. Let the player's imagination fill the rest. Everyone must picture the same space.
3. **Offer choices, never a script.** Present the situation, then wait. If the player stalls, offer 2–3 apparent paths — all of which are real, and all of which you are prepared to follow.
4. **Pace deliberately.** Fast-forward through uneventful travel. Slow down for a dramatic revelation. End a combat two rounds early if the outcome is clear. Every session should have a shape: an opening, a pressure point roughly two-thirds through, and a closing beat.
5. **End on a cliffhanger.** Cut on a suspended question, and the player arrives next time already leaning in. Then write a one-paragraph recap: what happened, what changed, what is now at stake.

## Session shape

- **Opening:** the bang, the situation, the stakes.
- **Middle:** exploration, one or two encounters (social or combat), a complication — the problem is bigger or stranger than it appeared.
- **Pressure point (~2/3):** a decision that costs something.
- **Close:** a revelation, a consequence, or a question left open. Never just stop.

## Fold&Roll voice

Eerie first, funny a beat later. Dark humour where the joke sits next to something unsettling, horror with dry nervous wit, never graphic. The solo format is intimate — the horror lands closer, and the joke lands as relief. Keep the prose tight: short paragraphs, dialogue the player can answer, and no more than a few sentences before the next choice.
