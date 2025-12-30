# Crypto Dashboard Installation Instructions

## Files Created:
1. `crypto_dashboard.html` - The main dashboard
2. `launch_crypto_dashboard.sh` - Script to launch in kiosk mode
3. `start_server.py` - Python web server (fixes CORS issues)

## Installation Steps:

### 1. Copy files to your home directory
```bash
cp crypto_dashboard.html /home/pi/
cp launch_crypto_dashboard.sh /home/pi/
cp start_server.py /home/pi/
chmod +x /home/pi/launch_crypto_dashboard.sh
chmod +x /home/pi/start_server.py
```

### 2. Install unclutter (to hide mouse cursor)
```bash
sudo apt-get update
sudo apt-get install -y unclutter
```

### 3. Test the dashboard manually first
```bash
/home/pi/launch_crypto_dashboard.sh
```
Press Alt+F4 or F11 to exit fullscreen when testing.

### 4. Set up auto-start on boot

#### Option A: Using autostart (Recommended for LXDE/Raspberry Pi OS Desktop)
```bash
mkdir -p /home/pi/.config/lxsession/LXDE-pi
nano /home/pi/.config/lxsession/LXDE-pi/autostart
```

Add this line at the end:
```
@/home/pi/launch_crypto_dashboard.sh
```

Save (Ctrl+O, Enter) and exit (Ctrl+X).

#### Option B: Using .bashrc (if you auto-login to terminal)
```bash
nano /home/pi/.bashrc
```

Add this at the end:
```bash
if [ -z "$SSH_CLIENT" ] && [ -z "$SSH_TTY" ]; then
    startx -- -nocursor &
    /home/pi/launch_crypto_dashboard.sh
fi
```

### 5. Reboot to test
```bash
sudo reboot
```

## Features:
- Updates every 45 seconds
- Shows BTC, ETH, ZEC, and LINK prices
- Displays current price, 24h change %, 24h high/low
- Terminal-style black background with bright green text
- Last update timestamp at bottom
- If API fails, timestamp turns RED and BOLD
- Fullscreen kiosk mode (no browser UI)
- Hidden mouse cursor

## Troubleshooting:

### Dashboard doesn't load on boot:
- Check file permissions: `ls -la /home/pi/launch_crypto_dashboard.sh`
- Check autostart file: `cat /home/pi/.config/lxsession/LXDE-pi/autostart`

### Prices not updating:
- Check internet: `ping 8.8.8.8`
- Check API access: `curl https://api.coingecko.com/api/v3/ping`

### To stop/exit the dashboard:
- Press Alt+F4 or Ctrl+W
- Or SSH in and run: `pkill chromium`

## API Information:
Uses CoinGecko's free public API. Rate limit: ~10-50 requests/minute (we only make 1 request per 45 seconds, so well within limits).

## Customization:
To change update frequency, edit `crypto_dashboard.html` and find this line:
```javascript
updateInterval = setInterval(fetchCryptoData, 45000);
```
Change 45000 to desired milliseconds (30000 = 30 seconds, 60000 = 1 minute)
