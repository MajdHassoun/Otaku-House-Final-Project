import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser.base_page import BasePage


class HomePage(BasePage):
    """ Initialize the locators"""
    LOGIN_BUTTON = '//a[@data-rb-event-key="#/login"]'
    CART_BUTTON_HOME_PAGE = '//a[@data-rb-event-key="#/cart"]'
    SEARCH_SUBMIT_BUTTON = '//button[@type="submit"]'
    SEARCH_INPUT_BAR = '//input[@name="q"]'
    CART_PAGE_BUTTON = '//a[@data-rb-event-key="#/cart"]'
    ITEMS_FROM_HOME_PAGE = '//div[@class="card-title"]//strong'
    PAGE_2_BUTTON = '//a[text() ="2"]'
    CARROUSEL_NEXT_BUTTON = '//span[@class="carousel-control-next-icon"]'
    ACTIVE_CARROUSEL_ITEM = '//div[@class ="active carousel-item"]'
    CARROUSEL_ITEMS = '//div[@class="carousel-item"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_button(self):
        """ Waits for the element to be clickable and clicks it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON)))
        element.click()

    def click_cart_button(self):
        """ Waits for the element to be clickable and clicks it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CART_BUTTON_HOME_PAGE)))
        element.click()

    def insert_search_query_input(self, query):
        """ Waits for the element to be located and send keys to it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.SEARCH_INPUT_BAR)))
        element.clear()
        element.send_keys(query)

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

    def click_random_home_page_item(self, index):
        """ Gets the index of the element and waits for it to be clickable and clicks it"""
        elements = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.ITEMS_FROM_HOME_PAGE))
        )
        element = elements[index]
        self.scroll_to_element(element)
        element_text = element.text
        element.click()
        return element_text

    def get_random_home_page_item_name(self, index):
        """ Waits for the element to be visible and returns it's name"""
        elements = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.ITEMS_FROM_HOME_PAGE))
        )
        self.scroll_to_element(elements[index])
        return elements[index].text

    def click_second_page_button(self):
        """ Waits for the element to be clickable scroll to it and clicks it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PAGE_2_BUTTON)))
        self.scroll_to_element(element)
        element.click()

    def click_carrousel_next_button(self):
        """ Waits for the element to be clickable and clicks it"""
        time.sleep(1)
        element = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.CARROUSEL_NEXT_BUTTON))
        )
        element.click()
        time.sleep(1)

    def click_carrousel_dynamic_item(self):
        """ Waits for the element to be clickable and clicks it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ACTIVE_CARROUSEL_ITEM)))
        time.sleep(0.5)
        element.click()

    def is_carrousel_dynamic_item_displayed(self):
        """ Waits for the element to be clickable and returns True if it's displayed and False if it's not"""
        element = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.ACTIVE_CARROUSEL_ITEM))
        )
        return element.is_displayed()

    def get_carrousel_items_number(self):
        """ Waits for all the elements to be present and returns their number"""
        elements = WebDriverWait(self._driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.CARROUSEL_ITEMS))
        )
        if len(elements) == 0:
            return 1
        else:
            return len(elements)
