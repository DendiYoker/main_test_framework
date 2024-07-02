import allure
import pytest

from core.core_fixtures import story, feature
from core.logging import log
from test_scenarios.base_test import BaseTest
from core.tools import current_time
from core import environment_settings

@feature('Nice_test')
class Test11(BaseTest):
    @story('001')
    @allure.description('Описание первого теста')
    def test_orangeherm_authorization(self):
        self.set_page('Страница авторизации')
        self.run_step('тестовый_шаг_1')
        self.run_step('тестовый_шаг_2')
        self.set_page('Главная страница')
        self.run_step('тестовый_шаг_4')
        self.run_step('тестовый_шаг_5')


class Test12(BaseTest):

    @story('002')
    @allure.description('Описание второго теста')
    def test_002(self):
        with allure.step("шаг 2"):
            log('тестируем приклад 2', 'какой то аттач')
        log(f"Завершаем тест № 2")


