from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_links")

class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.XPATH,'//button[@class = "btn btn-lg btn-primary btn-add-to-basket"]')
    BOOK_NAME = (By.XPATH,'//h1')
    BOOK_PRICE = (By.XPATH, '//p[@class="price_color"]')
    ADD_TO_BASKET_MSG_BOOK = (By.XPATH,'(//div[@class="alertinner "])[1]/strong')
    ADD_TO_BASKET_MSG_PRICE = (By.XPATH,'(//div[@class="alertinner "])[3]')
