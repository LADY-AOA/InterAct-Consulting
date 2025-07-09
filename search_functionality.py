from playwright.sync_api import sync_playwright, expect


class SearchPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_search(self, page):
        self.page.goto("https://www.interactconsulting.co.uk/")
        self.page.locator("#ctl00_inner_content_want_a_job_link").click()
        self.page.goto(
            "https://www.interactconsulting.co.uk/search-jobs-p17.aspx?k=&l=")

    def valid_search_for_keyword(self, page):
        self.page.goto(
            "https://www.interactconsulting.co.uk/search-jobs-p17.aspx?k=&l=")
        self.page.locator("input[name=\"k\"]").click()
        self.page.locator("input[name=\"k\"]").fill("Automation ")
        self.page.get_by_role("button", name="Submit").click()

    def valid_search_for_location(self, page):
        self.page.goto(
            "https://www.interactconsulting.co.uk/search-jobs-p17.aspx?k=&l=")
        self.page.locator("input[name=\"l\"]").click()
        self.page.locator("input[name=\"l\"]").fill("Manchester")
        self.page.get_by_role("button", name="Submit").click()
