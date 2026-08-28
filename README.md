# Mímir

**Cofacilitador de IA para procesos de grupo.** Un agente conversacional con criterio
de facilitación profesional que **asiste a un facilitador humano** en el prediseño y
diseño de procesos grupales — y que tiene prohibido, por diseño, ocupar su lugar.

> En la mitología nórdica, Mímir es una cabeza sin cuerpo: aconseja a Odín, le dice lo
> que sabe, y no puede hacer nada más. Odín decide. Ése es exactamente su lugar.

## Qué es (y qué no es)

Mímir no es un chatbot de facilitación genérica. Es la compilación de una doctrina de
trabajo concreta — basada en escuelas publicadas (IIFACe / Escorihuela 'Ulises',
Trabajo de Procesos de Arnold Mindell, Beatrice Briggs) más el criterio volcado por un
facilitador en ejercicio — con tres propiedades poco habituales en agentes:

1. **Señala, no decide.** Toda su salida termina devolviendo la decisión al humano.
2. **Declara sus huecos.** Si algo no está en su corpus, lo dice; no rellena con
   plausibilidad.
3. **Se audita a sí mismo.** Autochequeos obligatorios sobre su propia salida (puerta
   de entrega, chequeo del sesgo salvador, registro de aprendizaje).

El detalle completo de capacidades está en [HABILIDADES.md](HABILIDADES.md).

## Estructura del repo

```
mimir/
├── PROMPT.md        ← el núcleo del agente (system prompt completo, autosuficiente)
├── HABILIDADES.md   ← enumeración de capacidades y límites
├── INSTALL.md       ← instalación en distintos ecosistemas
├── SKILL.md         ← definición de skill para Claude Code (el repo se clona como skill)
└── README.md
```

## Instalación rápida

Ver [INSTALL.md](INSTALL.md). Resumen: el agente es **un solo archivo de prompt**
(`PROMPT.md`) — funciona en cualquier ecosistema que acepte un system prompt (Claude
Code, Claude Projects, API de cualquier LLM capaz, asistentes locales). En Claude Code,
clonar este repo dentro de `~/.claude/skills/mimir/` lo deja invocable como `/mimir`.

## Procedencia y anonimización

- Esta distribución deriva de la versión **v3 cerrada** del despliegue original:
  el núcleo v3 validado por su autor, más las reglas de instrumento que quedaron
  convertidas (y probadas) durante un caso real de una semana — un proceso de grupo
  con equipo de facilitación humano. Está **anonimizada**: sin nombres de personas,
  sin material de casos reales, sin referencias resolubles al cuaderno de trabajo
  privado.
- Los códigos entre paréntesis en el prompt (A1, D8, F17…) son **marcadores de
  trazabilidad** del corpus original. Se conservan como procedencia; no hay que
  resolverlos para usar el agente.
- El corpus de consulta ampliado (apuntes por fuente, baterías de prueba, protocolos
  extendidos) **no se distribuye**: es privado. El núcleo del prompt fue validado como
  autosuficiente.

## Filosofía de uso

Mímir asume que **cliente y grupo saben siempre que hay una IA en la preparación**, que
**todo lo que sale de su cuaderno de trabajo sale anonimizado o por rol**, y que **la
conducción en directo jamás se delega**. Si vas a desplegarlo, esas tres no son
opcionales: son el contrato del rol.

## Licencia

**CC BY-NC-SA 4.0** — puedes usar y adaptar Mímir citando al autor, sin uso comercial,
y compartiendo cualquier derivado bajo la misma licencia. Texto completo en
[LICENSE](LICENSE).
