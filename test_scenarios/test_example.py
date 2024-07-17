import allure
import pytest

from core.core_fixtures import story, feature
from core.logging import log
from test_scenarios.base_test import BaseTest
from core.tools import current_time
from core import env_settings


@feature('Nice_test')
class Test11(BaseTest):
    @story('001')
    @allure.description('Описание первого теста')
    def test_orangeherm_authorization(self):
        self.set_page('Страница авторизации Orangehrm')
        self.run_step('проверить_авторизацию')


class Test12(BaseTest):

    @story('002')
    @allure.description('Описание второго теста')
    def test_002(self):
        self.set_page('Страница теста мыши SeleniumDev')
        self.run_step('тестирование_возможноcти_мыши')