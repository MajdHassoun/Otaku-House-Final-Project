import time
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.api.api_carrousel_items import ApiCarrouselItems
from logic.browser.home_page import HomePage
from logic.browser.item_page import ItemPage


class DynamicCarrouselTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.api_request = APIWrapper()
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.browser.close_browser()

    def test_dynamic_carrousel_item_change(self):
        # Arrange
        items_number = self.home_page.get_carrousel_items_number()
        for i in range(items_number + 1):
            # Act
            self.home_page.click_carrousel_next_button()
            # Assert
            self.assertTrue(self.home_page.is_carrousel_dynamic_item_displayed())

    def test_carrousel_item_click(self):
        # Arrange
        self.carrousel_items = ApiCarrouselItems(self.api_request)
        self.item_page = ItemPage(self.driver)
        num_of_clicks = 0
        # Act
        items_number = self.home_page.get_carrousel_items_number()
        for i in range(items_number + 1):
            self.home_page.click_carrousel_dynamic_item()
            current_url = self.driver.current_url
            item_id = self.carrousel_items.get_carrousel_items().data[i]["_id"]
            item_page_url = f'{self.config["item_page_url"]}{item_id}'
            num_of_clicks += 1
            self.item_page.click_go_back_button()
            for j in range(num_of_clicks):
                time.sleep(0.5)
                self.home_page.click_carrousel_next_button()
                time.sleep(0.5)
            # Assert
            print(item_id)
            self.assertEqual(current_url, item_page_url)
