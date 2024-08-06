from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.utils_infra import UtilsInfra


class ApiSearch:
    ENDPOINT = '/api/products/?keyword='
    ENDPOINT_PT2 = '&'

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_search(self):
        url = (
            f'{self.config["url"]}{self.ENDPOINT}{self.config["search_query"]}{self.ENDPOINT_PT2}{self.config["page_number"]}')
        return self._request.get_request(url, headers=self.config["headers"])

    def get_search_negative(self):
        url = (
            f'{self.config["url"]}{self.ENDPOINT}{UtilsInfra.generate_random_string(8)}{self.ENDPOINT_PT2}{self.config["page_number"]}')
        return self._request.get_request(url, headers=self.config["headers"])
