#!/usr/bin/python3

import http.server, socketserver

class Handler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("Hello, this is a simple API!")

with socketserver.TCPServer(("", 8000), Handler) as httpd:
    print("serving at port", 8000)
    httpd.serve_forever()
