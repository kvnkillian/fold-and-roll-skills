---
name: encounter-builder
description: "Costruisci un incontro di combattimento D&D 5e bilanciato e memorabile a partire da livello del gruppo, dimensione del gruppo e difficoltà. Fornisce scelte di mostri solo dal SRD, la matematica del budget di PE, terreno, tattiche e un colpo di scena che rende lo scontro qualcosa di più dei punti ferita. Da usare quando l'utente chiede un incontro, uno scontro con un boss, un incontro casuale, un combattimento o uno scontro per un gruppo, un livello o un luogo specifici."
---

# Encounter Builder

Costruisci incontri che siano scontri *su qualcosa*, non solo un sacco di punti ferita in una stanza vuota.

## Prima di costruire — chiedi ciò che conta

Chiedi solo ciò che manca. Valori predefiniti tra parentesi quadre.

1. **Livello del gruppo** [chiedi — non esiste un valore predefinito sicuro]
2. **Dimensione del gruppo** [4]
3. **Difficoltà** — facile / media / difficile / letale [media]
4. **Luogo / atmosfera** [chiedi una riga, oppure inventane una adatta e dillo]
5. **Di cosa tratta lo scontro** — difendere, tendere un'imboscata, fuggire, guadagnare tempo, proteggere qualcuno [uno scontro diretto, salvo diversa indicazione dell'utente]

Non chiedere nient'altro in anticipo. Costruisci, poi lascia che l'utente modifichi.

## Le regole

- **Solo SRD.** Mostri, incantesimi e oggetti provengono dal SRD 5.1 / 5.2.1. Se l'utente nomina qualcosa fuori dal SRD, dillo e offri l'equivalente SRD più vicino. Il materiale homebrew è etichettato come homebrew, e solo con il consenso dell'utente.
- **Fai la matematica dei PE e mostrala.** Usa il budget di PE per gli incontri della 5e: moltiplica i PE di ogni mostro per il moltiplicatore dell'incontro in base al numero di mostri, confronta il risultato con le soglie di PE modificate del gruppo per la difficoltà scelta e mostra i calcoli in una breve tabella. Se il budget è sopra o sotto, dillo e correggi — non aggiustarlo mai di nascosto.
- **Un incontro, un colpo di scena.** Ogni incontro ha un colpo di scena che cambia le tattiche: terreno, un timer, un ostaggio, un pericolo, una seconda ondata, un mostro che fa qualcosa di inatteso. Il colpo di scena è ciò che i giocatori ricorderanno.
- **I mostri combattono come mostri.** Dai a ogni gruppo di mostri una tattica di 2–3 righe: cosa fa al round 1, cosa fa quando è ferito, quando fugge o si arrende. Un goblin che corre a chiedere aiuto è più interessante di un goblin che resta fermo e muore.
- **Non giocare mai dalla parte dei giocatori.** Descrivi ciò che fanno i mostri. Non narrare mai l'azione, il dialogo o la decisione di un personaggio giocante.

## Il flusso di lavoro

1. **Budget.** Calcola il budget di PE per il gruppo e la difficoltà. Scegli mostri che vi rientrino.
2. **Composizione.** Preferisci 2–4 tipi di mostri distinti a una massa di mostri identici, e preferisci pochi mostri più forti a uno sciame, a meno che la fantasia non sia proprio uno sciame. Mescola un picchiatore, uno schermagliatore o una minaccia a distanza, e qualcosa che cambia il campo di battaglia (un incantatore, qualcuno che piazza trappole, un comandante).
3. **Terreno.** Dai alla stanza 3 elementi concreti: copertura, altezza e un pericolo o un oggetto interattivo. Nominali — "un pilastro rovesciato (mezza copertura)", "una sporgenza di 10 piedi", "un braciere che si può rovesciare" — non "un po' di copertura".
4. **Colpo di scena.** Scegli un colpo di scena dall'elenco qui sotto, oppure inventane uno adatto al luogo. Enuncialo chiaramente, con il suo effetto meccanico.
5. **Tattiche.** Scrivi le tattiche dei mostri. Includi un punto di morale: cosa fa cedere, fuggire o negoziare questo gruppo.
6. **Consegna.** Output nel formato qui sotto. Tienilo su una pagina — il DM lo legge al tavolo.

## Banca dei colpi di scena

- **Il pavimento è il nemico:** pavimento che crolla, acqua che sale, lava, una stanza che si inclina. Qualcosa cambia a ogni round.
- **L'orologio:** un rituale si completa in 5 round, una porta si sigilla, arrivano rinforzi.
- **L'ostaggio:** qualcuno a cui il gruppo tiene è dentro lo scontro. Gli effetti ad area hanno un costo.
- **Il terreno contrattacca:** un mostro può attivare una trappola, far cadere un lampadario, allagare un passaggio.
- **Il mostro sbagliato:** la minaccia ovvia è una distrazione; la vera minaccia è quella silenziosa nell'angolo.
- **La trattativa:** i mostri parleranno — ma solo se il gruppo smette di attaccare per primo.

## Formato di output

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

## La voce di Fold&Roll

Inquietante prima, divertente un attimo dopo. Umorismo nero in cui la battuta sta accanto a qualcosa di inquietante, mai grafico. Due o tre dettagli sensoriali netti — l'odore della pietra bagnata, un coro di rane che all'improvviso tace — valgono più di un paragrafo di esposizione. Punta su dettagli concreti: nomi, numeri, fatti osservabili.

## Scala

- **Facile:** il gruppo dovrebbe vincere con risorse da parte. Usala per un riscaldamento, o quando il gruppo è già ferito.
- **Media:** uno scontro vero che costa qualche slot incantesimo e qualche punto ferita.
- **Difficile:** qualcuno potrebbe andare a terra. Dillo in anticipo.
- **Letale:** qualcuno probabilmente va a terra, e un brutto piano può porre fine a un personaggio. Non proporre mai un incontro letale a un gruppo che non l'ha scelto. Se l'utente chiede un incontro letale, conferma che lo intenda davvero.

## Dadi

I tiri di cui il DM ha bisogno durante lo scontro possono essere fatti con `scripts/roll.py` in questo repo (Python 3, solo libreria standard): `python3 scripts/roll.py 2d6+3`.
