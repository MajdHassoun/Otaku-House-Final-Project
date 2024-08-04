import unittest
from infra.api.api_wrapper import APIWrapper
from logic.api.api_draw_card import APIDrawCard
from logic.api.api_reshuffel_cards import APIReshuffelCards
from logic.api.api_shuffle_cards import APIShuffleCards
from infra.config_provider import ConfigProvider


class TestDrawCard(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()
        self._api_draw_card = APIDrawCard(self._api_request)
        self._config = ConfigProvider.load_config_json()
        self._shuffle_cards = APIShuffleCards(self._api_request)
        shuffle_result = self._shuffle_cards.get_shuffle_cards()
        self._shuffle_body = shuffle_result.json()
        self._deck_id = self._shuffle_body["deck_id"]
        draw_cards = APIDrawCard(self._api_request)
        draw_result = draw_cards.get_draw_card(self._config["base_url"], self._deck_id, self._config["cards_drown"])
        self._draw_body = draw_result.json()

    def test_reshuffel_cards(self):
        reshuffel_cards = APIReshuffelCards(self._api_request)
        reshuffel_result = reshuffel_cards.get_reshuffel_cards(self._config["base_url"], self._deck_id, True)
        reshuffel_body = reshuffel_result.json()
        self.assertTrue(reshuffel_body["shuffled"])
        self.assertEqual(self._deck_id, reshuffel_body["deck_id"])
        is_remaining = True
        if not is_remaining:
            self.assertEqual(reshuffel_body['remaining'], self._shuffle_body["remaining"])
        else:
            self.assertEqual(reshuffel_body['remaining'], self._draw_body['remaining'])

