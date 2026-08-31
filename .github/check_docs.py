"""Guardián del ciclo federado: cada recompilación del prompt debe conservar
las secciones que el SKILL y el protocolo de cierre dan por existentes, y
ningún enlace interno de la documentación puede quedar colgando.

No valida doctrina — solo que la estructura prometida sigue ahí.
Uso: python .github/check_docs.py  (sale 1 si algo falla)
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).parent.parent
fallos = []

# 1. Secciones del PROMPT que otros archivos dan por existentes
prompt = (RAIZ / "PROMPT.md").read_text(encoding="utf-8")
REQUERIDAS = [
    "## SYSTEM PROMPT",          # SKILL.md paso 2
    "Cómo te presentas",         # SKILL.md regla de arranque
    "LA PUERTA DE ENTREGA",      # README: autochequeos
    "EL SALVADOR",               # README: chequeo del sesgo
    "P6",                        # cierre federado / template
    "REGLA DE PARADA",
]
for seccion in REQUERIDAS:
    if seccion not in prompt:
        fallos.append(f"PROMPT.md: falta la sección requerida «{seccion}»")

# 2. Frontmatter con version: (el template de issue la pide)
if not re.search(r"(?m)^version:\s*\S+", prompt):
    fallos.append("PROMPT.md: falta «version:» en el frontmatter (el registro federado la pide)")

# 3. Enlaces internos .md resolubles en toda la documentación
for archivo in RAIZ.glob("*.md"):
    texto = archivo.read_text(encoding="utf-8")
    for destino in re.findall(r"\]\(([^)#http][^)]*)\)", texto):
        if not (RAIZ / destino).exists():
            fallos.append(f"{archivo.name}: enlace roto → {destino}")

# 4. El template declara un label que debe existir en el repo (comprobación
#    estática: solo que declare alguno; la existencia real la garantiza el repo)
template = (RAIZ / ".github/ISSUE_TEMPLATE/registro-de-aprendizaje.md").read_text(encoding="utf-8")
if "labels:" not in template:
    fallos.append("template registro-de-aprendizaje: sin labels declarados")

if fallos:
    print("DOC-LINT: FALLOS")
    for f in fallos:
        print(" -", f)
    sys.exit(1)
print(f"DOC-LINT OK: {len(REQUERIDAS)} secciones, frontmatter y enlaces verificados")
