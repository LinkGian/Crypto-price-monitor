#!/bin/bash
# Simplified launcher for crypto dashboard with better error handling

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🚀 Starting Crypto Dashboard..."
echo "Working directory: $SCRIPT_DIR"
echo ""

# Check if crypto_dashboard.html exists
if [ ! -f "crypto_dashboard.html" ]; then
    echo "❌ ERROR: crypto_dashboard.html not found!"
    echo "   Please make sure you're running this from the correct directory."
    echo "   Current directory: $SCRIPT_DIR"
    exit 1
fi

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python 3 not found!"
    echo "   Please install Python 3: sudo apt-get install python3"
    exit 1
fi

echo "✅ Files found"
echo ""

# Kill any existing server on port 8080
if lsof -ti:8080 &> /dev/null; then
    echo "⚠️  Killing existing process on port 8080..."
    lsof -ti:8080 | xargs kill -9 2>/dev/null
    sleep 1
fi

# Start the server in background
echo "Starting HTTP server..."
python3 "$SCRIPT_DIR/start_server_simple.py" &
SERVER_PID=$!

# Wait for server to start
sleep 3

# Check if server is running
if ! ps -p $SERVER_PID > /dev/null 2>&1; then
    echo "❌ ERROR: Server failed to start!"
    echo "   Try running manually: python3 start_server_simple.py"
    exit 1
fi

echo "✅ Server started (PID: $SERVER_PID)"
echo ""

# Test if dashboard is accessible
echo "Testing dashboard accessibility..."
if curl -s http://localhost:8080/crypto_dashboard.html > /dev/null; then
    echo "✅ Dashboard is accessible!"
else
    echo "❌ ERROR: Dashboard not accessible"
    kill $SERVER_PID 2>/dev/null
    exit 1
fi

echo ""
echo "Dashboard URL: http://localhost:8080/crypto_dashboard.html"
echo ""

# Check if we're in a graphical environment
if [ -n "$DISPLAY" ]; then
    echo "Launching browser..."

    # Disable screen blanking
    xset s off 2>/dev/null
    xset -dpms 2>/dev/null

    # Hide mouse cursor
    if command -v unclutter &> /dev/null; then
        unclutter -idle 1 &
        UNCLUTTER_PID=$!
    else
        echo "⚠️  unclutter not found (mouse cursor won't auto-hide)"
        echo "   Install with: sudo apt-get install unclutter"
    fi

    # Launch browser (try chromium first, then other browsers)
    if command -v chromium-browser &> /dev/null; then
        chromium-browser --kiosk --noerrdialogs --disable-infobars \
            --incognito --disable-session-crashed-bubble \
            --disable-restore-session-state \
            http://localhost:8080/crypto_dashboard.html
    elif command -v chromium &> /dev/null; then
        chromium --kiosk --noerrdialogs --disable-infobars \
            --incognito --disable-session-crashed-bubble \
            --disable-restore-session-state \
            http://localhost:8080/crypto_dashboard.html
    elif command -v firefox &> /dev/null; then
        firefox --kiosk http://localhost:8080/crypto_dashboard.html
    else
        echo "❌ No browser found!"
        echo "   The server is running. Open this URL in any browser:"
        echo "   http://localhost:8080/crypto_dashboard.html"
        echo ""
        echo "   Press Ctrl+C to stop the server"
        wait $SERVER_PID
    fi

    # Clean up when browser closes
    echo ""
    echo "Browser closed. Cleaning up..."
    kill $SERVER_PID 2>/dev/null
    [ -n "$UNCLUTTER_PID" ] && kill $UNCLUTTER_PID 2>/dev/null
    echo "✅ Done"
else
    echo "⚠️  No display found (running headless)"
    echo "   Server is running at: http://localhost:8080/crypto_dashboard.html"
    echo "   Press Ctrl+C to stop"
    wait $SERVER_PID
fi
