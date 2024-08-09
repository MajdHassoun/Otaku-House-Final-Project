import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils_infra import UtilsInfra
from logic.browser.home_page import HomePage
from logic.browser.item_page import ItemPage


class PageNavigateTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.browser.close_browser()

    def test_navigate_between_pages(self):
        """ checks if page navigates correctly"""
        # Act
        self.home_page.click_second_page_button()
        # Assert
        self.assertEqual(self.driver.current_url, self.config["second_page_url"])

    def test_navigate_click_and_check_item_price(self):
        """ checks if page navigates correctly and checks an item details(price) from the second page"""
        # Arrange
        self.home_page.click_second_page_button()
        # Act
        self.home_page.click_random_home_page_item(UtilsInfra.pick_random_number_one_to_eight())
        self.item_page = ItemPage(self.driver)
        # Assert
        self.assertTrue(self.item_page.is_item_price_displayed())
