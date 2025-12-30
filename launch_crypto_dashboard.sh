#!/bin/bash

# Wait for X server to be ready
sleep 5

# Start the Python web server in the background
python3 /home/pi/start_server.py &
SERVER_PID=$!

# Wait a moment for server to start
sleep 2

# Disable screen blanking and power management
xset s off
xset -dpms
xset s noblank

# Hide mouse cursor after 1 second of inactivity
unclutter -idle 1 &

# Launch Chromium in kiosk mode with the crypto dashboard
chromium-browser --kiosk --noerrdialogs --disable-infobars --incognito \
  --disable-session-crashed-bubble --disable-restore-session-state \
  http://localhost:8080/crypto_dashboard.html

# When Chromium closes, kill the web server
kill $SERVER_PID
