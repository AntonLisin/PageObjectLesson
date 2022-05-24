from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_text_empty(self):
        self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT)

    def shouldnt_be_goods_in_basket(self):
        self.is_not_element_present(*BasketPageLocators.GOODS)
