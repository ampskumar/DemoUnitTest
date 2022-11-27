# https://cheatography.com/davechild/cheat-sheets/regular-expressions/

import re

s = "I am amit      "

m = re.search("(.*)", s)
if m:
    print(m.group(1))
