import unittest
from infra.api.api_wrapper import APIWrapper
from logic.api.api_draw_card import APIDrawCard
from logic.api.api_shuffle_cards import APIShuffleCards
from infra.config_provider import ConfigProvider


class TestDrawCard(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()
        self._api_draw_card = APIDrawCard(self._api_request)
        self._config = ConfigProvider.load_config_json()
        self._shuffle_cards = APIShuffleCards(self._api_request)
        self._shuffle_result = self._shuffle_cards.get_shuffle_cards()
        self._shuffle_body = self._shuffle_result.json()
        self._deck_id = self._shuffle_body["deck_id"]

    def test_draw_card(self):
        draw_cards = APIDrawCard(self._api_request)
        draw_result = draw_cards.get_draw_card(self._config["base_url"], self._deck_id, self._config["cards_drown"])
        draw_body = draw_result.json()
        original_cards_number = self._shuffle_body["remaining"]
        self.assertEqual(self._shuffle_result.status_code, 200)
        self.assertEqual(draw_body["remaining"], original_cards_number - self._config["cards_drown"])
