import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils_infra import UtilsInfra
from logic.browser.cart_page import CartPage
from logic.browser.home_page import HomePage
from logic.browser.item_page import ItemPage


class LoginAddItemTest(unittest.TestCase):

    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.browser.close_browser()

    def test_add_item(self):
        """ Adds item to cart and checks if it was added"""
        # Arrange
        random_number = UtilsInfra.pick_random_number_one_to_eight()
        home_page_item_name = self.home_page.get_random_home_page_item_name(random_number)
        self.home_page.click_random_home_page_item(random_number)
        self.item_page = ItemPage(self.driver)
        # Act
        self.item_page.click_add_to_cart_button()
        self.cart_page = CartPage(self.driver)
        # Assert
        self.assertEqual(self.cart_page.item_name_in_cart(), home_page_item_name)

    def test_add_item_with_quantity(self):
        """ Adds item to cart and checks if it was added with quantity"""
        # Arrange
        self.home_page.click_random_home_page_item(UtilsInfra.pick_random_number_one_to_eight())
        self.item_page = ItemPage(self.driver)
        # Act
        random_quantity = UtilsInfra.pick_random_number_one_to_ten()
        self.item_page.set_quantity_dropdown_by_value(random_quantity)
        self.item_page.click_add_to_cart_button()
        self.home_page.click_cart_button()
        self.cart_page = CartPage(self.driver)
        # Assert
        self.assertEqual(random_quantity, int(self.cart_page.get_item_quantity_from_cart(random_quantity)))

    def test_remove_item_from_cart(self):
        """ Adds item to cart and deletes it and checks if it was deleted"""
        # Arrange
        random_number = UtilsInfra.pick_random_number_one_to_eight()
        self.home_page.click_random_home_page_item(random_number)
        self.item_page = ItemPage(self.driver)
        self.item_page.click_add_to_cart_button()
        self.cart_page = CartPage(self.driver)
        # Act
        self.cart_page.click_remove_item_button()
        # Assert
        self.assertTrue(self.cart_page.is_cart_empty_message_displayed)
