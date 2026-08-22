from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright
import json
import time
from pathlib import Path

CACHE_FILE = Path("ibm_stock_cache.json")
CACHE_TTL_SECONDS = 60


def format_value(value):
    """Format values for display, handling None gracefully."""
    if value is None:
        return "N/A"
    if isinstance(value, (float, int)):
        return f"{value:,.2f}"
    return str(value)


def load_cache():
    """Load recent cached stock data, if available."""
    if CACHE_FILE.exists() and time.time() - CACHE_FILE.stat().st_mtime <= CACHE_TTL_SECONDS:
        try:
            cache_data = json.loads(CACHE_FILE.read_text())
            return cache_data.get("data")
        except (json.JSONDecodeError, IOError):
            return None
    return None


def save_cache(data):
    """Save stock data for the next short-lived lookup."""
    try:
        CACHE_FILE.write_text(json.dumps({"timestamp": time.time(), "data": data}))
    except IOError as e:
        print(f"[WARN] Could not save cache: {e}")


def fetch_ibm_stock():
    """Fetch the latest IBM quote using Playwright."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            with page.expect_response(
                lambda response: "query1.finance.yahoo.com/v7/finance/quote" in response.url,
                timeout=30000,
            ) as response_info:
                page.goto(
                    "https://finance.yahoo.com/quote/IBM/",
                    wait_until="domcontentloaded",
                    timeout=30000,
                )

            payload = response_info.value.json()
            result = payload.get("quoteResponse", {}).get("result", [])
            ibm_data = next((item for item in result if item.get("symbol") == "IBM"), None)
            if ibm_data is None:
                raise RuntimeError("IBM quote not found in API response")

            return {
                "regularMarketPrice": ibm_data.get("regularMarketPrice"),
                "regularMarketChange": ibm_data.get("regularMarketChange"),
                "regularMarketChangePercent": ibm_data.get("regularMarketChangePercent"),
            }
        except PlaywrightError as error:
            page.screenshot(path="ibm_stock_error.png")
            raise RuntimeError(f"Yahoo Finance page request failed: {error}") from error
        finally:
            browser.close()


def print_stock_status(data):
    """Print a stock quote in the existing console format."""
    print("\n===============================")
    print("       IBM STOCK STATUS        ")
    print("===============================")
    print(f" Current Price : ${format_value(data.get('regularMarketPrice'))}")
    print(
        f" Movement      : {format_value(data.get('regularMarketChange'))} "
        f"({format_value(data.get('regularMarketChangePercent'))}%)"
    )
    print("===============================\n")


def check_ibm_stock():
    """Fetch and display the latest IBM stock data."""
    cached_data = load_cache()
    if cached_data:
        print_stock_status(cached_data)
        return

    try:
        data = fetch_ibm_stock()
        print_stock_status(data)
        save_cache(data)
    except RuntimeError as error:
        print(f"\n[!] Execution failed: {error}")


if __name__ == "__main__":
    check_ibm_stock()
