import pytest
import configparser
from core import env_settings
from core.logging import log
from core.setup_test_env import set_logger, clear_reports_dir

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
    log(f'добавлены настройки по стенду: {env_settings.stand_settings} из config.ini, в env_settings.stand_settings ')


@pytest.fixture(autouse=True, scope="session")
def start_set_up():
    set_logger()
    clear_reports_dir()
    """
    в таком варианте создается одна сессия, и браузер в итоге если закрыть нужно переоткрывать в
     методе get start_session({}) а в этом случае окно открываетя не на всю ширину ES.driver_chrome.start_session({})
    """
    # set_browser()
    # yield
    # close_browser()

