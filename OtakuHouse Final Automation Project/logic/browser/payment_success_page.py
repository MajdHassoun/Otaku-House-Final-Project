from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser.base_page import BasePage


class PaymentSuccessPage(BasePage):
    PAYMENT_SUCCESS_MESSAGE = '//div[@class="fade alert alert-success show"]'

    def __init__(self, driver):
        super().__init__(driver)


def is_payment_success_message_displayed(self):
    element = WebDriverWait(self._driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, self.PAYMENT_SUCCESS_MESSAGE))
    )
    return element.is_displayed()
