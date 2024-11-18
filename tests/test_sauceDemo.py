from playwright.sync_api import Page, expect
import tests

def test_title(page: Page):
    page.goto("https://www.saucedemo.com/")
    assert page.title()=="Swag Labs"
    #expect(page.get_by_text("Swag Labs")).to_be_visible()
    page.wait_for_timeout(2000)

def test_inventory_title(page:Page):
    page.goto("/inventory.html")
    assert page.inner_text("h3")== "Epic sadface: You can only access '/inventory.html' when you are logged in."

    page.wait_for_timeout(2000)





