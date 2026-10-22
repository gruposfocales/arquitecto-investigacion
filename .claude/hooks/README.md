# Hooks

Un hook es un script que Claude Code corre solo en un momento fijo (al abrir sesión, antes o después de una herramienta, al terminar). Se activan en `.claude/settings.json`; el script vive aquí.

| Hook | Cuándo | Qué hace |
|---|---|---|
| `nota-del-dia.sh` | Al abrir sesión (`SessionStart`) | Le dice al agente qué nota leer y avisa si falta la de hoy. No modifica archivos. |

Funciona en Claude Code (terminal, web o desktop con el repo abierto). En claude.ai sin Claude Code no corre: ahí rige `rules/notas-diarias.md`.
