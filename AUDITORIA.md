# Auditoría del agente v3.5 → v4.0 — 2026-10-17

Alcance: `AGENTS.md` v3.5, `MANUAL-FASES.md`, `CHANGELOG-AGENTS.md`, `ADN.md` y los archivos del proyecto Observatorio (`DASHBOARD.md` y `PROYECTO.md` del 16-oct, más los dos archivos del 17-oct). La carpeta original no se modificó; todo está en `github-repo/`.

---

## 1. Diagnóstico de v3.5

### El dolor: demasiadas interacciones
| Causa | Evidencia en el proyecto |
|---|---|
| Una pregunta por turno × 289 ítems, más repreguntas | El ítem 12.6 (filtro) necesitó más de 25 entradas de bitácora. |
| Doble aprobación: `siguiente` = base aceptada y luego se vuelve a aprobar en el gate | 13.8 quedó en base aceptada y hubo que aprobarlo de nuevo; 10.4 sigue igual. |
| Ceremonia de cierre por fase, por bloque y por gate | 21 fases + 7 bloques + 5 gates = hasta 33 turnos solo de cierre. |
| El agente preguntaba cosas que podía deducir | 10.2 y 10.4 se "registraron sin repreguntar" porque ya estaban; 12.2-12.9 y 19.x son revisiones que el agente puede hacer solo. |
| El usuario ya pedía delegar | "analiza y decide", "resuelve y avanza", "revísalo", "decide": el sistema no tenía un camino corto para eso. |

### Deriva entre archivos (el estado se contradecía)
- `DASHBOARD.md` (16-oct) decía 167/289, pero tenía 169 `[x]`; la Fase 9 figuraba como "1/3" con sus 3 ítems aprobados; la alerta 13 daba por `[r]` ítems que estaban en `[x]`.
- 10.14 estaba `[x]` en el tablero y `[PENDIENTE]` en la bitácora.
- Los archivos del 17-oct decían 176/289, "6/100" en el Bloque 6 (son 91) y "67/68" en el Bloque 4 (son 67).
- **Causa:** el avance se calculaba de memoria y el mismo estado vivía en dos archivos (casillas en el DASHBOARD y estados en `PROYECTO.md`).

### Riesgos de integridad
- **Horas imposibles:** entradas fechadas "17-oct 16:47-17:20" dentro de un archivo guardado el 17-oct a las 08:48. La secuencia indica que fueron el 16-oct por la tarde (ver `BITACORA.md`, parte II).
- **Pérdida de historia por compresión:** el `PROYECTO` del 17-oct pesaba 8 KB frente a 134 KB. Cuando el archivo crece, el agente tiende a resumirlo y a perder la historia (choca con la regla 12).
- **Un archivo de memoria sin límite:** los 134 KB de `PROYECTO.md` se cargaban en cada sesión, lo que vuelve todo más lento y caro, y aumenta los errores.
- **Instrumentos sin hogar:** el texto aprobado del filtro y del bot estaba repartido en decenas de entradas de bitácora. El texto completo de F0 (versión 2) y las opciones finales de P2 y P3 nunca se copiaron.

### Complejidad innecesaria
- 14 estados epistemológicos + 6 casillas + avance provisional → errores de clasificación (`[~]` que sobrevivieron, `[b]` frente a `[x]`).
- Modo Tutor con un protocolo de 7 pasos: casi no se usó.
- Turno de 5 secciones fijas: respuestas largas para aprobar un solo ítem.

### Lo que v3.5 hacía bien (se conserva)
Cero invención · aprobación humana · nunca borrar historia · cascada `[r]` · explicaciones rivales · instrumentos después de la muestra · la evidencia como dato y no como orden · los 289 ítems y los criterios de gate.

---

## 2. Qué cambia en v4.0

| Antes (v3.5) | Ahora (v4.0) |
|---|---|
| 1 pregunta por turno | 1 **lote** por turno (una fase o hasta 10 ítems) con la respuesta ya propuesta |
| Pregunta los 289 | Pregunta solo los **63 ★** sin base, con opciones A/B/C |
| `siguiente` = base aceptada; luego se aprueba en el gate | `ok` = aprobado; el gate solo revisa riesgos y lo que esté abierto |
| Auditoría opcional en una sección aparte | Auditoría de máximo 3 puntos en cada lote |
| 14 estados + 6 casillas + 2 avances | 5 marcas + 5 casillas + 1 avance contado |
| `PROYECTO.md` con estado + historia (134 KB) | `DASHBOARD.md` (31 KB, estado y ficha) + `BITACORA.md` (historia, no se carga) + `INSTRUMENTOS.md` |
| Registro por ítem | Registro por lote |
| Modo Tutor | `?X` (explica y da opciones) y `uno a uno` |
| 20 comandos | 14 comandos |

