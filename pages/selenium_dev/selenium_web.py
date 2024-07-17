import time

from pages.base_page import WebBasePage
from core.core_fixtures import init
from core.logging import log

from locators.selenium_dev import SeleniumDev


@init
class MouseInteraction(WebBasePage, SeleniumDev):
    title = 'Страница теста мыши SeleniumDev'

    @classmethod
    def тестирование_возможноcти_мыши(cls):
        cls.открыть_web_страницу(SeleniumDev.MouseInteraction.url)
        cls.screenshot(2)
        cls.нажать_на_кнопку(SeleniumDev.MouseInteraction.CLICK_fOR_RESULT_PAGE)
        cls.screenshot()
        cls.нажать_на_кнопку(SeleniumDev.MouseInteraction.DRAGGABLE)
        cls.screenshot()
        cls.закрыть_окно_браузера()


    def тестовый_шаг_2(self, *args):
        log("Запущен шаг 2 странциы авторизации")