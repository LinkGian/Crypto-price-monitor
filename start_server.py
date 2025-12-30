#!/usr/bin/env python3
import http.server
import socketserver
import os

# Change to the directory where the HTML file is located
os.chdir('/home/pi')

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    print(f"Serving crypto_dashboard.html")
    httpd.serve_forever()
