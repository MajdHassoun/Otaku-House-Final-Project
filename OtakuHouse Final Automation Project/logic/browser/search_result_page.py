from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser.base_page import BasePage


class SearchResultPage(BasePage):
    """ Initialize the locators"""
    RESULT = '//div[@class="card-title"]//strong'
    EMPTY_RESULTS_PAGE = '//main[@class="py-3"]//div[@class="row"]'
    RESULT_ELEMENT = '//div[@class="col-xl-3 col-lg-4 col-md-6 col-sm-12"]'

    def __init__(self, driver):
        super().__init__(driver)

    def get_result_title(self):
        """ Waits for the element to be visible and returns it's text"""
        element = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.RESULT)))

        return element.text

    def get_empty_result(self):
        """ Waits for element to be present and returns 0 if there is no attribute """
        elements = WebDriverWait(self._driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.EMPTY_RESULTS_PAGE)))
        try:
            elements.__getattribute__(self.RESULT_ELEMENT)
        except:
            return 0
