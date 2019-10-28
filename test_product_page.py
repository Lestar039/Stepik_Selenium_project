from .pages.product_page import ProductPage

import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()
    page.solve_quiz_and_get_code()
    # time.sleep(200)
    # time.sleep(10)
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page()
