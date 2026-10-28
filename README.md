# Práctica 2 · Laboratorio local de verificación

Aplicación web de aula para practicar **control de acceso, cierre de sesión y validación de datos**. Está pensada para grupos que empiezan desde cero: el alumnado trabaja desde el navegador y no necesita leer ni modificar código.

## Qué incluye

- Una aplicación de citas con dos cuentas y datos inventados.
- Un **modo aula** con tres fallos preparados para que el grupo los compruebe.
- Un **modo resuelto** con los comportamientos esperados, para la puesta en común.
- Una guía del alumnado y una hoja para registrar las pruebas.

## Arranque rápido

Necesitas Python 3.10 o posterior. No hay que instalar paquetes.

### macOS o Linux

1. Abre Terminal.
2. Entra en esta carpeta. Si la has descargado en `Descargas`, por ejemplo:

   ```bash
   cd ~/Downloads/practica2-laboratorio-ens
   ```

3. Inicia el modo aula:

   ```bash
   python3 app.py --mode aula
   ```

4. En el mismo ordenador, abre el navegador en <http://127.0.0.1:8000>.
5. Para parar el laboratorio, vuelve a Terminal y pulsa `Ctrl+C`.

### Windows

1. Abre Símbolo del sistema o PowerShell.
2. Entra en la carpeta del proyecto, por ejemplo:

   ```powershell
   cd $HOME\Downloads\practica2-laboratorio-ens
   ```

3. Inicia el modo aula:

   ```powershell
   py app.py --mode aula
   ```

4. En el mismo ordenador, abre el navegador en <http://127.0.0.1:8000>.
5. Para parar el laboratorio, vuelve a la terminal y pulsa `Ctrl+C`.

## Cuentas ficticias

| Usuario | Contraseña | Cita de ejemplo |
|---|---|---|
| `ana` | `ana123` | 1001 |
| `luis` | `luis123` | 2002 |

La página de inicio incluye los dos enlaces para poder hacer la prueba de acceso. El portal y los enlaces solo funcionan en el ordenador donde se ha iniciado el laboratorio.

## Cómo se desarrolla la práctica

1. El alumnado inicia sesión como ANA y prueba los comportamientos indicados en [la guía del alumnado](GUIA_ALUMNADO.md).
2. Cada grupo completa una copia de [la hoja de resultados](practica/hoja_resultados.md).
3. El docente detiene el servidor con `Ctrl+C` y arranca `--mode resuelto` para comparar los resultados.
4. Para la puesta en común, cada grupo comparte una prueba y explica si pasa, falla o no se pudo comprobar.

## Alcance y seguridad

Este proyecto es un **laboratorio educativo local**, no una aplicación real ni una plantilla para producción. Solo usa datos ficticios, escucha en `127.0.0.1` y no está diseñado para exponerse a Internet, una red del centro o un servidor público. No introduzcas datos reales ni contraseñas que se usen en otros servicios.
