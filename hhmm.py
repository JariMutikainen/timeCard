'''
This file defines a class, which is used for doing math with time stamps.
The time stamps can be positive or negative. They are strings in the format
'HH:MM' - i.e. '20:35' or '-02:30'.
'''

import re

class HhMm:
    '''
    This class operates on time stamps in the format 'HH:MM' - i.e. '02:17'
    for example. It defines methods for ain and subtrackting such time
    stamps from one another. The time stamps are first converted to
    minutes. The calculations are made on minutes and finally the
    result is converted back into the original 'HH:MM'-format.
    '''

    def __init__(self, hhmm='00:00'):
        rex = re.compile(r'^([-])?([0-9]{2}):([0-9]{2})$')
        mo = re.search(rex, hhmm)
        if mo:
            self.negative = bool(mo.group(1))
            self.hh = int(mo.group(2))
            self.mm = int(mo.group(3))
            self.minutes = self.hh * 60 + self.mm
            if self.negative:
                self.minutes = 0 - self.minutes
        else:
            raise AttributeError(f'Bad format for time. '
                                 f'It should be like "HH:MM" '
                                 f'- not "{hhmm}"')

    def __repr__(self):
        sign_str = '-' if self.negative else ''
        return sign_str + f'{self.hh:0>2d}:{self.mm:0>2d}'

    def __add__(self, other):
        out = HhMm()
        out.minutes = self.minutes + other.minutes
        out.negative = bool(out.minutes < 0)
        out.hh = abs(out.minutes) // 60
        out.mm = abs(out.minutes) - out.hh * 60
        return out

    def __sub__(self, other):
        out = HhMm()
        out.minutes = self.minutes - other.minutes
        out.negative = bool(out.minutes < 0)
        out.hh = abs(out.minutes) // 60
        out.mm = abs(out.minutes) - out.hh * 60
        return out

    def __lt__(self, other):
        return bool(self.minutes < other.minutes)

    def __eq__(self, other):
        return bool(self.minutes == other.minutes)

if __name__ == '__main__':
    # Testing
    t1 = HhMm('20:36')
    t2 = HhMm('-02:10')
    #t3 = HhMm('Jari')
    print(t1)
    print(t2)
    t4 = t1 + t2
    print(t4)
    t5 = t1 - t2
    print(t5)
    print(type(t5))
    print(t2 < t1)
    print(t1 < t2)
    print(t1 != t2)
