import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://total-qa.com/checkbox-example/")
    expect(page.get_by_text("SELENIUM QTP LOAD RUNNER")).to_be_visible()
    page.get_by_role("checkbox").first.check()
    expect(page.get_by_role("checkbox").first).to_be_visible()
    page.get_by_role("checkbox").nth(2).check()
    expect(page.get_by_role("checkbox").nth(2)).to_be_visible()
    page.get_by_role("checkbox").nth(2).uncheck()
    expect(page.get_by_role("checkbox").nth(2)).to_be_visible()

