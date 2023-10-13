import pytest
from fixtures.setup import browser
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from data.messages import LOGIN_ERROR_MESSAGE
from data.messages import LOCKED_OUT_MESSAGE
from config.config import *

positive_test_data = [
    (USERNAME_STANDARD, PASSWORD),
    (USERNAME_PROBLEM, PASSWORD),
    (USERNAME_PERFORMANCE_GLITCH, PASSWORD),
    (USERNAME_ERROR, PASSWORD),
]
locked_test_data = [
    (USERNAME_LOCKED_OUT, PASSWORD),
]
negative_test_data = [
    (USERNAME_STANDARD, INCORRECT_PASSWORD),
    (USERNAME_PROBLEM, INCORRECT_PASSWORD),
    (USERNAME_PERFORMANCE_GLITCH, INCORRECT_PASSWORD),
    (USERNAME_ERROR, INCORRECT_PASSWORD),
    (USERNAME_LOCKED_OUT, INCORRECT_PASSWORD),
]


@pytest.mark.parametrize("username, password", positive_test_data)
def test_successful_login_with_valid_credentials(username, password, browser):
    login_page = LoginPage(browser)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    inventory_page = InventoryPage(browser)
    assert inventory_page.are_all_elements_displayed(), "One or more elements are not displayed after login attempt"
    assert browser.current_url == INVENTORY_URL


@pytest.mark.parametrize("username, password", locked_test_data)
def test_negative_login_with_locked_out_credentials(username, password, browser):
    login_page = LoginPage(browser)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()
    login_page.assert_error_message_displayed(LOCKED_OUT_MESSAGE)
    assert browser.current_url == BASE_URL


@pytest.mark.parametrize("username, password", negative_test_data)
def test_negative_login_with_invalid_credentials(username, password, browser):
    login_page = LoginPage(browser)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()
    login_page.assert_error_message_displayed(LOGIN_ERROR_MESSAGE)
    assert browser.current_url == BASE_URL
