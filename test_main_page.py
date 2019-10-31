from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import ToBasketPage
from .pages.basket_page import BasketPage

import time


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()


# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    main_to_basket_head = ToBasketPage(browser, link)
    main_to_basket_head.should_go_to_basket_in_head()
    empty_basket = BasketPage(browser, link)
    empty_basket.should_be_empty_basket()
    empty_basket.should_be_empty_basket_text()


