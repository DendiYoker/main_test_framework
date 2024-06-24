import time
import pytest
import allure

from core.page_factory import PageFactory
from core import environment_settings


def story(str):
    environment_settings.stash["STORY"] = str
    return allure.story(str)


def feature(str):
    environment_settings.stash["FEATURE"] = str
    return allure.feature(str)


def init(page):
    """
    Аннотация для класса страницы
    :param page: класс страницы
    :return:
    """
    if environment_settings.PF is None:
        environment_settings.PF = PageFactory()

    page()
