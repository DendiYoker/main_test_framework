import allure

from automation_framework.core.core_fixtures import story, feature
from automation_framework.base_test import BaseTest


@feature('Nice_test')
class Test11(BaseTest):
    @story('001')
    @allure.description('Описание первого теста')
    def test_orangeherm_authorization(self):
        self.set_page('Страница авторизации Orangehrm')
        # self.run_step('проверить_авторизацию')

    @story('003')
    @allure.description('Описание 3 теста')
    def test_authorization(self):
        print('опа')


class Test12(BaseTest):

    @story('002')
    @allure.description('Описание второго теста')
    def test_002(self):
        self.set_page('Страница теста мыши SeleniumDev')
        # self.run_step('тестирование_возможноcти_мыши')