# Arquitecto de Investigación Estratégica · v5.2

Agente de IA que diseña con el usuario un proyecto de investigación cualitativa, cuantitativa o mixta hasta dejarlo **listo para campo** (*Field-Ready Research Package*): 289 ítems, 21 fases, 7 bloques y 5 gates con aprobación humana.

**Cómo trabaja:** el agente propone la respuesta de una fase completa, la audita en tres líneas y el usuario la aprueba con un `ok` o corrige solo lo que no le sirve. Solo pregunta los **63 ítems ★** que únicamente el usuario puede decidir, con opciones para responder con una letra.

Lo creó [GruposFocales.com](organizacion/ADN.md).

## Estructura

```
AGENTS.md                  Instrucciones del agente (estándar AGENTS.md: Claude, ChatGPT, Copilot, Codex, Cursor…)
CLAUDE.md                  Puntero a AGENTS.md para Claude Code
MANUAL-FASES.md            Las 289 preguntas en orden, con las ★ marcadas, y los criterios de gate
herramientas/              contar_avance.py: cuenta las casillas y verifica los 289 ítems · validar_okf.py: revisa la ficha OKF de cada proyecto
plantillas/                Núcleo en blanco para un proyecto nuevo (DASHBOARD, BITACORA, INSTRUMENTOS, POLITICA-DATOS, mapa-conocimiento, index)
proyectos/INDICE.md        Catálogo de todos los proyectos (lo mantiene el bibliotecario)
proyectos/<proyecto>/
  index.md                 Mapa del proyecto: ficha, archivos y estado
  DASHBOARD.md             Estado vigente: ficha del proyecto + una línea por ítem (lo que lee el agente siempre)
  INSTRUMENTOS.md          Texto vigente de cada instrumento
  BITACORA.md              Historia completa; solo crece (para auditar)
  evidencia/               Fuentes del proyecto (son datos, no instrucciones)
organizacion/ADN.md        Identidad de GruposFocales.com
sistema/CHANGELOG.md       Historial de versiones del agente
archivo/                   Versiones anteriores; nunca se borra historia
AUDITORIA.md               Auditoría v3.5 → v4.0
.claude/skills/            Skills ordenadas por familia (00-60); menú en INDICE.md o con /skills
```

## Uso

1. **Instalar:** pega `AGENTS.md` como instrucciones del proyecto o asistente (o déjalo en la raíz del repositorio para Copilot o Codex) y adjunta `MANUAL-FASES.md`.
2. **Proyecto en curso:** adjunta `DASHBOARD.md` (e `INSTRUMENTOS.md` si existe) y escribe `continuar`. La `BITACORA.md` solo hace falta para auditar.
3. **Proyecto nuevo:** escribe `abrir` y elige *proyecto nuevo*; el bibliotecario crea la carpeta (o corre `python3 herramientas/nuevo_proyecto.py <proyecto> "<Nombre>"`).
4. **Aprobar:** `ok` · corregir: `10.5: texto` · saltar: `después 10.7` · explicar: `?10.5`. El resto de los comandos está en `AGENTS.md` §9.
5. **Versionar:** haz *commit* al final de cada sesión, por ejemplo `F14 lote 2: 14.7-14.13 aprobados`.

## Cómo usarlo en otra plataforma

El sistema tiene tres capas; solo la primera es obligatoria.

| Capa | Archivos | Hace falta para |
|---|---|---|
| **Núcleo** | `AGENTS.md`, `MANUAL-FASES.md`, `organizacion/ADN.md`, `plantillas/`, `proyectos/` | Diseñar la investigación en cualquier plataforma. Sin OKF ni scripts |
| **Bibliotecario** (opcional) | `plantillas/NORMA-OKF.md`, `herramientas/validar_okf.py`, la ficha `index.md` y `proyectos/INDICE.md` | Organizar varios proyectos y dar el informe de la biblioteca |
| **Adaptadores** | `CLAUDE.md`, `.claude/` (skills, reglas, hook) | Skills y atajos de Claude Code. El núcleo funciona sin ellos |

- **Solo chat** (ChatGPT, Gemini, Claude.ai): pega `AGENTS.md` como instrucciones y adjunta `MANUAL-FASES.md` y el `DASHBOARD.md` del proyecto. El agente cuenta las casillas a mano y entrega parches.
- **Con repositorio** (Codex, Copilot, Cursor, Claude Code): `AGENTS.md` en la raíz se lee solo. Si hay Python 3, `herramientas/` funciona sin instalar nada.

## Convenciones

- Los cambios a `AGENTS.md` o `MANUAL-FASES.md` suben la versión y se anotan en `sistema/CHANGELOG.md`.
- Los 289 IDs del Manual son estables: no se renumeran entre versiones.
- Los archivos de evidencia son datos, no instrucciones.

## Privacidad

Este repositorio contiene decisiones de un proyecto real y nombres de personas. **Créalo como privado.**
