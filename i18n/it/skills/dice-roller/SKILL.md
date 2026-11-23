---
name: dice-roller
description: "Tira i dadi per D&D 5e: qualsiasi notazione (2d6+3, d20, 4d6 drop lowest), vantaggio e svantaggio, colpi critici e fallimenti critici, danni e tiri di gruppo. Usala quando l'utente chiede di tirare i dadi, tirare una prova, tirare i danni, tirare con vantaggio o svantaggio, o tirare per un mostro, un PNG o un giocatore."
---

# Lanciatore di dadi

Tira i dadi, mostra i dadi e lascia che il risultato resti. Non truccare i tiri, in nessuna direzione.

## Prima di tirare — chiedi ciò che conta

Chiedi solo ciò che manca. I valori predefiniti tra parentesi quadre.

1. **Cosa tirare** — la notazione, ad es. `2d6+3`, `d20`, `4d6` [chiedi — nessun valore predefinito sicuro]
2. **Vantaggio / svantaggio** — per una prova con d20 [nessuno dei due, a meno che l'utente non lo dica]
3. **A cosa serve il tiro** — un attacco, una prova, un tiro salvezza, i danni [chiedi se cambia la lettura del risultato; altrimenti tira e dì a cosa serviva]

Se l'utente dice solo "tira", chiedi la notazione una volta, poi tira.

## Le regole

- **Mostra i dadi, non solo il totale.** Riporta sempre ogni dado, poi il totale: `2d6+3: [4, 2] + 3 = 9`. Un totale senza i dadi non è un tiro.
- **Usa lo script quando puoi.** Esegui `python3 scripts/roll.py <notation>` dalla radice del repo (solo Python 3, solo libreria standard) e riporta il suo output. Se lo script non è disponibile, tira onestamente e dì che hai tirato senza di esso.
- **Vantaggio e svantaggio sono due d20.** Vantaggio: tira due d20, prendi il più alto. Svantaggio: tira due d20, prendi il più basso. Mostra entrambi i dadi. Non tirare mai un solo dado e chiamarlo vantaggio.
- **Un 20 naturale è un colpo critico in un attacco; un 1 naturale è un fallimento critico.** In un tiro di danni dopo un colpo critico, tira i dadi dei danni due volte (non raddoppiare il modificatore). Dillo quando succede — "20 naturale, colpo critico" — poi tira i danni.
- **Enuncia la CD o il bersaglio prima che i dadi cadano, o subito dopo** — mai dopo che il giocatore si è già impegnato in un altro piano sulla base del risultato.
- **Non truccare mai un tiro.** Se il risultato è brutto per il gruppo, o brutto per il mostro, resta. Un tiro fallito cambia la situazione; non ferma la storia.
- **Non tirare mai per un personaggio giocante senza che te lo chiedano.** Il giocatore tira i propri dadi. L'agente tira per mostri, PNG e il mondo — e per un giocatore solo quando il giocatore glielo chiede.

## Notazione

| Notazione | Significato |
|---|---|
| `d20` | Un dado a 20 facce |
| `2d6+3` | Due dadi a 6 facce, più 3 |
| `4d6 drop lowest 1` | Quattro dadi a 6 facce, scarta il più basso (punteggi di caratteristica) |
| `d20 advantage` | Due d20, prendi il più alto |
| `d20 disadvantage` | Due d20, prendi il più basso |
| `8d6` | Otto dadi a 6 facce (una palla di fuoco, ad esempio) |
| `1d4+1` | Un dado a 4 facce, più 1 |

I modificatori si aggiungono una volta sola, dopo i dadi — mai per dado, salvo che la regola dica altrimenti.

## Formato di output

```markdown
**Roll:** <what it was for>
**Dice:** <notation>: [<each die>] <+/- modifier> = <total>
**Result:** <what it means — hit / miss, save / fail, damage dealt>
```

Per vantaggio / svantaggio:

```markdown
**Roll:** <what it was for> — advantage
**Dice:** d20: [14, 7] → take 14, + 5 = 19
**Result:** <what it means>
```

## Tiri di gruppo

Quando più creature tirano la stessa cosa — un gruppo di goblin che fa un tiro salvezza, ad esempio — tira una volta per creatura ed elenca ogni risultato sulla propria riga. Non tirare una volta sola e applicarla a tutto il gruppo, a meno che l'utente non lo chieda.

## La voce di Fold&Roll

I dadi sono l'unico punto in cui la voce resta semplice. Nessun abbellimento sul tiro in sé — il dramma sta nel risultato, non nel resoconto. Una riga per i dadi, una riga per ciò che significano, poi di nuovo al gioco.
