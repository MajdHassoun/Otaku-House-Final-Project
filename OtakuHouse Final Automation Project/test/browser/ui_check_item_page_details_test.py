import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils_infra import UtilsInfra
from logic.browser.home_page import HomePage
from logic.browser.item_page import ItemPage


class UiCheckItemPageDetailsTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)
        self.item_page = ItemPage(self.driver)

    def test_item_page_price(self):
        """ checks if item price is displayed"""
        # Act
        self.home_page.click_random_home_page_item(UtilsInfra.pick_random_number_one_to_eight())
        # Assert
        self.assertTrue(self.item_page.is_item_price_displayed())

    def test_item_page_summary(self):
        """ checks if item summary is displayed"""
        # Act
        self.home_page.click_random_home_page_item(UtilsInfra.pick_random_number_one_to_eight())
        # Assert
        self.assertTrue(self.item_page.is_item_summary_displayed())

    def test_item_page_status(self):
        """ checks if item status is displayed"""
        # Act
        self.home_page.click_random_home_page_item(UtilsInfra.pick_random_number_one_to_eight())
        # Assert
        self.assertTrue(self.item_page.is_item_status_displayed())

    def test_item_page_reviews_counter(self):
        """ checks if item reviews counter is displayed"""
        # Act
        self.home_page.click_random_home_page_item(UtilsInfra.pick_random_number_one_to_eight())
        # Assert
        self.assertTrue(self.item_page.is_reviews_counter_displayed())
