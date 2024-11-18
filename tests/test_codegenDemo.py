#import tests
import re
from playwright.sync_api import Page, expect


#@tests.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 14"]}


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("user")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.pause()
    page.locator("form").click()
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
