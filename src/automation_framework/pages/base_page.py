import time
import allure

from automation_framework.configs.config import ConfigurationTest
from automation_framework.core.logging import log
from automation_framework.core.page import Page
from automation_framework.core.web_element import WebElementHelper



class WebBasePage(Page):
    title = 'Web base page'

    @staticmethod
    def открыть_web_страницу(url):
        ConfigurationTest.driver_chrome.get(url)
        log(f'Открыта web страница {url}')


    @staticmethod
    def заполнить_поле(text, locator):
        WebElementHelper(locator).send_keys(text)
        log(f'Поле {locator[1]}, заполнено {text}')

    @staticmethod
    def screenshot(str_time=0):
        # ToDo слишком быстро скринит, в итоге белый экран подумать про ожидание загрузки странциы, пока костыль time
        time.sleep(str_time)
        allure.attach(ConfigurationTest.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    @staticmethod
    def нажать_на_кнопку(locator):
        WebElementHelper(locator).click_button()
        log(f'Кнопка {locator[1]} нажата')

    @staticmethod
    def очистить_поле(locator):
        WebElementHelper(locator).clear()
        log(f'Поле {locator[1]} очищено')

    @staticmethod
    def закрыть_окно_браузера():
        ConfigurationTest.driver.close()
        log(f'Текущее окно браузера закрыто')
