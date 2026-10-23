"""Revisa la capa OKF de la biblioteca: proyectos/INDICE.md y la ficha (index.md) de cada proyecto.
Solo lee; no cambia nada. Norma: plantillas/NORMA-OKF.md
Uso: python3 herramientas/validar_okf.py
"""
import re, sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PROYECTOS = RAIZ / "proyectos"
OBLIGATORIOS = ["type", "proyecto", "estado", "fase", "generated", "stale_after"]
ESTADOS = {"#diseño", "#campo", "#analisis", "#cerrado", "#pausado"}


def encabezado(ruta):
    """Campos de primer nivel del YAML inicial (clave: valor), sin dependencias."""
    texto = ruta.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", texto, flags=re.S)
    if not m:
        return None
    campos = {}
    for linea in m.group(1).splitlines():
        par = re.match(r"([A-Za-z_]+):\s*(.*)", linea)
        if par:
            campos[par.group(1)] = par.group(2).strip().strip("\"'")
    return campos


def revisar_ficha(ruta, hoy):
    yaml = encabezado(ruta)
    if yaml is None:
        return ["sin encabezado OKF"], []
    errores = [f"falta `{c}`" for c in OBLIGATORIOS if not yaml.get(c)]
    avisos = []
    if yaml.get("proyecto") and not re.fullmatch(r"GF-\d{4}-\d{3}-[A-Za-z0-9-]+", yaml["proyecto"]):
        errores.append(f"`proyecto` no es un tag GF-AAAA-NNN-Sector: {yaml['proyecto']}")
    if yaml.get("estado") and yaml["estado"] not in ESTADOS:
        errores.append(f"`estado` desconocido: {yaml['estado']}")
    if yaml.get("fase") and not re.fullmatch(r"F\d+", yaml["fase"]):
        errores.append(f"`fase` debe ser F<n>: {yaml['fase']}")
    if yaml.get("stale_after") and yaml["stale_after"] < hoy:
        avisos.append(f"`stale_after` vencido ({yaml['stale_after']})")
    return errores, avisos


def main():
    hoy = date.today().isoformat()
    total_errores = 0
    indice = PROYECTOS / "INDICE.md"
    catalogo = indice.read_text(encoding="utf-8") if indice.exists() else ""
    if not catalogo:
        print("❌ proyectos/INDICE.md no existe")
        total_errores += 1
    elif not (encabezado(indice) or {}).get("type"):
        print("❌ proyectos/INDICE.md sin `type`")
        total_errores += 1
    for carpeta in sorted(p for p in PROYECTOS.iterdir() if p.is_dir()):
        ficha = carpeta / "index.md"
        nombre = carpeta.name
        if not ficha.exists():
            errores, avisos = ["falta index.md (la ficha)"], []
        else:
            errores, avisos = revisar_ficha(ficha, hoy)
        if f"({nombre}/index.md)" not in catalogo:
            avisos.append("sin fila en proyectos/INDICE.md")
        marca = "❌" if errores else ("⚠️" if avisos else "✅")
        print(f"{marca} {nombre}" + "".join(f"\n   - {x}" for x in errores + avisos))
        total_errores += len(errores)
    sys.exit(1 if total_errores else 0)


if __name__ == "__main__":
    main()
