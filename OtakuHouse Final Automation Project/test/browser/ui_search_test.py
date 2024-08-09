import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils_infra import UtilsInfra
from logic.browser.home_page import HomePage
from logic.browser.search_result_page import SearchResultPage


class UiSearchTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)
        self.result_page = SearchResultPage(self.driver)

    def test_search_for_item(self):
        """ checks search functionality with UI"""
        # Arrange
        self.home_page.insert_search_query_input(self.config["search_query"])
        # Act
        self.home_page.click_submit_search_button()
        # Assert
        self.assertIn(self.config["search_query"], self.result_page.get_result_title())

    def test_negative_search_for_item(self):
        """ checks negative search functionality with UI"""
        # Arrange
        self.home_page.insert_search_query_input(UtilsInfra.generate_random_string(5))
        # Act
        self.home_page.click_submit_search_button()
        # Assert
        self.assertEqual(0, self.result_page.get_empty_result())
