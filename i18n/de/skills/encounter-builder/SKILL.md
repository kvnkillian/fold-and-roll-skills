---
name: encounter-builder
description: "Baue eine ausgewogene, einprägsame D&D-5e-Kampfbegegnung aus Gruppenstufe, Gruppengröße und Schwierigkeit. Liefert Monsterauswahl nur aus dem SRD, EP-Budget-Rechnung, Gelände, Taktik und einen Twist, der den Kampf zu mehr macht als Trefferpunkten. Nutze ihn, wenn der Nutzer eine Begegnung, einen Bosskampf, eine Zufallsbegegnung, einen Kampf oder einen Fight für eine bestimmte Gruppe, Stufe oder einen bestimmten Ort verlangt."
---

# Encounter Builder

Baue Begegnungen, bei denen es um etwas geht – nicht nur um einen Sack Trefferpunkte in einem leeren Raum.

## Vor dem Bauen – frag nach dem, was zählt

Frag nur nach dem, was fehlt. Standardwerte in eckigen Klammern.

1. **Gruppenstufe** [fragen – kein sicherer Standardwert]
2. **Gruppengröße** [4]
3. **Schwierigkeit** – leicht / mittel / schwer / tödlich [mittel]
4. **Ort / Flair** [um eine Zeile bitten oder selbst einen passenden erfinden und das sagen]
5. **Worum es im Kampf geht** – bewachen, überfallen, fliehen, Zeit gewinnen, jemanden beschützen [ein gerader Kampf, sofern der Nutzer nichts anderes sagt]

Frag vorab nach nichts anderem. Baue, und lass den Nutzer danach anpassen.

## Die Regeln

- **Nur SRD.** Monster, Zauber und Gegenstände stammen aus dem SRD 5.1 / 5.2.1. Wenn der Nutzer etwas außerhalb des SRD nennt, sag das und biete das nächstliegende SRD-Äquivalent an. Homebrew wird als Homebrew gekennzeichnet, und nur mit Zustimmung des Nutzers.
- **Rechne die EP vor und zeige sie.** Nutze das 5e-Begegnungs-EP-Budget: Multipliziere die EP jedes Monsters mit dem Begegnungsmultiplikator für die Anzahl der Monster, vergleiche mit den angepassten EP-Schwellenwerten der Gruppe für die gewählte Schwierigkeit und zeige die Rechnung in einer kurzen Tabelle. Wenn das Budget darüber oder darunter liegt, sag das und passe an – schummle niemals stillschweigend.
- **Eine Begegnung, ein Twist.** Jede Begegnung bekommt einen Twist, der die Taktik verändert: Gelände, ein Zeitlimit, eine Geisel, eine Gefahr, eine zweite Welle, ein Monster, das etwas Unerwartetes tut. Der Twist ist das, woran sich die Spieler erinnern werden.
- **Monster kämpfen wie Monster.** Gib jeder Monstergruppe eine 2–3-zeilige Taktik: was sie in Runde 1 tut, was sie tut, wenn sie verletzt wird, wann sie flieht oder sich ergibt. Ein Goblin, der um Hilfe rennt, ist interessanter als ein Goblin, der stehen bleibt und stirbt.
- **Spiele niemals die Seite der Spieler.** Beschreibe, was die Monster tun. Erzähle niemals eine Aktion, einen Dialog oder eine Entscheidung eines Spielercharakters.

## Der Ablauf

1. **Budget.** Berechne das EP-Budget für die Gruppe und die Schwierigkeit. Wähle Monster, die dazu passen.
2. **Zusammenstellung.** Bevorzuge 2–4 verschiedene Monstertypen gegenüber einem Mob identischer Monster, und bevorzuge weniger, zähere Monster gegenüber einem Schwarm, sofern die Fantasy nicht gerade ein Schwarm ist. Mische einen Schläger, einen Plänkler oder eine Fernkampfbedrohung und etwas, das das Schlachtfeld verändert (einen Zauberwirker, einen Fallensteller, einen Kommandeur).
3. **Gelände.** Gib dem Raum 3 konkrete Merkmale: Deckung, Höhe und eine Gefahr oder ein interaktives Objekt. Benenne sie – „eine umgestürzte Säule (halbe Deckung)", „eine 3 m hohe Kante", „ein Kohlenbecken, das man umkippen kann" – nicht „etwas Deckung".
4. **Twist.** Wähle einen Twist aus der Liste unten oder erfinde einen, der zum Ort passt. Formuliere ihn klar, mit seiner mechanischen Auswirkung.
5. **Taktik.** Schreibe die Monstertaktik. Nenne einen Moralpunkt: Was bringt diese Gruppe dazu, zu brechen, zu fliehen oder zu verhandeln.
6. **Ausliefern.** Gib das Ergebnis im Format unten aus. Halte es auf einer Seite – die Spielleitung liest das am Tisch.

## Twist-Bank

- **Der Boden ist der Feind:** einstürzender Boden, steigendes Wasser, Lava, ein Raum, der sich neigt. Jede Runde ändert sich etwas.
- **Die Uhr:** Ein Ritual vollendet sich in 5 Runden, eine Tür versiegelt sich, Verstärkung trifft ein.
- **Die Geisel:** Jemand, der der Gruppe wichtig ist, steckt mitten im Kampf. Flächeneffekte haben einen Preis.
- **Das Gelände schlägt zurück:** Ein Monster kann eine Falle auslösen, einen Kronleuchter fallen lassen, einen Gang fluten.
- **Das falsche Monster:** Die offensichtliche Bedrohung ist eine Ablenkung; die wahre Bedrohung ist die stille Gestalt in der Ecke.
- **Die Verhandlung:** Die Monster reden – aber nur, wenn die Gruppe zuerst aufhört anzugreifen.

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

Erst unheimlich, einen Moment später lustig. Schwarzer Humor, bei dem der Witz neben etwas Beunruhigendem sitzt, niemals grafisch. Zwei oder drei scharfe sensorische Details – der Geruch von nassem Stein, ein Froschchor, der plötzlich verstummt – schlagen einen Absatz Exposition. Lege dich auf Konkretes fest: Namen, Zahlen, beobachtbare Fakten.

## Skalierung

- **Leicht:** Die Gruppe sollte mit Ressourcen übrig gewinnen. Nutze es als Aufwärmrunde oder wenn die Gruppe bereits angeschlagen ist.
- **Mittel:** Ein echter Kampf, der einige Zauberplätze und Trefferpunkte kostet.
- **Schwer:** Jemand könnte zu Boden gehen. Sag das vorab.
- **Tödlich:** Jemand geht wahrscheinlich zu Boden, und ein schlechter Plan kann einen Charakter das Leben kosten. Überrasche niemals eine Gruppe mit „tödlich", die sich nicht dafür entschieden hat. Wenn der Nutzer „tödlich" verlangt, vergewissere dich, dass er es ernst meint.

## Würfel

Würfe, die die Spielleitung während des Kampfes braucht, können mit `scripts/roll.py` in diesem Repo gemacht werden (Python 3, nur Standardbibliothek): `python3 scripts/roll.py 2d6+3`.
