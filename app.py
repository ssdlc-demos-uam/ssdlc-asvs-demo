#!/usr/bin/env python3
"""Local classroom lab for ENS/ASVS practice. Standard library only."""

from __future__ import annotations

import argparse
import html
import secrets
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse


HOST = "127.0.0.1"  # Deliberately local-only.
PORT = 8000
MAX_REASON_LENGTH = 100

USERS = {
    "ana": {"password": "ana123", "name": "Ana"},
    "luis": {"password": "luis123", "name": "Luis"},
}

# Invented records for the exercise. Never put real personal data here.
APPOINTMENTS = {
    "1001": {"owner": "ana", "day": "martes", "time": "10:00", "reason": "Certificado de ejemplo"},
    "2002": {"owner": "luis", "day": "jueves", "time": "12:30", "reason": "Consulta de ejemplo"},
}

SESSIONS: dict[str, str] = {}
MODE = "aula"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def page(title: str, body: str, username: str | None = None, message: str = "") -> str:
    who = f"Sesión activa: <strong>{esc(USERS[username]['name'])}</strong>" if username in USERS else "Sin sesión iniciada"
    alert = f'<p class="notice">{esc(message)}</p>' if message else ""
    home = '<a href="/">Inicio</a>'
    logout = (
        '<form class="inline" method="post" action="/logout"><button class="quiet" type="submit">Cerrar sesión</button></form>'
        if username in USERS else ""
    )
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} · Portal municipal de citas</title>
<style>
  :root {{ color-scheme: light; font-family: Arial, sans-serif; color: #17202a; background: #f4f6f8; }}
  body {{ margin: 0; }} header {{ background: #234f79; color: white; padding: 18px max(22px, calc((100vw - 900px)/2)); }}
  header h1 {{ font-size: 1.35rem; margin: 0 0 8px; }} header p {{ margin: 0; font-size: .95rem; }}
  main {{ max-width: 900px; margin: 28px auto; padding: 0 20px 40px; }}
  section {{ background: white; border: 1px solid #d5dce3; padding: 20px; margin: 16px 0; }}
  h2 {{ margin-top: 0; }} p {{ line-height: 1.5; }}
  .meta {{ color: #455a64; font-size: .95rem; }} .notice {{ background: #edf4fa; border-left: 4px solid #3976a8; padding: 12px; }}
  label {{ display: block; font-weight: bold; margin: 14px 0 6px; }} input {{ box-sizing: border-box; max-width: 100%; width: 420px; padding: 10px; font: inherit; }}
  button {{ background: #245e8e; color: white; border: 0; padding: 10px 16px; font: inherit; cursor: pointer; margin-top: 14px; }}
  button.quiet {{ background: transparent; color: white; text-decoration: underline; padding: 4px; margin: 0; }}
  a {{ color: #145c91; }} nav {{ display:flex; justify-content:space-between; align-items:center; gap:12px; }} nav .inline {{ display:inline; }}
  .test-link {{ display:inline-block; margin: 6px 12px 6px 0; }} code {{ background:#edf0f2; padding:2px 4px; }}
</style></head><body>
<header><nav><div><h1>Portal municipal de citas</h1><p>Entorno local de prácticas · solo datos ficticios</p></div><div>{who}<br>{home} {logout}</div></nav></header>
<main><h2>{esc(title)}</h2>{alert}{body}</main></body></html>"""


class LabHandler(BaseHTTPRequestHandler):
    server_version = "CitasLab/1.0"

    def log_message(self, fmt: str, *args: object) -> None:
        # Keep the terminal readable for a classroom projector.
        print("[servidor] " + (fmt % args))

    def current_user(self) -> str | None:
        cookie = SimpleCookie(self.headers.get("Cookie", ""))
        morsel = cookie.get("lab_session")
        return SESSIONS.get(morsel.value) if morsel else None

    def send_html(self, content: str, status: int = 200, extra_headers: list[tuple[str, str]] | None = None) -> None:
        data = content.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        for key, value in extra_headers or []:
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(data)

    def redirect(self, location: str, cookie: str | None = None) -> None:
        self.send_response(303)
        self.send_header("Location", location)
        self.send_header("Cache-Control", "no-store")
        if cookie:
            self.send_header("Set-Cookie", cookie)
        self.end_headers()

    def read_form(self) -> dict[str, str]:
        try:
            size = min(int(self.headers.get("Content-Length", "0")), 100_000)
        except ValueError:
            size = 0
        raw = self.rfile.read(size).decode("utf-8", errors="replace")
        return {key: values[0] for key, values in parse_qs(raw, keep_blank_values=True).items()}

    def login_screen(self, message: str = "") -> None:
        body = """<section><p>Inicia sesión con una de las cuentas ficticias:</p>
<ul><li><code>ana</code> / <code>ana123</code></li><li><code>luis</code> / <code>luis123</code></li></ul>
<form method="post" action="/login"><label for="username">Usuario</label><input id="username" name="username" autocomplete="username">
<label for="password">Contraseña</label><input id="password" name="password" type="password" autocomplete="current-password">
<br><button type="submit">Entrar</button></form></section>"""
        self.send_html(page("Iniciar sesión", body, message=message))

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        route = parsed.path
        username = self.current_user()

        if route in ("/", "/login"):
            if not username:
                self.login_screen()
                return
            own_id = next(key for key, item in APPOINTMENTS.items() if item["owner"] == username)
            body = f"""<section><p>Hola, {esc(USERS[username]['name'])}. Esta es la página de pruebas del portal.</p>
<p><a href="/citas/{own_id}">Abrir mi cita ficticia</a></p>
<hr><h3>Enlaces que ha preparado el profesor para la práctica</h3>
<a class="test-link" href="/citas/1001">Cita de ANA (1001)</a>
<a class="test-link" href="/citas/2002">Cita de LUIS (2002)</a>
<p class="meta">Usa estos enlaces únicamente dentro de este ejercicio local.</p></section>"""
            self.send_html(page("Inicio", body, username))
            return

        if route.startswith("/citas/"):
            appointment_id = route.removeprefix("/citas/")
            appointment = APPOINTMENTS.get(appointment_id)
            if not appointment:
                self.send_html(page("Cita no encontrada", '<p>El identificador no existe en los datos de ejemplo.</p>', username), 404)
                return
            if not username:
                self.redirect("/login")
                return
            if MODE == "resuelto" and appointment["owner"] != username:
                self.send_html(page("Acceso denegado", '<p>Esta cita pertenece a otra cuenta. No se muestran sus datos.</p><p><a href="/">Volver al inicio</a></p>', username), 403)
                return
            owner_name = USERS[appointment["owner"]]["name"]
            body = f"""<section><p><strong>Propietario:</strong> {esc(owner_name)}</p>
<p><strong>Día:</strong> {esc(appointment['day'])} · <strong>Hora:</strong> {esc(appointment['time'])}</p>
<form method="post" action="/citas/{esc(appointment_id)}"><label for="reason">Motivo (obligatorio, máximo 100 caracteres)</label>
<input id="reason" name="reason" value="{esc(appointment['reason'])}">
<br><button type="submit">Guardar cambios</button></form></section>
<p><a href="/">Volver al inicio y usar otro enlace de prueba</a></p>"""
            self.send_html(page(f"Cita {appointment_id}", body, username))
            return

        self.send_html(page("Página no encontrada", '<p><a href="/">Volver al inicio</a></p>', username), 404)

    def do_POST(self) -> None:
        route = urlparse(self.path).path
        form = self.read_form()
        username = self.current_user()

        if route == "/login":
            user = form.get("username", "").strip().lower()
            password = form.get("password", "")
            if user not in USERS or USERS[user]["password"] != password:
                self.login_screen("Usuario o contraseña incorrectos. Prueba con las cuentas ficticias indicadas.")
                return
            token = secrets.token_urlsafe(24)
            SESSIONS[token] = user
            self.redirect("/", f"lab_session={token}; HttpOnly; SameSite=Lax; Path=/")
            return

        if route == "/logout":
            cookie = SimpleCookie(self.headers.get("Cookie", ""))
            morsel = cookie.get("lab_session")
            token = morsel.value if morsel else ""
            if MODE == "resuelto":
                SESSIONS.pop(token, None)
                self.redirect("/login", "lab_session=; Max-Age=0; HttpOnly; SameSite=Lax; Path=/")
            else:
                # Classroom mode intentionally simulates a logout that does not revoke the server session.
                body = '<section><p>El portal muestra “Sesión cerrada”.</p><p>Comprueba la promesa: vuelve al inicio y abre el enlace de una cita.</p><a href="/">Volver al inicio</a></section>'
                self.send_html(page("Has cerrado sesión", body, username, "Prueba pendiente: ¿se ha invalidado realmente la sesión?"))
            return

        if route.startswith("/citas/"):
            appointment_id = route.removeprefix("/citas/")
            appointment = APPOINTMENTS.get(appointment_id)
            if not appointment:
                self.send_html(page("Cita no encontrada", '<p>El identificador no existe en los datos de ejemplo.</p>', username), 404)
                return
            if not username:
                self.redirect("/login")
                return
            if MODE == "resuelto" and appointment["owner"] != username:
                self.send_html(page("Acceso denegado", '<p>Esta cita pertenece a otra cuenta. No se guardó ningún cambio.</p><p><a href="/">Volver al inicio</a></p>', username), 403)
                return
            reason = form.get("reason", "")
            if MODE == "resuelto" and (not reason.strip() or len(reason) > MAX_REASON_LENGTH):
                message = "Escribe un motivo de hasta 100 caracteres. No se guardaron los cambios."
                owner_name = USERS[appointment["owner"]]["name"]
                body = f"""<section><p><strong>Propietario:</strong> {esc(owner_name)}</p>
<p><strong>Día:</strong> {esc(appointment['day'])} · <strong>Hora:</strong> {esc(appointment['time'])}</p>
<form method="post" action="/citas/{esc(appointment_id)}"><label for="reason">Motivo (obligatorio, máximo 100 caracteres)</label>
<input id="reason" name="reason" value="{esc(reason)}"><br><button type="submit">Guardar cambios</button></form></section>"""
                self.send_html(page(f"Cita {appointment_id}", body, username, message), 400)
                return
            appointment["reason"] = reason
            self.redirect(f"/citas/{appointment_id}")
            return

        self.send_html(page("Página no encontrada", '<p><a href="/">Volver al inicio</a></p>', username), 404)


def main() -> None:
    global MODE
    parser = argparse.ArgumentParser(description="Laboratorio local de práctica ENS/ASVS")
    parser.add_argument("--mode", choices=("aula", "resuelto"), default="aula", help="aula presenta fallos de práctica; resuelto aplica controles esperados")
    args = parser.parse_args()
    MODE = args.mode
    server = ThreadingHTTPServer((HOST, PORT), LabHandler)
    print(f"Laboratorio {MODE} iniciado en http://{HOST}:{PORT}")
    print("Solo accesible desde este ordenador. Pulsa Ctrl+C para pararlo.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nLaboratorio detenido.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
