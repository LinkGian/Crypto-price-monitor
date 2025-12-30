#!/usr/bin/env python3
"""
Simulate the crypto dashboard display with sample data
Shows what the dashboard would look like in a terminal
"""

from datetime import datetime

# Sample crypto data (simulating what CoinGecko API would return)
crypto_data = {
    'Bitcoin': {
        'symbol': 'BTC',
        'price': 94234.56,
        'change_24h': 2.47,
        'high_24h': 95123.45,
        'low_24h': 92456.78
    },
    'Ethereum': {
        'symbol': 'ETH',
        'price': 3456.78,
        'change_24h': -1.23,
        'high_24h': 3512.34,
        'low_24h': 3401.23
    },
    'Zcash': {
        'symbol': 'ZEC',
        'price': 47.89,
        'change_24h': 5.67,
        'high_24h': 49.12,
        'low_24h': 45.23
    },
    'Chainlink': {
        'symbol': 'LINK',
        'price': 23.45,
        'change_24h': -0.89,
        'high_24h': 24.12,
        'low_24h': 23.01
    }
}

# ANSI color codes for terminal styling
GREEN = '\033[92m'
RED = '\033[91m'
BRIGHT_GREEN = '\033[1;92m'
BOLD = '\033[1m'
RESET = '\033[0m'

def format_price(price):
    """Format price similar to dashboard"""
    if price >= 1000:
        return f"${price:,.2f}"
    elif price >= 1:
        return f"${price:.4f}"
    else:
        return f"${price:.6f}"

def format_change(change):
    """Format change percentage with color"""
    sign = '+' if change >= 0 else ''
    color = GREEN if change >= 0 else RED
    return f"{color}{sign}{change:.2f}%{RESET}"

def print_crypto_card(name, data):
    """Print a styled crypto card"""
    print(f"\n{BRIGHT_GREEN}╔{'═' * 50}╗{RESET}")
    print(f"{BRIGHT_GREEN}║{RESET} {BOLD}{GREEN}{name:^48}{RESET} {BRIGHT_GREEN}║{RESET}")
    print(f"{BRIGHT_GREEN}║{RESET} {GREEN}({data['symbol']}){RESET:^54} {BRIGHT_GREEN}║{RESET}")
    print(f"{BRIGHT_GREEN}╠{'═' * 50}╣{RESET}")
    print(f"{BRIGHT_GREEN}║{RESET}                                                  {BRIGHT_GREEN}║{RESET}")
    print(f"{BRIGHT_GREEN}║{RESET}  {BOLD}{GREEN}Price:{RESET} {format_price(data['price']):>30}      {BRIGHT_GREEN}║{RESET}")
    print(f"{BRIGHT_GREEN}║{RESET}                                                  {BRIGHT_GREEN}║{RESET}")
    print(f"{BRIGHT_GREEN}║{RESET}  {GREEN}24h Change:{RESET} {format_change(data['change_24h']):>35}     {BRIGHT_GREEN}║{RESET}")
    print(f"{BRIGHT_GREEN}║{RESET}                                                  {BRIGHT_GREEN}║{RESET}")
    print(f"{BRIGHT_GREEN}║{RESET}  {GREEN}24h High:{RESET} {format_price(data['high_24h']):>30}      {BRIGHT_GREEN}║{RESET}")
    print(f"{BRIGHT_GREEN}║{RESET}  {GREEN}24h Low:{RESET}  {format_price(data['low_24h']):>30}      {BRIGHT_GREEN}║{RESET}")
    print(f"{BRIGHT_GREEN}║{RESET}                                                  {BRIGHT_GREEN}║{RESET}")
    print(f"{BRIGHT_GREEN}╚{'═' * 50}╝{RESET}")

def simulate_dashboard():
    """Simulate the full dashboard display"""
    # Clear screen effect
    print("\n" * 2)

    # Title
    print(f"{BRIGHT_GREEN}{'=' * 60}{RESET}")
    print(f"{BRIGHT_GREEN}{BOLD}⚡ CRYPTO PRICE MONITOR ⚡{RESET}".center(68))
    print(f"{BRIGHT_GREEN}{'=' * 60}{RESET}")

    # Display all crypto cards in grid (2x2 layout simulation)
    cryptos = list(crypto_data.items())

    # Row 1: Bitcoin and Ethereum
    for name, data in cryptos[:2]:
        print_crypto_card(name, data)

    # Row 2: Zcash and Chainlink
    for name, data in cryptos[2:]:
        print_crypto_card(name, data)

    # Timestamp
    current_time = datetime.now().strftime('%b %d, %Y, %I:%M:%S %p')
    print(f"\n{BRIGHT_GREEN}{'─' * 60}{RESET}")
    print(f"{GREEN}Last Updated: {current_time}{RESET}".center(68))
    print(f"{BRIGHT_GREEN}{'─' * 60}{RESET}\n")

    # Dashboard stats
    print(f"{GREEN}Dashboard Status:{RESET}")
    print(f"  ✅ HTTP Server: Running on port 8080")
    print(f"  ✅ Update Interval: 45 seconds")
    print(f"  ✅ API Source: CoinGecko")
    print(f"  ✅ Cryptocurrencies Tracked: 4 (BTC, ETH, ZEC, LINK)")
    print(f"  ✅ Auto-refresh: Enabled")
    print(f"  ✅ Error Handling: Active")

    print(f"\n{BRIGHT_GREEN}{'=' * 60}{RESET}")
    print(f"{GREEN}Access dashboard at: {BOLD}http://localhost:8080/crypto_dashboard.html{RESET}")
    print(f"{BRIGHT_GREEN}{'=' * 60}{RESET}\n")

if __name__ == '__main__':
    simulate_dashboard()
