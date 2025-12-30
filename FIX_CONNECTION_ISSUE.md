# 🔧 Fix "localhost refused to connect" Issue

## Quick Fix (Try This First!)

The problem is likely that the files aren't in `/home/pi` or the server didn't start. Here's the fix:

### Step 1: Navigate to where you cloned the repo
```bash
cd ~/Crypto-price-monitor
# OR wherever you cloned it to
```

### Step 2: Make the simple scripts executable
```bash
chmod +x start_server_simple.py
chmod +x launch_simple.sh
chmod +x troubleshoot.sh
```

### Step 3: Run the troubleshooter
```bash
./troubleshoot.sh
```

This will tell you exactly what's wrong!

### Step 4: Use the simplified launcher
```bash
./launch_simple.sh
```

This works from ANY directory (you don't need to copy files to `/home/pi`).

---

## Manual Testing (If Above Doesn't Work)

### Test 1: Start server manually
```bash
cd ~/Crypto-price-monitor
python3 start_server_simple.py
```

You should see:
```
✅ crypto_dashboard.html found
✅ Server running at http://localhost:8080/
✅ Dashboard URL: http://localhost:8080/crypto_dashboard.html
```

**Leave this terminal open** and go to Test 2.

### Test 2: Open browser manually
Open Chromium browser and go to:
```
http://localhost:8080/crypto_dashboard.html
```

If it works, great! If not, continue to Test 3.

### Test 3: Check if server is actually running
In a NEW terminal:
```bash
curl http://localhost:8080/crypto_dashboard.html
```

You should see HTML code. If you do, the server works!

### Test 4: Check what's listening on port 8080
```bash
sudo lsof -i :8080
```

or

```bash
sudo netstat -tlnp | grep 8080
```

You should see `python3` listening on port 8080.

---

## Common Issues & Fixes

### Issue 1: "crypto_dashboard.html not found"
**Problem:** Files not in the right place
**Fix:**
```bash
cd ~/Crypto-price-monitor
ls -la crypto_dashboard.html
# If you see "No such file", then you need to pull the files:
git pull origin claude/test-functionality-b8idj
```

### Issue 2: "Port 8080 already in use"
**Problem:** Something else is using port 8080
**Fix:**
```bash
# Kill whatever is using port 8080
sudo lsof -ti:8080 | xargs sudo kill -9

# OR use a different port - edit start_server_simple.py:
# Change PORT = 8080 to PORT = 8081
# Then use http://localhost:8081/crypto_dashboard.html
```

### Issue 3: "Permission denied"
**Problem:** Script not executable
**Fix:**
```bash
chmod +x launch_simple.sh
chmod +x start_server_simple.py
```

### Issue 4: Browser won't launch
**Problem:** Chromium not found
**Fix:**
```bash
# Install chromium
sudo apt-get update
sudo apt-get install -y chromium-browser

# Or just open the URL manually after starting the server
```

### Issue 5: "No internet connection" / Prices don't load
**Problem:** Pi not connected to internet
**Fix:**
```bash
# Test internet connection
ping -c 3 google.com

# If fails, connect to WiFi:
sudo raspi-config
# Navigate to: System Options → Wireless LAN
```

---

## The Easiest Method (Copy & Paste This)

Just run these commands one by one:

```bash
# 1. Go to the repo
cd ~/Crypto-price-monitor

# 2. Pull latest changes
git checkout claude/test-functionality-b8idj
git pull

# 3. Make scripts executable
chmod +x *.sh *.py

# 4. Run troubleshooter
./troubleshoot.sh

# 5. Launch dashboard
./launch_simple.sh
```

If that doesn't work, show me what error messages you get!

---

## Still Not Working?

Run this and send me the output:

```bash
cd ~/Crypto-price-monitor
./troubleshoot.sh > ~/troubleshoot_output.txt 2>&1
cat ~/troubleshoot_output.txt
```

This will help me see exactly what's wrong!

---

## What Should Happen When It Works

1. ✅ Server starts with message "Server running at http://localhost:8080/"
2. ✅ Browser opens in fullscreen
3. ✅ You see "CRYPTO PRICE MONITOR" header
4. ✅ 4 crypto cards appear with Bitcoin, Ethereum, Zcash, Chainlink
5. ✅ Prices start loading (may take a few seconds)
6. ✅ Timestamp at bottom updates every 45 seconds
7. ✅ Mouse cursor hides after 1 second

**To exit:** Press `Alt + F4` or `Ctrl + W`
