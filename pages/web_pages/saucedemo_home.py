from pages.base_page import WebBasePage
from core.core_fixtures import init
from core import environment_settings


@init
class Authorization(WebBasePage):
    title = 'Авторизация'