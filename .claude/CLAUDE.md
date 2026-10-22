# .claude/CLAUDE.md

Las instrucciones viven en [`../AGENTS.md`](../AGENTS.md) y [`../MANUAL-FASES.md`](../MANUAL-FASES.md). Este archivo solo orienta dentro de `.claude/`.

| Carpeta | Qué guarda |
|---|---|
| `skills/` | Skills del sistema (menú en `skills/INDICE.md`) |
| `rules/` | Reglas cortas de trabajo; se leen al arrancar |
| `agents/` | Subagentes (un `.md` por agente) |
| `mcps/` | Conectores MCP que usa el proyecto |
| `hooks/` | Scripts automáticos (antes/después de una acción) |

Al arrancar: lee `rules/` y la nota más reciente de `proyectos/<proyecto>/notas/`.
