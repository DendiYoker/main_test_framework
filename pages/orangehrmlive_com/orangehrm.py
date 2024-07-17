import time

from pages.base_page import WebBasePage
from core.core_fixtures import init
from core.logging import log

from locators.orangehrm import Orangehrm
from locators.selenium_dev import SeleniumDev


@init
class AuthorizationPage(WebBasePage, Orangehrm):
    title = 'Страница авторизации Orangehrm'

    @classmethod
    def проверить_авторизацию(cls):
        cls.открыть_web_страницу(Orangehrm.AuthorizationPage.url)
        #ToDo слишком быстро скринит, в итоге белый экран подумать про ожидание загрузки странциы
        cls.screenshot(5)
        cls.заполнить_поле('Admin', Orangehrm.AuthorizationPage.ЛОГИН)
        cls.заполнить_поле('admin123', Orangehrm.AuthorizationPage.ПАРОЛЬ)
        cls.screenshot()
        cls.нажать_на_кнопку(Orangehrm.AuthorizationPage.КНОПКА_LOGIN)
        cls.screenshot()
        cls.закрыть_окно_браузера()


    def тестовый_шаг_2(self, *args):
        log("Запущен шаг 2 странциы авторизации")


@init
class HomePage(WebBasePage, SeleniumDev):
    title = 'Главная страница'

    def тестовый_шаг3(self, *args):
        log("Запущен шаг 3 главной страницы")

    def тестовый_шаг_5(self, *args):
        log("Запущен шаг 5 главной страницы")
