from .pages.product_page import ProductPage

import pytest


@pytest.mark.parametrize('promo', ['?promo=offer0', '?promo=offer1', '?promo=offer2', '?promo=offer3',
                                   '?promo=offer4', '?promo=offer5', '?promo=offer6',
                                   pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                   '?promo=offer8', '?promo=offer9'])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()
    page.solve_quiz_and_get_code()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page()
