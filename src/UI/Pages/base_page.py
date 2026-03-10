from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.context = page.context

    def open(self, url):
        self.page.goto(url)

    def add_auth_cookie(self, cookies):
        self.context.add_cookies(cookies)