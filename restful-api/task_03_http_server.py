#!/usr/bin/python3

import http.server, socketserver, json

class Handler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            yeison = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(yeison.encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Ok")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            yeison = json.dumps({"version": "1.0", "description": "A simple API built with http.server"})
            self.wfile.write(yeison.encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

with socketserver.TCPServer(("", 8000), Handler) as httpd:
    print("serving at port", 8000)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass