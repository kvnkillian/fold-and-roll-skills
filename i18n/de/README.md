> Diese Übersetzung wurde maschinell erstellt – eine Prüfung durch Muttersprachler ist willkommen.

# Fold&Roll DM Skills

Kostenlose KI-Agenten-Skills zum Leiten von Dungeons & Dragons – von den Machern von Fold&Roll.

Installiere sie in Claude Code, Codex, Cursor oder jedem Agenten, der den offenen Standard Agent Skills liest, und dein Agent improvisiert D&D-Ratschläge nicht mehr aus dem Bauch heraus, sondern bereitet sich vor wie ein Spielleiter: Situationen statt Plots, Konsequenzen statt Ereignisse, erst unheimlich, einen Moment später lustig.

**Alle am Tisch.**

## Die Skills

| Skill | Was er kann |
|---|---|
| `encounter-builder` | Ausgewogene, einprägsame 5e-Begegnungen aus Gruppenstufe, Gruppengröße und Schwierigkeit – mit Gelände, Taktik und einem Twist. |
| `npc-generator` | NSCs mit einer Eigenart, einem Wunsch und einem Geheimnis – dazu eine Stimme, ein Aufhänger und was passiert, wenn die Gruppe sie ignoriert. |
| `session-prep` | Eine einseitige Sitzungsvorbereitung: Situation, 3–5 Knoten, Szenenaufhänger, Fraktionszüge und ein Cliffhanger zum Abschluss. |
| `one-shot-builder` | Ein komplettes One-Shot für 3–4 Stunden: Aufhänger, drei Akte, Begegnungen, NSCs und ein Payoff, der sitzt. |
| `solo-adventure` | Ein Solo-Abenteuer für eine Spielerin oder einen Spieler und einen Agenten als Spielleiter – Entscheidungen, Konsequenzen und ein echtes Ende. |
| `campaign-arc` | Ein Kampagnenbogen in drei Akten und sechs Beats, definiert durch das, was sich ändert – nicht durch das, was passiert. |

## Installation

### Claude Code

```sh
claude plugin install fold-and-roll-skills@kvnkillian
```

Oder kopiere die Skills in deinen persönlichen Skills-Ordner:

```sh
git clone https://github.com/kvnkillian/fold-and-roll-skills.git
cp -r fold-and-roll-skills/skills/* ~/.claude/skills/
```

### Codex / Cursor / Copilot

```sh
npx skills@latest add kvnkillian/fold-and-roll-skills
```

Oder kopiere die Skills in `.agents/skills/` in deinem Projekt oder in `~/.agents/skills/` für den persönlichen Gebrauch.

### Jeder andere Agent

Kopiere einen `skills/<name>/`-Ordner dorthin, wo dein Agent Skills liest. Jeder Skill ist eine einzige `SKILL.md`-Datei – kein Build-Schritt, keine Abhängigkeiten. Der Würfel-Helfer in `scripts/roll.py` braucht nur Python 3.

## Anwendung

Frag deinen Agenten in einfachen Worten. Die Skill-Beschreibungen sagen ihm, wann er aktiv werden soll:

- „Baue eine Begegnung für vier Charaktere der Stufe 5, Schwierigkeit schwer, in einem überfluteten Tempel."
- „Gib mir einen NSC – einen Schmied, der zu viel weiß."
- „Bereite die Sitzung heute Abend vor. Letztes Mal hat die Gruppe die Brücke zur Gilde abgebrannt."
- „Schreib mir ein One-Shot für einen Spuk-Leuchtturm."
- „Leite ein Solo-Abenteuer für meinen Schurken der Stufe 3."
- „Plane einen Kampagnenbogen über eine Stadt, die ihren eigenen Namen vergessen hat."

Der Agent fragt nach den wenigen Details, die er wirklich braucht – Gruppenstufe und -größe, Ton, Sitzungslänge – und liefert dann das fertige Ergebnis, bereit zum Spielen.

## Die Fold&Roll-Art

Diese Skills folgen denselben Regeln, auf denen Fold&Roll aufgebaut ist:

- **Bereite Situationen vor, keine Plots.** Eine Situation übersteht den Kontakt mit deinen Spielern. Ein Plot bricht beim ersten Mal, wenn sie etwas Ungeplantes tun.
- **Spieler sind Mitautoren.** Erzähle niemals die Dialoge, Gedanken oder Entscheidungen eines Spielercharakters. Die Entscheidung liegt immer bei ihnen.
- **Erst unheimlich, einen Moment später lustig.** Schwarzer Humor, bei dem der Witz neben etwas Beunruhigendem sitzt, Horror mit trockenem, nervösem Witz – niemals grafisch, niemals blutig um des Blutes willen.
- **Nur SRD, sofern du nichts anderes sagst.** Monster, Zauber und Gegenstände stammen aus dem SRD 5.1 / 5.2.1. Homebrew wird als Homebrew gekennzeichnet, und der Agent fragt vorher, bevor er etwas erfindet.
- **Sicherheit zuerst.** Session Zero, Lines & Veils und eine X-Card gehören zur Vorbereitung, nicht zum Nachgedanken.
- **Alle am Tisch.** Inhalte bleiben für jede Spielerin und jeden Spieler nutzbar – klare Sprache, keine Informationen, die nur visuell vermittelt werden, kein Witz, der Sehen oder Hören voraussetzt, um zu zünden.

## Du willst den ganzen Tisch?

Diese Skills sind die Vorbereitung. Fold&Roll ist der Tisch – Charakterbögen, Kampfkarte, Initiative und Würfel, gebaut für ein Handy in jeder Hand und einen gemeinsamen Tisch in der Mitte.

- **iOS:** https://apps.apple.com/app/fold-roll/id6822885522
- **Android-Beta:** https://play.google.com/apps/testing/com.kevin.rpgcompanion
- **Website:** https://kvnkillian.github.io/

Tritt über die Website dem Discord bei, um deine Tischgeschichten zu teilen, einen Skill anzufragen oder einen schlechten Wurf zu melden.

## Lizenz

MIT. Nutze die Skills, forke sie, remixe sie, spiele sie an deinem Tisch. Wenn du einen Remix veröffentlichst, ist ein Link zurück willkommen, aber nicht erforderlich.

SRD-Inhalte in diesen Skills werden unter der Creative Commons Attribution 4.0 International License (SRD 5.2.1) und der Open Game License v1.0a (SRD 5.1) verwendet. Wizards of the Coast, Dungeons & Dragons und D&D sind Marken von Wizards of the Coast. Dieses Projekt ist nicht mit Wizards of the Coast verbunden und wird von ihnen nicht unterstützt.
