import requests
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class ApiAddItemToCart:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def api_add_item_to_cart(self, url):
        return self._request.get_request(f"{url}#/product/24", self.config["headers"])
