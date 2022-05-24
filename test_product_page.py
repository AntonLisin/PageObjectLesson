import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest

@pytest.mark.parametrize('offer', ["/?promo=offer0",
                                  "/?promo=offer1",
                                  "/?promo=offer2",
                                  "/?promo=offer3",
                                  "/?promo=offer4",
                                  "/?promo=offer5",
                                  "/?promo=offer6",
                                  pytest.param("/?promo=offer7", marks=pytest.mark.xfail),
                                  "/?promo=offer8",
                                  "/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, offer):
    product = ProductPage(browser, f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207{offer}")
    product.open()
    product.add_to_basket()
    product.solve_quiz_and_get_code()
    product.should_be_msg_for_goods()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product = ProductPage(browser,'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    product.open()
    product.add_to_basket()
    # product.solve_quiz_and_get_code()
    product.should_not_be_success_msg()

def test_guest_cant_see_success_message(browser):
    product = ProductPage(browser,'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    product.open()
    product.should_not_be_success_msg()

def test_message_disappeared_after_adding_product_to_basket(browser):
    product = ProductPage(browser,'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    product.open()
    product.add_to_basket()
    product.should_be_success_msg_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    product = ProductPage(browser,'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    product.open()
    product.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    product = ProductPage(browser,'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    product.open()
    product.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product = ProductPage(browser,'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    product.open()
    product.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_text_empty()
    basket_page.shouldnt_be_goods_in_basket()




