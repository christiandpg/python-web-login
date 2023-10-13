from helpers.selenium_helpers import SeleniumHelpers


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelpers(driver)
        self.menu_id = "react-burger-menu-btn"
        self.cart_icon_css = "#shopping_cart_container a"
        self.products_header_css = ".header_secondary_container span"
        self.logout_css = ".bm-menu-wrap #logout_sidebar_link"

    def is_menu_icon_displayed(self):
        try:
            menu_button = self.helper.wait_for_element_by_id(self.menu_id)
            return menu_button.is_displayed()
        except Exception:
            return False

    def is_shopping_cart_icon_displayed(self):
        try:
            cart_icon = self.helper.wait_for_element_by_css(self.cart_icon_css)
            return cart_icon.is_displayed()
        except Exception:
            return False

    def are_all_elements_displayed(self):
        return self.is_menu_icon_displayed() and self.is_shopping_cart_icon_displayed()

    def click_hamburger_menu_button(self):
        menu_button = self.helper.wait_for_element_clickable_by_id(self.menu_id)
        menu_button.click()

    def click_logout_button(self):
        self.click_hamburger_menu_button()
        logout_button = self.helper.wait_for_element_clickable_by_css(self.logout_css)
        logout_button.click()