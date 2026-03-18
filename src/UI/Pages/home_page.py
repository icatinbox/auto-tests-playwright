from src.UI.Pages.base_page import BasePage
from playwright.sync_api import Page, expect

log_in_btn = '[id="login2"]'
sign_in_btn = '[id="signin2"]'
input_login = '[id="loginusername"]'
input_password = '[id="loginpassword"]'
user_of_name = '[id="nameofuser"]'
log_out_btn = '[id="logout2"]'

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open_login_modal(self):
        self.page.locator('[data-target="#logInModal"]').click()

    def fill_username(self, username):
        self.page.locator(input_login).fill(username)

    def fill_password(self, password):
        self.page.locator(input_password).fill(password)

    def click_login_btn(self):
        self.page.get_by_role('button', name='Log in').click()

    def get_name_of_user(self):
        return self.page.locator(user_of_name)

    def get_log_in_btn(self):
        return self.page.locator(log_in_btn)

    def get_sign_in_btn(self):
        return self.page.locator(sign_in_btn)

    def get_logout_btn(self):
        return self.page.locator(log_out_btn)

    def logout(self):
        self.get_logout_btn().click()

    def get_items_carousel(self):
        return self.page.locator(".carousel-inner .carousel-item")

    def get_items_carousel_indicator(self):
        return self.page.locator('li[data-target="#carouselExampleIndicators"]')

    def click_carousel_next_control_btn(self):
        return self.page.locator("#contcar .carousel-control-next").click()

    def click_carousel_previous_control_btn(self):
        return self.page.locator("#contcar .carousel-control-prev").click()

    def get_active_item_carousel(self):
        items = self.get_items_carousel()
        for i in range(items.count()):
            item = items.nth(i)
            if 'active' in item.get_attribute('class'):
                return i
        return None

    def get_active_item_carousel_indicator(self):
        items_indicator = self.get_items_carousel_indicator()
        for i in range(items_indicator.count()):
            item = items_indicator.nth(i)
            if 'active' in item.get_attribute('class'):
                return i
        return None

    def click_category_phones(self):
        return self.page.get_by_role('link', name="Phones").click()

    def click_category_laptops(self):
        return self.page.get_by_role('link', name="Laptops").click()

    def click_category_monitors(self):
        return self.page.get_by_role('link', name="Monitors").click()

    def get_title_products(self):
        titles = self.page.locator('.card-title a')
        expect(titles.first).to_be_visible()
        result = []
        for i in range(titles.count()):
            result.append(titles.nth(i).inner_text())
        return result

    def get_link_products(self):
        links = self.page.locator('.card-title a')
        expect(links.first).to_be_visible()
        result = []
        for i in range(links.count()):
            result.append(links.nth(i).get_attribute('href'))
        return result