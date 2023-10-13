from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumHelpers:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_by_id(self, element_id, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, element_id)))

    def wait_for_element_by_css(self, element_id, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_id)))

    def wait_for_element_clickable_by_id(self, element_id, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.ID, element_id)))

    def wait_for_element_clickable_by_css(self, element_id, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_id)))