import pytest
from fixtures.setup import browser
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from config.config import *

positive_test_data = [
    (USERNAME_STANDARD, PASSWORD),
    (USERNAME_PROBLEM, PASSWORD),
    (USERNAME_PERFORMANCE_GLITCH, PASSWORD),
    (USERNAME_ERROR, PASSWORD),
]


@pytest.mark.parametrize("username, password", positive_test_data)
def test_successful_logout(username, password, browser):
    login_page = LoginPage(browser)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    inventory_page = InventoryPage(browser)
    assert inventory_page.are_all_elements_displayed(), "One or more elements are not displayed after login attempt"

    inventory_page.click_logout_button()
    assert login_page.are_all_elements_displayed(), "One or more elements are not displayed after logout"
    assert browser.current_url == BASE_URL
