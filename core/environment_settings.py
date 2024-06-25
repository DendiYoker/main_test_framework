import sys
#from typing import re

from core.page_factory import PageFactory

#IN_ARGS = re.split("|=", " ".join(sys.argv))
PF: PageFactory = None
stash: set = {}
logger = None