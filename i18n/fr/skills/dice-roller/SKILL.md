---
name: dice-roller
description: "Lancez les dés pour D&D 5e : toute notation (2d6+3, d20, 4d6 sans le plus petit), avantage et désavantage, coups critiques et échecs critiques, dégâts et jets de groupe. À utiliser quand l'utilisateur demande de lancer les dés, de lancer un jet, de lancer des dégâts, de lancer avec avantage ou désavantage, ou de lancer pour un monstre, un PNJ ou un joueur."
---

# Lanceur de dés

Lancez les dés, montrez les dés, et laissez le résultat tel quel. Pas de triche, dans un sens comme dans l'autre.

## Avant de lancer — demandez ce qui compte

Demandez seulement ce qui manque. Les valeurs par défaut sont entre crochets.

1. **Quoi lancer** — la notation, par ex. `2d6+3`, `d20`, `4d6` [à demander — pas de valeur par défaut sûre]
2. **Avantage / désavantage** — pour un jet de d20 [ni l'un ni l'autre, sauf si l'utilisateur le dit]
3. **À quoi sert le jet** — une attaque, un jet, un jet de sauvegarde, des dégâts [à demander si cela change la lecture du résultat ; sinon lancez et dites à quoi il servait]

Si l'utilisateur dit simplement « lance », demandez la notation une fois, puis lancez.

## Les règles

- **Montrez les dés, pas seulement le total.** Indiquez toujours chaque dé, puis le total : `2d6+3: [4, 2] + 3 = 9`. Un total sans les dés n'est pas un jet.
- **Utilisez le script quand vous pouvez.** Exécutez `python3 scripts/roll.py <notation>` depuis la racine du dépôt (Python 3, bibliothèque standard uniquement) et rapportez sa sortie. Si le script n'est pas disponible, lancez honnêtement et dites que vous avez lancé sans lui.
- **L'avantage et le désavantage, c'est deux d20.** Avantage : lancez deux d20, gardez le plus élevé. Désavantage : lancez deux d20, gardez le plus faible. Montrez les deux dés. Ne lancez jamais un seul dé en l'appelant avantage.
- **Un 20 naturel est un coup critique sur une attaque ; un 1 naturel est un échec critique.** Sur un jet de dégâts après un critique, lancez les dés de dégâts deux fois (ne doublez pas le modificateur). Dites-le quand cela arrive — « 20 naturel, coup critique » — puis lancez les dégâts.
- **Énoncez le DD ou la cible avant que les dés tombent, ou juste après** — jamais après que le joueur s'est déjà engagé dans un autre plan sur la base du résultat.
- **Ne truquez jamais un jet.** Si le résultat est mauvais pour le groupe, ou mauvais pour le monstre, il tient. Un jet raté change la situation ; il n'arrête pas l'histoire.
- **Ne lancez jamais pour un personnage joueur sans qu'on vous le demande.** Le joueur lance ses propres dés. L'agent lance pour les monstres, les PNJ et le monde — et pour un joueur seulement quand le joueur le lui demande.

## Notation

| Notation | Signification |
|---|---|
| `d20` | Un dé à 20 faces |
| `2d6+3` | Deux dés à 6 faces, plus 3 |
| `4d6 drop lowest 1` | Quatre dés à 6 faces, sans le plus petit (caractéristiques) |
| `d20 advantage` | Deux d20, gardez le plus élevé |
| `d20 disadvantage` | Deux d20, gardez le plus faible |
| `8d6` | Huit dés à 6 faces (une boule de feu, par exemple) |
| `1d4+1` | Un dé à 4 faces, plus 1 |

Les modificateurs s'ajoutent une seule fois, après les dés — jamais par dé, sauf si la règle le dit.

## Format de sortie

```markdown
**Jet :** <à quoi il servait>
**Dés :** <notation> : [<chaque dé>] <+/- modificateur> = <total>
**Résultat :** <ce que cela signifie — touche / rate, sauvegarde réussie / ratée, dégâts infligés>
```

Pour l'avantage / le désavantage :

```markdown
**Jet :** <à quoi il servait> — avantage
**Dés :** d20 : [14, 7] → gardez 14, + 5 = 19
**Résultat :** <ce que cela signifie>
```

## Jets de groupe

Quand plusieurs créatures lancent la même chose — un groupe de gobelins qui fait un jet de sauvegarde, par exemple — lancez une fois par créature et listez chaque résultat sur sa propre ligne. Ne lancez pas une seule fois pour appliquer le résultat à tout le groupe, sauf si l'utilisateur le demande.

## Voix Fold&Roll

Les dés sont le seul endroit où la voix reste simple. Aucune fioriture sur le jet lui-même — le drame est dans le résultat, pas dans le compte rendu. Une ligne pour les dés, une ligne pour ce que cela signifie, puis retour au jeu.
