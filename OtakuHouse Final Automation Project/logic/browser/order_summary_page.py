import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser.base_page import BasePage


class OrderSummaryPage(BasePage):
    """ Initialize the locators"""
    IFRAME = '//iframe[@allowtransparency="true"]'
    CREDIT_CARD_BUTTON = '//div[@aria-label="כרטיס אשראי"]'
    CARD_NUMBER = '//input[@id="credit-card-number"]'
    CARD_DATE = '//input[@id="expiry-date"]'
    CARD_CVV = '//input[@id="credit-card-security"]'
    COSTUMER_NAME = '//input[@id="billingAddress.givenName"]'
    COSTUMER_FAMILY = '//input[@id="billingAddress.familyName"]'
    COSTUMER_STREET = '//input[@id="billingAddress.line1"]'
    COSTUMER_CITY = '//input[@id="billingAddress.city"]'
    COSTUMER_ZIPCODE = '//input[@id="billingAddress.postcode"]'
    COSTUMER_PHONE = '//input[@id="phone"]'
    COSTUMER_EMAIL = '//input[@id="email"]'
    PAY_NOW_BUTTON = '//button[@id="submit-button"]'

    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_iframe(self):
        # Wait for the iframe to be present and switch to it
        iframe_element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.IFRAME))
        )
        self._driver.switch_to.frame(iframe_element)

    def switch_to_default_content(self):
        # Switch back to the default content
        self._driver.switch_to.default_content()

    def click_credit_card_button(self):
        """ switches to iframe content, waits for the element and clicks it """
        self.switch_to_iframe()

        credit_card_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.CREDIT_CARD_BUTTON))
        )
        credit_card_button.click()

    def enter_card_number(self, card_number):
        """ switches to iframe content, waits for the element and sends keys to it """
        self.switch_to_iframe()

        credit_card_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.CARD_NUMBER))
        )
        credit_card_button.clear()
        credit_card_button.send_keys(card_number)

    def enter_card_date(self, card_date):
        """ switches to iframe content, waits for the element and sends keys to it """
        card_date_field = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CARD_DATE))
        )
        card_date_field.clear()
        card_date_field.send_keys(card_date)

    def enter_card_cvv(self, card_cvv):
        """ switches to iframe content, waits for the element and sends keys to it """
        card_cvv_field = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CARD_CVV))
        )
        card_cvv_field.clear()
        card_cvv_field.send_keys(card_cvv)

    def enter_customer_name(self, name):
        """ switches to iframe content, waits for the element and sends keys to it """
        customer_name_field = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_NAME))
        )
        customer_name_field.clear()
        customer_name_field.send_keys(name)

    def enter_customer_family(self, family):
        """ switches to iframe content, waits for the element and sends keys to it """
        customer_family_field = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_FAMILY))
        )
        customer_family_field.clear()
        customer_family_field.send_keys(family)

    def enter_customer_street(self, street):
        """ switches to iframe content, waits for the element and sends keys to it """
        customer_street_field = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_STREET))
        )
        customer_street_field.clear()
        customer_street_field.send_keys(street)

    def enter_customer_city(self, city):
        """ switches to iframe content, waits for the element and sends keys to it """
        customer_city_field = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_CITY))
        )
        customer_city_field.clear()
        customer_city_field.send_keys(city)

    def enter_customer_zipcode(self, zipcode):
        """ switches to iframe content, waits for the element and sends keys to it """
        customer_zipcode_field = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_ZIPCODE))
        )
        customer_zipcode_field.clear()
        customer_zipcode_field.send_keys(zipcode)

    def enter_customer_phone(self, phone):
        """ switches to iframe content, waits for the element and sends keys to it """
        customer_phone_field = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_PHONE))
        )
        customer_phone_field.clear()
        customer_phone_field.send_keys(phone)

    def enter_customer_email(self, email):
        """ switches to iframe content, waits for the element and sends keys to it """
        customer_email_field = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_EMAIL))
        )
        customer_email_field.clear()
        customer_email_field.send_keys(email)

    def click_pay_now_button(self):
        """ switches to iframe content, waits for the element, scrolls to it, clicks it
          and returns to default content"""
        pay_now_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PAY_NOW_BUTTON))
        )
        time.sleep(3)
        self.scroll_to_element(pay_now_button)
        pay_now_button.click()
        self.switch_to_default_content()

    def insert_card_details_flow(self, card_number, date, cvv, name, family, street_name, city, zipcode, phone, email):
        """ preforms a card details insertion process"""
        self.enter_card_number(card_number)
        self.enter_card_date(date)
        self.enter_card_cvv(cvv)
        self.enter_customer_name(name)
        self.enter_customer_family(family)
        self.enter_customer_street(street_name)
        self.enter_customer_city(city)
        self.enter_customer_zipcode(zipcode)
        self.enter_customer_phone(phone)
        self.enter_customer_email(email)
