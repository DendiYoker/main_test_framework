import logging
import allure
from core.tools import now


def log(message, attach='attachment'):
    """
    Функция выводит лог в консоль, а так же дублирует его в отчете allure
    :param message: Заголовок сообщения
    :param attach: Содержательная часть (по умолчанию attachment)
    :return:
    """

    logger_ingo = logging.getLogger()
    logger_ingo.setLevel(logging.INFO)
    # Обработчик добавляется каждый раз, когда вызывается из вне, поэтому необходимо очистить
    logger_ingo.handlers.clear()

    handler_1 = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    handler_1.setFormatter(formatter)
    logger_ingo.addHandler(handler_1)

    allure.attach(name=f'{now()}: {message}', body=attach, attachment_type=allure.attachment_type.TEXT)
    logger_ingo.info(f"{message}") if attach == 'attachment' else logger_ingo.info(f"{message}: {attach}")
