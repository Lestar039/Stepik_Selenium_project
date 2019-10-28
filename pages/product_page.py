from .base_page import BasePage
from .locators import BasketButtonLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_link()
        self.should_be_basket_button()
        self.should_be_correct_product_name()
        self.should_be_correct_price()

    def should_be_add_product_to_basket(self):
        basket_button = self.browser.find_element(*BasketButtonLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_product_link(self):
        assert "?promo=newYear" in self.browser.current_url, "'?promo=newYear' is not presented"

    def should_be_basket_button(self):
        assert self.is_element_present(*BasketButtonLocators.BASKET_BUTTON), "Basket button is not presented"

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*BasketButtonLocators.PRODUCT_NAME)
        product_in_basket = self.browser.find_element(*BasketButtonLocators.PRODUCT_NAME_IN_BASKET)
        assert product_name.text == product_in_basket.text, "Product name is not correct"

    def should_be_correct_price(self):
        product_price = self.browser.find_element(*BasketButtonLocators.PRODUCT_PRICE)
        price_in_basket = self.browser.find_element(*BasketButtonLocators.PRODUCT_PRICE_IN_BASKET)
        assert product_price.text == price_in_basket.text, "Price is not correct"
