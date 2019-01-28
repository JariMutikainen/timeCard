# This file defines a class, which is used for doing math with time stamps.
# The time stamps can be positive or negative. They are strings in the format
# 'HH:MM' - i.e. '20:35' or '-02:30'.

import re

class HhMm:

    def __init__(self, hhmm):
        rex = re.compile(r'^([-])?([0-9]{2}):([0-9]{2})$')
        mo = re.search(rex, hhmm)
        print(mo.group(0))

        self.minutes = 0


if __name__ == '__main__':
    # Testing
    t1 = HhMm('20:36')
    t2 = HhMm('-02:10')

