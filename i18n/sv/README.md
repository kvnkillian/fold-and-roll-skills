> Obs: Det här är en maskinöversättning till svenska — granskning av modersmålstalare är välkommen.

# Fold&Roll DM-färdigheter

Gratis AI-agentfärdigheter för att spelleda Dungeons & Dragons — från skaparna av Fold&Roll.

Installera dem i Claude Code, Codex, Cursor eller en annan agent som läser den öppna standarden Agent Skills, så slutar din agent att improvisera D&D-råd på känsla och börjar förbereda som en spelledare (Dungeon Master): situationer, inte intriger; konsekvenser, inte händelser; kusligt först, roligt ett ögonblick senare.

**Alla vid bordet.**

## Färdigheterna

| Färdighet | Vad den gör |
|---|---|
| `encounter-builder` | Balanserade, minnesvärda 5e-möten utifrån gruppens nivå, storlek och svårighetsgrad — med terräng, taktik och en vändning. |
| `npc-generator` | SLP:er (NPC:er) med en egenhet, en vilja och en hemlighet — plus en röst, en krok och vad som händer om gruppen ignorerar dem. |
| `session-prep` | En förberedelse på en sida inför en spelsession: situation, 3–5 noder, scenöppningar, fraktionsdrag och en cliffhanger att avsluta med. |
| `one-shot-builder` | Ett komplett one-shot på 3–4 timmar: krok, tre akter, möten, SLP:er och en avslutning som landar. |
| `solo-adventure` | Ett soloäventyr för en spelare och en agent som spelledare — val, konsekvenser och ett riktigt slut. |
| `campaign-arc` | En kampanjbåge i tre akter och sex takter, definierad av vad som förändras — inte av vad som händer. |
| `dice-roller` | Slå vilka tärningar som helst — fördel, nackdel, kritiska träffar, skada, gruppkast — och visa tärningarna, inte bara summan. |

## Installera

### Claude Code

```sh
claude plugin install fold-and-roll-skills@kvnkillian
```

Eller kopiera färdigheterna till din personliga färdighetsmapp:

```sh
git clone https://github.com/kvnkillian/fold-and-roll-skills.git
cp -r fold-and-roll-skills/skills/* ~/.claude/skills/
```

### Codex / Cursor / Copilot

```sh
npx skills@latest add kvnkillian/fold-and-roll-skills
```

Eller kopiera färdigheterna till `.agents/skills/` i ditt projekt, eller `~/.agents/skills/` för personligt bruk.

### Alla andra agenter

Kopiera en mapp `skills/<namn>/` dit din agent läser färdigheter ifrån. Varje färdighet är en enda `SKILL.md`-fil — inget byggsteg, inga beroenden. Tärningshjälpen i `scripts/roll.py` behöver bara Python 3.

## Använd dem

Fråga din agent med vanliga ord. Färdighetsbeskrivningarna talar om för den när den ska aktiveras:

- "Bygg ett möte för fyra rollpersoner på nivå 5, svår svårighetsgrad, i ett översvämmat tempel."
- "Ge mig en SLP — en smed som vet för mycket."
- "Förbered kvällens session. Förra gången brände gruppen bron till gillet."
- "Skriv ett one-shot åt mig om en hemsökt fyr."
- "Kör ett soloäventyr för min skurk på nivå 3."
- "Planera en kampanjbåge om en stad som har glömt sitt eget namn."

Agenten frågar efter de få detaljer den faktiskt behöver — gruppens nivå och storlek, ton, sessionens längd — och levererar sedan saken, färdig att spela.

## Fold&Roll-sättet

Dessa färdigheter följer samma regler som Fold&Roll är byggt på:

- **Förbered situationer, inte intriger.** En situation överlever kontakten med dina spelare. En intrig går sönder första gången de gör något oplanerat.
- **Spelarna är medförfattare.** Berätta aldrig en spelarkaraktärs dialog, tankar eller beslut. Valet är alltid deras.
- **Kusligt först, roligt ett ögonblick senare.** Mörk humor där skämtet sitter bredvid något obehagligt, skräck med torr, nervös kvickhet — aldrig grafiskt, aldrig blodigt för sin egen skull.
- **Endast SRD, om du inte säger annat.** Monster, besvärjelser och föremål kommer från SRD 5.1 / 5.2.1. Hemmagjort material märks som hemmagjort, och agenten frågar innan den hittar på det.
- **Säkerhet först.** Session zero, Lines & Veils och ett X-card är en del av förberedelsen, inte en eftertanke.
- **Alla vid bordet.** Innehållet ska gå att använda av alla spelare — tydligt språk, ingen information som bara är visuell, inget skämt som kräver syn eller hörsel för att fungera.

## Vill du ha hela bordet?

Dessa färdigheter är förberedelsen. Fold&Roll är bordet — rollformulär, stridskarta, initiativ och tärningar, byggt för en telefon i varje hand och ett gemensamt bord i mitten.

- **iOS:** https://apps.apple.com/app/fold-roll/id6822885522
- **Android beta:** https://play.google.com/apps/testing/com.kevin.rpgcompanion
- **Webbplats:** https://kvnkillian.github.io/

Gå med i Discord via webbplatsen för att dela dina bordshistorier, begära en färdighet eller rapportera ett dåligt tärningskast.

## Licens

MIT. Använd färdigheterna, forka dem, remixa dem, spela dem vid ditt bord. Om du publicerar en remix uppskattas en länk tillbaka, men det krävs inte.

SRD-innehållet i dessa färdigheter används under Creative Commons Attribution 4.0 International License (SRD 5.2.1) och Open Game License v1.0a (SRD 5.1). Wizards of the Coast, Dungeons & Dragons och D&D är varumärken som tillhör Wizards of the Coast. Detta projekt är inte anslutet till eller godkänt av Wizards of the Coast.
