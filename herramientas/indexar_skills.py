"""Lee la ficha de cada .claude/skills/*/SKILL.md y regenera .claude/skills/INDICE.md.
Uso: python3 herramientas/indexar_skills.py
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent / ".claude" / "skills"
CAMPOS = ["name", "description", "familia", "version", "entra", "sale", "siguiente", "estado"]

MENU = [
    ("Diseñar o continuar el estudio", "10"),
    ("Montar el filtro, el bot o la encuesta en WhatsApp", "20"),
    ("Diseñar el estímulo y codificar comentarios de redes", "30"),
    ("Bajar piezas, transcripciones y comentarios con Apify", "31"),
    ("Convertir transcripciones en personajes", "40"),
    ("Escribir una serie o un guion de microdrama", "50"),
    ("Producir con IA: personajes, storyboard y prompts de Seedance", "60"),
    ("No sé qué usar", "00"),
]


def ficha(path):
    texto = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", texto, flags=re.S)
    if not m:
        return None
    datos = {}
    for linea in m.group(1).splitlines():
        if ":" in linea:
            k, v = linea.split(":", 1)
            datos[k.strip()] = v.strip().strip('"')
    datos["carpeta"] = path.parent.name
    return datos


skills = sorted(
    (f for f in (ficha(p) for p in RAIZ.glob("*/SKILL.md")) if f),
    key=lambda d: d["carpeta"],
)
por_num = {s["carpeta"][:2]: s for s in skills}

faltan = [s["carpeta"] for s in skills if any(c not in s for c in CAMPOS)]

out = ["# Índice de skills", "",
       "> Generado por `herramientas/indexar_skills.py`. No lo edite a mano: cambie la ficha de cada `SKILL.md` y vuelva a correr el script.",
       "", "## ¿Qué quiere hacer?", "", "| Quiero… | Use |", "|---|---|"]
for tarea, num in MENU:
    s = por_num.get(num)
    if s:
        out.append(f"| {tarea} | `/{s['name']}` |")

out += ["", "## Cadena de trabajo", "", "```",
        " → ".join(f"{s['carpeta'][:2]} {s['name']}" for s in skills if s["carpeta"][:2] != "00"),
        "                    ↑ 30 alimenta de vuelta a 10 (hallazgos triangulados)", "```",
        "", "## Catálogo", "",
        "| # | Comando | Familia | Versión | Estado | Entra | Sale | Siguiente |",
        "|---|---|---|---|---|---|---|---|"]
for s in skills:
    out.append("| {} | `/{}` | {} | {} | {} | {} | {} | {} |".format(
        s["carpeta"][:2], s.get("name", "?"), s.get("familia", "?"), s.get("version", "?"),
        s.get("estado", "?"), s.get("entra", "?"), s.get("sale", "?"), s.get("siguiente", "?")))

out += ["", "## Para agregar una skill", "",
        "1. Cree `.claude/skills/NN-nombre/SKILL.md` (NN = familia: 10 diseño · 20 campo · 30-39 escucha · 40 personajes · 50 contenido · 60 producción).",
        "2. Llene la ficha: " + ", ".join(f"`{c}`" for c in CAMPOS) + ".",
        "3. Corra `python3 herramientas/indexar_skills.py`."]
if faltan:
    out += ["", "⚠️ Fichas incompletas: " + ", ".join(faltan)]

(RAIZ / "INDICE.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"INDICE.md: {len(skills)} skills" + (f" · ⚠️ incompletas: {faltan}" if faltan else " · fichas completas"))
