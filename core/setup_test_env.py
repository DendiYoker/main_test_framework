import pathlib
import logging

from core import env_settings
from core.logging import log

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


def set_logger():
    """
    Функция добавляет logger в environment_settings.logger
    """
    logger = logging.getLogger("logger_info")
    logger.setLevel(logging.INFO)
    # обработчик добавляется каждый раз, когда вызывается извне поэтому удаляем все потоки
    logger.handlers.clear()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    env_settings.logger = logger


def clear_reports_dir():
    # ToDo Вынести путь к папке с отчетам в config.ini или считаывать его из входящих парамтеров
    path_reports_dir = pathlib.Path.cwd() / 'reports'
    all_files_reports = list(map(str, path_reports_dir.glob('*.*')))
    for i in all_files_reports:
        pathlib.Path(i).unlink()
    log(f'Папка с отчетами allure {path_reports_dir} очищена, удалено {len(all_files_reports)} файла/(ов)')


def set_browser():
    options = Options()
    # аргумент для запуска браузера в режиме максимального окна.
    options.add_argument("start-maximized")
    # экспериментальная опция, исключающая переключатель "enable-automation", чтобы предотвратить автоматическое
    # обнаружение, что браузер управляется WebDriver.
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # экспериментальная опция, отключающая расширение автоматизации в браузере, что также помогает скрыть
    # использование WebDriver.
    options.add_experimental_option('useAutomationExtension', False)
    # Отключаются уведомления в браузере.
    options.add_argument("--disable-notifications")
    # Отключается блокировка всплывающих окон
    options.add_argument("—disable-popup-blocking")
    # normal (полная загрузка страницы)
    # options.set_capability('pageLoadStrategy', "normal")
    env_settings.driver_chrome = webdriver.Chrome(options=options)
    env_settings.driver_wait_short = WebDriverWait(env_settings.driver_chrome, env_settings.SHORT_TIME_WAIT)
    log(f'webdriver для Chrome добавлен в env_settings.driver_chrome')


def close_browser():
    if env_settings.driver_chrome is not None:
        env_settings.driver_chrome.quit()
    log(f'Драйвер браузера закрыт')


def set_story(cls, method):
    log(f'епта новый метод {cls}, {method}')
    try:
        env_settings.stash['STORY'] = [el.args[0] for el in method.pytestmark if "story" in str(el)]
        log(f'STORY: {env_settings.stash['STORY'][0]}')
        env_settings.stash['FEATURE'] = [el.args[0] for el in method.pytestmark if "feature" in str(el)]
        log(f'FEATURE: {env_settings.stash['FEATURE'][0]}')
    except IndexError:
        try:
            env_settings.stash['FEATURE'] = [el.args[0] for el in cls.pytestmark if "feature" in str(el)]
            log(f'FEATURE: {env_settings.stash['FEATURE'][0]}')
        except AttributeError:
            log(f'FEATURE не определена')
