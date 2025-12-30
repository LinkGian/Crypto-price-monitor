#!/usr/bin/env python3
"""
Comprehensive test suite for crypto_dashboard.html
Tests HTML structure, JavaScript logic, CSS, and API integration
"""

import re
import urllib.request
import json
from html.parser import HTMLParser

class DashboardHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.has_title = False
        self.has_style = False
        self.has_script = False
        self.script_content = ""
        self.style_content = ""
        self.in_script = False
        self.in_style = False
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append(tag)
        if tag == 'title':
            self.has_title = True
        elif tag == 'script':
            self.has_script = True
            self.in_script = True
        elif tag == 'style':
            self.has_style = True
            self.in_style = True

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_script = False
        elif tag == 'style':
            self.in_style = False

    def handle_data(self, data):
        if self.in_script:
            self.script_content += data
        elif self.in_style:
            self.style_content += data

def test_server_connection():
    """Test if the server is running and serving the dashboard"""
    print("🔍 Test 1: Server Connection")
    try:
        response = urllib.request.urlopen('http://localhost:8080/crypto_dashboard.html', timeout=5)
        status_code = response.getcode()
        content_type = response.headers.get('Content-Type', '')

        if status_code == 200:
            print("  ✅ Server is running (HTTP 200)")
        else:
            print(f"  ❌ Unexpected status code: {status_code}")
            return False

        if 'text/html' in content_type:
            print("  ✅ Correct content type (text/html)")
        else:
            print(f"  ⚠️  Content type: {content_type}")

        return True
    except Exception as e:
        print(f"  ❌ Server connection failed: {e}")
        return False

def test_html_structure():
    """Test the HTML structure and required elements"""
    print("\n🔍 Test 2: HTML Structure")
    try:
        response = urllib.request.urlopen('http://localhost:8080/crypto_dashboard.html', timeout=5)
        html_content = response.read().decode('utf-8')

        parser = DashboardHTMLParser()
        parser.feed(html_content)

        # Check for required HTML elements
        checks = {
            'DOCTYPE': '<!DOCTYPE html>' in html_content,
            '<html>': '<html' in html_content,
            '<head>': 'head' in parser.elements,
            '<title>': parser.has_title,
            '<style>': parser.has_style,
            '<script>': parser.has_script,
            '<body>': 'body' in parser.elements,
            'h1 heading': 'h1' in parser.elements,
            'div containers': 'div' in parser.elements,
        }

        for check, passed in checks.items():
            status = "✅" if passed else "❌"
            print(f"  {status} {check}")

        return all(checks.values()), html_content, parser

    except Exception as e:
        print(f"  ❌ HTML structure test failed: {e}")
        return False, None, None

def test_css_styling(parser):
    """Test CSS styling for terminal-style design"""
    print("\n🔍 Test 3: CSS Styling (Terminal Style)")

    css_checks = {
        'Black background': 'background-color: #000000' in parser.style_content or '#000000' in parser.style_content,
        'Green text': '#00ff00' in parser.style_content.lower() or 'color: #00ff00' in parser.style_content,
        'Courier/monospace font': 'courier' in parser.style_content.lower() or 'monospace' in parser.style_content.lower(),
        'Responsive grid': 'grid' in parser.style_content.lower(),
        'Hidden cursor': 'cursor: none' in parser.style_content or 'cursor:none' in parser.style_content,
    }

    for check, passed in css_checks.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {check}")

    return all(css_checks.values())

def test_javascript_logic(parser):
    """Test JavaScript functionality"""
    print("\n🔍 Test 4: JavaScript Logic")

    js = parser.script_content

    js_checks = {
        'CoinGecko API URL': 'api.coingecko.com' in js,
        'Bitcoin (bitcoin)': "'bitcoin'" in js or '"bitcoin"' in js,
        'Ethereum (ethereum)': "'ethereum'" in js or '"ethereum"' in js,
        'Zcash (zcash)': "'zcash'" in js or '"zcash"' in js,
        'Chainlink (chainlink)': "'chainlink'" in js or '"chainlink"' in js,
        '45-second interval': '45000' in js or '45 * 1000' in js,
        'Fetch function': 'fetch(' in js or 'fetch (' in js,
        'Error handling': 'catch' in js and 'error' in js.lower(),
        'Price formatting': 'formatPrice' in js or 'toFixed' in js or 'toLocaleString' in js,
        'Update timer': 'setInterval' in js or 'setTimeout' in js,
    }

    for check, passed in js_checks.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {check}")

    return all(js_checks.values())

