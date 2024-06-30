import pathlib
import logging

from core import environment_settings
from core.logging import log

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
    environment_settings.logger = logger


def clear_reports_dir():
    # ToDo Вынести путь к папке с отчетам в config.ini или считаывать его из входящих парамтеров
    path_reports_dir = pathlib.Path.cwd() / 'reports'
    all_files_reports = list(map(str, path_reports_dir.glob('*.*')))
    log(f'Папка с отчетами allure будет очищена: {path_reports_dir}')
    for i in all_files_reports:
        pathlib.Path(i).unlink()
    log(f'Папка с отчетами allure очищена, удалено {len(all_files_reports)} файла/(ов)')


def set_browser():
    options = Options()
    # аргумент для запуска браузера в режиме максимального окна.
    options.add_argument("start-maximized")
    # экспериментальная опция, исключающая переключатель "enable-automation", чтобы предотвратить автоматическое обнаружение, что браузер управляется WebDriver.
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # экспериментальная опция, отключающая расширение автоматизации в браузере, что также помогает скрыть использование WebDriver.
    options.add_experimental_option('useAutomationExtension', False)
    # Отключаются уведомления в браузере.
    options.add_argument("--disable-notifications")
    # Отключается блокировка всплывающих окон
    options.add_argument("—disable-popup-blocking")

    environment_settings.browser_chrome = webdriver.Chrome(options=options)


def close_browser():
    if environment_settings.browser_chrome is not None:
        environment_settings.browser_chrome.quit()
