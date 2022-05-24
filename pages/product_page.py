from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def should_be_msg_for_goods(self):
        self.should_be_book_name()
        self.should_be_basket_price()

    def should_be_book_name(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_MSG_BOOK).text

    def should_be_basket_price(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text in self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_MSG_PRICE).text

    def should_not_be_success_msg(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_MSG_BOOK), "Element is here"

    def should_be_success_msg_disappeared(self):
        assert self.is_element_disappeared(*ProductPageLocators.ADD_TO_BASKET_MSG_BOOK), "Element not disappeared"

