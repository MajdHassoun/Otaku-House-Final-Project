from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser.base_page import BasePage


class ItemPage(BasePage):
    """ Initialize the locators"""
    ADD_TO_CART_BUTTON = '//button[text() = "Add to Cart"]'
    REVIEWS_COUNTER = '//span[contains(text(),"reviews")]'
    ITEM_SUMMARY = '//div[contains(text(),"Description:")]'
    ITEM_PRICE = '//div[contains(text(),"Price: ₹")]'
    ITEM_STATUS = '//div[@class="list-group-item"]//div[@class="row"]'
    QUANTITY_DROPBOX_BUTTON = '//div[@class="my-1 col-auto"]//select[@class="form-control"]//option[@value]'
    RATING_DROPBOX_PICK = '//select[@id="rating"]'
    REVIEW_INPUT = '//textarea[@id="comment"]'
    SUBMIT_REVIEW_BUTTON = '//div[@class="list-group-item"]//button[@type="submit"]'
    USER_ITEM_REVIEWS = '//div[@class="list-group-item"]//strong'
    SELECT_RATING_MESSAGE = '//div[text() ="Please Select a rating"]'
    GO_BACK_BUTTON = '//a[text()="Go Back"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_add_to_cart_button(self):
        """ Waits for the element to be clickable scroll to it and clicks it"""

        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.ADD_TO_CART_BUTTON)))
        self.scroll_to_element(element)
        element.click()

    def is_reviews_counter_displayed(self):
        """ Waits for the element to be present and returns True if it's displayed and False if it's not"""
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.REVIEWS_COUNTER))
        )
        return element.is_displayed()

    def is_item_summary_displayed(self):
        """ Waits for the element to be present and returns True if it's displayed and False if it's not"""
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.ITEM_SUMMARY))
        )
        return element.is_displayed()

    def is_item_price_displayed(self):
        """ Waits for the element to be present and returns True if it's displayed and False if it's not"""
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.ITEM_PRICE))
        )
        return element.is_displayed()

    def is_item_status_displayed(self):
        """ Waits for the element to be present and returns True if it's displayed and False if it's not"""
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.ITEM_STATUS))
        )
        return element[1].is_displayed()

    def set_quantity_dropdown_by_value(self, random_value):
        """ Waits for the element to be clickable, gets a random value  and clicks it"""

        elements = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.QUANTITY_DROPBOX_BUTTON)))

        elements[random_value].click()

    def set_rating_dropdown_by_value(self, random_value):
        """ Waits for the element to be clickable, gets a random value  and clicks it"""
        elements = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.RATING_DROPBOX_PICK)))

        elements[random_value].click()

    def enter_review_text(self, review_text):
        """ Waits for the element to be located, scrolls to it and send keys to it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.REVIEW_INPUT))
        )
        self.scroll_to_element(element)
        element.clear()
        element.send_keys(review_text)

    def click_submit_review_button(self):
        """ Waits for the element to be clickable, gets a random value  and clicks it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SUBMIT_REVIEW_BUTTON))
        )

        element.click()

    def get_last_rating_user_name(self):
        """ Waits for the element to be visible and returns it's text"""
        elements = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.USER_ITEM_REVIEWS))
        )
        return elements[-1].text

    def is_select_rating_message_displayed(self):
        """ Waits for the element to be visible and returns it's text"""
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.SELECT_RATING_MESSAGE))
        )
        return element.is_displayed()

    def click_go_back_button(self):
        """ Waits for the element to be clickable and clicks it"""
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.GO_BACK_BUTTON))
        )
        element.click()
