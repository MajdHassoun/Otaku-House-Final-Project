from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser.base_page import BasePage


class BasePageApp(BasePage):
    # HEADER_HOME_BUTTON = '//a[@class="active navbar-brand"]'
    SEARCH_SUBMIT_BUTTON = '//button[@type="submit"]'
    SEARCH_INPUT_BAR = '//input[@name="q"]'
    CART_PAGE_BUTTON = '//a[@data-rb-event-key="#/cart"]'

    def __init__(self, diver):
        super().__init__(diver)

    def insert_search_query_input(self, query):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.SEARCH_INPUT_BAR)))
        element.clear()
        element.send_keys(query)

    def click_submit_search_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_SUBMIT_BUTTON)))
        element.click()

    def click_cart_page_button(self):
        element = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.CART_PAGE_BUTTON))
        )
        element.click()

    def search_flow(self, query):
        self.insert_search_query_input(query)
        self.click_submit_search_button()
