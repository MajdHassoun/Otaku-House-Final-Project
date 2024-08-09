import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.jira_handler import JiraHandler
from logic.browser.home_page import HomePage


class FailedTestForJira(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)
        self.jira_handler = JiraHandler()
        self.test_errors = []

    def tearDown(self):
        self.driver.close()
        self.jira_handler.create_issue(self.config["project_key"], self.config["jira_issue_summary"],
                                       self.config["jira_issue_description"])

    def test_failed_navigate_between_pages(self):
        """ Adds a bug to JIRA account project page"""
        try:
            # Act
            self.home_page.click_second_page_button()
            # Assert
            self.assertEqual(self.driver.current_url, 1)

        except AssertionError as e:
            self.test_errors.append(e)
            raise AssertionError
