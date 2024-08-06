import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.api_search import ApiSearch


class ApiSearchTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()
        self.api_search = ApiSearch(self.api_request)

    def test_api_search(self):
        # Act
        result = self.api_search.get_search()
        # Assert
        self.assertEqual(200, result.status)
        self.assertTrue(result.ok)
        self.assertEqual(result.data["products"][0]["name"], self.config["api_body_product_name"])

    def test_negative_api_search(self):
        # Act
        result = self.api_search.get_search_negative()
        # Assert
        self.assertEqual(200, result.status)
        self.assertTrue(result.ok)
        self.assertEqual(result.data["products"], [])
