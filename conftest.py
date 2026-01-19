import pytest
import configparser
from datetime import datetime

from automation_framework.configs.config import ConfigurationTest
from src.automation_framework.core.logging import log
from src.automation_framework.core.setup_test_env import setup_logger, clear_reports_dir, set_browser


def pytest_addoption(parser):
    parser.addoption('--stand', action="store", default="PSI", help="Укажите стенд: PSI/ PREDPROM")


@pytest.fixture()
def args_stand(pytestconfig):
    return pytestconfig.option.stand


@pytest.fixture(autouse=True)
def config_parser_fix(args_stand):
    """
    Парсинг файла config.ini
    """
    ConfigurationTest.STAND = args_stand  # set the stand from the incoming parameters
    t = configparser.ConfigParser()
    t.read('config.ini')
    ConfigurationTest.stand_settings = dict(t[args_stand])
    log(f'добавлены настройки по стенду: {ConfigurationTest.stand_settings} из config.ini, в env_settings.stand_settings ')


@pytest.fixture(autouse=True, scope="session")
def global_setup():
    """Глобальная настройка тестовой сессии"""
    setup_logger()
    log(f"Starting test session at {datetime.now()}")
    clear_reports_dir()
    set_browser()

    yield
    # close_browser()

