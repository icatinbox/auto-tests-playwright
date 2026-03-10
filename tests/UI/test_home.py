from playwright.sync_api import expect

from tests.conftest import home_page_auth
from utils.data import BASE_URL

def test_visible_name_of_user(home_page_auth):
    home_page_auth.open(BASE_URL)
    expect(home_page_auth.get_name_of_user()).to_be_visible()
    expect(home_page_auth.get_logout_btn()).to_be_visible()

def test_visible_login_btn(home_page):
    home_page.open(BASE_URL)
    expect(home_page.get_log_in_btn()).to_be_visible()
    expect(home_page.get_sign_in_btn()).to_be_visible()
    expect(home_page.get_name_of_user()).not_to_be_visible()
    expect(home_page.get_logout_btn()).not_to_be_visible()

def test_logout(home_page_auth):
    home_page_auth.open(BASE_URL)
    expect(home_page_auth.get_name_of_user()).to_be_visible()
    expect(home_page_auth.get_logout_btn()).to_be_visible()
    home_page_auth.logout()
    expect(home_page_auth.get_log_in_btn()).to_be_visible()
    expect(home_page_auth.get_sign_in_btn()).to_be_visible()
    expect(home_page_auth.get_name_of_user()).not_to_be_visible()
    expect(home_page_auth.get_logout_btn()).not_to_be_visible()

def test_next_item_carousel(home_page_auth):
    home_page_auth.open(BASE_URL)
    items = home_page_auth.get_items_carousel()
    old_item_index = home_page_auth.get_active_item_carousel()
    old_indicator_index = home_page_auth.get_active_item_carousel_indicator()
    assert items.nth(old_item_index).is_visible()
    assert old_item_index == old_indicator_index

    home_page_auth.click_carousel_next_control_btn()

    expect(items.nth(old_item_index)).not_to_be_visible()

    new_item_index = home_page_auth.get_active_item_carousel()
    new_indicator_index = home_page_auth.get_active_item_carousel_indicator()
    assert items.nth(new_item_index).is_visible()

    assert new_item_index == new_indicator_index

def test_prev_item_carousel_indicator(home_page_auth):
    home_page_auth.open(BASE_URL)
    items = home_page_auth.get_items_carousel()
    old_item_index = home_page_auth.get_active_item_carousel()
    old_indicator_index = home_page_auth.get_active_item_carousel_indicator()
    assert items.nth(old_item_index).is_visible()
    assert old_item_index == old_indicator_index

    home_page_auth.click_carousel_next_control_btn()

    expect(items.nth(old_item_index)).not_to_be_visible()

    new_item_index = home_page_auth.get_active_item_carousel()
    new_indicator_index = home_page_auth.get_active_item_carousel_indicator()
    assert items.nth(new_item_index).is_visible()

    assert new_item_index == new_indicator_index
