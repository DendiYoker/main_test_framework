import os
import logging

from automation_framework.configs.config import ConfigurationTest
from src.automation_framework.core.logging import log

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# ==================== НАЗВАНИЕ НЕ ПРИДУМАЛ ====================

def set_story(cls, method):
    log(f'новый метод {cls}, {method}')
    try:
        ConfigurationTest.stash['STORY'] = [el.args[0] for el in method.pytestmark if "story" in str(el)]
        log(f"STORY: {ConfigurationTest.stash['STORY'][0]}")
        ConfigurationTest.stash['FEATURE'] = [el.args[0] for el in method.pytestmark if "feature" in str(el)]
        log(f"FEATURE: {ConfigurationTest.stash['FEATURE'][0]}")
    except IndexError:
        try:
            ConfigurationTest.stash['FEATURE'] = [el.args[0] for el in cls.pytestmark if "feature" in str(el)]
            log(f"FEATURE: {ConfigurationTest.stash['FEATURE'][0]}")
        except AttributeError:
            log(f'FEATURE не определена')

# ==================== НАСТРОЙКА БРАУЗЕРА ====================
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
    ConfigurationTest.driver = webdriver.Chrome(service=service, options=chrome_options)

    # Даем браузеру время на инициализацию
    ConfigurationTest.driver.implicitly_wait(10)

    yield ConfigurationTest.driver

    # Закрываем браузер после теста
    ConfigurationTest.driver.quit()

def close_browser():
    if ConfigurationTest.driver is not None:
        ConfigurationTest.driver.quit()
    log(f'Драйвер браузера закрыт')

# ==================== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ====================
def is_running_in_ci():
    """Проверяем, запущены ли мы в CI среде"""
    return os.getenv('CI') == 'true' or os.getenv('GITHUB_ACTIONS') == 'true'

def clear_reports_dir():
    """Очистка директории с отчетами (только локально)"""
    if not is_running_in_ci():
        import shutil
        reports_dir = "allure-results"
        if os.path.exists(reports_dir):
            shutil.rmtree(reports_dir)
        os.makedirs(reports_dir, exist_ok=True)
        log(f'Папка с отчетами allure {reports_dir} очищена')

    # path_reports_dir = pathlib.Path.cwd() / 'reports'
    # all_files_reports = list(map(str, path_reports_dir.glob('*.*')))
    # for i in all_files_reports:
    #     pathlib.Path(i).unlink()
    # log(f'Папка с отчетами allure {path_reports_dir} очищена, удалено {len(all_files_reports)} файла/(ов)')

def setup_logger():
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
    ConfigurationTest.logger = logger
    return logger
