import unittest
from infra.api.api_wrapper import APIWrapper
from logic.api.api_shuffle_cards import APIShuffleCards
from infra.config_provider import ConfigProvider


class TestShuffleCards(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()
        self._api_shuffle_cards = APIShuffleCards(self._api_request)
        self._config = ConfigProvider.load_config_json()

    def test_shuffle_cards_get(self):
        result = self._api_shuffle_cards.get_shuffle_cards()
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertTrue(body["success"])
        self.assertEqual(body["remaining"], int(self._config["deck_count"])*52)



