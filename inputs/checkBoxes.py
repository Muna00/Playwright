from lib2to3.fixes.fix_input import context

from playwright.sync_api import sync_playwright,expect



with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://demoqa.com/checkbox")

    expect(page.locator("#tree-node span").nth(1)).to_be_visible()
    page.locator("#tree-node").get_by_role("img").nth(3).click()
    expect(page.locator("#result")).to_be_visible()

