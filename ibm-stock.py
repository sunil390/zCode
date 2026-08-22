from playwright.sync_api import sync_playwright
import json
import time
from pathlib import Path


def format_value(value):
    """Format values for display, handling None gracefully."""
    if value is None:
        return "N/A"
    if isinstance(value, (float, int)):
        return f"{value:,.2f}"
    return str(value)


def load_cache():
    """Load cached stock data if available."""
    if CACHE_FILE.exists():
        try:
            cache_data = json.loads(CACHE_FILE.read_text())
            print(f"[INFO] Loaded cached data from {CACHE_FILE.name}")
            return cache_data.get("data")
        except (json.JSONDecodeError, IOError):
            pass
    return None


def save_cache(data):
    """Save stock data to cache file."""
    try:
        CACHE_FILE.write_text(json.dumps({"timestamp": time.time(), "data": data}))
        print(f"[INFO] Cached data saved to {CACHE_FILE.name}")
    except IOError as e:
        print(f"[WARN] Could not save cache: {e}")


def check_ibm_stock():
    """Fetch IBM stock data with performance optimizations."""
    # Try to load cached data first
    cached_data = load_cache()
    if cached_data:
        print("\n===============================")
        print("       IBM STOCK STATUS        ")
        print("===============================")
        price = cached_data.get("regularMarketPrice")
        change = cached_data.get("regularMarketChange")
        percent = cached_data.get("regularMarketChangePercent")
        
        print(f" Current Price : ${format_value(price)}")
        print(f" Movement      : {format_value(change)} ({format_value(percent)}%)")
        print("===============================\n")
        return
    
    # Use optimized browser configuration
    with sync_playwright() as p:
        print("Launching optimized headless browser...")
        browser = p.chromium.launch(
            headless=True,
            args=[
                '--disable-gpu',
                '--no-sandbox',
                '--window-size=1920,1080'
            ]
        )
        page = browser.new_page()

        try:
            print("Navigating to Yahoo Finance (IBM)...")
            # Use networkidle for more reliable waiting with reduced timeout
            page.goto("https://finance.yahoo.com/quote/IBM/", wait_until="networkidle", timeout=15000)
            
            # Wait a bit for dynamic content to load
            time.sleep(2)
            
            response = page.response()
            payload = response.json()

            result = payload.get("quoteResponse", {}).get("result", [])
            ibm_data = next((item for item in result if item.get("symbol") == "IBM"), None)

            if ibm_data is None:
                raise RuntimeError("IBM quote not found in API response")

            price = ibm_data.get("regularMarketPrice")
            change = ibm_data.get("regularMarketChange")
            percent = ibm_data.get("regularMarketChangePercent")

            print("\n===============================")
            print("       IBM STOCK STATUS        ")
            print("===============================")
            print(f" Current Price : ${format_value(price)}")
            print(f" Movement      : {format_value(change)} ({format_value(percent)}%)")
            print("===============================\n")

            page.screenshot(path="ibm_stock_success.png")
            print("Artifact saved: ibm_stock_success.png")
            
            # Save to cache for future runs
            save_cache({
                "regularMarketPrice": price,
                "regularMarketChange": change,
                "regularMarketChangePercent": percent
            })

        except Exception as e:
            print(f"\n[!] Execution failed: {e}")
            page.screenshot(path="ibm_stock_error.png")
            print("Debug artifact saved: ibm_stock_error.png. Please inspect the workspace.")

        finally:
            browser.close()


if __name__ == "__main__":
    check_ibm_stock()
