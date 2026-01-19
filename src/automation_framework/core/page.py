from automation_framework.configs.config import ConfigurationTest


class Page:
    title = 'Page'

    def __init__(self):
        if not ConfigurationTest.PF is None:
            ConfigurationTest.PF.append_page(self)
            ConfigurationTest.PF.set_current_page(self.title)
