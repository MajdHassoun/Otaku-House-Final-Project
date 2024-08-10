from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser.base_page import BasePage


class PlaceOrderPage(BasePage):
    """ Initialize the locators"""
    PLACE_ORDER_BUTTON = '//button[text()="Place Order"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_place_order_button(self):
        """ Waits for the element to be clickable and clicks it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PLACE_ORDER_BUTTON)))
        element.click()
