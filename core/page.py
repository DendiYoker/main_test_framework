from core import env_settings


class Page:
    title = 'Page'

    def __init__(self):
        if not env_settings.PF is None:
            env_settings.PF.append_page(self)
            env_settings.PF.set_current_page(self.title)
