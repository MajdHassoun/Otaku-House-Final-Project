import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser.base_page import BasePage


class PaymentSuccessPage(BasePage):
    PAYMENT_SUCCESS_MESSAGE = '//div[contains(text(), "Paid on")]'

    def __init__(self, driver):
        super().__init__(driver)

    def is_payment_success_message_displayed(self):
        element = WebDriverWait(self._driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, self.PAYMENT_SUCCESS_MESSAGE))
        )
        return element.is_displayed()
