"""
server.py — Servidor local para desarrollo
==========================================
Sirve el dashboard en tu red WiFi local.
Útil para probar antes de subir a GitHub Pages.

Uso:
    python server.py

Luego abre en el navegador:
    http://localhost:8000          (en tu PC)
    http://192.168.x.x:8000       (en tu Android, misma WiFi)
"""

import http.server
import socketserver
import os
import socket

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # silencia logs de cada request

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "localhost"

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    ip = get_local_ip()

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\n  Dashboard disponible en:")
        print(f"    Local:   http://localhost:{PORT}")
        print(f"    Android: http://{ip}:{PORT}")
        print(f"\n  Ctrl+C para detener\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Servidor detenido.")
