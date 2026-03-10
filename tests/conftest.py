import pytest
from playwright._impl._api_structures import SetCookieParam
from playwright.sync_api import Page, expect

from src.API.api_client import ClientApi
from src.API.login_api import LoginApi
from src.UI.Pages.home_page import HomePage
from utils.data import LOGIN, PASSWORD, BASE_URL, BASE_URL_API

@pytest.fixture
def client_api(request):
   return ClientApi(BASE_URL_API)

@pytest.fixture
def login_api(client_api):
    return LoginApi(client_api)

@pytest.fixture
def auth_page(login_api, page: Page):
    response = login_api.login(LOGIN, PASSWORD)
    assert response.status_code == 200, f'login failed: {response.text}'
    token = login_api.get_token_from_response(response)
    cookie: SetCookieParam = {'name': 'tokenp_', 'value': token, 'url': BASE_URL}
    page.context.add_cookies([cookie])
    return page

@pytest.fixture
def home_page(page: Page):
    return HomePage(page)

@pytest.fixture
def home_page_auth(auth_page):
    return HomePage(auth_page)

@pytest.fixture
def auth_user_ui(home_page):
    home_page.open('https://www.demoblaze.com/index.html')
    home_page.open_login_modal()
    home_page.fill_username(LOGIN)
    home_page.fill_password(PASSWORD)
    home_page.click_login_btn()
    expect(home_page.get_name_of_user()).to_be_visible()
    return home_page