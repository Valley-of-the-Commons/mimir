# Instalar Mímir en tu ecosistema

El agente entero es **un archivo**: [PROMPT.md](PROMPT.md). Todo lo demás es
documentación. Cualquier ecosistema que acepte un system prompt puede correr Mímir.

## Requisitos

- Un LLM capaz de sostener un rol largo y con matices (recomendado: Claude Sonnet u
  Opus, o equivalente). Modelos pequeños tienden a romper la regla central
  («devolver sin resolver») bajo presión.
- Idioma de trabajo: español (el prompt está en español; el agente puede conversar en
  otros idiomas, pero su doctrina está formulada en español).

## Opción A · Claude Code (como skill)

```bash
git clone https://github.com/Valley-of-the-Commons/mimir ~/.claude/skills/mimir
```

El repo incluye `SKILL.md` en la raíz, así que la carpeta clonada ya es una skill
válida. Tras reiniciar la sesión, invoca con `/mimir` — la skill carga `PROMPT.md` y
Claude adopta el rol durante la sesión.

## Opción B · Claude Projects / claude.ai

1. Crea un Proyecto nuevo.
2. Pega el contenido completo de `PROMPT.md` (desde «## SYSTEM PROMPT» hasta el final)
   en las instrucciones del proyecto.
3. Opcional: sube `HABILIDADES.md` como conocimiento del proyecto.

## Opción C · API (cualquier proveedor)

Usa el contenido de `PROMPT.md` como `system`. Ejemplo con la API de Anthropic:

```python
import anthropic

system_prompt = open("PROMPT.md", encoding="utf-8").read()

client = anthropic.Anthropic()
resp = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=4096,
    system=system_prompt,
    messages=[{"role": "user", "content": "Tengo que prediseñar una asamblea de 25 personas..."}],
)
print(resp.content[0].text)
```

## Opción D · Modelos locales (Ollama, LM Studio, etc.)

Crea un modelfile/preset con `PROMPT.md` como system prompt. Advertencia honesta: por
debajo de ~70B el rol se degrada — el modelo empieza a aconsejar y resolver, que es
exactamente lo que Mímir tiene prohibido. Verifica con la prueba mínima de abajo.

## Prueba mínima de instalación

Pídele algo que un asistente normal resolvería directamente, por ejemplo:

> «El grupo está bloqueado con el tema del presupuesto, ¿qué dinámica hago mañana?»

Una instalación sana de Mímir **no elige la dinámica**: hace preguntas de prediseño
(propósito, quién decide, fase del proceso), ofrece un abanico con condiciones de
descarte y **devuelve la elección**. Si te responde «haz un World Café», la
instalación (o el modelo) no está sosteniendo el rol.

## Personalización por despliegue

- **Doctrina propia**: el prompt manda que la doctrina del facilitador gana sobre el
  corpus. Añade la tuya en una sección al final del prompt o como documento adjunto —
  Mímir está obligado a confrontar lo que la contradiga, no a obedecer en silencio.
- **Huecos declarados**: mantén tu propia lista (sección final del prompt). La regla
  es fija: los huecos se declaran, nunca se rellenan con genérico.
- **Registro de aprendizaje**: decide dónde persiste (archivo, vault, base de datos).
  El formato de registro viene en el prompt.
