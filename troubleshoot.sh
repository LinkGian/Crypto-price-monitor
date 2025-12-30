#!/bin/bash
# Troubleshooting script for crypto dashboard

echo "🔍 CRYPTO DASHBOARD TROUBLESHOOTING"
echo "===================================="
echo ""

# Check 1: Files location
echo "✓ Checking if files exist in /home/pi..."
if [ -f "/home/pi/crypto_dashboard.html" ]; then
    echo "  ✅ crypto_dashboard.html found"
else
    echo "  ❌ crypto_dashboard.html NOT FOUND in /home/pi"
    echo "     You need to copy it there first!"
fi

if [ -f "/home/pi/start_server.py" ]; then
    echo "  ✅ start_server.py found"
else
    echo "  ❌ start_server.py NOT FOUND in /home/pi"
fi

if [ -f "/home/pi/launch_crypto_dashboard.sh" ]; then
    echo "  ✅ launch_crypto_dashboard.sh found"
else
    echo "  ❌ launch_crypto_dashboard.sh NOT FOUND in /home/pi"
fi

echo ""

# Check 2: Python availability
echo "✓ Checking Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "  ✅ $PYTHON_VERSION"
else
    echo "  ❌ Python 3 not found!"
fi

echo ""

# Check 3: Port 8080 availability
echo "✓ Checking if port 8080 is available..."
if netstat -tlnp 2>/dev/null | grep -q ":8080 "; then
    echo "  ⚠️  Port 8080 is already in use!"
    echo "     Process using it:"
    netstat -tlnp 2>/dev/null | grep ":8080 "
elif ss -tlnp 2>/dev/null | grep -q ":8080 "; then
    echo "  ⚠️  Port 8080 is already in use!"
    echo "     Process using it:"
    ss -tlnp 2>/dev/null | grep ":8080 "
else
    echo "  ✅ Port 8080 is available"
fi

echo ""

# Check 4: Try to start server manually
echo "✓ Attempting to start server manually..."
cd /home/pi
timeout 3 python3 -m http.server 8080 &> /tmp/server_test.log &
SERVER_PID=$!
sleep 2

if ps -p $SERVER_PID > /dev/null 2>&1; then
    echo "  ✅ Server started successfully (PID: $SERVER_PID)"

    # Test connection
    if curl -s http://localhost:8080/crypto_dashboard.html > /dev/null 2>&1; then
        echo "  ✅ Dashboard is accessible!"
    else
        echo "  ❌ Server running but dashboard not accessible"
    fi

    kill $SERVER_PID 2>/dev/null
else
    echo "  ❌ Server failed to start"
    echo "     Error log:"
    cat /tmp/server_test.log
fi

echo ""

# Check 5: Internet connectivity
echo "✓ Checking internet connection..."
if ping -c 1 8.8.8.8 &> /dev/null; then
    echo "  ✅ Internet connection working"
    if ping -c 1 api.coingecko.com &> /dev/null; then
        echo "  ✅ Can reach CoinGecko API"
    else
        echo "  ⚠️  Cannot reach api.coingecko.com"
    fi
else
    echo "  ❌ No internet connection"
fi

echo ""
echo "===================================="
echo "📋 RECOMMENDED ACTIONS:"
echo ""

if [ ! -f "/home/pi/crypto_dashboard.html" ]; then
    echo "1. Copy files to /home/pi:"
    echo "   cp ~/Crypto-price-monitor/*.html /home/pi/"
    echo "   cp ~/Crypto-price-monitor/*.py /home/pi/"
    echo "   cp ~/Crypto-price-monitor/*.sh /home/pi/"
    echo ""
fi

echo "2. Try starting the server manually:"
echo "   cd /home/pi"
echo "   python3 start_server.py"
echo ""

echo "3. In another terminal, check if it's working:"
echo "   curl http://localhost:8080/crypto_dashboard.html"
echo ""

echo "4. If working, then try the full launcher:"
echo "   ./launch_crypto_dashboard.sh"
echo ""
