# This file contains a class for interfacing the history file on the disk.
# When the 1st login of a new day takes place in working_day.py the
# previous working day is sent ino this interface to be appended into the
# end of the existing history file for future reference.

#from working_day import WorkingDay
import working_day
import jsonpickle

class HistoryInterface():

    def append_working_day(self, w_day):
        print('\nAppending the following working day into the history file:\n')
        print(w_day)

if __name__ == '__main__':
    # Testing
    #hi = HistoryInterface()
    wh = working_day.WorkingDay()
    print(wh)
    #hi.append_working_day()
