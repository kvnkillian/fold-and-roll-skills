> *Cette traduction française a été réalisée par machine ; une relecture par des francophones natifs est la bienvenue.*

# Compétences de MJ Fold&Roll

Des compétences gratuites pour agents IA pour mener Donjons & Dragons — par les créateurs de Fold&Roll.

Installez-les dans Claude Code, Codex, Cursor ou tout agent qui lit le standard ouvert Agent Skills, et votre agent cessera d'improviser des conseils de D&D au feeling pour commencer à préparer comme un MJ : des situations, pas des intrigues ; des conséquences, pas des événements ; l'étrange d'abord, le rire un temps plus tard.

**Tout le monde à la table.**

## Les compétences

| Compétence | Ce qu'elle fait |
|---|---|
| `encounter-builder` | Des rencontres 5e équilibrées et mémorables à partir du niveau, de la taille et de la difficulté du groupe — avec terrain, tactiques et rebondissement. |
| `npc-generator` | Des PNJ avec une manie, un désir et un secret — plus une voix, un crochet et ce qui se passe si le groupe les ignore. |
| `session-prep` | Une préparation de session d'une page : situation, 3 à 5 nœuds, scènes-choc, manœuvres des factions et un cliffhanger pour conclure. |
| `one-shot-builder` | Un one-shot complet de 3 à 4 heures : crochet, trois actes, rencontres, PNJ et un dénouement. |
| `solo-adventure` | Une aventure solo pour un joueur et un MJ agent — des choix, des conséquences et une vraie fin. |
| `campaign-arc` | Un arc de campagne en trois actes et six temps forts, définis par ce qui change — et non par ce qui se passe. |

## Installation

### Claude Code

```sh
claude plugin install fold-and-roll-skills@kvnkillian
```

Ou copiez les compétences dans votre dossier personnel de compétences :

```sh
git clone https://github.com/kvnkillian/fold-and-roll-skills.git
cp -r fold-and-roll-skills/skills/* ~/.claude/skills/
```

### Codex / Cursor / Copilot

```sh
npx skills@latest add kvnkillian/fold-and-roll-skills
```

Ou copiez les compétences dans `.agents/skills/` dans votre projet, ou dans `~/.agents/skills/` pour un usage personnel.

### Tout autre agent

Copiez un dossier `skills/<nom>/` là où votre agent lit les compétences. Chaque compétence est un seul fichier `SKILL.md` — aucune étape de compilation, aucune dépendance. L'assistant de dés de `scripts/roll.py` ne nécessite que Python 3.

## Utilisez-les

Demandez à votre agent en mots simples. Les descriptions des compétences lui disent quand se déclencher :

- « Construis une rencontre pour quatre personnages de niveau 5, en difficulté difficile, dans un temple inondé. »
- « Donne-moi un PNJ — un forgeron qui en sait trop. »
- « Prépare la session de ce soir. La dernière fois, le groupe a brûlé ses ponts avec la guilde. »
- « Écris-moi un one-shot pour un phare hanté. »
- « Mène une aventure solo pour mon voleur de niveau 3. »
- « Planifie un arc de campagne sur une ville qui a oublié son propre nom. »

L'agent demandera les quelques détails dont il a vraiment besoin — le niveau et la taille du groupe, le ton, la durée de la session — puis livrera la chose, prête à jouer.

## La méthode Fold&Roll

Ces compétences suivent les mêmes règles que celles sur lesquelles Fold&Roll est construit :

- **Préparez des situations, pas des intrigues.** Une situation survit au contact de vos joueurs. Une intrigue se brise dès qu'ils font quelque chose d'imprévu.
- **Les joueurs sont co-auteurs.** Ne racontez jamais le dialogue, les pensées ou les décisions d'un personnage joueur. Le choix leur appartient toujours.
- **L'étrange d'abord, le rire un temps plus tard.** De l'humour noir où la blague côtoie quelque chose de dérangeant, de l'horreur avec un humour sec et nerveux — jamais graphique, jamais gore pour le gore.
- **SRD uniquement, sauf indication contraire.** Les monstres, les sorts et les objets proviennent du SRD 5.1 / 5.2.1. Le homebrew est étiqueté homebrew, et l'agent demande avant de l'inventer.
- **La sécurité d'abord.** Session zéro, Lignes et voiles (Lines & Veils) et carte X (X-card) font partie de la préparation, pas un ajout de dernière minute.
- **Tout le monde à la table.** Le contenu reste utilisable par chaque joueur — langage clair, aucune information uniquement visuelle, aucune blague qui nécessite la vue ou l'ouïe pour fonctionner.

## Vous voulez la table complète ?

Ces compétences sont la préparation. Fold&Roll est la table — fiches de personnage, carte de combat, initiative et dés, conçus pour un téléphone dans chaque main et une table partagée au milieu.

- **iOS :** https://apps.apple.com/app/fold-roll/id6822885522
- **Bêta Android :** https://play.google.com/apps/testing/com.kevin.rpgcompanion
- **Site web :** https://kvnkillian.github.io/

Rejoignez le Discord depuis le site web pour partager vos histoires de table, demander une compétence ou signaler un mauvais jet.

## Licence

MIT. Utilisez les compétences, forkez-les, remixez-les, jouez-les à votre table. Si vous publiez un remix, un lien de retour est apprécié mais pas obligatoire.

Le contenu du SRD dans ces compétences est utilisé sous la licence Creative Commons Attribution 4.0 International (SRD 5.2.1) et l'Open Game License v1.0a (SRD 5.1). Wizards of the Coast, Dungeons & Dragons et D&D sont des marques déposées de Wizards of the Coast. Ce projet n'est ni affilié à Wizards of the Coast ni soutenu par l'entreprise.
