---
name: dice-roller
description: "Würfle für D&D 5e: jede Notation (2d6+3, d20, 4d6 drop lowest), Vorteil und Nachteil, kritische Treffer und Fehlschläge, Schaden und Gruppenwürfe. Verwende ihn, wenn der Nutzer würfeln, eine Probe würfeln, Schaden würfeln, mit Vorteil oder Nachteil würfeln oder für ein Monster, einen NSC oder einen Spieler würfeln will."
---

# Dice Roller

Würfle, zeige die Würfel und lass das Ergebnis stehen. Kein Schummeln – in keine Richtung.

## Bevor du würfelst – frag nach, was wichtig ist

Frag nur nach dem, was fehlt. Standardwerte in eckigen Klammern.

1. **Was gewürfelt wird** — die Notation, z. B. `2d6+3`, `d20`, `4d6` [fragen – kein sicherer Standardwert]
2. **Vorteil / Nachteil** — für eine d20-Probe [keines von beiden, es sei denn, der Nutzer sagt es]
3. **Wofür der Wurf ist** — ein Angriff, eine Probe, ein Rettungswurf, Schaden [fragen, wenn es die Deutung des Ergebnisses ändert; sonst würfeln und sagen, wofür er war]

Wenn der Nutzer nur „würfeln" sagt, frag einmal nach der Notation und würfle dann.

## Die Regeln

- **Zeige die Würfel, nicht nur die Summe.** Berichte immer jeden Würfel, dann die Summe: `2d6+3: [4, 2] + 3 = 9`. Eine Summe ohne die Würfel ist kein Wurf.
- **Nutze das Skript, wenn du kannst.** Führe `python3 scripts/roll.py <notation>` vom Stammverzeichnis des Repos aus (nur Python 3, nur Standardbibliothek) und gib seine Ausgabe wieder. Wenn das Skript nicht verfügbar ist, würfle ehrlich und sag, dass du ohne es gewürfelt hast.
- **Vorteil und Nachteil sind zwei d20.** Vorteil: würfle zwei d20 und nimm den höheren. Nachteil: würfle zwei d20 und nimm den niedrigeren. Zeige beide Würfel. Würfle niemals nur einen Würfel und nenne das Vorteil.
- **Eine natürliche 20 ist ein kritischer Treffer bei einem Angriff; eine natürliche 1 ist ein kritischer Fehlschlag.** Bei einem Schadenswurf nach einem kritischen Treffer würfle die Schadenswürfel zweimal (verdopple nicht den Modifikator). Sag es, wenn es passiert – „natürliche 20, kritischer Treffer" – und würfle dann den Schaden.
- **Nenne den SG (Schwierigkeitsgrad) oder das Ziel, bevor die Würfel fallen, oder unmittelbar danach** – niemals erst, nachdem der Spieler sich auf der Grundlage des Ergebnisses bereits für einen anderen Plan entschieden hat.
- **Schummle niemals bei einem Wurf.** Wenn das Ergebnis schlecht für die Gruppe oder schlecht für das Monster ist, steht es. Ein gescheiterter Wurf ändert die Situation; er stoppt die Geschichte nicht.
- **Würfle niemals für einen Spielercharakter, ohne darum gebeten worden zu sein.** Der Spieler würfelt seine eigenen Würfel. Der Agent würfelt für Monster, NSCs und die Welt – und für einen Spieler nur, wenn der Spieler ihn darum bittet.

## Notation

| Notation | Bedeutung |
|---|---|
| `d20` | Ein 20-seitiger Würfel |
| `2d6+3` | Zwei 6-seitige Würfel, plus 3 |
| `4d6 drop lowest 1` | Vier 6-seitige Würfel, den niedrigsten wegstreichen (Fähigkeitswerte) |
| `d20 advantage` | Zwei d20, nimm den höheren |
| `d20 disadvantage` | Zwei d20, nimm den niedrigeren |
| `8d6` | Acht 6-seitige Würfel (zum Beispiel ein Feuerball) |
| `1d4+1` | Ein 4-seitiger Würfel, plus 1 |

Modifikatoren werden einmal addiert, nach den Würfeln – niemals pro Würfel, es sei denn, die Regel sagt es so.

## Output format

```markdown
**Roll:** <what it was for>
**Dice:** <notation>: [<each die>] <+/- modifier> = <total>
**Result:** <what it means — hit / miss, save / fail, damage dealt>
```

Bei Vorteil / Nachteil:

```markdown
**Roll:** <what it was for> — advantage
**Dice:** d20: [14, 7] → take 14, + 5 = 19
**Result:** <what it means>
```

## Gruppenwürfe

Wenn mehrere Kreaturen dasselbe würfeln – zum Beispiel eine Gruppe Goblins, die einen Rettungswurf macht – würfle einmal pro Kreatur und liste jedes Ergebnis in einer eigenen Zeile auf. Würfle nicht einmal und wende es auf die ganze Gruppe an, es sei denn, der Nutzer bittet darum.

## Die Fold&Roll-Art

Bei Würfeln bleibt die Stimme schlicht. Kein Schnörkel beim Wurf selbst – die Dramatik liegt im Ergebnis, nicht in der Berichterstattung. Eine Zeile für die Würfel, eine Zeile dafür, was es bedeutet, dann zurück zum Spiel.
