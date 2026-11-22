---
name: one-shot-builder
description: "Écrivez un one-shot complet pour D&D 5e pour une session de 3 à 4 heures : crochet, trois actes, rencontres, PNJ et un dénouement qui marque. À utiliser quand l'utilisateur demande un one-shot, une aventure en une session, un jeu de convention, une aventure d'introduction pour de nouveaux joueurs ou une histoire autonome."
---

# Créateur de one-shot

Un one-shot est une histoire complète en une seule séance : un crochet que les joueurs ne peuvent pas ignorer, un milieu qui le complique, et une fin qui change quelque chose. Ce n'est pas un chapitre de campagne dont on aurait limé les numéros de série.

## Avant de construire — demandez ce qui compte

Ne demandez que ce qui manque. Les valeurs par défaut sont entre crochets.

1. **Niveau du groupe** [3]
2. **Taille du groupe** [4]
3. **Durée de la session** [3 à 4 heures]
4. **Cadre / idée de crochet** [demandez une ligne, ou inventez-en une et dites-le]
5. **Ton** — horreur, comédie, intrigue, exploration de donjon [l'étrange d'abord avec un humour sec]
6. **Nouveaux joueurs ?** [non — si oui, allégez la charge de règles et mettez le plaisir en avant]

## Les règles

- **Un crochet, un méchant, un dénouement.** Un one-shot ne peut pas porter d'intrigue secondaire. Coupez tout ce qui ne sert ni le crochet ni la fin.
- **SRD uniquement.** Monstres, sorts et objets du SRD 5.1 / 5.2.1. Le homebrew est étiqueté homebrew, et seulement avec l'accord de l'utilisateur.
- **Trois actes, et le milieu doit compliquer.** Acte 1 : le crochet devient personnel. Acte 2 : le problème est plus grand ou plus étrange qu'il n'y paraissait. Acte 3 : la confrontation décisive et la résolution. Si l'acte 2 n'est que « davantage d'acte 1 », réécrivez-le.
- **La fin est une conséquence, pas un événement.** Définissez la fin par ce qui doit être différent après elle — pas par la façon dont elle se produit. Une douzaine de scènes pourraient la livrer ; un seul événement anticipé la tue.
- **Personnages prétirés facultatifs, pas obligatoires.** Si l'utilisateur veut des prétirés, proposez-les en suivi — quatre personnages de niveau adapté avec un désir, un secret et un lien avec le crochet. Ne les construisez pas sans qu'on vous le demande.
- **Les outils de sécurité d'abord.** Lignes et voiles (Lines & Veils) et carte X (X-card), énoncés avant de jouer. Si le one-shot touche une ligne courante (horreur corporelle (body horror), enfants en danger, contrôle mental), signalez-le dans le pitch, pas au milieu de la partie.
- **Ne jouez jamais du côté des joueurs.** Écrivez ce que le monde présente. N'écrivez jamais ce qu'un personnage joueur dit, pense ou décide.

## Le déroulement

1. **Le crochet.** Un paragraphe, et une ligne que le MJ peut lire à voix haute. Le crochet doit toucher ce qu'un *personnage* veut, pas seulement « un travail est disponible ». Donnez au groupe une raison de se soucier de l'histoire dans les dix premières minutes.
2. **Le méchant.** Un objectif que le groupe peut comprendre, un plan pour ce qui se passe si le groupe ne fait rien, et une raison qui rend difficile de simplement le tuer. Le méchant est le moteur.
3. **Acte 1 — le crochet devient personnel.** L'incident déclencheur, une rencontre, un PNJ qui compte.
4. **Acte 2 — la complication.** Le problème est plus grand ou plus étrange qu'il n'y paraissait. Une scène d'exploration ou sociale, une rencontre de combat, une révélation.
5. **Acte 3 — la confrontation et le dénouement.** Le moment décisif, puis la résolution : ce qui est différent dans le monde et pour les personnages après.
6. **La distribution.** 3 à 4 PNJ, chacun avec une manie, un désir et un secret (utilisez la forme de `npc-generator` — ne redites pas toutes ses règles ici).
7. **Les rencontres.** 2 à 3 rencontres, chacune avec un budget de PX, un terrain et un rebondissement (utilisez la forme de `encounter-builder` — ne redites pas toutes ses règles ici).
8. **Livrez.** Dans le format ci-dessous. Visez 2 à 3 pages — un MJ devrait pouvoir le lire une fois et le mener.

## Format de sortie

```markdown
# <Title> — a one-shot for <n> level <x> characters, <3–4> hours

**Pitch:** <one line — the hook, as a sentence a DM could say to recruit players>
**Tone:** <tone> | **Lines & Veils:** <note the table's lines, or "confirm before play">

## The hook
<one paragraph. Then: **Read aloud:** "<one or two lines>">

## The villain: <name>
**Goal:** <one line> | **Plan if the party does nothing:** <one line> | **Why they are hard to kill:** <one line>

## Act 1 — <title>
<what happens, the NPC, the encounter>

## Act 2 — <title>
<the complication, the reveal, the encounter>

## Act 3 — <title>
<the confrontation, then the resolution — what is different after>

## Cast
- **<Name>** (<role>): <quirk> | Wants <want> | Hiding <secret>

## Encounters
- **<Name>** — <difficulty>, <monsters>, <terrain + twist in one line>

## If the party goes sideways
<one paragraph — the situation, not the plot: what moves, what surfaces elsewhere, what the villain does next>
```

## Voix Fold&Roll

L'étrange d'abord, le rire un temps plus tard. De l'humour noir où la blague côtoie quelque chose de dérangeant, de l'horreur avec un humour sec et nerveux, jamais graphique. Un phare hanté fait peur parce que la lumière est allumée et que personne n'est à la maison — pas à cause de ce qu'il y a dans la cave. Engagez-vous sur le concret : un nom, une odeur, un son qui s'arrête.
