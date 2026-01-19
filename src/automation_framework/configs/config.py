from typing import Optional
from dataclasses import dataclass, field

import pytest
from selenium import webdriver
import sys

from automation_framework.core.page_factory import PageFactory

@dataclass
class ConfigurationTest:
    """Конфигурация для всей сессии тестов"""
    driver: Optional[webdriver.Chrome] = None
    browser_version: str = "latest"
    window_size: tuple = (1920, 1080)
    logger: Optional= None
    timeout: int = 10
    base_url: str = "https://your-app.com"
    headless: bool = False
    stash: dict = field(default_factory=dict)
    PF: PageFactory = None
    IN_ARGS = sys.argv
    stand_settings: dict = field(default_factory=dict)


# Синглтон конфига (можно заменить на фикстуру позже)
config = ConfigurationTest()