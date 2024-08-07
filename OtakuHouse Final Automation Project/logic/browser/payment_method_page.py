from infra.browser.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaymentMethodPage(BasePage):
    CONTINUE_BUTTON = '//button[text()="Continue"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_continue(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CONTINUE_BUTTON))
        )
        element.click()

