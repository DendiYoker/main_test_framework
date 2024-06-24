from pages.base_page import WebBasePage
from core.core_fixtures import init


@init
class Korzina(WebBasePage):
    title = 'Новая страница2'

    def __init__(self):
        super().__init__()