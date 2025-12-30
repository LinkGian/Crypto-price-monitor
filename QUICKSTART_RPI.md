# 🚀 Quick Start Guide - Raspberry Pi Setup

## Step 1: Get the Files on Your Raspberry Pi

### Option A: Clone from GitHub (Recommended)
```bash
cd ~
git clone https://github.com/LinkGian/Crypto-price-monitor.git
cd Crypto-price-monitor
```

### Option B: Download as ZIP
1. Go to: https://github.com/LinkGian/Crypto-price-monitor
2. Click "Code" → "Download ZIP"
3. Extract to `/home/pi/Crypto-price-monitor`

## Step 2: Move Files to /home/pi

The scripts expect files in `/home/pi/`. Move them there:

```bash
# If you cloned to a different location
cp ~/Crypto-price-monitor/*.html /home/pi/
cp ~/Crypto-price-monitor/*.py /home/pi/
cp ~/Crypto-price-monitor/*.sh /home/pi/

# OR if you're already in the right place
cd ~/Crypto-price-monitor
cp crypto_dashboard.html start_server.py launch_crypto_dashboard.sh /home/pi/
```

## Step 3: Make Scripts Executable

```bash
cd /home/pi
chmod +x launch_crypto_dashboard.sh
chmod +x start_server.py
```

## Step 4: Install Dependencies

Install `unclutter` (hides mouse cursor in kiosk mode):

```bash
sudo apt-get update
sudo apt-get install -y unclutter
```

## Step 5: Test It!

### Quick Test (Manual Launch)
```bash
cd /home/pi
./launch_crypto_dashboard.sh
```

This will:
- Start the Python web server on port 8080
- Launch Chromium in fullscreen kiosk mode
- Display the crypto dashboard
- Hide the mouse cursor after 1 second

**To exit:** Press `Alt + F4` or `Ctrl + W`

### Alternative: Test Just the Server
```bash
cd /home/pi
python3 start_server.py
```

Then open Chromium manually and go to: `http://localhost:8080/crypto_dashboard.html`

## Step 6: Auto-Start on Boot (Optional)

### Method 1: LXDE Autostart (Recommended for Raspberry Pi OS Desktop)

```bash
# Create autostart directory if it doesn't exist
mkdir -p ~/.config/lxsession/LXDE-pi

# Edit autostart file
nano ~/.config/lxsession/LXDE-pi/autostart
```

Add this line at the end:
```
@/home/pi/launch_crypto_dashboard.sh
```

Save with `Ctrl + O`, `Enter`, then exit with `Ctrl + X`

### Method 2: .bashrc (Terminal Auto-Launch)

```bash
nano ~/.bashrc
```

Add at the end:
```bash
if [ -z "$SSH_CLIENT" ] && [ -z "$SSH_TTY" ]; then
    /home/pi/launch_crypto_dashboard.sh
fi
```

Save and exit.

### Method 3: systemd Service (Advanced)

Create a service file:
```bash
sudo nano /etc/systemd/system/crypto-dashboard.service
```

Add:
```ini
[Unit]
Description=Crypto Price Monitor Dashboard
After=graphical.target

[Service]
Type=simple
User=pi
Environment=DISPLAY=:0
ExecStart=/home/pi/launch_crypto_dashboard.sh
Restart=on-failure

[Install]
WantedBy=graphical.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable crypto-dashboard.service
sudo systemctl start crypto-dashboard.service
```

## Troubleshooting

### Dashboard doesn't show prices
- **Cause:** No internet connection
- **Fix:** Check your Pi is connected to WiFi/Ethernet
- **Test:** `ping api.coingecko.com`

### Chromium doesn't launch
- **Cause:** Chromium not installed
- **Fix:** `sudo apt-get install -y chromium-browser`

### Server says "Address already in use"
- **Cause:** Port 8080 is occupied
- **Fix:** Kill existing server: `pkill -f "python3.*start_server"`
- Or use a different port by editing `start_server.py`

### Mouse cursor won't hide
- **Cause:** unclutter not installed
- **Fix:** `sudo apt-get install -y unclutter`

### Screen keeps blanking
- **Cause:** Screen saver still active
- **Fix:** The launch script disables it, but you can also do:
  ```bash
  sudo nano /etc/lightdm/lightdm.conf
  ```
  Add under `[Seat:*]`:
  ```
  xserver-command=X -s 0 -dpms
  ```

## Customization

### Change Update Frequency
Edit `crypto_dashboard.html`:
```javascript
// Find this line (around line 186)
const UPDATE_INTERVAL = 45000; // 45 seconds

// Change to whatever you want (in milliseconds)
const UPDATE_INTERVAL = 30000; // 30 seconds
const UPDATE_INTERVAL = 60000; // 1 minute
```

### Add/Remove Cryptocurrencies
Edit `crypto_dashboard.html`:
```javascript
// Find this line (around line 185)
const CRYPTO_IDS = ['bitcoin', 'ethereum', 'zcash', 'chainlink'];

// Add more coins (use CoinGecko IDs)
const CRYPTO_IDS = ['bitcoin', 'ethereum', 'zcash', 'chainlink', 'cardano', 'dogecoin'];
```

[CoinGecko API Coin List](https://api.coingecko.com/api/v3/coins/list)

### Change Colors
Edit `crypto_dashboard.html` CSS section:
```css
/* Find these lines in the <style> section */
background-color: #000000;  /* Black background */
color: #00ff00;             /* Green text */

/* Change to any colors you want */
background-color: #0a0e27;  /* Dark blue */
color: #00d4ff;             /* Cyan */
```

## What You Should See

When running correctly, you'll see:
- **Fullscreen display** with no browser UI
- **4 crypto cards** in a 2x2 grid showing BTC, ETH, ZEC, LINK
- **Terminal-style design** with black background and bright green text
- **Prices updating** every 45 seconds
- **Timestamp** at the bottom showing last update time
- **Mouse cursor hidden** after 1 second of inactivity

## Need Help?

- Check `INSTALL_INSTRUCTIONS.md` for detailed info
- Run the test suite: `python3 test_dashboard.py`
- View simulation: `python3 simulate_dashboard.py`
- Check server logs for errors

## System Requirements

- **Raspberry Pi OS** (with Desktop/GUI)
- **Python 3** (pre-installed)
- **Chromium Browser** (pre-installed on Pi OS Desktop)
- **Internet connection** for fetching crypto prices
- **unclutter** (install with apt-get)

That's it! Enjoy your crypto price monitor! 🚀
