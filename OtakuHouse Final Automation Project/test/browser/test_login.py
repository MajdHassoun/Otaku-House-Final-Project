import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.browser.home_page import HomePage
from logic.browser.sign_in_page import SignInPage


class TestLogin(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.email = self.config["email"]
        self.password = self.config["password"]
        self.invalid_password = self.config["invalid_password"]
        self.home_page.click_login_button()

    def tearDown(self):
        self.browser.close_browser()

    def test_valid_login(self):
        """ checks valid login"""
        # Act
        self.sign_in_page.sign_in_flow(self.email, self.password)
        # Assert
        self.assertTrue(self.sign_in_page.is_username_displayed())

    def test_invalid_login(self):
        """ checks log in with invalid password"""
        # Act
        self.sign_in_page.sign_in_flow(self.email, self.invalid_password)
        # Assert
        self.assertTrue(self.sign_in_page.is_invalid_message_displayed())
