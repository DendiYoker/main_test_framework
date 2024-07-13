from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC

from core import environment_settings as ES
from core.logging import log


class WebElementHelper:
    """
     Класс для работы с web элементом
    """

    def __init__(self, locator):
        self.locator = locator

    def find_element(self):
        try:
            return ES.driver_wait_short.until(EC.presence_of_element_located(self.locator))
        except TimeoutException:
            #ToDo подумать про проброску ошибок run_test
            raise log(f'Элемент "{self.locator[1]}" не найден')

    def send_keys(self, text):
        self.find_element().send_keys(text)

    def clear(self):
        self.find_element().clear()

    def click_button(self):
        # ToDo добавить проверку на кликабельность
        self.find_element().click()