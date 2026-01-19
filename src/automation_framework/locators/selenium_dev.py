from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class SeleniumDev:
    class MouseInteraction:
        url = 'https://selenium.dev/selenium/web/mouse_interaction.html'
        CLICK_fOR_RESULT_PAGE = [By.ID, "clickable"]
        DRAGGABLE = [By.ID, "absolute-location"]
