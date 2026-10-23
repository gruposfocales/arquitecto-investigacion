"""Crea proyectos/<proyecto>/ desde plantillas/ y lo agrega a proyectos/INDICE.md.
Uso: python3 herramientas/nuevo_proyecto.py <proyecto> "<Nombre del proyecto>"
"""
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
# plantilla → destino dentro del proyecto
PLANTILLAS = {
    "DASHBOARD.md": "DASHBOARD.md",
    "BITACORA.md": "BITACORA.md",
    "INSTRUMENTOS.md": "INSTRUMENTOS.md",
    "POLITICA-DATOS.md": "POLITICA-DATOS.md",
    "mapa-conocimiento.md": "evidencia/mapa-conocimiento.md",
    "index.md": "index.md",
}


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    slug, nombre = sys.argv[1], sys.argv[2]
    destino = RAIZ / "proyectos" / slug
    if destino.exists():
        sys.exit(f"Ya existe {destino.relative_to(RAIZ)}; no se toca.")
    hoy = date.today().isoformat()
    for carpeta in ("evidencia", "notas"):
        (destino / carpeta).mkdir(parents=True)
        (destino / carpeta / ".gitkeep").touch()
    for archivo, ruta in PLANTILLAS.items():
        texto = (RAIZ / "plantillas" / archivo).read_text(encoding="utf-8")
        texto = texto.replace("[Nombre del proyecto]", nombre).replace("[proyecto]", slug)
        if archivo == "index.md":
            texto = texto.replace("| **Abierto** | [fecha PENDIENTE] |", f"| **Abierto** | {hoy} |")
        if archivo == "BITACORA.md":
            texto += f"\n## {hoy} · Apertura del proyecto\n- Carpeta creada por el bibliotecario.\n"
        (destino / ruta).write_text(texto, encoding="utf-8")
    indice = RAIZ / "proyectos" / "INDICE.md"
    with indice.open("a", encoding="utf-8") as f:
        f.write(f"| [{nombre}]({slug}/index.md) | activo | 0 % (0/289) | 0 · Configuración | {hoy} |\n")
    print(f"Creado proyectos/{slug}/ y agregado a proyectos/INDICE.md")


if __name__ == "__main__":
    main()
