import time
import pytest
import allure

from core.page_factory import PageFactory
from core import environment_settings


def story(number_story):
    environment_settings.stash["STORY"] = number_story
    return allure.story(number_story)


def feature(number_feature):
    environment_settings.stash["FEATURE"] = number_feature
    return allure.feature(number_feature)


def init(page):
    """
    Аннотация для класса страницы
    :param page: класс страницы
    :return:
    """
    if environment_settings.PF is None:
        environment_settings.PF = PageFactory()
    page()
