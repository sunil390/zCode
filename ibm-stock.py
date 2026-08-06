from playwright.sync_api import sync_playwright


def format_value(value):
    if value is None:
        return "N/A"
    if isinstance(value, (float, int)):
        return f"{value:,.2f}"
    return str(value)


def check_ibm_stock():
    with sync_playwright() as p:
        print("Launching disposable headless browser...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            print("Navigating to Yahoo Finance (IBM)...")
            with page.expect_response(lambda response: "query1.finance.yahoo.com/v7/finance/quote" in response.url) as response_info:
                page.goto("https://finance.yahoo.com/quote/IBM/", wait_until="domcontentloaded", timeout=30000)
            response = response_info.value
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

        except Exception as e:
            print(f"\n[!] Execution failed: {e}")
            page.screenshot(path="ibm_stock_error.png")
            print("Debug artifact saved: ibm_stock_error.png. Please inspect the workspace.")

        finally:
            browser.close()


if __name__ == "__main__":
    check_ibm_stock()
