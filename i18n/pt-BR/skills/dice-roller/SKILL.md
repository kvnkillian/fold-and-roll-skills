---
name: dice-roller
description: "Role dados para D&D 5e: qualquer notação (2d6+3, d20, 4d6 descartando o menor), vantagem e desvantagem, acertos críticos e falhas críticas, dano e rolagens em grupo. Use quando o usuário pedir para rolar dados, rolar um teste, rolar dano, rolar com vantagem ou desvantagem, ou rolar por um monstro, NPC ou jogador."
---

# Rolador de Dados

Role os dados, mostre os dados e deixe o resultado valer. Sem trapacear, em nenhuma das direções.

## Antes de rolar — pergunte o que importa

Pergunte apenas o que estiver faltando. Os padrões estão entre colchetes.

1. **O que rolar** — a notação, por exemplo, `2d6+3`, `d20`, `4d6` [pergunte — não há padrão seguro]
2. **Vantagem / desvantagem** — para um teste com d20 [nenhuma, a menos que o usuário diga o contrário]
3. **Para que é a rolagem** — um ataque, um teste, uma salvaguarda, dano [pergunte se isso muda a leitura do resultado; caso contrário, role e diga para que foi]

Se o usuário disser apenas "role", pergunte a notação uma vez e então role.

## As regras

- **Mostre os dados, não só o total.** Sempre informe cada dado e depois o total: `2d6+3: [4, 2] + 3 = 9`. Um total sem os dados não é uma rolagem.
- **Use o script quando puder.** Execute `python3 scripts/roll.py <notation>` a partir da raiz do repositório (Python 3, apenas a biblioteca padrão) e informe a saída dele. Se o script não estiver disponível, role honestamente e diga que rolou sem ele.
- **Vantagem e desvantagem são dois d20.** Vantagem: role dois d20 e fique com o maior. Desvantagem: role dois d20 e fique com o menor. Mostre os dois dados. Nunca role um só dado e chame isso de vantagem.
- **Um 20 natural é um acerto crítico em um ataque; um 1 natural é uma falha crítica.** Em uma rolagem de dano após um crítico, role os dados de dano duas vezes (não dobre o modificador). Diga quando isso acontecer — "20 natural, acerto crítico" — e então role o dano.
- **Informe a CD ou o alvo antes de os dados caírem, ou imediatamente depois** — nunca depois de o jogador já ter se comprometido com um plano diferente com base no resultado.
- **Nunca trapaceie uma rolagem.** Se o resultado for ruim para o grupo ou ruim para o monstro, ele vale. Uma rolagem falha muda a situação; ela não interrompe a história.
- **Nunca role por um personagem de jogador sem que peçam.** O jogador rola os próprios dados. O agente rola por monstros, NPCs e pelo mundo — e por um jogador apenas quando o jogador pedir.

## Notação

| Notação | Significado |
|---|---|
| `d20` | Um dado de 20 lados |
| `2d6+3` | Dois dados de 6 lados, mais 3 |
| `4d6 drop lowest 1` | Quatro dados de 6 lados, descarte o menor (valores de habilidade) |
| `d20 advantage` | Dois d20, fique com o maior |
| `d20 disadvantage` | Dois d20, fique com o menor |
| `8d6` | Oito dados de 6 lados (uma bola de fogo, por exemplo) |
| `1d4+1` | Um dado de 4 lados, mais 1 |

Os modificadores são somados uma vez, depois dos dados — nunca por dado, a menos que a regra diga o contrário.

## Formato de saída

```markdown
**Rolagem:** <para que foi>
**Dados:** <notação>: [<cada dado>] <+/- modificador> = <total>
**Resultado:** <o que significa — acerto / erro, sucesso / falha na salvaguarda, dano causado>
```

Para vantagem / desvantagem:

```markdown
**Rolagem:** <para que foi> — vantagem
**Dados:** d20: [14, 7] → fique com 14, + 5 = 19
**Resultado:** <o que significa>
```

## Rolagens em grupo

Quando várias criaturas rolam a mesma coisa — um grupo de goblins fazendo uma salvaguarda, por exemplo — role uma vez por criatura e liste cada resultado em sua própria linha. Não role uma vez só e aplique a todo o grupo, a menos que o usuário peça isso.

## A voz do Fold&Roll

Os dados são o único lugar em que a voz fica direta. Nada de floreio na rolagem em si — o drama está no resultado, não no relato. Uma linha para os dados, uma linha para o que isso significa, e de volta ao jogo.
