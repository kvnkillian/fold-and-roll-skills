---
name: dice-roller
description: "Slå tärningar för D&D 5e: vilken notation som helst (2d6+3, d20, 4d6 ta bort lägsta), fördel och nackdel, kritiska träffar och missar, skada och gruppkast. Använd när användaren ber om att slå tärningar, slå ett egenskapskast, slå skada, slå med fördel eller nackdel, eller slå för ett monster, en SLP eller en spelare."
---

# Tärningskastare

Slå tärningarna, visa tärningarna och låt resultatet stå. Inget fusk, åt något håll.

## Innan du slår — fråga om det som spelar roll

Fråga bara om det som saknas. Standardvärden inom hakparenteser.

1. **Vad som ska slås** — notationen, t.ex. `2d6+3`, `d20`, `4d6` [fråga — inget säkert standardvärde]
2. **Fördel / nackdel** — för ett tärningskast med d20 [ingendera, om inte användaren säger det]
3. **Vad kastet gäller** — en attack, ett egenskapskast, ett räddningskast, skada [fråga om det ändrar hur resultatet ska tolkas; annars slå och säg vad det var]

Om användaren bara säger "slå", fråga en gång om notationen och slå sedan.

## Reglerna

- **Visa tärningarna, inte bara summan.** Rapportera alltid varje tärning, sedan summan: `2d6+3: [4, 2] + 3 = 9`. En summa utan tärningarna är inget kast.
- **Använd skriptet när du kan.** Kör `python3 scripts/roll.py <notation>` från repositoriets rot (endast Python 3, standardbiblioteket) och rapportera dess utdata. Om skriptet inte finns tillgängligt, slå ärligt och säg att du slog utan det.
- **Fördel och nackdel är två d20.** Fördel: slå två d20 och ta den högre. Nackdel: slå två d20 och ta den lägre. Visa båda tärningarna. Slå aldrig en enda tärning och kalla det fördel.
- **En naturlig 20 är en kritisk träff vid en attack; en naturlig 1 är en kritisk miss.** Vid ett skadekast efter en kritisk träff, slå skadetärningarna två gånger (dubbla inte modifikatorn). Säg det när det händer — "naturlig 20, kritisk träff" — och slå sedan skadan.
- **Ange svårighetsgraden (DC) eller målet innan tärningarna landar, eller direkt efter** — aldrig efter att spelaren redan har bestämt sig för en annan plan utifrån resultatet.
- **Fuska aldrig med ett kast.** Om resultatet är dåligt för gruppen, eller dåligt för monstret, så står det. Ett misslyckat kast förändrar situationen; det stoppar inte berättelsen.
- **Slå aldrig för en rollperson utan att bli ombedd.** Spelaren slår sina egna tärningar. Agenten slår för monster, SLP:er och världen — och för en spelare bara när spelaren ber om det.

## Notation

| Notation | Betydelse |
|---|---|
| `d20` | En 20-sidig tärning |
| `2d6+3` | Två 6-sidiga tärningar, plus 3 |
| `4d6 drop lowest 1` | Fyra 6-sidiga tärningar, ta bort den lägsta (egenskapsvärden) |
| `d20 advantage` | Två d20, ta den högre |
| `d20 disadvantage` | Två d20, ta den lägre |
| `8d6` | Åtta 6-sidiga tärningar (till exempel ett eldklot (fireball)) |
| `1d4+1` | En 4-sidig tärning, plus 1 |

Modifikatorer läggs till en gång, efter tärningarna — aldrig per tärning, om inte regeln säger det.

## Utdataformat

```markdown
**Kast:** <vad det gällde>
**Tärningar:** <notation>: [<varje tärning>] <+/- modifikator> = <summa>
**Resultat:** <vad det betyder — träff / miss, räddning / misslyckande, skada utdelad>
```

För fördel / nackdel:

```markdown
**Kast:** <vad det gällde> — fördel
**Tärningar:** d20: [14, 7] → ta 14, + 5 = 19
**Resultat:** <vad det betyder>
```

## Gruppkast

När flera varelser slår samma sak — till exempel en grupp goblins som gör ett räddningskast — slå en gång per varelse och lista varje resultat på en egen rad. Slå inte en gång och tillämpa det på hela gruppen om inte användaren ber om det.

## Fold&Roll-röst

Tärningar är det enda stället där rösten förblir enkel. Ingen utsmyckning på själva kastet — dramatiken ligger i resultatet, inte i rapporteringen. En rad för tärningarna, en rad för vad det betyder, sedan tillbaka till spelet.
