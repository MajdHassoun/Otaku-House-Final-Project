import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils_infra import UtilsInfra
from logic.browser.cart_page import CartPage
from logic.browser.home_page import HomePage
from logic.browser.item_page import ItemPage
from logic.browser.order_summary_page import OrderSummaryPage
from logic.browser.place_order_page import PlaceOrderPage
from logic.browser.payment_method_page import PaymentMethodPage
from logic.browser.payment_success_page import PaymentSuccessPage
from logic.browser.shipping_details_page import ShippingDetailsPage
from logic.browser.sign_in_page import SignInPage


class EndToEndPurchaseProcessTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)
        self.item_page = ItemPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.shipping_details_page = ShippingDetailsPage(self.driver)
        self.payment_method = PaymentMethodPage(self.driver)
        self.place_order_page = PlaceOrderPage(self.driver)
        self.order_summary_page = OrderSummaryPage(self.driver)
        self.payment_success_page = PaymentSuccessPage(self.driver)
        self.signin_page = SignInPage(self.driver)
        self.card_number = self.config["card_number"]
        self.card_date = self.config["card_date"]
        self.card_cvv = self.config["card_cvv"]
        self.zipcode = self.config["zip_code"]
        self.phone = self.config["phone_number"]
        self.email = self.config["fake_email"]
        self.costumer_name = self.config["costumer_name"]
        self.street = self.config["street"]
        self.city = self.config["city"]
        self.family = self.config["family_name"]
        self.home_page.click_login_button()
        self.signin_page.sign_in_flow(self.config["email"], self.config["password"])

    def test_end_to_end_purchase(self):
        # Arrange
        self.home_page.click_random_home_page_item(UtilsInfra.pick_random_number_one_to_eight())
        self.item_page.click_add_to_cart_button()
        self.cart_page.click_proceed_to_check_in_button()
        self.shipping_details_page.fill_shipping_data_flow(UtilsInfra.generate_random_string(5),
                                                           UtilsInfra.generate_random_string(5),
                                                           UtilsInfra.generate_random_string(5),
                                                           UtilsInfra.generate_random_string(5))
        self.payment_method.click_continue()
        self.place_order_page.click_place_order_button()
        self.order_summary_page.click_credit_card_button()

        # Act
        self.order_summary_page.insert_card_details_flow(self.card_number, self.card_date, self.card_cvv,
                                                         self.costumer_name,
                                                         self.family,
                                                         self.street,
                                                         self.city, self.zipcode, self.phone,
                                                         self.email)
        self.order_summary_page.click_pay_now_button()
        # Assert
        self.assertTrue(self.payment_success_page.is_payment_success_message_displayed())
