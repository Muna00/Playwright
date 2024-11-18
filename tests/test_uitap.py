from playwright.sync_api import sync_playwright, expect
import pytest




def test_main(page):
    page.goto("http://uitestingplayground.com/")
    assert page.title()=="UI Test Automation Playground"

def test_dynamic(page):
    page.goto("http://uitestingplayground.com/")
    page.click('text=Dynamic ID')
    assert page.title()=="Dynamic ID"

def test_sample_app(page):
    page.goto("http://uitestingplayground.com/")
    page.click('text=Sample App')
    assert page.title() == "Sample App"
    page.fill('[placeholder="User Name"]','d')
    page.fill('[placeholder="********"]','pwd')
    page.click('text=Log In')
    expect(page.locator("label")).to_have_text("Welcome, d!")

