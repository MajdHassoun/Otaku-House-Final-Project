import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.browser.browser_wrapper import BrowserWrapper
from infra.utils_infra import UtilsInfra
from logic.api.api_add_review import ApiAddReview
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
        """ Adds a review to a random item by choosing an item with UI and adding a review with
        a POST API call and finally checks it with UI"""
        # Arrange
        item_number_url = UtilsInfra.pick_random_number_url()
        item_number_home_page = UtilsInfra.from_item_num_to_home_page_num(item_number_url)
        review_details_body = ReviewDetails(UtilsInfra.generate_random_string(8),
                                            UtilsInfra.pick_random_number_one_to_five())
        add_review = ApiAddReview(self.api_request)
        # Act
        add_review.api_add_review(item_number_url, review_details_body.to_dict())
        self.home_page.click_random_home_page_item(item_number_home_page)
        self.item_page = ItemPage(self.driver)
        # Assert
        self.assertEqual(self.item_page.get_last_rating_user_name(), self.config["user_name"])

    def test_negative_add_review_ui(self):
        """ Negative test that adds a review without choosing a rating"""
        # Arrange
        self.home_page.click_random_home_page_item(UtilsInfra.pick_random_number_one_to_eight())
        self.item_page.enter_review_text(UtilsInfra.generate_random_string(8))
        # Act
        self.item_page.click_submit_review_button()
        # Assert
        self.assertTrue(self.item_page.is_select_rating_message_displayed())
