> Nota: questa è una traduzione automatica; una revisione da parte di madrelingua è benvenuta.

# Fold&Roll DM Skills

Skill gratuite per agenti IA per condurre Dungeons & Dragons — dai creatori di Fold&Roll.

Installale in Claude Code, Codex, Cursor o in qualsiasi agente che legga lo standard aperto Agent Skills, e il tuo agente smetterà di improvvisare consigli su D&D a sensazione e inizierà a prepararsi come un DM: situazioni, non trame; conseguenze, non eventi; inquietante prima, divertente un attimo dopo.

**Tutti al tavolo.**

## Le skill

| Skill | Cosa fa |
|---|---|
| `encounter-builder` | Incontri 5e bilanciati e memorabili a partire da livello, dimensione del gruppo e difficoltà — con terreno, tattiche e un colpo di scena. |
| `npc-generator` | PNG con una stranezza, un desiderio e un segreto — più una voce, un gancio e cosa succede se il gruppo li ignora. |
| `session-prep` | Una preparazione di sessione su una pagina: situazione, 3–5 nodi, aperture di scena, mosse delle fazioni e un colpo di scena finale su cui chiudere. |
| `one-shot-builder` | Un one-shot completo di 3–4 ore: gancio, tre atti, incontri, PNG e un finale che lascia il segno. |
| `solo-adventure` | Un'avventura in solitario per un giocatore e un DM agente — scelte, conseguenze e un vero finale. |
| `campaign-arc` | Un arco di campagna in tre atti e sei battute, definito da ciò che cambia — non da ciò che accade. |
| `dice-roller` | Tira qualsiasi dado — vantaggio, svantaggio, critici, danni, tiri di gruppo — mostrando i dadi, non solo il totale. |

## Installazione

### Claude Code

```sh
claude plugin install fold-and-roll-skills@kvnkillian
```

Oppure copia le skill nella tua cartella personale delle skill:

```sh
git clone https://github.com/kvnkillian/fold-and-roll-skills.git
cp -r fold-and-roll-skills/skills/* ~/.claude/skills/
```

### Codex / Cursor / Copilot

```sh
npx skills@latest add kvnkillian/fold-and-roll-skills
```

Oppure copia le skill in `.agents/skills/` nel tuo progetto, o in `~/.agents/skills/` per uso personale.

### Qualsiasi altro agente

Copia una cartella `skills/<name>/` dove il tuo agente legge le skill. Ogni skill è un unico file `SKILL.md` — nessun passaggio di build, nessuna dipendenza. L'helper per i dadi in `scripts/roll.py` richiede solo Python 3.

## Come usarle

Chiedi al tuo agente con parole semplici. Le descrizioni delle skill gli dicono quando attivarsi:

- "Costruisci un incontro per quattro personaggi di livello 5, difficoltà difficile, in un tempio allagato."
- "Dammi un PNG — un fabbro che sa troppo."
- "Prepara la sessione di stasera. L'ultima volta il gruppo ha bruciato i ponti con la gilda."
- "Scrivimi un one-shot per un faro infestato."
- "Conduci un'avventura in solitario per il mio ladro di livello 3."
- "Pianifica un arco di campagna su una città che ha dimenticato il proprio nome."

L'agente chiederà i pochi dettagli che servono davvero — livello e dimensione del gruppo, tono, durata della sessione — e poi consegnerà il materiale, pronto da giocare.

## Il modo Fold&Roll

Queste skill seguono le stesse regole su cui è costruito Fold&Roll:

- **Prepara situazioni, non trame.** Una situazione sopravvive al contatto con i giocatori. Una trama si rompe la prima volta che fanno qualcosa di imprevisto.
- **I giocatori sono coautori.** Non narrare mai i dialoghi, i pensieri o le decisioni di un personaggio giocante. La scelta è sempre loro.
- **Inquietante prima, divertente un attimo dopo.** Umorismo nero in cui la battuta sta accanto a qualcosa di inquietante, orrore con arguzia secca e nervosa — mai grafico, mai splatter fine a sé stesso.
- **Solo SRD, salvo diversa indicazione.** Mostri, incantesimi e oggetti provengono dal SRD 5.1 / 5.2.1. Il materiale homebrew è etichettato come homebrew, e l'agente chiede prima di inventarlo.
- **La sicurezza prima di tutto.** Sessione zero, Linee e Veli e X-card fanno parte della preparazione, non sono un ripensamento.
- **Tutti al tavolo.** I contenuti restano fruibili da ogni giocatore — linguaggio chiaro, nessuna informazione solo visiva, nessuna battuta che richieda vista o udito per funzionare.

## Vuoi il tavolo completo?

Queste skill sono la preparazione. Fold&Roll è il tavolo — schede personaggio, mappa di battaglia, iniziativa e dadi, costruiti per un telefono in ogni mano e un tavolo condiviso al centro.

- **iOS:** https://apps.apple.com/app/fold-roll/id6822885522
- **Beta Android:** https://play.google.com/apps/testing/com.kevin.rpgcompanion
- **Sito web:** https://kvnkillian.github.io/

Unisciti al Discord dal sito web per condividere le storie del tuo tavolo, richiedere una skill o segnalare un brutto tiro.

## Licenza

MIT. Usa le skill, forkale, remixale, giocale al tuo tavolo. Se pubblichi un remix, un link di ritorno è gradito ma non obbligatorio.

I contenuti SRD in queste skill sono usati sotto la licenza Creative Commons Attribution 4.0 International (SRD 5.2.1) e la Open Game License v1.0a (SRD 5.1). Wizards of the Coast, Dungeons & Dragons e D&D sono marchi di Wizards of the Coast. Questo progetto non è affiliato né approvato da Wizards of the Coast.
