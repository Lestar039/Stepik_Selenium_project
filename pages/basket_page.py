from .base_page import BasePage
from .locators import BasketInHead


class BasketPage(BasePage):
    def should_be_basket_page(self):
        # self.should_be_product()
        self.should_be_empty_basket()
        self.should_be_empty_basket_text()

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketInHead.BASKET_FULL), "Basket is not empty"

    def should_be_empty_basket_text(self):
        empty_basket_text = self.browser.find_element(*BasketInHead.BASKET_EMPTY_TEXT)
        assert empty_basket_text, "Basket empty text is not here"
