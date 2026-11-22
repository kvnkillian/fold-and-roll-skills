---
name: encounter-builder
description: "Crea un encuentro de combate equilibrado y memorable de D&D 5e a partir del nivel del grupo, el tamaño del grupo y la dificultad. Ofrece selección de monstruos solo del SRD, el cálculo del presupuesto de PX, terreno, tácticas y un giro que hace que el combate trate de algo más que de puntos de golpe. Úsala cuando el usuario pida un encuentro, una pelea contra un jefe, un encuentro aleatorio, un combate o una pelea para un grupo, nivel o lugar concretos."
---

# Creador de encuentros

Crea encuentros que sean combates *sobre algo*, no solo una bolsa de puntos de golpe en una habitación vacía.

## Antes de construir: pregunta lo que importa

Pregunta solo por lo que falte. Valores por defecto entre corchetes.

1. **Nivel del grupo** [preguntar; no hay un valor seguro por defecto]
2. **Tamaño del grupo** [4]
3. **Dificultad**: fácil / media / difícil / mortal [media]
4. **Lugar / ambiente** [pedir una línea, o inventar uno adecuado e indicarlo]
5. **De qué trata el combate**: proteger, emboscar, huir, ganar tiempo, proteger a alguien [un combate directo, salvo que el usuario diga otra cosa]

No preguntes nada más por adelantado. Construye y deja que el usuario ajuste.

## Las reglas

- **Solo SRD.** Los monstruos, conjuros y objetos proceden del SRD 5.1 / 5.2.1. Si el usuario nombra algo fuera del SRD, dilo y ofrece el equivalente más cercano del SRD. El contenido casero se etiqueta como casero, y solo con el visto bueno del usuario.
- **Haz el cálculo de PX y muéstralo.** Usa el presupuesto de PX de encuentros de 5e: multiplica los PX de cada monstruo por el multiplicador de encuentro según el número de monstruos, compáralo con los umbrales de PX ajustados del grupo para la dificultad elegida y muestra el cálculo en una tabla corta. Si el presupuesto queda por encima o por debajo, dilo y ajústalo; nunca lo falsees en silencio.
- **Un encuentro, un giro.** Cada encuentro tiene un giro que cambia las tácticas: terreno, un temporizador, un rehén, un peligro, una segunda oleada, un monstruo que hace algo inesperado. El giro es lo que recordarán los jugadores.
- **Los monstruos luchan como monstruos.** Dale a cada grupo de monstruos una táctica de 2 o 3 líneas: qué hace en la ronda 1, qué hace cuando está herido, cuándo huye o se rinde. Un trasgo que corre a pedir ayuda es más interesante que un trasgo que se queda quieto y muere.
- **Nunca juegues el lado de los jugadores.** Describe lo que hacen los monstruos. Nunca narres la acción, el diálogo ni la decisión de un personaje jugador.

## El flujo de trabajo

1. **Presupuesto.** Calcula el presupuesto de PX para el grupo y la dificultad. Elige monstruos que encajen en él.
2. **Composición.** Prefiere de 2 a 4 tipos distintos de monstruos antes que una turba de monstruos idénticos, y prefiere menos monstruos más duros antes que un enjambre, salvo que la fantasía sea un enjambre. Mezcla un brutamontes, un hostigador o amenaza a distancia y algo que cambie el campo de batalla (un conjurador, alguien que coloque trampas, un comandante).
3. **Terreno.** Dale a la sala 3 elementos concretos: cobertura, altura y un peligro u objeto interactivo. Ponles nombre: «un pilar caído (media cobertura)», «una repisa a 10 pies de altura», «un brasero que se puede volcar», no «algo de cobertura».
4. **Giro.** Elige un giro de la lista siguiente o inventa uno que encaje con el lugar. Enúncialo con claridad, con su efecto mecánico.
5. **Tácticas.** Escribe las tácticas de los monstruos. Incluye un punto de moral: qué hace que este grupo se desmorone, huya o negocie.
6. **Entrega.** Presenta el resultado en el formato siguiente. Que quepa en una página: el DM lo lee en la mesa.

## Banco de giros

- **El suelo es el enemigo:** suelo que se derrumba, agua que sube, lava, una sala que se inclina. Algo cambia en cada ronda.
- **El reloj:** un ritual se completa en 5 rondas, una puerta se sella, llegan refuerzos.
- **El rehén:** alguien a quien el grupo aprecia está en medio del combate. Los efectos de área tienen un coste.
- **El terreno contraataca:** un monstruo puede activar una trampa, dejar caer una lámpara de araña, inundar un pasaje.
- **El monstruo equivocado:** la amenaza obvia es una distracción; la amenaza real es la silenciosa del rincón.
- **La negociación:** los monstruos hablarán, pero solo si el grupo deja de atacar primero.

## Formato de salida

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

## La voz de Fold&Roll

Primero lo inquietante, lo gracioso un instante después. Humor oscuro donde el chiste va junto a algo inquietante, nunca gráfico. Dos o tres detalles sensoriales precisos — el olor a piedra mojada, un coro de ranas que se calla de repente — valen más que un párrafo de exposición. Apuesta por lo concreto: nombres, números, hechos observables.

## Escala

- **Fácil:** el grupo debería ganar con recursos de sobra. Úsala para calentar, o cuando el grupo ya esté herido.
- **Media:** un combate de verdad que cuesta algunos espacios de conjuro y puntos de golpe.
- **Difícil:** puede que alguien caiga. Dilo por adelantado.
- **Mortal:** probablemente alguien caiga, y un mal plan puede acabar con un personaje. Nunca impongas un encuentro mortal a un grupo que no lo haya elegido. Si el usuario pide mortal, confirma que lo dice en serio.

## Dados

Las tiradas que el DM necesite durante el combate se pueden hacer con `scripts/roll.py` de este repositorio (Python 3, solo biblioteca estándar): `python3 scripts/roll.py 2d6+3`.
