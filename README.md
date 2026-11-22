# Fold&Roll DM Skills

Free AI agent skills for running Dungeons & Dragons — from the makers of Fold&Roll.

Install them in Claude Code, Codex, Cursor, or any agent that reads the Agent Skills open standard, and your agent stops improvising D&D advice from vibes and starts prepping like a DM: situations, not plots; consequences, not events; eerie first, funny a beat later.

**Everyone at the table.**

## Languages

The skills are available in all 11 Fold&Roll languages. English is the source of truth; the other 10 are machine translations as a starting point, and native review is welcome.

- English — this README
- [Español](i18n/es/README.md) · [Français](i18n/fr/README.md) · [日本語](i18n/ja/README.md) · [Deutsch](i18n/de/README.md) · [Português (Brasil)](i18n/pt-BR/README.md) · [Svenska](i18n/sv/README.md) · [Italiano](i18n/it/README.md) · [한국어](i18n/ko/README.md) · [简体中文](i18n/zh-Hans/README.md) · [繁體中文](i18n/zh-Hant/README.md)

To install a translated set, copy that language's `skills/` folder instead of the English one — for example, `i18n/es/skills/*` into `~/.claude/skills/`.

## The skills

| Skill | What it does |
|---|---|
| `encounter-builder` | Balanced, memorable 5e encounters from party level, size, and difficulty — with terrain, tactics, and a twist. |
| `npc-generator` | NPCs with a quirk, a want, and a secret — plus a voice, a hook, and what happens if the party ignores them. |
| `session-prep` | A one-page session prep: situation, 3–5 nodes, scene bangs, faction moves, and a cliffhanger to close on. |
| `one-shot-builder` | A complete 3–4 hour one-shot: hook, three acts, encounters, NPCs, and a payoff. |
| `solo-adventure` | A solo adventure for one player and an agent DM — choices, consequences, and a real ending. |
| `campaign-arc` | A campaign arc in three acts and six beats, defined by what changes — not by what happens. |

## Install

### Claude Code

```sh
claude plugin install fold-and-roll-skills@kvnkillian
```

Or copy the skills into your personal skills folder:

```sh
git clone https://github.com/kvnkillian/fold-and-roll-skills.git
cp -r fold-and-roll-skills/skills/* ~/.claude/skills/
```

### Codex / Cursor / Copilot

```sh
npx skills@latest add kvnkillian/fold-and-roll-skills
```

Or copy the skills into `.agents/skills/` in your project, or `~/.agents/skills/` for personal use.

### Any other agent

Copy a `skills/<name>/` folder into wherever your agent reads skills from. Each skill is one `SKILL.md` file — no build step, no dependencies. The dice helper in `scripts/roll.py` needs Python 3 only.

## Use them

Ask your agent in plain words. The skill descriptions tell it when to fire:

- "Build an encounter for four level 5 characters, hard difficulty, in a flooded temple."
- "Give me an NPC — a blacksmith who knows too much."
- "Prep tonight's session. Last time the party burned the bridge with the guild."
- "Write me a one-shot for a haunted lighthouse."
- "Run a solo adventure for my level 3 rogue."
- "Plan a campaign arc about a city that forgot its own name."

The agent will ask for the few details it actually needs — party level and size, tone, session length — and then deliver the thing, ready to run.

## The Fold&Roll way

These skills follow the same rules Fold&Roll is built on:

- **Prep situations, not plots.** A situation survives contact with your players. A plot breaks the first time they do something unplanned.
- **Players are co-authors.** Never narrate a player character's dialogue, thoughts, or decisions. The choice is always theirs.
- **Eerie first, funny a beat later.** Dark humor where the joke sits next to something unsettling, horror with dry nervous wit — never graphic, never gory for its own sake.
- **SRD only, unless you say otherwise.** Monsters, spells, and items come from the SRD 5.1 / 5.2.1. Homebrew is labelled homebrew, and the agent asks before inventing it.
- **Safety first.** Session zero, Lines & Veils, and an X-card are part of the prep, not an afterthought.
- **Everyone at the table.** Content stays usable by every player — clear language, no visual-only information, no joke that needs sight or hearing to land.

## Want the full table?

These skills are the prep. Fold&Roll is the table — character sheets, battle map, initiative, and dice, built for a phone in each hand and a shared table in the middle.

- **iOS:** https://apps.apple.com/app/fold-roll/id6822885522
- **Android beta:** https://play.google.com/apps/testing/com.kevin.rpgcompanion
- **Website:** https://kvnkillian.github.io/

Join the Discord from the website to share your table stories, request a skill, or report a bad roll.

## License

MIT. Use the skills, fork them, remix them, run them at your table. If you publish a remix, a link back is appreciated but not required.

SRD content in these skills is used under the Creative Commons Attribution 4.0 International License (SRD 5.2.1) and the Open Game License v1.0a (SRD 5.1). Wizards of the Coast, Dungeons & Dragons, and D&D are trademarks of Wizards of the Coast. This project is not affiliated with or endorsed by Wizards of the Coast.
