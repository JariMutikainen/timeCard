# This file defines the class, which contains all the methods and attributes
# of one working day. The data is stored in a json file on the disk.

import jsonpickle
from time import strftime
#from history_if import HistoryInterface

class WorkingDay:

    TARGET_HOURS = '05:00'
    TODAY_FILE = 'currently_out.json'
#    TODAY_FILE = 'currently_in.json'
#    TODAY_FILE = 'today.json'

    def __init__(self):
#        Keep the out commented lines as a remainder of the data structure.
#        self.date = '26.01.2019'
#        self.now_at_work = True
#        self.morning_balance = '02:35'
#        self.dipped_balance = '-03:35'
#        self.balance = '01:35'
#        self.events = [ ('07:03', 'in', '-03:35'), 
#                        ('11:33', 'out', '01:35'),
#                        ('12:00', 'in', '01:35') ]
        # jsonpickle needs the following 'empty' placeholders:
        self.date = ''
        self.now_at_work = None
        self.morning_balance = ''
        self.dipped_balance = ''
        self.balance = ''
        self.events = []
        # Load the data from an external file
        self.load_working_day()

    def __repr__(self):
        o_string = '-' * 16 + ' Working day data ' + '-' * 16 + '\n'
        o_string += f'''
        Date: {self.date}
        Now at work: {self.now_at_work}
        Morning balance: {self.morning_balance}
        Dipped balance: {self.dipped_balance}\t(subtracted target hours)
        Current balance: {self.balance}
        '''
        o_string += '\n'
        if self.events:
            for event in self.events:
                time, direction, balance = event
                o_string += f'\tAt {time} logged {direction: >3s} -> '
                o_string += f'Balance = {balance}\n'
            o_string += '\n' + '-' * 50
        else:
            o_string += "\tNo recorded events were found for today."
        return o_string

    def show_working_day(self):
        print(self)

    def dump_working_day(self):
        '''Śtores the data of the working day into the disk.'''
        with open(WorkingDay.TODAY_FILE, 'w') as fh:
            frozen = jsonpickle.encode(self)
            fh.write(frozen)

    def load_working_day(self):
        '''Loads the data of the working day from the disk.'''
        try:
            with open(WorkingDay.TODAY_FILE, 'r') as fh:
                contents = fh.read()
                unfrozen = jsonpickle.decode(contents)
                self.date = unfrozen.date
                self.now_at_work = unfrozen.now_at_work
                self.morning_balance = unfrozen.morning_balance
                self.dipped_balance = unfrozen.dipped_balance
                self.balance = unfrozen.balance
                self.events = unfrozen.events
        except FileNotFoundError:
            self.date = '17.06.1964'
            self.now_at_work = False
            self.morning_balance = '00:00'
            self.dipped_balance = '-05:00'
            self.balance = '-05:00'
            self.events = []

    def login(self):
        self.load_working_day()
        time_stamp = strftime('%H:%M')
        date_stamp = strftime('%d.%m.%Y')
        if self.now_at_work:
            print("\nCan't log you in, because you are already in.\n")
            #self.show_working_day()
            return
        if date_stamp != self.date:
            # The first stamp of a new day.
            # Instantiate a history interface and append the previous working 
            # day into the end of the history file before initializing 'today'.
            #h1 = HistoryInterface()
            #h1.append_working_day(self)
            # Initialize a new working day
            pass


if __name__ == '__main__':
    # Testing
    wd = WorkingDay()
    print(wd)
    #wd.login()
    #print(wd)


