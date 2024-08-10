import time

from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def refresh_page(self):
        """ Refreshes the page"""
        self._driver.refresh()

    def scroll_to_element(self, element):
        """ Scrolls to the desired element"""
        self._driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        time.sleep(0.5)
