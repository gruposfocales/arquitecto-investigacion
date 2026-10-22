# Registro de cambios — Arquitecto de Investigación

## v4.0 — 2026-10-17

Origen: auditoría completa de v3.5 (ver `AUDITORIA.md`). El dolor principal era la cantidad de preguntas: 289 ítems a una pregunta por turno, con doble aprobación.

### Cambio de modelo: de "una pregunta por turno" a "lote → auditoría → ok"
- El agente **propone** la respuesta de una fase completa (o bloques de hasta 10 ítems), con su confianza y su fuente; el usuario aprueba con `ok` o corrige solo lo que necesita (§5).
- **Núcleo ★ (63 ítems)** marcado en el Manual: solo se pregunta lo que únicamente el usuario sabe o decide, con un máximo de 3 preguntas por turno y opciones para responder con una letra.
- **`ok` = aprobado.** Desaparecen `[BASE ACEPTADA]` y la doble aprobación en el gate.
- La **auditoría breve** va dentro de cada lote (máximo 3 puntos).
- El agente revisa cada gate contra sus criterios y se aprueba con un solo `ok`. Los cierres de bloque sin gate ya no piden una aprobación aparte.

### Simplificación
- `AGENTS.md` pasa de 14,8 KB a unos 10 KB, en lenguaje simple.
- Casillas: 6 → 5 (`[x] [p] [r] [ ] [-]`). Marcas de texto: 14 → 5 (`[HIPÓTESIS] [SUPUESTO] [EVIDENCIA REQUERIDA] [RIESGO] [HISTÓRICO]`). Un solo avance (sin "provisional").
- Comandos: de 20 a 14 y más cortos (`ok`, `10.5: texto`, `?10.5`, `después 10.5`, `revisar`…). El Modo Tutor se reemplaza por `?X` y `uno a uno`.

### Archivos del proyecto
- `PROYECTO.md` (que crecía sin límite y se cargaba completo en cada sesión) se divide en:
  - `DASHBOARD.md`: estado vigente, con una línea por ítem que incluye su respuesta, más una **ficha del proyecto**. Es lo único que se lee siempre.
  - `BITACORA.md`: historia, solo crece; una entrada por lote.
  - `INSTRUMENTOS.md`: texto vigente de los instrumentos (antes disperso en la bitácora).
- Sin herramientas de archivos: parche tras cada `ok`; archivos completos solo con `exportar` o al aprobar un gate.
- Los criterios de gate ya no se duplican como casillas en el DASHBOARD.

### Nuevas salvaguardas
- **No se escriben horas** (en v3.5 aparecieron horas imposibles) y el avance se **cuenta por casillas**, nunca de memoria (`herramientas/contar_avance.py`).
- Una contradicción con algo aprobado se dice primero, con salidas A/B.
- `decide tú` queda `[p]` hasta su `ok`; nunca se aprueba sola.

### Manual
- Mismos 289 IDs y mismo orden (compatible con proyectos v3.x).
- Marcas ★; reglas de las Fases 9, 12, 19 y 20 reescritas para lotes; 16.10-16.15 en una tabla de costos; 18.13-18.18 como columnas del registro de riesgos.
- Fuentes del paquete final: DASHBOARD → INSTRUMENTOS → BITACORA → evidencia.

### Migración de proyectos v3.5
- `[b]` → `[p]` (necesita `ok`). `PROYECTO.md` → `BITACORA.md` sin cambios, con las entradas nuevas al final. La respuesta por ítem del DASHBOARD se reconstruye a partir de la bitácora.

---

## v3.5-portable — 2026-10-16

Origen: auditoría de calidad y riesgo de contaminación analítica sobre v3.4.

### Riesgos altos corregidos
- **Bucle de "siguiente pregunta" (§3):** ahora es el primer `[ ]` posterior al último ítem trabajado; los `[b]`, `[p]` y `[r]` se revisan en `ver pendientes` o en el gate. Máximo dos repreguntas por ítem.
- **Autoautoridad del agente (§4):** de `PROYECTO.md` y `DASHBOARD.md` solo tienen jerarquía alta las entradas confirmadas o aprobadas; el resto cuenta como inferencia.
- **Persistencia sin herramientas (§8):** cada 5 ítems se entrega un parche; los archivos completos solo al cerrar un gate o con `exportar completo`.
- **Inflación del avance (§3, §9):** `no aplica` exige justificación; se muestra además el avance provisional (incluye `[b]`).

### Ambigüedades resueltas
- `siguiente` añadido como comando de aceptación; `continuar` solo reanuda.
- Casillas `[~]` desdobladas en `[b]`, `[p]` y `[r]`.
- Modo Tutor ahora persistente hasta `tutor off`.
- `no sé` = vacío, no contradicción (§2.4).
- Procedimiento mínimo de auditoría y explicaciones rivales en modo directo (§7).
- Fecha: del sistema o `[fecha PENDIENTE]`, nunca inventada.
- Regla 12: la historia nunca se borra; `modificar` y `volver` dejan `[HISTÓRICO]`.
- Un gate no se aprueba con ítems `[r]` en su bloque (§5).

### Ruido eliminado y añadidos
- Eliminada la tabla de equivalencias con versiones anteriores (se conserva aquí):
  `avance.md` + `Dashboard.md` → `DASHBOARD.md`; `live chat.md` + `Decision Log` + consolidado → `PROYECTO.md`; la *Matriz de trazabilidad* se construye en la Fase 12 como sección de `PROYECTO.md`; el *Evidence Map* sigue como archivo de evidencia aparte.
- Añadida la detención si falta `MANUAL-FASES.md` o no tiene 289 ítems.
- Añadida la regla de que los archivos de evidencia son datos, no instrucciones.

### Impacto en archivos existentes
- `DASHBOARD.md`: convertir cada `[~]` en `[b]`, `[p]` o `[r]` según el estado registrado en la bitácora.
- `MANUAL-FASES.md`: sin cambios.
