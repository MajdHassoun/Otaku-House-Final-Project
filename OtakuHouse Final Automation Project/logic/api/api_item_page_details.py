from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class ApiItemPageDetails:
    """ EndPoints for the URL"""
    ENDPOINT = 'api/products/'
    ENDPOINT_PT2 = '/'

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_item_page_details(self, item_id):
        """ Sends API Get request to get the item's details"""
        url = (
            f'{self.config["url"]}{self.ENDPOINT}{item_id}{self.ENDPOINT_PT2}')
        return self._request.get_request(url, headers=self.config["headers"])
