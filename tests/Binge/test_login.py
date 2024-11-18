import re
from playwright.sync_api import Page, expect,sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(no_viewport=True, permissions=["autoplay"])
    page = context.new_page()

def test_example(page: Page) -> None:
    page.goto("https://binge.buzz/")
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Welcome toAfghanistanÅland")).to_be_visible()
    expect(page.get_by_text("Welcome to")).to_be_visible()
    expect(page.locator(".BingeBox-root > img").first).to_be_visible()
    expect(page.locator(".BingeBox-root > div > div > div > div > div").first).to_be_visible()
    expect(page.get_by_label("Login with Email")).to_be_visible()
    expect(page.get_by_text("By logging in, you agree to")).to_be_visible()
    page.get_by_label("Login with Email").click()
    expect(page.locator(".BingeInputBase-root").first).to_be_visible()
    expect(page.locator("div:nth-child(2) > div > .BingeInputBase-root")).to_be_visible()
    expect(page.get_by_role("button", name="Submit")).to_be_visible()
    page.get_by_placeholder("Enter Email to Sign-in").click()
    page.get_by_placeholder("Enter Email to Sign-in").fill("testtmuna@gmail.com")
    page.locator("div:nth-child(2) > div > .BingeInputBase-root").click()
    page.get_by_placeholder("Enter password").fill("TestMuna@123")
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("banner").get_by_role("button").nth(1).click()
    expect(page.get_by_role("banner").get_by_role("button").nth(1)).to_be_visible()



