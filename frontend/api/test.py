from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {
            "message": "Python API is working!",
            "timestamp": datetime.now().isoformat(),
            "path": self.path
        }
        self.wfile.write(json.dumps(response).encode())
        return