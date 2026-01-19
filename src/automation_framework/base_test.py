import allure
import datetime

from automation_framework.core.logging import log
from automation_framework.configs.config import ConfigurationTest
from automation_framework.pages import __all__
from automation_framework.core.setup_test_env import set_browser, close_browser, set_story


class BaseTest(object):

    @classmethod
    def setup_method(cls, method):
        with allure.step("setup_method"):
            len(__all__)  #init all pages
            log(f'setup metod: {method.__name__}')
            set_browser()
            # set_story(cls, method)


    @staticmethod
    def set_page(page_name):
        ConfigurationTest.PF.set_current_page(page_name)

    @staticmethod
    def run_step(step, *args):
        log(f'Запущен шаг: {step}')
        start = datetime.datetime.now().replace(microsecond=0)
        with allure.step(step):
            try:
                ConfigurationTest.PF.run_action(step, *args)
                end = datetime.datetime.now().replace(microsecond=0)
                log(f'шаг отработал за {end - start} секунд')
            except:
                # ToDo подумать про проброску ошибок с шагов теста
                raise 'шаг запущен с ошибкой'


    @classmethod
    def teardown_method(cls, method):
        with allure.step('запуск teardown_method'):
            log('teardown_method запущен')
            close_browser()
