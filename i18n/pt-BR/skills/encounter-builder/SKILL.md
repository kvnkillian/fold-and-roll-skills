---
name: encounter-builder
description: "Monte um encontro de combate equilibrado e memorável de D&D 5e a partir do nível do grupo, do tamanho do grupo e da dificuldade. Traz escolhas de monstros apenas do SRD, a matemática do orçamento de XP, terreno, táticas e uma reviravolta que faz a luta ser mais do que pontos de vida. Use quando o usuário pedir um encontro, uma luta contra um chefe, um encontro aleatório, um combate ou uma luta para um grupo, nível ou local específico."
---

# Construtor de Encontros

Monte encontros que são lutas *sobre alguma coisa*, não apenas um saco de pontos de vida em uma sala vazia.

## Antes de montar — pergunte o que importa

Pergunte apenas o que estiver faltando. Padrões entre colchetes.

1. **Nível do grupo** [pergunte — não há padrão seguro]
2. **Tamanho do grupo** [4]
3. **Dificuldade** — fácil / médio / difícil / mortal [médio]
4. **Local / clima** [peça uma linha, ou invente um adequado e diga isso]
5. **Sobre o que é a luta** — guardar, emboscar, fugir, ganhar tempo, proteger alguém [uma luta direta, a menos que o usuário diga o contrário]

Não pergunte mais nada de início. Monte e deixe o usuário ajustar.

## As regras

- **Somente SRD.** Monstros, magias e itens vêm do SRD 5.1 / 5.2.1. Se o usuário citar algo fora do SRD, diga isso e ofereça o equivalente mais próximo do SRD. Homebrew é rotulado como homebrew, e somente com a permissão do usuário.
- **Faça a matemática do XP e mostre-a.** Use o orçamento de XP de encontro do 5e: multiplique o XP de cada monstro pelo multiplicador de encontro correspondente ao número de monstros, compare com os limites de XP ajustado do grupo para a dificuldade escolhida e mostre o cálculo em uma tabela curta. Se o orçamento estiver acima ou abaixo, diga isso e ajuste — nunca ajuste às escondidas.
- **Um encontro, uma reviravolta.** Todo encontro ganha uma reviravolta que muda as táticas: terreno, um cronômetro, um refém, um perigo, uma segunda onda, um monstro que faz algo inesperado. A reviravolta é o que os jogadores vão lembrar.
- **Monstros lutam como monstros.** Dê a cada grupo de monstros uma tática de 2 a 3 linhas: o que ele faz na rodada 1, o que faz quando é ferido, quando foge ou se rende. Um goblin que corre para pedir ajuda é mais interessante do que um goblin que fica parado e morre.
- **Nunca jogue do lado dos jogadores.** Descreva o que os monstros fazem. Nunca narre a ação, o diálogo ou a decisão de um personagem do jogador.

## O fluxo de trabalho

1. **Orçamento.** Calcule o orçamento de XP para o grupo e a dificuldade. Escolha monstros que caibam nele.
2. **Composição.** Prefira 2 a 4 tipos distintos de monstros em vez de uma multidão de monstros idênticos, e prefira menos monstros mais fortes a um enxame, a menos que a fantasia seja um enxame. Misture um bruto, um escaramuçador ou ameaça à distância, e algo que mude o campo de batalha (um conjurador, alguém que arma armadilhas, um comandante).
3. **Terreno.** Dê à sala 3 elementos concretos: cobertura, altura e um perigo ou objeto interativo. Nomeie-os — "um pilar tombado (meia cobertura)", "uma saliência de 3 m", "um braseiro que pode ser derrubado" — e não "alguma cobertura".
4. **Reviravolta.** Escolha uma reviravolta da lista abaixo ou invente uma que combine com o local. Declare-a claramente, com seu efeito mecânico.
5. **Táticas.** Escreva as táticas dos monstros. Inclua um ponto de moral: o que faz este grupo quebrar, fugir ou negociar.
6. **Entrega.** Saída no formato abaixo. Mantenha em uma página — o Mestre lê isso na mesa.

## Banco de reviravoltas

- **O chão é o inimigo:** piso que desaba, água que sobe, lava, uma sala que inclina. Algo muda a cada rodada.
- **O relógio:** um ritual se completa em 5 rodadas, uma porta se fecha, reforços chegam.
- **O refém:** alguém com quem o grupo se importa está na luta. Efeitos em área têm um custo.
- **O terreno revida:** um monstro pode acionar uma armadilha, derrubar um lustre, inundar uma passagem.
- **O monstro errado:** a ameaça óbvia é uma distração; a ameaça real é a silenciosa no canto.
- **O parlamento:** os monstros vão conversar — mas somente se o grupo parar de atacar primeiro.

## Formato de saída

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

## A voz do Fold&Roll

Sinistro primeiro, engraçado um instante depois. Humor sombrio em que a piada fica ao lado de algo perturbador, nunca gráfico. Dois ou três detalhes sensoriais marcantes — o cheiro de pedra molhada, um coro de sapos que de repente silencia — valem mais do que um parágrafo de exposição. Comprometa-se com detalhes específicos: nomes, números, fatos observáveis.

## Escala

- **Fácil:** o grupo deve vencer com recursos de sobra. Use para um aquecimento, ou quando o grupo já estiver ferido.
- **Médio:** uma luta de verdade que custa alguns espaços de magia e pontos de vida.
- **Difícil:** alguém pode cair. Diga isso logo de início.
- **Mortal:** alguém provavelmente cai, e um plano ruim pode acabar com um personagem. Nunca jogue uma luta mortal em um grupo que não a escolheu. Se o usuário pedir mortal, confirme se ele realmente quer isso.

## Dados

As rolagens de que o Mestre precisa durante a luta podem ser feitas com `scripts/roll.py` neste repositório (Python 3, apenas biblioteca padrão): `python3 scripts/roll.py 2d6+3`.
