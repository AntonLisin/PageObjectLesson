from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer ") # Задаем объект класса MainPage, передаем ему экземпляр драйвера и url
    page.open()                                                        # Открываем страницу, используем метод open класса BasePage
    page.go_to_login_page()                                            # Переходим на страницу логина используя метод класса MainPage
def test_quest_should_see_login_link(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer ")
    page.open()
    page.should_be_login_link()
