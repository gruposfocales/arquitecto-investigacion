"""Cuenta las casillas de un DASHBOARD.md v4 y verifica que haya 289 ítems.
Uso: python3 herramientas/contar_avance.py proyectos/<proyecto>/DASHBOARD.md
"""
import re, sys
from collections import Counter

texto = open(sys.argv[1], encoding="utf-8").read()
items = re.findall(r"^- \[([ xpr-])\] (\d+\.\d+) ", texto, flags=re.M)
c = Counter(st for st, _ in items)
total = len(items)
hechos = c["x"] + c["-"]
print(f"Ítems: {total} {'OK' if total == 289 else '⚠️ deben ser 289'}")
print(f"Avance: {round(100 * hechos / 289)} % ({hechos}/289)")
print("Casillas:", {k if k != ' ' else 'vacío': v for k, v in sorted(c.items())})
for marca in "pr":
    ids = [n for st, n in items if st == marca]
    if ids:
        print(f"[{marca}]:", ", ".join(ids))
