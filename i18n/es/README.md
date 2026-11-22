> Nota: esta es una traducción automática; se agradece la revisión de hablantes nativos.

# Habilidades de DM de Fold&Roll

Habilidades gratuitas de agente de IA para dirigir Dungeons & Dragons, de los creadores de Fold&Roll.

Instálalas en Claude Code, Codex, Cursor o cualquier agente que lea el estándar abierto de Agent Skills, y tu agente dejará de improvisar consejos de D&D por intuición para empezar a preparar como un DM: situaciones, no tramas; consecuencias, no eventos; primero lo inquietante, lo gracioso un instante después.

**Todos en la mesa.**

## Las habilidades

| Habilidad | Qué hace |
|---|---|
| `encounter-builder` | Encuentros equilibrados y memorables de 5e a partir del nivel, el tamaño del grupo y la dificultad, con terreno, tácticas y un giro. |
| `npc-generator` | PNJ con una peculiaridad, un deseo y un secreto, además de una voz, un gancho y qué pasa si el grupo los ignora. |
| `session-prep` | Una preparación de sesión en una página: situación, de 3 a 5 nodos, inicios de escena, movimientos de facciones y un final en suspenso. |
| `one-shot-builder` | Una aventura autoconclusiva completa de 3 a 4 horas: gancho, tres actos, encuentros, PNJ y un desenlace que llega a buen puerto. |
| `solo-adventure` | Una aventura en solitario para un jugador y un DM agente: decisiones, consecuencias y un final de verdad. |
| `campaign-arc` | Un arco de campaña en tres actos y seis hitos, definidos por lo que cambia, no por lo que sucede. |

## Instalación

### Claude Code

```sh
claude plugin install fold-and-roll-skills@kvnkillian
```

O copia las habilidades en tu carpeta personal de habilidades:

```sh
git clone https://github.com/kvnkillian/fold-and-roll-skills.git
cp -r fold-and-roll-skills/skills/* ~/.claude/skills/
```

### Codex / Cursor / Copilot

```sh
npx skills@latest add kvnkillian/fold-and-roll-skills
```

O copia las habilidades en `.agents/skills/` dentro de tu proyecto, o en `~/.agents/skills/` para uso personal.

### Cualquier otro agente

Copia una carpeta `skills/<nombre>/` dondequiera que tu agente lea las habilidades. Cada habilidad es un solo archivo `SKILL.md`: sin paso de compilación ni dependencias. El ayudante de dados de `scripts/roll.py` solo necesita Python 3.

## Cómo usarlas

Pídeselo a tu agente con palabras sencillas. Las descripciones de las habilidades le indican cuándo activarse:

- "Crea un encuentro para cuatro personajes de nivel 5, dificultad difícil, en un templo inundado".
- "Dame un PNJ: un herrero que sabe demasiado".
- "Prepara la sesión de esta noche. La última vez, el grupo quemó el puente con el gremio".
- "Escríbeme una aventura autoconclusiva para un faro encantado".
- "Dirige una aventura en solitario para mi pícaro de nivel 3".
- "Planifica un arco de campaña sobre una ciudad que olvidó su propio nombre".

El agente te pedirá los pocos detalles que de verdad necesita — nivel y tamaño del grupo, tono, duración de la sesión — y luego entregará el material, listo para jugar.

## El estilo Fold&Roll

Estas habilidades siguen las mismas reglas sobre las que se construye Fold&Roll:

- **Prepara situaciones, no tramas.** Una situación sobrevive al contacto con tus jugadores. Una trama se rompe la primera vez que hacen algo imprevisto.
- **Los jugadores son coautores.** Nunca narres el diálogo, los pensamientos ni las decisiones de un personaje jugador. La decisión siempre es de ellos.
- **Primero lo inquietante, lo gracioso un instante después.** Humor oscuro donde el chiste va junto a algo inquietante, horror con ingenio seco y nervioso; nunca gráfico, nunca sangriento por el mero hecho de serlo.
- **Solo SRD, salvo que digas lo contrario.** Los monstruos, conjuros y objetos proceden del SRD 5.1 / 5.2.1. El contenido casero se etiqueta como casero, y el agente pregunta antes de inventarlo.
- **La seguridad primero.** La sesión cero, las Líneas y Velos y la tarjeta X forman parte de la preparación, no son un añadido de última hora.
- **Todos en la mesa.** El contenido sigue siendo utilizable por todos los jugadores: lenguaje claro, sin información solo visual, sin chistes que necesiten vista u oído para entenderse.

## ¿Quieres la mesa completa?

Estas habilidades son la preparación. Fold&Roll es la mesa: fichas de personaje, mapa de batalla, iniciativa y dados, pensados para un teléfono en cada mano y una mesa compartida en el centro.

- **iOS:** https://apps.apple.com/app/fold-roll/id6822885522
- **Beta de Android:** https://play.google.com/apps/testing/com.kevin.rpgcompanion
- **Sitio web:** https://kvnkillian.github.io/

Únete al Discord desde el sitio web para compartir las historias de tu mesa, pedir una habilidad o denunciar una mala tirada.

## Licencia

MIT. Usa las habilidades, bifurca el proyecto, remézclalas, úsalas en tu mesa. Si publicas una remezcla, se agradece un enlace de vuelta, pero no es obligatorio.

El contenido del SRD en estas habilidades se usa bajo la licencia Creative Commons Atribución 4.0 Internacional (SRD 5.2.1) y la Licencia de Juego Abierto v1.0a (SRD 5.1). Wizards of the Coast, Dungeons & Dragons y D&D son marcas comerciales de Wizards of the Coast. Este proyecto no está afiliado a Wizards of the Coast ni cuenta con su respaldo.
