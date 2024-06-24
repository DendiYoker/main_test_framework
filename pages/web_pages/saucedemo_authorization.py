from pages.base_page import WebBasePage
from core.core_fixtures import init


@init
class HomeAuto(WebBasePage):
    title = 'Старая страница'
