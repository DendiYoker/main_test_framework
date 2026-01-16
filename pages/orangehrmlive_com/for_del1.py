from pages.base_page import WebBasePage
from core.core_fixtures import init
from core import config


@init
class Base1(WebBasePage):
    title = 'База 1'