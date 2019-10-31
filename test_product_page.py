from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

import pytest


# @pytest.mark.parametrize('promo', ['?promo=offer0', '?promo=offer1', '?promo=offer2', '?promo=offer3',
#                                    '?promo=offer4', '?promo=offer5', '?promo=offer6',
#                                    pytest.param("?promo=offer7", marks=pytest.mark.xfail),
#                                    '?promo=offer8', '?promo=offer9'])
# def test_guest_can_add_product_to_basket(browser, promo):
#     link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/{promo}"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     product_page = ProductPage(browser, browser.current_url)
#     product_page.should_be_product_page()
#     time.sleep(120)


# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_product_to_basket()
#     page.should_not_be_success_message()


# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()


# Проверяем, что нет сообщения об успехе с помощью is_disappeared
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_product_to_basket()
#     page.should_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
