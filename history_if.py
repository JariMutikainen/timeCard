'''
This file contains HistoryInterface for interfacing
the history file on the disk.

When the 1st login of a new day takes place in working_day.py the
previous working day is sent into this interface to be appended into the
end of the existing history file for future reference.
'''

from day import Day

class HistoryInterface:
    '''
    This class implements an interface to an external file, which contains
    a list of gone WorkingDays - that is: Days. Methods are offered
    for printing out some of those days.
    '''

    def __init__(self):
        self.history_list = []

    def append_working_day(self, w_day):
        print('\nAppending the following working day into the history file:\n')
        print(w_day)

if __name__ == '__main__':
    # Testing
    hd = Day()
    print(hd)
    #hi = HistoryInterface()
    #hi.append_working_day()
