---
type: Norma de biblioteca
title: OKF 0.2 para GruposFocales
description: Norma mínima con la que el bibliotecario organiza los proyectos de investigación con Open Knowledge Format 0.2.
tags: [biblioteca, okf, norma]
proyecto: global
doc: NORMA-OKF
version: "0.3"
alcance: global
generated: { by: claude-bibliotecario/2.3, at: 2026-10-23T09:30:00-05:00 }
status: draft
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Especificación OKF v0.2
  - id: doc-propuesta
    resource: https://claude.ai/artifact/MJuDFmdmj9fmjUJ3LyMESG
    title: OKF 0.2 para GruposFocales (Claude Doc, propuesta original v0.2)
---

# OKF 0.2 para GruposFocales

Desde la v0.3 manda este archivo. El [Claude Doc](https://claude.ai/artifact/MJuDFmdmj9fmjUJ3LyMESG) queda como propuesta original.

## Qué es OKF 0.2

OKF 0.2 es un formato de archivos, no un programa: no se instala. Lo publicó Google Cloud (v0.1 el 12 de junio de 2026, v0.2 el 24 de julio de 2026)[^okf-spec]. Un archivo cumple OKF si empieza con un encabezado YAML que tiene `type`; lo demás es opcional. La v0.2 añade señales de confianza: `generated`, `verified`, `sources`, `status` (draft, stable, deprecated) y `stale_after`.

## Alcance: solo la capa de organización

OKF sirve para que el bibliotecario organice **los proyectos**, no para reescribir su contenido. Cada proyecto conserva su propia lógica interna (DASHBOARD, BITACORA, INSTRUMENTOS, evidencia, notas): esos archivos **no necesitan** encabezado OKF y no se migran.

Llevan encabezado OKF solo estos archivos:

| Archivo | `type` | Para qué |
| --- | --- | --- |
| `proyectos/INDICE.md` | Catálogo de proyectos | Una fila por proyecto |
| `proyectos/<carpeta>/index.md` | Índice de proyecto | La **ficha** del proyecto: lo único que el bibliotecario necesita leer para el informe |
| `/log.md` (cuando exista) | Log | Historial global, lo más nuevo arriba |
| `plantillas/NORMA-OKF.md` | Norma de biblioteca | Esta norma |

## La ficha del proyecto

Es el encabezado de `proyectos/<carpeta>/index.md`. Campos obligatorios:

| Campo | Ejemplo | Regla |
| --- | --- | --- |
| `type` | `Índice de proyecto` | Fijo |
| `proyecto` | `GF-2026-001-Salud` | Tag `GF-AAAA-NNN-Sector`: año de apertura, consecutivo de 3 dígitos, sector sin tildes ni espacios |
| `estado` | `"#diseño"` | `#diseño` · `#campo` · `#analisis` · `#cerrado` · `#pausado` |
| `fase` | `F19` | Fase activa, tal como la da el `DASHBOARD.md` del proyecto |
| `generated` | `{ by: claude-bibliotecario/2.3, at: 2026-10-23T09:30:00-05:00 }` | Quién actualizó la ficha y cuándo |
| `stale_after` | `2026-11-06` | Fecha en que la ficha debe revisarse (14 días por defecto) |

Opcionales: `title`, `description`, `tags`, `carpeta` (si no coincide con el tag), `ultimo_gate` (`"G2 · 2026-10-16"`), `status`, `sources`.

```yaml
---
type: Índice de proyecto
title: Guía de salud · mapa
proyecto: GF-2026-002-Salud
estado: "#diseño"
fase: F0
ultimo_gate: "—"
generated: { by: claude-bibliotecario/2.3, at: 2026-10-23T09:30:00-05:00 }
stale_after: 2026-11-06
---
```

Las fechas de `generated.at` llevan la hora de Bogotá con su zona: `2026-10-23T09:30:00-05:00`. En el texto, `AAAA-MM-DD`.

## Carpetas

- Proyectos nuevos: carpeta con el tag (`proyectos/GF-2026-002-Salud/`).
- Proyectos existentes: conservan su carpeta y llevan `carpeta:` en la ficha. No se renombran.
- Los maestros (`AGENTS.md`, `MANUAL-FASES.md`, `organizacion/ADN.md`) siguen en la raíz.

## Rutina del bibliotecario

1. Correr `python3 herramientas/validar_okf.py`: revisa el catálogo y las fichas, no cambia nada.
2. Leer la ficha de cada proyecto y armar el informe: tag, estado, fase, último gate y alertas.
3. Alertas: ficha sin campo obligatorio, `stale_after` vencido, carpeta de `proyectos/` sin fila en `INDICE.md`.
4. Al cambiar de estado o de fase: actualizar la ficha y la fila del catálogo.

## Decisiones (2026-10-23)

- La biblioteca vive en el repositorio GitHub `gruposfocales/arquitecto-investigacion`.
- OKF solo en la capa de organización; los documentos internos de cada proyecto no se migran (el Observatorio sigue con su lógica).
- Zona horaria: America/Bogota (-05:00).
- `BITACORA.md` se queda en cada proyecto como registro de aprobaciones. `/log.md` es solo el historial global.

[^okf-spec]: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
