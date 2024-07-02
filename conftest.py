import shutil
import pytest
import os
from core.logging import log

# #TODO подумать как очищать папку reports один раз
# @pytest.fixture(scope='session')
# def clear_reports():
#     log('Удаляем старые allure из папки reports')
#     shutil.rmtree(os.path.join('reports'))
#
#     """yield
#     log('а это запись после отработки тестов?')"""
