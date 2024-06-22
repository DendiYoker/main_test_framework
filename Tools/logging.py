import logging
import allure
import datetime


def log(text_log, attach='attachment'):
    """
    Функция выводит лог в консоль, а так же дублирует его в отчете allure
    :param text_log: Заголовок сообщения
    :param attach: Содержательная часть (по умолчанию attachment)
    :return:
    """
    # формирует в консоле запись в виде INFO:root:23:33:46 для каждой строки лога
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(level=logging.INFO)
    logg = logging.getLogger()

    now = datetime.datetime.now().strftime("%H:%M:%S")
    allure.attach(name=f'{now}: {text_log}', body=attach, attachment_type=allure.attachment_type.TEXT)
    logg.info(f"{now} {text_log}") if attach == 'attachment' else logg.info(f"{now} {text_log}: {attach}")
