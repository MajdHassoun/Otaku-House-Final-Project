from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class ApiCarrouselItems:
    ENDPOINT = 'api/products/top/'

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_carrousel_items(self):
        """ Sends API Get request to get the details of the carrousel items"""
        url = f'{self.config["url"]}{self.ENDPOINT}'
        return self._request.get_request(url, headers=self.config["headers"])
