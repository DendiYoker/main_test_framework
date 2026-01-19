from automation_framework.pages.base_page import WebBasePage
from automation_framework.core.core_fixtures import init
from automation_framework.core.logging import log

from automation_framework.locators.selenium_dev import SeleniumDev


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