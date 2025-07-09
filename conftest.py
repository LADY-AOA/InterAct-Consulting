import pytest
from playwright.sync_api import sync_playwright
from search_functionality import SearchPage


@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=500)
        page = browser.new_page()
        search_page = SearchPage(page)
        search_page.navigate_to_search(page)
        yield page
        browser.close()
