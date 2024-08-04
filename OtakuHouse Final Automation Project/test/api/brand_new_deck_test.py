import unittest

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.api_brand_new_deck import APIBrandNewDeck
from logic.api.api_shuffle_cards import APIShuffleCards


class TestBrandNewDeck(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()
        self.cards_shuffle = APIShuffleCards(self.api_request)
        shuffle_result = self.cards_shuffle.get_shuffle_cards()
        self.shuffle_body = shuffle_result.json()
        self.deck_id = self.shuffle_body["deck_id"]
        self.brand_new_deck = APIBrandNewDeck(self.api_request)

    def test_brand_new_deck(self):
        response = self.brand_new_deck.get_brand_new_deck(self.config["url"], False)
        deck_data = response.json()
        self.assertNotEqual(self.deck_id, deck_data["deck_id"])
        self.assertEqual(deck_data["remaining"], self.shuffle_body["remaining"], "Deck does not have 52 cards remaining")

    def test_create_brand_new_deck_with_jokers(self):
        """
        Tests creating a brand-new deck of cards with jokers.
        """
        response = self.brand_new_deck.get_brand_new_deck(self.config["base_url"], True)
        deck_data = response.json()
        self.assertIn("deck_id", deck_data, "Deck ID not found in response data")
        self.assertEqual(deck_data["remaining"], 54, "Deck does not have 54 cards remaining")