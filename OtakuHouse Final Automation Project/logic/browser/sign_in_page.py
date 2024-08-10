from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser.base_page import BasePage


class SignInPage(BasePage):
    """ Initialize the locators"""
    EMAIL_INPUT = '//input[@placeholder="Enter Email"]'
    PASSWORD_INPUT = '//input[@placeholder="Enter Password"]'
    SUBMIT_SIGNIN_BUTTON = '//button[text()="Sign In"]'
    USERNAME_LOGGED_IN = '//a[@id="username"]'
    INVALID_LOGIN_MESSAGE = '//div[text()="No active account found with the given credentials"]'

    def __init__(self, driver):
        super().__init__(driver)

    def insert_email_input(self, email):
        """ Waits for the element to be located and send keys to it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.EMAIL_INPUT)))
        element.clear()
        element.send_keys(email)

    def insert_password_input(self, password):
        """ Waits for the element to be located and send keys to it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.PASSWORD_INPUT)))
        element.clear()
        element.send_keys(password)

    def click_submit_login_button(self):
        """ Waits for the element to be clickable and clicks it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SUBMIT_SIGNIN_BUTTON)))
        element.click()

    def is_username_displayed(self):
        """ Waits for the element to be visible and returns True if it's displayed and False if it's not"""
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.USERNAME_LOGGED_IN))
        )

        return element.is_displayed()

    def is_invalid_message_displayed(self):
        """ Waits for the element to be visible and returns True if it's displayed and False if it's not"""
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.INVALID_LOGIN_MESSAGE))
        )
        return element.is_displayed()

    def sign_in_flow(self, email, password):
        """ preforms sign in process flow"""
        self.insert_email_input(email)
        self.insert_password_input(password)
        self.click_submit_login_button()
