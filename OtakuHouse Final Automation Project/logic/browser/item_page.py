from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser.base_page import BasePage
from selenium.webdriver.support.ui import Select


class ItemPage(BasePage):
    ADD_TO_CART_BUTTON = '//button[text() = "Add to Cart"]'
    REVIEWS_COUNTER = '//span[contains(text(),"reviews")]'
    ITEM_DESCRIPTION = '//div[contains(text(),"Description:")]'
    ITEM_PRICE = '//div[contains(text(),"Price: ₹")]'
    ITEM_STATUS = '//div[@class="list-group-item"]//div[@class="row"]'
    QUANTITY_DROPBOX_BUTTON = '//div[@class="my-1 col-auto"]//select[@class="form-control"]//option[@value]'
    RATING_DROPBOX_PICK = '//select[@id="rating"]'
    REVIEW_INPUT = '//textarea[@id="comment"]'
    SUBMIT_REVIEW_BUTTON = '//button[text()="Submit"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_add_to_cart_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.ADD_TO_CART_BUTTON)))
        self.scroll_to_element(element)
        element.click()

    def is_reviews_counter_displayed(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.REVIEWS_COUNTER))
        )
        return element.is_displayed()

    def is_item_description_displayed(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.ITEM_DESCRIPTION))
        )
        return element.is_displayed()

    def is_item_price_displayed(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.ITEM_PRICE))
        )
        return element.is_displayed()

    def is_item_status_displayed(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.ITEM_STATUS))
        )
        return element[1].is_displayed()

    def set_quantity_dropdown_by_value(self, random_value):
        elements = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.QUANTITY_DROPBOX_BUTTON)))

        elements[random_value].click()

    def set_rating_dropdown_by_value(self, random_value):
        elements = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.RATING_DROPBOX_PICK)))

        elements[random_value].click()

    def enter_review_text(self, review_text):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.REVIEW_INPUT))
        )
        self.scroll_to_element(element)
        element.clear()
        element.send_keys(review_text)

    def click_submit_review_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SUBMIT_REVIEW_BUTTON))
        )
        self.scroll_to_element(element)
        element.click()
