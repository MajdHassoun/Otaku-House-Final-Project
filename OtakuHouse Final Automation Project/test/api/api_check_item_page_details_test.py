import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.api_item_page_details import ApiItemPageDetails


class ApiCheckItemPageDetailsTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()
        self.item_page_details = ApiItemPageDetails(self.api_request)

    def test_item_page_details(self):
        result = self.item_page_details.get_item_page_details()
        self.assertTrue(result.ok)
        self.assertEqual(result.status, 200)
        self.assertEqual(result.data["name"], self.config["api_body_product_name"])
        self.assertEqual(result.data["brand"], self.config["api_item_page_details_brand"])
        self.assertEqual(result.data["price"], self.config["api_item_page_details_price"])
        self.assertEqual(result.data["_id"], self.config["api_item_page_details_id"])


