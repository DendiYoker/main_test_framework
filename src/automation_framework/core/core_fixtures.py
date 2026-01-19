import allure

from automation_framework.core.page_factory import PageFactory
from automation_framework.configs.config import ConfigurationTest


def story(number_story):
    """
    Для запуска конкретного теста
    :param number_story:
    :return: allure.story(number_story)
    """
    #ToDo перезаписыавет стори проходясь по всем
    # ConfigurationTest.stash["STORY"] = number_story
    return allure.story(number_story)


def feature(number_feature):
    """
        Для запуска группы тестов
        :param number_feature:
        :return: allure.feature(number_feature)
    """
    # ConfigurationTest.stash["FEATURE"] = number_feature
    return allure.feature(number_feature)


def init(page):
    """
    Аннотация для класса страницы
    :param page: класс страницы
    :return:
    """
    if ConfigurationTest.PF is None:
        ConfigurationTest.PF = PageFactory()
    page()
