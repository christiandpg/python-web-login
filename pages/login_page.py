from helpers.selenium_helpers import SeleniumHelpers


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelpers(driver)
        self.username_id = "user-name"
        self.password_id = "password"
        self.login_button_id = "login-button"
        self.error_message_css = ".error-message-container h3[data-test='error']"

    def enter_username(self, username):
        username_input = self.helper.wait_for_element_by_id(self.username_id)
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.helper.wait_for_element_by_id(self.password_id)
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.helper.wait_for_element_by_id(self.login_button_id)
        login_button.click()

    def is_error_message_displayed(self, message):
        try:
            error_message = self.helper.wait_for_element_by_css(self.error_message_css)
            return error_message.text == message
        except Exception:
            return False

    def assert_error_message_displayed(self, expected_message):
        assert self.is_error_message_displayed(expected_message), f"Expected error message: '{expected_message}'"

    def is_username_input_displayed(self):
        try:
            username_input = self.helper.wait_for_element_by_id(self.username_id)
            return username_input.is_displayed()
        except Exception:
            return False

    def is_password_input_displayed(self):
        try:
            password_input = self.helper.wait_for_element_by_id(self.password_id)
            return password_input.is_displayed()
        except Exception:
            return False

    def is_login_button_displayed(self):
        try:
            login_button = self.helper.wait_for_element_by_id(self.login_button_id)
            return login_button.is_displayed()
        except Exception:
            return False

    def are_all_elements_displayed(self):
        return self.is_username_input_displayed() and self.is_password_input_displayed() and self.is_login_button_displayed()