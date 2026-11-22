---
name: encounter-builder
description: "Construisez une rencontre de combat équilibrée et mémorable pour D&D 5e à partir du niveau du groupe, de sa taille et de la difficulté. Propose des monstres issus du SRD uniquement, le calcul du budget de PX, le terrain, les tactiques et un rebondissement qui fait du combat bien plus qu'une question de points de vie. À utiliser quand l'utilisateur demande une rencontre, un combat de boss, une rencontre aléatoire, un combat ou un affrontement pour un groupe, un niveau ou un lieu précis."
---

# Créateur de rencontres

Construisez des rencontres qui sont des combats *à propos de quelque chose*, et pas seulement un sac de points de vie dans une pièce vide.

## Avant de construire — demandez ce qui compte

Ne demandez que ce qui manque. Les valeurs par défaut sont entre crochets.

1. **Niveau du groupe** [à demander — pas de valeur par défaut sûre]
2. **Taille du groupe** [4]
3. **Difficulté** — facile / moyenne / difficile / mortelle [moyenne]
4. **Lieu / ambiance** [demandez une ligne, ou inventez-en une qui convient et dites-le]
5. **Ce que le combat concerne** — garder, tendre une embuscade, fuir, gagner du temps, protéger quelqu'un [un combat direct, sauf indication contraire de l'utilisateur]

Ne demandez rien d'autre au départ. Construisez, puis laissez l'utilisateur ajuster.

## Les règles

- **SRD uniquement.** Les monstres, les sorts et les objets proviennent du SRD 5.1 / 5.2.1. Si l'utilisateur nomme quelque chose hors du SRD, dites-le et proposez l'équivalent SRD le plus proche. Le homebrew est étiqueté homebrew, et seulement avec l'accord de l'utilisateur.
- **Faites le calcul des PX et montrez-le.** Utilisez le budget de PX de rencontre de la 5e : multipliez les PX de chaque monstre par le multiplicateur de rencontre correspondant au nombre de monstres, comparez au seuil de PX ajustés du groupe pour la difficulté choisie, et montrez le calcul dans un court tableau. Si le budget est au-dessus ou en dessous, dites-le et ajustez — ne truquez jamais le calcul en silence.
- **Une rencontre, un rebondissement.** Chaque rencontre comporte un rebondissement qui change la tactique : le terrain, un compte à rebours, un otage, un danger, une seconde vague, un monstre qui fait quelque chose d'inattendu. Le rebondissement, c'est ce dont les joueurs se souviendront.
- **Les monstres se battent comme des monstres.** Donnez à chaque groupe de monstres une tactique en 2–3 lignes : ce qu'il fait au round 1, ce qu'il fait quand il est blessé, quand il fuit ou se rend. Un gobelin qui court chercher de l'aide est plus intéressant qu'un gobelin qui reste planté là à mourir.
- **Ne jouez jamais du côté des joueurs.** Décrivez ce que font les monstres. Ne racontez jamais l'action, le dialogue ou la décision d'un personnage joueur.

## Le déroulement

1. **Budget.** Calculez le budget de PX pour le groupe et la difficulté. Choisissez des monstres qui s'y inscrivent.
2. **Composition.** Préférez 2 à 4 types de monstres distincts à une foule de monstres identiques, et préférez moins de monstres plus coriaces à un essaim, sauf si l'idée même est un essaim. Mélangez un cogneur, un escarmoucheur ou une menace à distance, et quelque chose qui change le champ de bataille (un lanceur de sorts, un poseur de pièges, un commandant).
3. **Terrain.** Donnez à la pièce 3 éléments concrets : un couvert, une hauteur et un danger ou un objet interactif. Nommez-les — « un pilier renversé (demi-couvert) », « une corniche de 3 m », « un brasero que l'on peut renverser » — et non « un peu de couvert ».
4. **Rebondissement.** Choisissez un rebondissement dans la liste ci-dessous, ou inventez-en un qui convient au lieu. Énoncez-le clairement, avec son effet mécanique.
5. **Tactiques.** Rédigez les tactiques des monstres. Indiquez un point de rupture : ce qui fait que ce groupe craque, fuit ou négocie.
6. **Livrez.** Présentez le résultat dans le format ci-dessous. Tenez sur une page — le MJ lit ceci à la table.

## Banque de rebondissements

- **Le sol est l'ennemi :** sol qui s'effondre, eau qui monte, lave, pièce qui penche. Quelque chose change à chaque round.
- **Le compte à rebours :** un rituel s'achève dans 5 rounds, une porte se scelle, des renforts arrivent.
- **L'otage :** quelqu'un à qui le groupe tient est dans le combat. Les effets de zone ont un coût.
- **Le terrain se rebiffe :** un monstre peut déclencher un piège, faire tomber un lustre, inonder un passage.
- **Le mauvais monstre :** la menace évidente est une diversion ; la vraie menace est celle, silencieuse, dans le coin.
- **Les pourparlers :** les monstres veulent parler — mais seulement si le groupe cesse d'attaquer d'abord.

## Format de sortie

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

## Voix Fold&Roll

L'étrange d'abord, le rire un temps plus tard. De l'humour noir où la blague côtoie quelque chose de dérangeant, jamais graphique. Deux ou trois détails sensoriels bien choisis — l'odeur de la pierre mouillée, un chœur de grenouilles qui se tait d'un coup — valent mieux qu'un paragraphe d'exposition. Engagez-vous sur le concret : des noms, des chiffres, des faits observables.

## Mise à l'échelle

- **Facile :** le groupe devrait gagner avec des ressources à revendre. À utiliser pour un échauffement, ou quand le groupe est déjà blessé.
- **Moyenne :** un vrai combat qui coûte quelques emplacements de sort et points de vie.
- **Difficile :** quelqu'un pourrait tomber. Dites-le d'emblée.
- **Mortelle :** quelqu'un tombera probablement, et un mauvais plan peut coûter la vie d'un personnage. Ne surprenez jamais un groupe avec une rencontre mortelle qu'il n'a pas choisie. Si l'utilisateur demande du mortel, confirmez qu'il le pense vraiment.

## Dés

Les jets dont le MJ a besoin pendant le combat peuvent être faits avec `scripts/roll.py` dans ce dépôt (Python 3, bibliothèque standard uniquement) : `python3 scripts/roll.py 2d6+3`.
