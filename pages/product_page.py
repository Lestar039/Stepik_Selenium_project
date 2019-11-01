from .base_page import BasePage
from .locators import BasketButtonLocators
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_basket_button()
        self.should_be_correct_product_name()
        self.should_be_correct_price()

    # Метод, добавляющий товар в корзину
    def should_be_add_product_to_basket(self):
        basket_button = self.browser.find_element(*BasketButtonLocators.BASKET_BUTTON)
        basket_button.click()

    # Проверка наличия кпонки "Положить в корзину"
    def should_be_basket_button(self):
        assert self.is_element_present(*BasketButtonLocators.BASKET_BUTTON), "Basket button is not presented"

    # Проверка совпадения названия товара с названием во всплывающем сообщении
    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*BasketButtonLocators.PRODUCT_NAME)
        product_in_basket = self.browser.find_element(*BasketButtonLocators.PRODUCT_NAME_IN_BASKET)
        assert product_name.text == product_in_basket.text, "Product name is not correct"

    # Проверка совпадения цены товара и цены во всплывающем сообщении
    def should_be_correct_price(self):
        product_price = self.browser.find_element(*BasketButtonLocators.PRODUCT_PRICE)
        price_in_basket = self.browser.find_element(*BasketButtonLocators.PRODUCT_PRICE_IN_BASKET)
        assert product_price.text == price_in_basket.text, "Price is not correct"

    # Метод, который проверяет, чтобы элемент не появлялся на странице в течение заданного времени
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    # Метод, который проверяет, чтобы элемент исчезал на странице в течение заданного времени
    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message not is presented, but should be"
