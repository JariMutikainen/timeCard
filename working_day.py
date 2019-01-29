# This file defines the class, which contains all the methods and attributes
# of one working day. The data is stored in a json file on the disk.

import json
from time import strftime
from history_if import HistoryInterface
from hhmm import HhMm # Self made time format of 'HH:MM' - like '03:45'

class WorkingDay:

    TARGET_HOURS = '05:00'
    FILE_OUT = 'temporary.json'
    FILE_IN = 'currently_in.json'
    #FILE_IN = 'currently_out.json'
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
        # json needs the following 'empty' placeholders:
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
        Morning Balance: {self.morning_balance}
            The target number of the working hours per day = ({WorkingDay.TARGET_HOURS})
            must be subtracted from the Morning Balance
            when making the 1st login of the day. This results in the 
            Dipped Balance - the new start balance for the new working day.

        Dipped Balance: {self.dipped_balance}\t(After subtracting the target hours)
        '''
        o_string += '\n'
        if self.events:
            for event in self.events:
                time, direction, balance = event
                o_string += f'\tAt {time} logged {direction: >3s} -> '
                o_string += f'Balance = {balance}\n'
            o_string += f'\n\tCurrent Balance: {self.balance}\n'
            o_string += '\n' + '-' * 50
        else:
            o_string += "\tNo recorded events were found for today.\n"

        return o_string

    def show_working_day(self):
        print(self)

    def dump_working_day(self):
        '''Śtores the data of the working day into the disk.'''
        with open(WorkingDay.FILE_OUT, 'w') as fh:
            frozen = {}
            
            frozen['date']              = self.date
            frozen['now_at_work']       = self.now_at_work
            frozen['morning_balance']   = self.morning_balance
            frozen['dipped_balance']    = self.dipped_balance
            frozen['balance']           = self.balance
            frozen['events']            = self.events
            json.dump(frozen, fh, indent=4, separators=(',', ': '))

    def load_working_day(self):
        '''Loads the data of the working day from the disk.'''
        try:
            with open(WorkingDay.FILE_IN, 'r') as fh:
                unfrozen = json.load(fh)
                self.date            = unfrozen['date']
                self.now_at_work     = unfrozen['now_at_work']
                self.morning_balance = unfrozen['morning_balance']   
                self.dipped_balance  = unfrozen['dipped_balance']
                self.balance         = unfrozen['balance']
                self.events          = unfrozen['events'][:]
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
            # The first time stamp of a new day.
            # Instantiate a history interface and append the previous working 
            # day into the end of the history file before initializing 'today'.
            HistoryInterface().append_working_day(self)
            # Initialize a new working day
            self.date = date_stamp
            self.now_at_work = True
            self.morning_balance = self.balance
            # Subtract the daily target hours from the morning balance.
            t_morning = HhMm(self.morning_balance)
            t_target = HhMm(WorkingDay.TARGET_HOURS)
            self.dipped_balance = str(t_morning - t_target)
            self.balance = self.dipped_balance
            self.events = [ [time_stamp, 'in', self.balance] ]
            self.dump_working_day()
        else:
            # A new login at an already existing day
            self.now_at_work = True
            self.events += [ [time_stamp, 'in', self.balance] ]
            self.dump_working_day()

    def logout(self):
        self.load_working_day()
        time_stamp = strftime('%H:%M')
        date_stamp = strftime('%d.%m.%Y')
        if not self.now_at_work:
            print("\nCan't log you out, because you are already out.\n")
            self.show_working_day()
            return
        if date_stamp != self.date:
            print("You can't start a new working day by making a logout.\n"
                  "Did you forget to logout yesterday?")
            self.show_working_day()
            return
        self.now_at_work = False
        # We have to retrieve the latest login time from the self.events
        # to be able to determine, how many hours to add into the balance
        # at this logout moment.
        last_login_time = self.events[-1][0]
        t1 = HhMm(last_login_time)
        t2 = HhMm(self.balance)
        t3 = HhMm(time_stamp)
        print(f'last-login: {t1}, balance before: {t2}, time stamp: {t3}')
        self.balance = str(t2 + (t3 - t1))
        print(f'Balance after. {self.balance}')


if __name__ == '__main__':
    # Testing
    wd = WorkingDay()
    #wd.dump_working_day()
    print(wd)
    #wd.login()
    wd.logout()
    print(wd)


