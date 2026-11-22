---
name: encounter-builder
description: "Bygg ett balanserat, minnesvärt stridsmöte i D&D 5e utifrån gruppens nivå, gruppens storlek och svårighetsgrad. Ger monsterval endast från SRD, matematik för erfarenhetspoängsbudgeten, terräng, taktik och en vändning som gör striden till mer än träffpoäng. Används när användaren ber om ett möte, en bossfight, ett slumpmässigt möte, en strid eller en fight för en viss grupp, nivå eller plats."
---

# Mötesbyggaren

Bygg möten som är strider *om något*, inte bara en säck träffpoäng i ett tomt rum.

## Innan du bygger — fråga efter det som spelar roll

Fråga bara efter det som saknas. Standardvärden inom hakparenteser.

1. **Gruppens nivå** [fråga — inget säkert standardvärde]
2. **Gruppens storlek** [4]
3. **Svårighetsgrad** — lätt / medel / svår / dödlig [medel]
4. **Plats / stämning** [be om en rad, eller hitta på en passande och säg det]
5. **Vad striden handlar om** — bevaka, lägga sig i bakhåll, fly, köpa tid, skydda någon [en rak strid, om inte användaren säger annat]

Fråga inte om något annat i förväg. Bygg, och låt sedan användaren justera.

## Reglerna

- **Endast SRD.** Monster, besvärjelser och föremål kommer från SRD 5.1 / 5.2.1. Om användaren nämner något utanför SRD, säg det och erbjud närmaste motsvarighet i SRD. Hemmagjort material märks som hemmagjort, och bara om användaren säger ja.
- **Räkna ut erfarenhetspoängsmatematiken och visa den.** Använd 5e:s budget för erfarenhetspoäng (XP) för möten: multiplicera varje monsters erfarenhetspoäng med mötesmultiplikatorn för antalet monster, jämför med gruppens justerade tröskelvärden för erfarenhetspoäng för den valda svårighetsgraden, och visa uträkningen i en kort tabell. Om budgeten är över eller under, säg det och justera — fiffla aldrig tyst med den.
- **Ett möte, en vändning.** Varje möte får en vändning som ändrar taktiken: terräng, en timer, en gisslan, en fara, en andra våg, ett monster som gör något oväntat. Vändningen är det spelarna kommer att minnas.
- **Monster slåss som monster.** Ge varje monstergrupp en taktik på 2–3 rader: vad den gör i runda 1, vad den gör när den blir skadad, när den flyr eller ger upp. En goblin som springer efter hjälp är mer intressant än en goblin som står still och dör.
- **Spela aldrig spelarnas sida.** Beskriv vad monstren gör. Berätta aldrig en spelarkaraktärs handling, dialog eller beslut.

## Arbetsflödet

1. **Budget.** Räkna ut erfarenhetspoängsbudgeten för gruppen och svårighetsgraden. Välj monster som passar den.
2. **Sammansättning.** Föredra 2–4 olika monstertyper framför en hop identiska monster, och föredra färre, tuffare monster framför en svärm om inte fantasin är en svärm. Blanda en slagskämpe (bruiser), en skärmytslare eller ett hot på avstånd, och något som förändrar slagfältet (en besvärjelsekastare, en fällsättare, en befälhavare).
3. **Terräng.** Ge rummet 3 konkreta inslag: skydd, höjd och en fara eller ett interaktivt föremål. Namnge dem — "en kullfallen pelare (halvt skydd)", "en avsats på 10 ft", "ett fyrfat som kan välta" — inte "lite skydd".
4. **Vändning.** Välj en vändning från listan nedan, eller hitta på en som passar platsen. Ange den tydligt, med dess mekaniska effekt.
5. **Taktik.** Skriv monstrens taktik. Ta med en moralpunkt: vad som får den här gruppen att bryta samman, fly eller förhandla.
6. **Leverera.** Leverera i formatet nedan. Håll det till en sida — spelledaren läser detta vid bordet.

## Vändningsbank

- **Golvet är fienden:** rasande golv, stigande vatten, lava, ett rum som lutar. Något förändras varje runda.
- **Klockan:** en ritual fullbordas om 5 rundor, en dörr förseglas, förstärkningar anländer.
- **Gisslan:** någon som gruppen bryr sig om är med i striden. Yteffekter har ett pris.
- **Terrängen slår tillbaka:** ett monster kan utlösa en fälla, fälla en ljuskrona, översvämma en passage.
- **Fel monster:** det uppenbara hotet är en avledning; det verkliga hotet är det tysta i hörnet.
- **Förhandlingen:** monstren vill prata — men bara om gruppen slutar anfalla först.

## Utdataformat

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

## Fold&Roll-rösten

Kusligt först, roligt ett ögonblick senare. Mörk humor där skämtet sitter bredvid något obehagligt, aldrig grafiskt. Två eller tre skarpa sinnesdetaljer — lukten av våt sten, en grodkör som plötsligt tystnar — slår ett stycke exposition. Satsa på det specifika: namn, siffror, observerbara fakta.

## Skalning

- **Lätt:** gruppen ska vinna med resurser kvar. Använd det för en uppvärmning, eller när gruppen redan är skadad.
- **Medel:** en riktig strid som kostar några besvärjelseplatser och träffpoäng.
- **Svår:** någon kan falla. Säg det i förväg.
- **Dödlig:** någon faller troligen, och en dålig plan kan avsluta en karaktär. Överraska aldrig en grupp med dödlig svårighetsgrad om den inte har valt det. Om användaren ber om dödlig, bekräfta att de menar det.

## Tärningar

Slag som spelledaren behöver under striden kan göras med `scripts/roll.py` i det här repot (Python 3, endast standardbiblioteket): `python3 scripts/roll.py 2d6+3`.
