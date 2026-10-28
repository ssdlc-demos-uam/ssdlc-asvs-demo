# Guía del alumnado · Práctica 2

## Misión

Comprobar tres promesas del portal municipal y dejar una explicación que otro grupo pueda repetir. No necesitas programar: sigue las instrucciones desde el navegador.

Trabaja solo en el laboratorio que ha preparado el docente y con las cuentas ficticias de esta guía.

## Antes de empezar

1. Abre <http://127.0.0.1:8000> en el ordenador donde está iniciado el laboratorio.
2. Inicia sesión como `ana`, con la contraseña `ana123`.
3. Forma un grupo de tres y repartid estos papeles:
   - **Probador/a:** sigue los pasos en el navegador.
   - **Observador/a:** compara lo ocurrido con lo esperado.
   - **Relator/a:** anota los pasos y el resultado.

## Prueba 1 · Ana no debe acceder a la cita de Luis

**Requisito que comprobamos:** cada usuario solo puede consultar y cambiar sus propias citas.

1. Confirma que has iniciado sesión como ANA.
2. Desde la página de inicio, abre el enlace **Cita de LUIS (2002)** que ha preparado el docente.
3. Comprueba si aparecen el propietario, el día, la hora o el motivo de la cita.
4. No cambies los datos. Anota el resultado y vuelve al inicio.

**Lo esperado:** el portal deniega el acceso y no muestra los datos de Luis.

## Prueba 2 · Cerrar sesión debe terminar el acceso

**Requisito que comprobamos:** después de cerrar sesión, una página privada no debe seguir disponible.

1. Abre la cita propia de ANA.
2. Pulsa **Cerrar sesión**.
3. Sigue la indicación que muestra el portal y vuelve a abrir un enlace de cita.
4. Anota si el portal pide iniciar sesión o muestra información privada.

**Lo esperado:** el portal pide iniciar sesión y no muestra la cita.

Si el navegador muestra una página antigua con el botón «Atrás», recárgala antes de decidir. Una página guardada en la pantalla no basta para saber si el servidor mantiene el acceso.

## Prueba 3 · El formulario debe rechazar entradas no válidas

El formulario indica que el motivo es obligatorio y admite hasta 100 caracteres.

1. Inicia sesión de nuevo como ANA si hace falta.
2. Abre su cita y borra todo el campo **Motivo**. Pulsa **Guardar cambios**.
3. Regresa a la cita, escribe un texto de 101 caracteres y vuelve a guardar.
4. Anota qué mensaje aparece y si el dato se ha guardado.

**Lo esperado:** el portal rechaza ambos casos con una explicación clara y no guarda los cambios.

## Registra cada comprobación

Rellena una copia de [la hoja de resultados](practica/hoja_resultados.md). Para cada prueba, apunta:

- El requisito que estás comprobando.
- Los pasos exactos que has seguido.
- El resultado esperado.
- El resultado que observaste.
- Una evidencia que ayudaría a revisar el resultado, por ejemplo una captura con datos ficticios.
- Una conclusión: **Pasa**, **Falla** o **No comprobado**.

**Falla** significa que ocurrió algo contrario al requisito. **No comprobado** significa que no pudiste obtener una conclusión. No son lo mismo.

## Puesta en común

Prepara una explicación de 30 segundos con esta estructura:

> «Comprobamos ___. Esperábamos ___. Ocurrió ___. La prueba ___ y guardaríamos ___ como evidencia.»
