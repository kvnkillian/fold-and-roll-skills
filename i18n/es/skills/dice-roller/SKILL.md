---
name: dice-roller
description: "Tira dados para D&D 5e: cualquier notación (2d6+3, d20, 4d6 descartando el más bajo), ventaja y desventaja, golpes críticos y fallos críticos, daño y tiradas en grupo. Úsala cuando el usuario pida tirar dados, hacer una tirada, tirar daño, tirar con ventaja o desventaja, o tirar por un monstruo, un PNJ o un jugador."
---

# Tirador de dados

Tira los dados, muestra los dados y deja que el resultado se mantenga. Sin falsear, en ninguna dirección.

## Antes de tirar — pregunta lo que importa

Pregunta solo por lo que falte. Valores por defecto entre corchetes.

1. **Qué tirar** — la notación, p. ej. `2d6+3`, `d20`, `4d6` [preguntar; no hay un valor seguro por defecto]
2. **Ventaja / desventaja** — para una prueba de d20 [ninguna, salvo que el usuario diga lo contrario]
3. **Para qué es la tirada** — un ataque, una prueba, una salvación, daño [preguntar si cambia la lectura del resultado; si no, tira y di para qué era]

Si el usuario solo dice «tira», pide la notación una vez y luego tira.

## Las reglas

- **Muestra los dados, no solo el total.** Informa siempre cada dado y luego el total: `2d6+3: [4, 2] + 3 = 9`. Un total sin los dados no es una tirada.
- **Usa el script cuando puedas.** Ejecuta `python3 scripts/roll.py <notation>` desde la raíz del repositorio (Python 3, solo biblioteca estándar) e informa su salida. Si el script no está disponible, tira con honradez y di que tiraste sin él.
- **La ventaja y la desventaja son dos d20.** Ventaja: tira dos d20 y quédate con el más alto. Desventaja: tira dos d20 y quédate con el más bajo. Muestra ambos dados. Nunca tires un solo dado y lo llames ventaja.
- **Un 20 natural es un golpe crítico en un ataque; un 1 natural es un fallo crítico (fumble).** En una tirada de daño tras un crítico, tira los dados de daño dos veces (no dupliques el modificador). Dilo cuando ocurra — «20 natural, golpe crítico» — y luego tira el daño.
- **Indica la CD o el objetivo antes de que caigan los dados, o inmediatamente después** — nunca después de que el jugador ya se haya comprometido con otro plan basándose en el resultado.
- **Nunca falsees una tirada.** Si el resultado es malo para el grupo o malo para el monstruo, se mantiene. Una tirada fallida cambia la situación; no detiene la historia.
- **Nunca tires por un personaje jugador sin que te lo pidan.** El jugador tira sus propios dados. El agente tira por los monstruos, los PNJ y el mundo — y por un jugador solo cuando el jugador se lo pide.

## Notación

| Notación | Significado |
|---|---|
| `d20` | Un dado de 20 caras |
| `2d6+3` | Dos dados de 6 caras, más 3 |
| `4d6 drop lowest 1` | Cuatro dados de 6 caras, descarta el más bajo (puntuaciones de característica) |
| `d20 advantage` | Dos d20, quédate con el más alto |
| `d20 disadvantage` | Dos d20, quédate con el más bajo |
| `8d6` | Ocho dados de 6 caras (una bola de fuego, por ejemplo) |
| `1d4+1` | Un dado de 4 caras, más 1 |

Los modificadores se suman una sola vez, después de los dados — nunca por dado, salvo que la regla diga lo contrario.

## Formato de salida

```markdown
**Tirada:** <para qué era>
**Dados:** <notación>: [<cada dado>] <+/- modificador> = <total>
**Resultado:** <qué significa — acierto / fallo, salvación / fallo, daño infligido>
```

Para ventaja / desventaja:

```markdown
**Tirada:** <para qué era> — ventaja
**Dados:** d20: [14, 7] → quédate con el 14, + 5 = 19
**Resultado:** <qué significa>
```

## Tiradas en grupo

Cuando varias criaturas tiran lo mismo — un grupo de trasgos haciendo una salvación, por ejemplo — tira una vez por criatura y enumera cada resultado en su propia línea. No tires una sola vez y la apliques a todo el grupo, salvo que el usuario lo pida.

## La voz de Fold&Roll

Los dados son el único lugar donde la voz se mantiene sencilla. Sin florituras en la tirada en sí — el dramatismo está en el resultado, no en el informe. Una línea para los dados, una línea para lo que significa, y de vuelta al juego.
