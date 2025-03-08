from playwright.sync_api import sync_playwright

def test_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Set headless=True for CI
        page = browser.new_page()
        page.goto("http://localhost:5173")

        assert "Welcome" in page.title()
        assert page.locator("text=Welcome to my webpage").is_visible()

        browser.close()