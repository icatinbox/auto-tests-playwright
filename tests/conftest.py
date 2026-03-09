import pytest
from playwright.sync_api import Page
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
def auth_user(login_api):
    response = login_api.login(LOGIN, PASSWORD)
    assert response.status_code == 200, f'login failed: {response.text}'
    return login_api.get_token_from_response(response)

@pytest.fixture
def home_page(page: Page):
    return HomePage(page)