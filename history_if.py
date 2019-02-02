'''
This file contains HistoryInterface for interfacing
the history file on the disk.

When the 1st login of a new day takes place in working_day.py the
previous working day is sent into this interface to be appended into the
end of the existing history file for future reference.
'''

import json
from day import Day

class HistoryInterface:
    '''
    This class implements an interface to an external file, which contains
    a list of gone WorkingDays - that is: Days. Methods are offered
    for printing out some of those days.
    '''
    HISTORY_FILE = 'history.json'
    # The maximum number of working days stored in the history file:
    MAX_DAYS = 5 

    def __init__(self):
        self.history_list = []
        self.a_day = Day()

    def load_history_data(self):
        '''Loads the history data from the disk.'''
        try:
            with open(HistoryInterface.HISTORY_FILE, 'r') as fh:
                self.history_list = json.load(fh)
        except FileNotFoundError:
            self.history_list = []

    def dump_history_data(self):
        '''Saves history data into the disk'''
        with open(HistoryInterface.HISTORY_FILE, 'w') as fh:
            json.dump(self.history_list, fh, indent=4, separators=(',', ': '))

    def show_history_data(self):
        '''Shows all the days in the history file.'''
        self.load_history_data()
        if self.history_list == []:
            print('\n\tNo history data is available at this point.\n')
            return
        for i, working_day in enumerate(self.history_list):
            # working_day is a dict containing data of one working day.
            # Suck that data into the instance self.a_day of the class Day.
            self.a_day.dict_to_day(working_day)
            print(f'History day number {i}:')
            print(self.a_day)

    def append_working_day(self, w_day):
        '''
        Loads the history data from the disk. Appends a new working day
        to that data. Dumps the updated history data back into the disk. 
        w_day is an instance of the class WorkingDay.
        '''
        #print('\nAppending the following working day into the history file:\n')
        #print(w_day)
        self.load_history_data()
        if len(self.history_list) >= HistoryInterface.MAX_DAYS:
            # Remove the oldest day to make room for the newest one
            self.history_list.pop(0)
        # Make a dict of the new day to be appended into self.history_list
        working_day = w_day.day_to_dict()
        self.history_list.append(working_day)
        self.dump_history_data()


if __name__ == '__main__':
    # Testing
    #hd = Day()
    #print(hd)
    hi = HistoryInterface()
#    hi.show_history_data()
#    d1 = Day()
#    hi.append_working_day(d1)
#    hi.show_history_data()
#    hi.append_working_day(d1)
#    hi.show_history_data()
#    hi.dump_history_data()
    hi.load_history_data()
    hi.show_history_data()

