import time
import pytest
import allure
import datetime

from core.page_factory import PageFactory
from core import config
from core.logging import log


def story(number_story):
    """
    Для запуска конкретного теста
    :param number_story:
    :return: allure.story(number_story)
    """
    #ToDo перезаписыавет стори проходясь по всем
    env_settings.stash["STORY"] = number_story
    return allure.story(number_story)


def feature(number_feature):
    """
        Для запуска группы тестов
        :param number_feature:
        :return: allure.feature(number_feature)
    """
    env_settings.stash["FEATURE"] = number_feature
    return allure.feature(number_feature)


def init(page):
    """
    Аннотация для класса страницы
    :param page: класс страницы
    :return:
    """
    if env_settings.PF is None:
        env_settings.PF = PageFactory()
    page()
