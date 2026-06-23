from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os

from load_env import load_env

load_env()

PORT = int(os.environ["PORT"])

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!")

def run_server():
    server_address = ("", PORT)
    httpd = ThreadingHTTPServer(server_address, MyHandler)
    print(f"Server running on port {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()

if __name__ == "__main__":
    run_server()