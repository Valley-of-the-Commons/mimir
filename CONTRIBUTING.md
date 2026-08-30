# Contribuir a Mímir — el ciclo de aprendizaje federado

Mímir mejora igual en todos los despliegues: **por conversión de fallos y hallazgos en
reglas**, nunca por volcado de casos. Si usas Mímir, tu despliegue genera aprendizaje
(el prompt le obliga a correr su REGISTRO DE APRENDIZAJE al cierre de cada vuelta).
Ese aprendizaje puede volver aquí y mejorar el Mímir de todos.

## El ciclo

```
tu despliegue usa a Mímir
        ↓
registro de aprendizaje (formato del prompt: qué pasó · clase · convierte en · funcionó)
        ↓
ANONIMIZAR (obligatorio, ver abajo)
        ↓
Issue «Registro de aprendizaje» en este repo  (o PR sobre PROMPT.md)
        ↓
revisión del mantenedor → entra como `candidato`
        ↓
validación contra la doctrina del autor → recompilación de PROMPT.md (nueva versión)
        ↓
cada despliegue absorbe con `git pull`
```

## Qué se acepta

- **Reglas al nivel de principio**, en el formato del registro del prompt. Una regla
  solo cuenta si **convierte** en: paso de loop · línea de puerta · línea de spec ·
  regla de instrumento. (Es la regla de conversión del propio Mímir: hallazgo que no
  convierte, se descarta.)
- **Lo que funcionó** también — el registro no es solo de fallos.
- Cada contribución entra con estatus **`candidato`** (taxonomía del prompt) hasta que
  el mantenedor la valida. Un `candidato` rechazado se archiva como `descartado` con su
  porqué — también es conocimiento.

## Qué NO se acepta — sin excepciones

- **Material de casos**: nombres, organizaciones, transcripciones, relatos de sesión,
  fechas identificables. La doctrina de Mímir lo prohíbe (memoria de proceso, no de
  personas; entre grupos solo cruza el principio anonimizado) y aplica también aquí:
  **el repo es una frontera — todo lo que cruza, anonimizado o no entra.**
- Juicios sobre personas, aunque vengan anonimizados («el cliente era X»).
- Facilitación genérica sin origen en uso real: si no salió de un registro de
  aprendizaje de un despliegue, no es una contribución — es opinión.
- Cambios a la doctrina núcleo (☉ NÚCLEO DURO, REGLA DE ORO, QUÉ NO HACES): esa capa
  es del autor. Puedes **señalar** un conflicto (la confrontación es obligación del
  rol, también hacia arriba) — la decisión es suya.

## Cómo

1. **Issue** con la plantilla «Registro de aprendizaje» (preferido para reglas sueltas).
   Tu propio Mímir lo prepara: el protocolo de cierre de sesión (paso 6 del prompt)
   genera el bloque anonimizado y te lo ofrece — tú apruebas el envío, cada vez.
2. **PR** sobre `PROMPT.md` solo para correcciones editoriales o cuando el mantenedor
   te lo pida tras discutir el Issue.

## Procedencia — el entrenamiento es conjunto y con crédito

- **Quién**: automático — cada Issue lleva la cuenta de GitHub que lo abrió. Si quieres
  otra atribución (organización, alias de despliegue), usa el campo «Despliegue» de la
  plantilla.
- **Qué versión**: la plantilla pide el `version:` del prompt con el que corría tu
  despliegue — sin eso, una regla no se puede situar.
- **El crédito viaja**: cuando una regla `candidato` se valida y recompila, el commit
  que la integra nombra el Issue de origen (`#N`) — la procedencia queda en el
  historial para siempre.

## Jerarquía — quién decide

La misma del prompt: **doctrina del autor > corpus > inferencia.** El mantenedor valida
o descarta cada `candidato`; las aceptadas se recompilan en una versión nueva de
`PROMPT.md` con su procedencia en el commit. No hay merge automático de conocimiento:
un prompt donde todo entra no tiene doctrina.

## Cómo absorbe tu despliegue

```bash
git pull
```

Con el repo clonado como skill (`~/.claude/skills/mimir`), el pull actualiza el prompt
y la siguiente sesión ya trabaja con las reglas nuevas. Revisa el CHANGELOG del commit
antes: tú también decides qué versión corre en tu casa.
