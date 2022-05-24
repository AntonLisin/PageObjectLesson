from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/") # Задаем объект класса MainPage, передаем ему экземпляр драйвера и url
    page.open()                                                        # Открываем страницу, используем метод open класса BasePage
    page.go_to_login_page()                                         # Переходим на страницу логина используя метод класса MainPage
    login_page = LoginPage(browser, browser.current_url)             #Переключаемся на loginpage в теле теста, задаем объект класса LoginPage
    login_page.should_be_login_page()                               #Проверки из loginpage

def test_quest_should_see_login_link(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_text_empty()
    basket_page.shouldnt_be_goods_in_basket()





