from infra.browser.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    ITEM_NAME_CART_PAGE = '//div[@m="3"]'
    PROCEED_TO_CHECK_IN_BUTTON = '//button[text()="Proceed To Checkout"]'
    REMOVE_ITEM_BUTTON = '//button[@class="btn btn-light"]'
    ITEM_QUANTITY = '//select[@class="form-control"]//option[@value]'

    def __init__(self, driver):
        super().__init__(driver)

    def item_name_in_cart(self):
        element = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.ITEM_NAME_CART_PAGE))
        )
        return element.text

    def click_proceed_to_check_in_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PROCEED_TO_CHECK_IN_BUTTON)))
        element.click()

    def click_remove_item_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.REMOVE_ITEM_BUTTON)))
        element.click()

    def get_item_quantity_from_cart(self, random):
        elements = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.ITEM_QUANTITY))
        )
        element = elements[random-1]
        return element.text
