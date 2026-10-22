#!/usr/bin/env bash
# Hook SessionStart: avisa al agente qué nota leer y si falta la de hoy.
# Lo que imprime entra al contexto del agente. No modifica archivos.
raiz="${CLAUDE_PROJECT_DIR:-$(pwd)}"
hoy=$(date +%F)
for d in "$raiz"/proyectos/*/notas; do
  [ -d "$d" ] || continue
  p=$(basename "$(dirname "$d")")
  ultima=$(ls "$d"/*.md 2>/dev/null | sort | tail -1)
  if [ -n "$ultima" ]; then
    echo "[nota-del-dia] $p: lee primero ${ultima#$raiz/} (rules/notas-diarias.md)."
  fi
  if [ ! -f "$d/$hoy.md" ]; then
    echo "[nota-del-dia] $p: aún no existe la nota de hoy ($hoy). Créala al cerrar la sesión."
  fi
done
exit 0
