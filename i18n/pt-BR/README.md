> Nota: esta é uma tradução automática; a revisão por falantes nativos é bem-vinda.

# Habilidades de Mestre do Fold&Roll

Habilidades gratuitas de agente de IA para mestrar Dungeons & Dragons — dos criadores do Fold&Roll.

Instale-as no Claude Code, Codex, Cursor ou em qualquer agente que leia o padrão aberto Agent Skills, e seu agente para de improvisar conselhos de D&D no achismo e começa a preparar como um Mestre: situações, não enredos; consequências, não eventos; sinistro primeiro, engraçado um instante depois.

**Todo mundo à mesa.**

## As habilidades

| Habilidade | O que ela faz |
|---|---|
| `encounter-builder` | Encontros de 5e equilibrados e memoráveis a partir do nível, do tamanho e da dificuldade do grupo — com terreno, táticas e uma reviravolta. |
| `npc-generator` | NPCs com uma mania, um desejo e um segredo — além de uma voz, um gancho e o que acontece se o grupo ignorá-los. |
| `session-prep` | A preparação de uma sessão em uma página: situação, 3 a 5 nós, aberturas de impacto, movimentos de facções e um gancho final para encerrar. |
| `one-shot-builder` | Um one-shot completo de 3 a 4 horas: gancho, três atos, encontros, NPCs e um desfecho. |
| `solo-adventure` | Uma aventura solo para um jogador e um agente Mestre — escolhas, consequências e um final de verdade. |
| `campaign-arc` | Um arco de campanha em três atos e seis momentos, definidos pelo que muda — não pelo que acontece. |
| `dice-roller` | Role qualquer dado — vantagem, desvantagem, críticos, dano, rolagens em grupo — mostrando os dados, não só o total. |

## Instalação

### Claude Code

```sh
claude plugin install fold-and-roll-skills@kvnkillian
```

Ou copie as habilidades para a sua pasta pessoal de habilidades:

```sh
git clone https://github.com/kvnkillian/fold-and-roll-skills.git
cp -r fold-and-roll-skills/skills/* ~/.claude/skills/
```

### Codex / Cursor / Copilot

```sh
npx skills@latest add kvnkillian/fold-and-roll-skills
```

Ou copie as habilidades para `.agents/skills/` no seu projeto, ou para `~/.agents/skills/` para uso pessoal.

### Qualquer outro agente

Copie uma pasta `skills/<nome>/` para onde quer que o seu agente leia habilidades. Cada habilidade é um único arquivo `SKILL.md` — sem etapa de build, sem dependências. O ajudante de dados em `scripts/roll.py` precisa apenas de Python 3.

## Como usar

Peça ao seu agente com palavras simples. As descrições das habilidades dizem a ele quando disparar:

- "Monte um encontro para quatro personagens de nível 5, dificuldade difícil, em um templo alagado."
- "Me dê um NPC — um ferreiro que sabe demais."
- "Prepare a sessão de hoje à noite. Na última vez, o grupo queimou a ponte com a guilda."
- "Escreva um one-shot para um farol assombrado."
- "Mestre uma aventura solo para o meu ladino de nível 3."
- "Planeje um arco de campanha sobre uma cidade que esqueceu o próprio nome."

O agente vai pedir os poucos detalhes de que realmente precisa — nível e tamanho do grupo, tom, duração da sessão — e então entregar a coisa pronta para jogar.

## O jeito Fold&Roll

Estas habilidades seguem as mesmas regras sobre as quais o Fold&Roll é construído:

- **Prepare situações, não enredos.** Uma situação sobrevive ao contato com os seus jogadores. Um enredo quebra na primeira vez que eles fazem algo não planejado.
- **Jogadores são coautores.** Nunca narre o diálogo, os pensamentos ou as decisões de um personagem do jogador. A escolha é sempre deles.
- **Sinistro primeiro, engraçado um instante depois.** Humor sombrio em que a piada fica ao lado de algo perturbador, horror com um humor seco e nervoso — nunca gráfico, nunca sangrento por si só.
- **Somente SRD, a menos que você diga o contrário.** Monstros, magias e itens vêm do SRD 5.1 / 5.2.1. Homebrew é rotulado como homebrew, e o agente pergunta antes de inventá-lo.
- **Segurança em primeiro lugar.** Sessão zero, Linhas e Véus e uma Carta X fazem parte da preparação, não são um detalhe de última hora.
- **Todo mundo à mesa.** O conteúdo continua utilizável por todos os jogadores — linguagem clara, nenhuma informação apenas visual, nenhuma piada que precise de visão ou audição para funcionar.

## Quer a mesa completa?

Estas habilidades são a preparação. O Fold&Roll é a mesa — fichas de personagem, mapa de batalha, iniciativa e dados, feitos para um celular em cada mão e uma mesa compartilhada no meio.

- **iOS:** https://apps.apple.com/app/fold-roll/id6822885522
- **Beta para Android:** https://play.google.com/apps/testing/com.kevin.rpgcompanion
- **Site:** https://kvnkillian.github.io/

Entre no Discord pelo site para compartilhar as histórias da sua mesa, pedir uma habilidade ou relatar uma rolagem ruim.

## Licença

MIT. Use as habilidades, faça fork, remixe, use-as na sua mesa. Se você publicar um remix, um link de volta é apreciado, mas não é obrigatório.

O conteúdo do SRD nestas habilidades é usado sob a Licença Creative Commons Atribuição 4.0 Internacional (SRD 5.2.1) e a Open Game License v1.0a (SRD 5.1). Wizards of the Coast, Dungeons & Dragons e D&D são marcas registradas da Wizards of the Coast. Este projeto não é afiliado à Wizards of the Coast nem endossado por ela.
