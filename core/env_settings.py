import sys
from selenium import webdriver

from core.page_factory import PageFactory

IN_ARGS = sys.argv
PF: PageFactory = None
stash: dict = {}
logger = None
driver_chrome: webdriver = None
driver_wait_short = None
SHORT_TIME_WAIT = 10
STAND = None
stand_settings: dict = {}
