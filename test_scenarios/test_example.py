import allure
import pytest

from core.core_fixtures import story, feature
from core.logging import log
from test_scenarios.base_test import BaseTest
from core.tools import now
from core import environment_settings

@feature('Nice_test')
class Test11(BaseTest):
    @story('001')
    @allure.description('Описание первого теста')
    def test_001(self):
        with allure.step(f"{now()} шаг 1"):
            log('тестируем приклад 1', 'какой то аттач')
        log(f"Завершаем тест № 1")


class Test12(BaseTest):

    @story('002')
    @allure.description('Описание второго теста')
    def test_002(self):
        with allure.step("шаг 2"):
            log('тестируем приклад 2', 'какой то аттач')
        log(f"Завершаем тест № 2")


