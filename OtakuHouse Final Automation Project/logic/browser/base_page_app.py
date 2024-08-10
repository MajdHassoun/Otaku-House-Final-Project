from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser.base_page import BasePage


class BasePageApp(BasePage):
    """ Initialize the locators"""
    HEADER_HOME_BUTTON = '//a[@class="active navbar-brand"]'
    SEARCH_SUBMIT_BUTTON = '//button[@type="submit"]'
    SEARCH_INPUT_BAR = '//input[@name="q"]'
    CART_PAGE_BUTTON = '//a[@data-rb-event-key="#/cart"]'
    USER_OPTIONS_MENU = '//a[@id="username"]'
    PROFILE_MENU_OPTION_BUTTON = '//a[text()="Profile"]'

    def __init__(self, diver):
        super().__init__(diver)

    def insert_search_query_input(self, query):
        """ Waits for the element to be located and send keys to it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.SEARCH_INPUT_BAR)))
        element.clear()
        element.send_keys(query)

    def click_header_home_button(self):
        """ Waits for the element to be clickable and clicks it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.HEADER_HOME_BUTTON)))
        self.scroll_to_element(element)
        element.click()

    def click_submit_search_button(self):
        """ Waits for the element to be clickable and clicks it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_SUBMIT_BUTTON)))
        element.click()

    def click_cart_page_button(self):
        """ Waits for the element to be clickable and clicks it"""
        element = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.CART_PAGE_BUTTON))
        )
        element.click()

    def click_user_options_menu(self):
        """ Waits for the element to be clickable and clicks it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.USER_OPTIONS_MENU))
        )
        self.scroll_to_element(element)
        element.click()

    def click_profile_option(self):
        """ Waits for the element to be clickable and clicks it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.PROFILE_MENU_OPTION_BUTTON))
        )
        element.click()

    def navigate_to_user_profile(self):
        """ navigates to user's profile"""
        self.click_user_options_menu()
        self.click_profile_option()

    def search_flow(self, query):
        """ Preforms a search flow"""
        self.insert_search_query_input(query)
        self.click_submit_search_button()
