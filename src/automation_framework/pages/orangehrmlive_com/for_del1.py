from automation_framework.pages.base_page import WebBasePage
from automation_framework.core.core_fixtures import init


@init
class Base1(WebBasePage):
    title = 'База 1'