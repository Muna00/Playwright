import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=False)
        page=await browser.new_page()
        await page.goto("https://www.whatismybrowser.com/")
        print(await page.title())
        page.wait_for_timeout(2000)
        browser.close()

asyncio.run(main())