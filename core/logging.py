import logging
import allure
from allure import attachment_type as at
import json
from core.tools import current_time
from core.config import TestConfig


def log(message, attach='attachment'):
    """
    Функция выводит лог в консоль, а так же дублирует его в отчете allure
    :param message: Заголовок сообщения
    :param attach: Содержательная часть (по умолчанию attachment)
    :return:
    """
    # Определяем тип вложения
    if isinstance(attach, dict):
        attach_body = json.dumps(attach, indent=2, ensure_ascii=False)
        attach_type = at.JSON
    elif isinstance(attach, list):
        attach_body = json.dumps(attach, indent=2, ensure_ascii=False)
        attach_type = at.JSON
    elif attach.startswith('http://') or attach.startswith('https://'):
        attach_body = attach
        attach_type = at.URI_LIST
    elif attach.endswith('.html') or '<html>' in attach.lower():
        attach_body = attach
        attach_type = at.HTML
    elif '\n' in attach and any(x in attach for x in [',', ';', '\t']):
        attach_body = attach
        attach_type = at.CSV
    else:
        attach_body = str(attach)
        attach_type = at.TEXT

    # Логируем
    allure.attach(name=f'{current_time()}: {message}',
                  body=attach,
                  attachment_type=attach_type)
    TestConfig.logger.info(f"{message}" if attach == 'attachment' else f"{message}: {attach}")
