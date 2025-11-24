from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_be_login_link()
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    #1 Открываем страницу
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()

    #2 Переходим в корзину
    page.should_be_basket_link()
    page.go_to_basket_page()
    bascket_page = BasketPage(browser, browser.current_url)

    #3 Ожидаем, что в корзине нет товаров
    bascket_page.should_be_empty_basket()

    #4 Ожидаем, что есть текст о том, что корзина пуста
    bascket_page.should_not_be_empty_text_basket()