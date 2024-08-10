from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class ApiSearch:
    ENDPOINT = '/api/products/?keyword='
    ENDPOINT_PT2 = '&'

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_search(self, search_query, page_number):
        """ Sends Api Get request to preform a search"""
        url = (
            f'{self.config["url"]}{self.ENDPOINT}{search_query}{self.ENDPOINT_PT2}{page_number}')
        return self._request.get_request(url, headers=self.config["headers"])

    def get_search_negative(self, search_query, page_number):
        """ Sends Api Get request to preform an invalid search"""
        url = (
            f'{self.config["url"]}{self.ENDPOINT}{search_query}{self.ENDPOINT_PT2}{page_number}')
        return self._request.get_request(url, headers=self.config["headers"])
