from infra.browser.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShippingDetailsPage(BasePage):
    ADDRESS_INPUT_BAR = '//input[@id="address"]'
    CITY_INPUT_BAR = '//input[@id="city"]'
    POSTAL_CODE_INPUT_BAR = '//input[@id="postalCode"]'
    COUNTRY_INPUT_BAR = '//input[@id="country"]'
    CONTINUE_BUTTON = '//button[text()="Continue"]'

    def __init__(self, driver):
        super().__init__(driver)

    def insert_address_data(self, data):
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ADDRESS_INPUT_BAR))
        )
        element.clear()
        element.send_keys(data)

    def insert_city_data(self, data):
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.CITY_INPUT_BAR))
        )
        element.clear()
        element.send_keys(data)

    def insert_postal_code_data(self, data):
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.POSTAL_CODE_INPUT_BAR))
        )
        element.clear()
        element.send_keys(data)

    def insert_country_data(self, data):
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.COUNTRY_INPUT_BAR))
        )
        element.clear()
        element.send_keys(data)

    def click_continue_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CONTINUE_BUTTON))
        )
        element.click()

    def fill_shipping_data_flow(self, address, city, postal_code, country):
        self.insert_address_data(address)
        self.insert_city_data(city)
        self.insert_postal_code_data(postal_code)
        self.insert_country_data(country)
        self.click_continue_button()


