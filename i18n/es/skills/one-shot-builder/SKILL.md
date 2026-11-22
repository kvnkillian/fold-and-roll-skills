---
name: one-shot-builder
description: "Escribe una aventura autoconclusiva completa de D&D 5e para una sesión de 3 a 4 horas: gancho, tres actos, encuentros, PNJ y un desenlace que llega a buen puerto. Úsala cuando el usuario pida una aventura autoconclusiva, una aventura de una sola sesión, una partida de convención, una aventura de introducción para jugadores nuevos o una historia independiente."
---

# Creador de aventuras autoconclusivas

Una aventura autoconclusiva es una historia completa en una sola sentada: un gancho que los jugadores no pueden ignorar, un medio que lo complica y un final que cambia algo. No es un capítulo de campaña al que se le hayan limado los números de serie.

## Antes de construir: pregunta lo que importa

Pregunta solo por lo que falte. Valores por defecto entre corchetes.

1. **Nivel del grupo** [3]
2. **Tamaño del grupo** [4]
3. **Duración de la sesión** [3–4 horas]
4. **Ambientación / idea del gancho** [pedir una línea, o inventar una e indicarlo]
5. **Tono**: terror, comedia, intriga, exploración de mazmorras [primero lo inquietante con humor seco]
6. **¿Jugadores nuevos?** [no; si la respuesta es sí, simplifica la carga de reglas y pon la diversión por delante]

## Las reglas

- **Un gancho, un villano, un desenlace.** Una aventura autoconclusiva no puede cargar con una subtrama. Recorta todo lo que no sirva al gancho o al final.
- **Solo SRD.** Monstruos, conjuros y objetos del SRD 5.1 / 5.2.1. El contenido casero se etiqueta como casero, y solo con el visto bueno del usuario.
- **Tres actos, y el medio debe complicar.** Acto 1: el gancho se vuelve personal. Acto 2: el problema es más grande o más extraño de lo que parecía al principio. Acto 3: la confrontación decisiva y la resolución. Si el acto 2 es solo «más de lo mismo del acto 1», reescríbelo.
- **El final es una consecuencia, no un evento.** Define el final por lo que debe ser distinto después de él, no por cómo sucede. Una docena de escenas podrían entregarlo; un solo evento anticipado lo mata.
- **Personajes pregenerados opcionales, no obligatorios.** Si el usuario quiere pregenerados, ofrécelos como continuación: cuatro personajes adecuados al nivel, con un deseo, un secreto y una conexión con el gancho. No los construyas sin que te los pidan.
- **Herramientas de seguridad desde el principio.** Las Líneas y Velos y la tarjeta X, enunciadas antes de jugar. Si la aventura autoconclusiva toca una línea habitual (horror corporal, niños en peligro, control mental), avísalo en la presentación, no en mitad de la partida.
- **Nunca juegues el lado de los jugadores.** Escribe lo que el mundo presenta. Nunca escribas lo que un personaje jugador dice, piensa o decide.

## El flujo de trabajo

1. **El gancho.** Un párrafo, y una línea que el DM pueda leer en voz alta. El gancho debe apelar a lo que un *personaje* quiere, no solo a que «hay un trabajo disponible». Dale al grupo una razón para implicarse en los primeros diez minutos.
2. **El villano.** Un objetivo que el grupo pueda entender, un plan para lo que pasa si el grupo no hace nada y una razón por la que no basta con matarlo sin más. El villano es el motor.
3. **Acto 1: el gancho se vuelve personal.** El incidente incitador, un encuentro, un PNJ que importa.
4. **Acto 2: la complicación.** El problema es más grande o más extraño de lo que parecía. Una escena de exploración o social, un encuentro de combate, una revelación.
5. **Acto 3: la confrontación y el desenlace.** El momento decisivo y luego la resolución: qué es distinto en el mundo y en los personajes después.
6. **El reparto.** De 3 a 4 PNJ, cada uno con una peculiaridad, un deseo y un secreto (usa la forma de `npc-generator`; no repitas aquí todas sus reglas).
7. **Los encuentros.** De 2 a 3 encuentros, cada uno con un presupuesto de PX, terreno y un giro (usa la forma de `encounter-builder`; no repitas aquí todas sus reglas).
8. **Entrega.** En el formato siguiente. Apunta a 2 o 3 páginas: un DM debería poder leerlo una vez y dirigirlo.

## Formato de salida

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

## La voz de Fold&Roll

Primero lo inquietante, lo gracioso un instante después. Humor oscuro donde el chiste va junto a algo inquietante, horror con ingenio seco y nervioso, nunca gráfico. Un faro encantado da miedo porque la luz está encendida y no hay nadie en casa, no por lo que hay en el sótano. Apuesta por lo concreto: un nombre, un olor, un sonido que se detiene.
