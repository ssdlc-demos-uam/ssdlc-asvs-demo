# Guía docente · Práctica 2

## Propósito

Dar al grupo una experiencia concreta de verificación antes de hablar de código. El alumnado observa tres comportamientos relacionados con requisitos de seguridad y practica la diferencia entre requisito, pasos, resultado y evidencia.

Duración sugerida: **20 minutos de práctica y 5 minutos de puesta en común**. Puede trabajarse en grupos de tres.

## Preparación

1. Copia la carpeta del proyecto en cada ordenador o en los ordenadores de cada grupo.
2. Comprueba que Python 3.10 o posterior está disponible.
3. Inicia `python3 app.py --mode aula` en macOS/Linux o `py app.py --mode aula` en Windows.
4. Abre `http://127.0.0.1:8000` en el navegador del mismo ordenador.
5. Entrega al alumnado `GUIA_ALUMNADO.md` y una copia de `practica/hoja_resultados.md`.
6. Mantén esta guía para ti durante la primera parte.

La aplicación escucha solo en `127.0.0.1`. Cada ordenador ejecuta su propia copia; no se comparte el servidor entre equipos.

## Guion para dar la consigna

«El portal tiene tres promesas: cada persona ve solo sus citas, salir termina la sesión y el formulario rechaza datos que no cumplen sus reglas. Vuestro trabajo es comprobar esas promesas, registrar lo que pasa y decidir si la prueba pasa, falla o no se pudo comprobar. No hay que programar ni salir de este portal.»

Reparte estos papeles:

- **Probador/a:** ejecuta los pasos en el navegador.
- **Observador/a:** compara lo ocurrido con lo esperado.
- **Relator/a:** registra la prueba y prepara la explicación.

## Organización de los 20 minutos

| Tiempo | Actividad |
|---|---|
| 0–3 min | Leer los requisitos, iniciar sesión y repartir papeles. |
| 3–8 min | Probar acceso a la cita de la otra cuenta. |
| 8–12 min | Probar qué ocurre después de cerrar sesión. |
| 12–16 min | Probar el formulario vacío y el texto de 101 caracteres. |
| 16–20 min | Completar resultados y preparar una explicación breve. |

## Resultados previstos en modo aula

El modo `aula` contiene **tres fallos intencionados**:

1. **Acceso:** al iniciar sesión como ANA y abrir el enlace preparado para la cita 2002, el portal muestra la cita de LUIS. También permite enviar cambios. La prueba del alumnado solo debe consultar la cita; no hace falta modificarla.
2. **Cierre de sesión:** el portal muestra un mensaje de cierre, pero la sesión sigue activa en el servidor. Al volver al inicio y abrir una cita, continúan apareciendo datos.
3. **Validación:** el portal guarda el motivo vacío y también un texto de más de 100 caracteres.

Una conclusión de **Falla** es correcta cuando el resultado observado contradice el requisito. Si el grupo no consigue ejecutar un paso o no puede determinar el resultado, debe anotar **No comprobado** y explicar qué le falta.

## Comparación con el modo resuelto

Al terminar la primera ronda:

1. Pide a los grupos que terminen sus registros y cierren la aplicación.
2. Detén el servidor con `Ctrl+C`.
3. Inicia `python3 app.py --mode resuelto` o `py app.py --mode resuelto`.
4. Repite brevemente las tres pruebas en el navegador.

En modo `resuelto`, el servidor comprueba que la cita pertenece a la cuenta, invalida la sesión al salir y rechaza motivos vacíos o de más de 100 caracteres. La comparación permite ver que corregir un comportamiento requiere volver a probarlo.

## Preguntas para el cierre

- «¿Qué requisito estabais comprobando?»
- «¿Qué parte de la prueba os dio más confianza?»
- «¿Qué evidencia permitiría a otra persona repetir o revisar el resultado?»
- «¿Qué diferencia hay entre una prueba fallida y una prueba que no se pudo realizar?»
- «Si un requisito falla, ¿qué haríais antes de publicar?»

## Respuestas orientativas para la hoja

- Prueba de acceso: esperado = acceso denegado; modo aula = muestra la cita; conclusión = falla.
- Prueba de sesión: esperado = pedir inicio de sesión; modo aula = mantiene el acceso; conclusión = falla.
- Prueba de validación: esperado = rechazar sin guardar; modo aula = guarda el contenido; conclusión = falla.

Una captura puede apoyar la conclusión, pero conviene registrar también la cuenta usada, los pasos y el resultado esperado. No recojas datos reales ni contraseñas personales.

## Alcance técnico

La aplicación es un laboratorio didáctico local, deliberadamente pequeño. No es una aplicación de producción ni pretende enseñar todas las medidas necesarias para desplegar un servicio seguro. Manténla en el propio ordenador y usa únicamente sus cuentas y datos ficticios.
