from core import environment_settings


class Page:
    title = 'Page'

    def __init__(self):
        if not environment_settings.PF is None:
            environment_settings.PF.append(self)
            environment_settings.PF.set_current_page(self.title)
            temp = 1
