import sys
#from typing import re
from selenium import webdriver

from core.page_factory import PageFactory

#IN_ARGS = re.split("|=", " ".join(sys.argv))
PF: PageFactory = None
stash: set = {}
logger = None
browser_chrome: webdriver = None