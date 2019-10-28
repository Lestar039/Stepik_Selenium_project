from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class BasketButtonLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner > p > strong")
