from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class ApiAddReview:
    """ EndPoints for the URL"""
    ENDPOINT_PT1 = 'api/products/'
    ENDPOINT_PT2 = '/reviews/'

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def api_add_review(self, item_number, review_details):
        """ Sends API Post request to add a review to an item"""
        url = f'{self.config["url"]}{self.ENDPOINT_PT1}{item_number}{self.ENDPOINT_PT2}'
        return self._request.post_request(url, self.config["headers"], review_details)
