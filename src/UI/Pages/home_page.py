from src.UI.Pages.base_page import BasePage
from playwright.sync_api import Page

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open_login_modal(self):
        self.page.locator('[data-target="#logInModal"]').click()

    def fill_username(self, username):
        self.page.locator('[id="loginusername"]').fill(username)

    def fill_password(self, password):
        self.page.locator('[id="loginpassword"]').fill(password)

    def click_login_btn(self):
        self.page.get_by_role('button', name='Log in').click()

    def get_name_of_user(self):
        return self.page.locator('[id="nameofuser"]')