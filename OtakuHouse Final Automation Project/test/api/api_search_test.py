import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.utils_infra import UtilsInfra
from logic.api.api_search import ApiSearch


class ApiSearchTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()
        self.api_search = ApiSearch(self.api_request)

    def test_api_search(self):
        """ This test sends an API get call  to validate search functionality"""
        # Act
        result = self.api_search.get_search(self.config["search_query"], self.config["page_number"])
        # Assert

        self.assertEqual(result.data["products"][0]["name"], self.config["api_body_product_name"])

    def test_negative_api_search(self):
        """ This is a negative test that sends an API get call  to validate search functionality"""
        # Act
        result = self.api_search.get_search_negative(UtilsInfra.generate_random_string(8), self.config["page_number"])
        # Assert

        self.assertEqual(result.data["products"], [])
