from pages.base_page import WebBasePage
from core.core_fixtures import init
from core import env_settings


@init
class Base1(WebBasePage):
    title = 'База 1'