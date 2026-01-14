import os
import pathlib
import logging
import platform

from core import env_settings
from core.logging import log

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


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
    chrome_options = Options()

    # Если запускаем в CI (GitHub Actions), используем headless режим
    if is_running_in_ci():
        chrome_options.add_argument("--headless")  # без графического интерфейса
        chrome_options.add_argument("--no-sandbox")  # обязательно для CI
        chrome_options.add_argument("--disable-dev-shm-usage")  # для ограниченной памяти в CI
        chrome_options.add_argument("--window-size=1920,1080")

    # Автоматически скачиваем и используем правильный ChromeDriver
    service = Service(ChromeDriverManager().install())
    env_settings.driver_chrome = webdriver.Chrome(service=service, options=chrome_options)

    # Даем браузеру время на инициализацию
    env_settings.driver_chrome.implicitly_wait(10)

    yield env_settings.driver_chrome

    # Закрываем браузер после теста
    env_settings.driver_chrome.quit()



def is_running_in_ci():
    """Проверяем, запущены ли мы в CI среде"""
    import os
    return os.getenv('CI') == 'true' or os.getenv('GITHUB_ACTIONS') == 'true'


def close_browser():
    if env_settings.driver_chrome is not None:
        env_settings.driver_chrome.quit()
    log(f'Драйвер браузера закрыт')


def set_story(cls, method):
    log(f'новый метод {cls}, {method}')
    try:
        env_settings.stash['STORY'] = [el.args[0] for el in method.pytestmark if "story" in str(el)]
        log(f"STORY: {env_settings.stash['STORY'][0]}")
        env_settings.stash['FEATURE'] = [el.args[0] for el in method.pytestmark if "feature" in str(el)]
        log(f"FEATURE: {env_settings.stash['FEATURE'][0]}")
    except IndexError:
        try:
            env_settings.stash['FEATURE'] = [el.args[0] for el in cls.pytestmark if "feature" in str(el)]
            log(f"FEATURE: {env_settings.stash['FEATURE'][0]}")
        except AttributeError:
            log(f'FEATURE не определена')
