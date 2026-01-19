from automation_framework.pages.base_page import WebBasePage
from automation_framework.core.core_fixtures import init


@init
class Base_3(WebBasePage):
    title = 'НБаза 3'

    def __init__(self):
        super().__init__()