import time


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def refresh_page(self):
        self._driver.refresh()

    def scroll_to_element(self, element):
        self._driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        time.sleep(0.5)
