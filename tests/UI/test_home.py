from playwright.sync_api import expect

from utils.data import LOGIN, PASSWORD


def test_login(auth_user, home_page):
    print(auth_user)
    home_page.open('https://www.demoblaze.com/index.html')
    home_page.open_login_modal()
    home_page.fill_username(LOGIN)
    home_page.fill_password(PASSWORD)
    home_page.click_login_btn()
    expect(home_page.get_name_of_user()).to_be_visible()
    cookie = home_page.page.context.cookies()