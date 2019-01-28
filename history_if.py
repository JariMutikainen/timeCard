# This file contains a class for interfacing the history file on the disk.
# When the 1st login of a new day takes place in working_day.py the
# previous working day is sent ino this interface to be appended into the
# end of the existing history file for future reference.


class HistoryInterface:

    def __init__(self):
        self.history_list =[]

    def append_working_day(self, w_day):
        print('\nAppending the following working day into the history file:\n')
        print(w_day)

if __name__ == '__main__':
    # Testing
    #hi = HistoryInterface()
    #hi.append_working_day()
    pass