import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.browser.browser_wrapper import BrowserWrapper
from infra.utils_infra import UtileInfra
from logic.api.ApiAddReview import ApiAddReview
from logic.api.entity.review_details import ReviewDetails
from logic.browser.home_page import HomePage
from logic.browser.item_page import ItemPage
from logic.browser.sign_in_page import SignInPage


class AddReviewTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.api_request = APIWrapper()
        self.home_page = HomePage(self.driver)
        self.signin_page = SignInPage(self.driver)
        self.item_page = ItemPage(self.driver)
        self.home_page.click_login_button()
        self.signin_page.sign_in_flow(self.config["email"], self.config["password"])

    def test_add_review(self):
        """ Adds a review to a random item"""
        # Arrange
        item_number_url = UtileInfra.pick_random_number_review_url()
        item_number_home_page = UtileInfra.from_item_num_to_home_page_num(item_number_url)
        review_details_body = ReviewDetails(UtileInfra.generate_random_string(self.config["string_len"]),
                                            UtileInfra.pick_random_number_one_to_five())
        add_review = ApiAddReview(self.api_request)
        # Act
        add_review.api_add_review(item_number_url, review_details_body.to_dict())
        self.home_page.click_random_home_page_item(item_number_home_page)
        self.item_page = ItemPage(self.driver)
        # Assert
        self.assertTrue(self.item_page.is_item_reviews_displayed())
