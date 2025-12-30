#!/usr/bin/env python3
"""
Simplified HTTP server for crypto dashboard
Serves from the current directory instead of hardcoded /home/pi
"""
import http.server
import socketserver
import os
import sys

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Change to script directory
os.chdir(SCRIPT_DIR)

PORT = 8080

print(f"Starting server...")
print(f"Serving from: {os.getcwd()}")
print(f"Port: {PORT}")
print("")

# Check if crypto_dashboard.html exists
if not os.path.exists('crypto_dashboard.html'):
    print("❌ ERROR: crypto_dashboard.html not found in current directory!")
    print(f"   Current directory: {os.getcwd()}")
    print(f"   Files in directory:")
    for file in os.listdir('.'):
        print(f"     - {file}")
    print("")
    print("Please make sure crypto_dashboard.html is in the same directory as this script.")
    sys.exit(1)

print("✅ crypto_dashboard.html found")
print("")

Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"✅ Server running at http://localhost:{PORT}/")
        print(f"✅ Dashboard URL: http://localhost:{PORT}/crypto_dashboard.html")
        print("")
        print("Press Ctrl+C to stop the server")
        print("")
        httpd.serve_forever()
except OSError as e:
    if e.errno == 98:
        print(f"❌ ERROR: Port {PORT} is already in use!")
        print("   Try killing the existing process:")
        print(f"   sudo lsof -ti:{PORT} | xargs kill -9")
        print("   Or use a different port")
        sys.exit(1)
    else:
        raise
except KeyboardInterrupt:
    print("\n\n✅ Server stopped")
    sys.exit(0)
