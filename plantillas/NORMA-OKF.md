---
type: Norma de biblioteca
title: OKF 0.2 para GruposFocales
description: Norma que sigue el bibliotecario orquestador para ordenar los proyectos de investigación con Open Knowledge Format 0.2.
tags: [biblioteca, okf, norma]
proyecto: global
doc: NORMA-OKF
version: "0.1"
alcance: global
generated: { by: claude-bibliotecario/0.1, at: 2026-10-23T13:50:00Z }
status: draft
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Especificación OKF v0.2
  - id: doc-propuesta
    resource: https://claude.ai/artifact/MJuDFmdmj9fmjUJ3LyMESG
    title: OKF 0.2 para GruposFocales (Claude Doc, versión editable)
---

# OKF 0.2 para GruposFocales

Versión editable: [Claude Doc](https://claude.ai/artifact/MJuDFmdmj9fmjUJ3LyMESG). Si ambos difieren, manda el Claude Doc.

## Qué es OKF 0.2

OKF 0.2 es un formato de archivos, no un programa: no se instala. Lo publicó Google Cloud (v0.1 el 12 de junio de 2026, v0.2 el 24 de julio de 2026)[^okf-spec]. Adoptarlo significa escribir nuestros .md siguiendo sus reglas:

- Un **bundle** es una carpeta de archivos markdown. Cada archivo es un "concepto" y su ruta es su identidad.
- Todo .md lleva encabezado YAML con un campo obligatorio: `type`. Se recomiendan `title`, `description`, `resource` y `tags`, y se permiten campos propios.
- `index.md` (índice de cada carpeta) y `log.md` (historial, fechas AAAA-MM-DD, lo más nuevo arriba) son nombres reservados.
- Los vínculos son links markdown normales, preferiblemente con ruta desde la raíz: `/proyectos/GF-2026-001-Salud/ADN.md`.
- La v0.2 añade señales de confianza: `generated`, `verified`, `sources`, `status` (draft, stable, deprecated) y `stale_after`.

## Estructura de carpetas

```
biblioteca/
├── index.md                 ← okf_version: "0.2" + lista de proyectos (lo escribe el bibliotecario)
├── log.md                   ← historial global
├── global/
│   ├── index.md
│   ├── ADN.md               ← maestro, alcance: global
│   ├── POLITICA-DATOS.md    ← maestro v0.3
│   └── MANUAL-FASES.md      ← plantilla maestra (289 preguntas y gates)
└── proyectos/
    ├── index.md
    └── GF-2026-001-Salud/
        ├── index.md
        ├── AGENTS.md
        ├── MANUAL-FASES.md
        ├── DASHBOARD.md
        ├── INSTRUMENTOS.md
        ├── BITACORA.md
        ├── POLITICA-DATOS.md
        ├── ADN.md
        ├── DEEPRESEARCH.md
        └── SKILLS.md
```

Los archivos con `alcance: global` en cada proyecto son copias de un maestro en `/global/` y lo citan en `sources`. Nombres de carpeta sin tildes ni espacios.

## Encabezado YAML

| Campo | Origen | Uso |
| --- | --- | --- |
| `type` | OKF, obligatorio | Clase del documento |
| `title` | OKF | Nombre legible |
| `description` | OKF | Una frase; se copia al `index.md` |
| `tags` | OKF | `[GF-2026-001, salud, F2]` |
| `proyecto` | Propio | `GF-2026-001-Salud` o `global` |
| `doc` | Propio | Nombre canónico, ej. `INSTRUMENTOS` |
| `version` | Propio | Versión del documento |
| `alcance` | Propio | `global` o `proyecto` |
| `generated` | OKF 0.2 | Quién escribió y cuándo; reemplaza `actualizado` |
| `verified` | OKF 0.2 | Aprobaciones; un `human:` = gate aprobado |
| `sources` | OKF 0.2 | Maestro global, evidencia, documentos citados |
| `status` | OKF 0.2 | `draft`, `stable` o `deprecated` |
| `stale_after` | OKF 0.2 | Fecha en que debe revisarse |

Ejemplo (`INSTRUMENTOS.md`):

```yaml
---
type: Instrumento
title: Guía de grupo focal — Salud
description: Guía de moderación y filtro de reclutamiento que sale a campo.
tags: [GF-2026-001, salud, F3]
proyecto: GF-2026-001-Salud
doc: INSTRUMENTOS
version: "1.2"
alcance: proyecto
generated: { by: arquitecto-investigacion/1.0, at: 2026-10-20T15:00:00-05:00 }
verified:
  - { by: "human:gruposfocales", at: 2026-10-22T10:00:00-05:00 }
status: stable
stale_after: 2027-01-31
sources:
  - { id: evidencia, resource: /proyectos/GF-2026-001-Salud/DEEPRESEARCH.md }
  - { id: politica, resource: /proyectos/GF-2026-001-Salud/POLITICA-DATOS.md }
---
```

Las fechas llevan zona horaria explícita (pendiente confirmar cuál).

## Los 9 archivos

| Archivo | `type` | `alcance` | Regla de confianza |
| --- | --- | --- | --- |
| AGENTS.md | Reglas de agente | proyecto | `verified` humano antes de usar el soul del proyecto |
| MANUAL-FASES.md | Manual de fases | global (copia) | `sources` → `/global/MANUAL-FASES.md` |
| DASHBOARD.md | Tablero | proyecto | Campos `estado` (#diseño, #campo, #analisis, #cerrado) y `fase`; `stale_after` corto (14 días) |
| INSTRUMENTOS.md | Instrumento | proyecto | `status: draft` hasta aprobar el gate |
| BITACORA.md | Bitácora | proyecto | Cada aprobación se registra aquí y se refleja como `verified` en el documento aprobado |
| POLITICA-DATOS.md | Política de datos | global (copia v0.3) | Sin `verified` humano vigente, no se sale a campo |
| ADN.md | Identidad de marca | global (copia) | `sources` → `/global/ADN.md` |
| DEEPRESEARCH.md | Base de evidencia | proyecto | Cada estudio es una entrada de `sources`, citado con notas al pie |
| SKILLS.md | Habilidades | proyecto | `deprecated` cuando una habilidad se retira |

## Rutina del bibliotecario

1. Leer `/index.md` y `/proyectos/index.md` para listar los proyectos abiertos.
2. Por cada proyecto, leer el encabezado de `DASHBOARD.md`: `estado`, `fase`, `stale_after`.
3. Revisar los 9 archivos y señalar alertas:
    - Falta un archivo del núcleo, o le falta `type`.
    - Un documento pasó su `stale_after`.
    - Una copia global tiene `version` menor que su maestro.
    - El proyecto está en #campo y POLITICA-DATOS.md o INSTRUMENTOS.md no tiene `verified` humano.
4. Saludar y presentar el informe: una línea por proyecto con estado, fase y alertas. Ofrecer abrir uno o crear uno nuevo.
5. Al crear un proyecto: copiar la plantilla, `status: draft` en todo, registrar en `/log.md`, regenerar los `index.md`.
6. Al aprobar un gate: anotar en BITACORA.md, añadir `verified` en el documento aprobado y pasarlo a `status: stable`.

## Pendiente

- Dónde vivirá la biblioteca (repositorio GitHub o carpeta local).
- Confirmar maestros en `/global/`.
- BITACORA.md se queda (recomendado) o pasa a `log.md`.
- Zona horaria.
- Validador de encabezados.

[^okf-spec]: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
