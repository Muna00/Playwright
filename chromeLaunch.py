from asyncio import wait_for

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page= browser.new_page()
    page.goto("https://www.saucedemo.com/")
    print(page.title())
    page.screenshot(path="demo.png")
    page.wait_for_timeout(1000)
    browser.close()

