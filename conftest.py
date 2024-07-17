import pytest
import configparser
from core import env_settings


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
    env_settings.STAND = args_stand  # set the stand from the incoming parameters
    t = configparser.ConfigParser()
    t.read('config.ini')
    env_settings.stand_settings = dict(t[args_stand])