### Efecto esperado `[estimación]`
- **Proyecto nuevo:** de más de 320 turnos (289 ítems + repreguntas + cierres) a unos **35-45 turnos** (alrededor de 30 lotes, hasta 21 turnos de preguntas ★ que suelen agruparse con su lote, y 5 gates).
- **Observatorio (lo que falta):** 104 ítems vacíos + 6 por revisar → unos **15-20 turnos**: 1 de revisión, unos 12 lotes (Fases 14-20) y 19 preguntas ★ (14.11, 14.13, 14.14; siete de la 15; cuatro de la 16; tres de la 17; 18.16 y 20.3) agrupadas de a 3.
- **Carga por sesión:** el agente lee unos 85 KB (AGENTS + MANUAL + DASHBOARD + INSTRUMENTOS) en lugar de unos 200 KB.

---

## 3. Curación del proyecto Observatorio

- **Integrado lo del 17-oct** (confirmado por el usuario): 4.13, 8.6, 12.1-12.5, Gate G2, 10.12 (orgánico, sin pauta), 14.1-14.6, preguntas B1-B6 del bot. En cascada: 10.13, 10.15 y 13.16 pasan a `[r]`.
- **Recuento real:** 179 `[x]` · 3 `[p]` · 3 `[r]` · 104 `[ ]` → **62 % (179/289)**.
- **`DASHBOARD.md`:** ficha del proyecto + una línea vigente por ítem, reconstruida desde la bitácora. 58 ítems de las Fases 0-6 quedan como *"Sin detalle en bitácora (Google Drive)"*: no se inventó su contenido.
- **`INSTRUMENTOS.md` (nuevo):** filtro F0-F9, bot B1-B7, módulo de pensionados, pregunta de red de apoyo, podcast (5 audiencias y 6 disparadores) y dramas. Las lagunas están señaladas.
- **`BITACORA.md`:** el antiguo `PROYECTO.md` sin cambios + los registros del 17-oct sin cambios (con una nota sobre las fechas) + la entrada de migración v4.

---

## 4. Lo que necesita al usuario (todo cabe en un `revisar`)

1. **`[p]` 10.4, 10.14 y 11.6, y la pregunta B7:** un `ok` o una corrección.
2. **`[r]` 10.13, 10.15 y 13.16:** ajustar a reclutamiento orgánico y a 65+ como prioridad 2.
3. **Recuperar** el texto completo de F0 (v2) y las opciones de P2 y P3 (en la conversación original o en Kapso).
4. **Evidencia:** edades 57/62, umbrales 18/60, corte de 80 años, política de datos.
5. **Antes de G3:** redactar las preguntas de grupo focal, díada, encuesta, podcast y dramas.

---

## 5. Archivos

| Origen | En el repo v4 |
|---|---|
| `AGENTS.md` v3.5 | `archivo/versiones-sistema/AGENTS.v3.5.md` → reemplazado por `AGENTS.md` v4.0 |
| `MANUAL-FASES.md` v3.5 | `archivo/versiones-sistema/MANUAL-FASES.v3.5.md` → reemplazado por v4.0 (★) |
| `CHANGELOG-AGENTS.md` | `sistema/CHANGELOG.md` (con la entrada v4.0) |
| `DASHBOARD.md` (16-oct) | `archivo/proyectos/observatorio-vejez/DASHBOARD.v3.5-2026-10-16.md` → nuevo `DASHBOARD.md` v4 |
| `PROYECTO.md` (16-oct) | parte I de `BITACORA.md` (copia también en `archivo/`) |
| `*_v3.5_actualizado_17oct.md` | parte II de `BITACORA.md` (originales en `archivo/`) |
| — | `INSTRUMENTOS.md`, `herramientas/contar_avance.py`, plantillas v4 (nuevos) |
| Auditoría de migración v3.5 | `archivo/AUDITORIA-MIGRACION-v3.5.md` |
