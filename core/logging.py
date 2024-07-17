import logging
import allure
from core.tools import current_time
from core import env_settings


def log(message, attach='attachment'):
    """
    Функция выводит лог в консоль, а так же дублирует его в отчете allure
    :param message: Заголовок сообщения
    :param attach: Содержательная часть (по умолчанию attachment)
    :return:
    """
    allure.attach(name=f'{current_time()}: {message}', body=attach, attachment_type=allure.attachment_type.TEXT)
    env_settings.logger.info(f"{message}" if attach == 'attachment' else f"{message}: {attach}")