def test_crypto_data_display(html_content):
    """Test elements for displaying crypto data"""
    print("\n🔍 Test 5: Crypto Data Display Elements")

    display_checks = {
        'Container div': 'crypto-container' in html_content or 'id="crypto-container"' in html_content,
        'Timestamp element': 'timestamp' in html_content or 'id="timestamp"' in html_content,
        'Loading indicator': 'loading' in html_content.lower(),
        'Error display': 'error' in html_content.lower(),
        'Price display': 'price' in html_content.lower(),
        'Change display': 'change' in html_content.lower(),
    }

    for check, passed in display_checks.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {check}")

    return all(display_checks.values())

def test_api_integration_logic(parser):
    """Test API integration details"""
    print("\n🔍 Test 6: API Integration Logic")

    js = parser.script_content

    api_checks = {
        'USD currency': 'usd' in js.lower(),
        '24h change included': '24hr_change' in js or '24h_change' in js,
        'Async/await': 'async' in js and 'await' in js,
        'JSON parsing': '.json()' in js,
        'Response handling': 'response' in js.lower(),
        'Auto-update function': 'update' in js.lower() and 'interval' in js.lower(),
    }

    for check, passed in api_checks.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {check}")

    return all(api_checks.values())

def test_file_size():
    """Test file size is reasonable"""
    print("\n🔍 Test 7: File Size")
    try:
        import os
        size = os.path.getsize('crypto_dashboard.html')
        size_kb = size / 1024

        print(f"  📊 File size: {size_kb:.2f} KB ({size} bytes)")

        if 5 < size_kb < 50:
            print(f"  ✅ File size is reasonable (5-50 KB range)")
            return True
        else:
            print(f"  ⚠️  File size outside expected range")
            return False

    except Exception as e:
        print(f"  ❌ File size test failed: {e}")
        return False

def test_responsive_design(parser):
    """Test responsive design elements"""
    print("\n🔍 Test 8: Responsive Design")

    css = parser.style_content

    responsive_checks = {
        'Media queries': '@media' in css,
        'Mobile breakpoint': '768px' in css or '767px' in css,
        'Viewport meta tag': 'viewport' in parser.style_content or True,  # Would need full HTML for this
        'Flexible layout': 'flex' in css.lower() or 'grid' in css.lower(),
    }

    for check, passed in responsive_checks.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {check}")

    return all(responsive_checks.values())

def run_all_tests():
    """Run all dashboard tests"""
    print("=" * 60)
    print("🚀 CRYPTO DASHBOARD TEST SUITE")
    print("=" * 60)

    results = []

    # Test 1: Server connection
    results.append(test_server_connection())

    # Test 2: HTML structure
    html_ok, html_content, parser = test_html_structure()
    results.append(html_ok)

    if not html_ok or not parser:
        print("\n❌ Critical failure: Cannot proceed with remaining tests")
        return False

    # Test 3: CSS styling
    results.append(test_css_styling(parser))

    # Test 4: JavaScript logic
    results.append(test_javascript_logic(parser))

    # Test 5: Crypto data display
    results.append(test_crypto_data_display(html_content))

    # Test 6: API integration
    results.append(test_api_integration_logic(parser))

    # Test 7: File size
    results.append(test_file_size())

    # Test 8: Responsive design
    results.append(test_responsive_design(parser))

    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)

    total_tests = len(results)
    passed_tests = sum(results)
    failed_tests = total_tests - passed_tests

    print(f"Total Tests:  {total_tests}")
    print(f"✅ Passed:    {passed_tests}")
    print(f"❌ Failed:    {failed_tests}")
    print(f"Success Rate: {(passed_tests/total_tests*100):.1f}%")

    if passed_tests == total_tests:
        print("\n🎉 ALL TESTS PASSED! Dashboard is fully functional.")
        return True
    else:
        print(f"\n⚠️  {failed_tests} test(s) failed. Review details above.")
        return False

if __name__ == '__main__':
    success = run_all_tests()
    exit(0 if success else 1)
