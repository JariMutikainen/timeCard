'''
This file defines the class, which contains all the methods and attributes
of one working day. The data is stored in a json file on the disk.
'''

import json
from time import strftime
from day import Day
from history_if import HistoryInterface
from hhmm import HhMm # Self made time format of 'HH:MM' - like '03:45'

class WorkingDay(Day):
    '''
    WorkingDay inherits the __repr__()-method from the Day.
    It inherits the __init__()-method from the Day, but extends
    that method by fetching the contents for the instance attributes
    from the disk.

    A WorkingDay consists of logins and logouts. Each time the user logs
    in or out the time stamp of the event is recored and stored in the
    list of events. All the instance data is maintained in an external file
    on the disk. Each time a new event takes place the data is loaded from
    the disk, the new event is recorded an the data is dumped back into the
    disk. In addition to the login and logout methods this class offers
    methods for manually adding or subtracting time from the balance.
    '''

    #FILE_OUT = 'temporary.json'
    #FILE_IN = 'currently_in.json'
    #FILE_IN = 'currently_out.json'
    FILE_IN = 'today.json'
    FILE_OUT = 'today.json'

    def __init__(self):
        super().__init__()
        self.load_working_day() # Load the data from an external file

    def dump_working_day(self):
        '''Śtores the data of the working day into the disk.'''
        with open(WorkingDay.FILE_OUT, 'w') as fh:
            # Make a dict of the working day to be stored in an external
            # .json-file on the disk.
            frozen = self.day_to_dict()
            json.dump(frozen, fh, indent=4, separators=(',', ': '))

    def load_working_day(self):
        '''Loads the data of the working day from the disk.'''
        try:
            with open(WorkingDay.FILE_IN, 'r') as fh:
                unfrozen = json.load(fh)
                # unfrozen is a dict containing data of one working day.
                # Suck that data into the instance self of the class
                # WorkingDay.
                self.dict_to_day(unfrozen)

        except FileNotFoundError:
            self.date = '17.06.1964'
            self.now_at_work = False
            self.morning_balance = '00:00'
            self.dipped_balance = '00:00'
            self.balance = '00:00'
            self.events = []

    def login(self):
        '''
        This method records the time stamp of a login event and updates
        the data of the working day on the disk accordingly.
        '''
        self.load_working_day()
        time_stamp = strftime('%H:%M')
        date_stamp = strftime('%d.%m.%Y')
        day_name = strftime('%A')
        if self.now_at_work:
            print("\nCan't log you in, because you are already in.\n")
            self.show_working_day()
            return
        if date_stamp != self.date:
            # The first time stamp of a new day.
            # Instantiate a history interface and append the previous working
            # day into the end of the history file before initializing 'today'.
            HistoryInterface().append_working_day(self)
            # Initialize a new working day
            self.date = date_stamp
            self.day_name = day_name
            self.now_at_work = True
            self.morning_balance = self.balance
            # Subtract the daily target hours from the morning balance.
            t_morning = HhMm(self.morning_balance)
            # The TARGET_HOURS for a weekend day is Zero.
            if self.day_name in ('Saturday', 'Sunday'):
                t_target = HhMm('00:00')
            else:
                t_target = HhMm(Day.TARGET_HOURS)
            self.dipped_balance = str(t_morning - t_target)
            self.balance = self.dipped_balance
            self.events = [ [time_stamp, 'in', self.balance] ]
            self.dump_working_day()
            self.show_working_day()
        else:
            # A new login at an already existing day
            self.now_at_work = True
            self.events += [ [time_stamp, 'in', self.balance] ]
            self.dump_working_day()
            self.show_working_day()

    def logout(self):
        '''
        This method records the time stamp of a logout event and updates
        the data of the working day on the disk accordingly.
        '''
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
        #last_login_time = self.events[-1][0]
        last_login_time = self.get_latest_login()
        t1 = HhMm(last_login_time)
        t2 = HhMm(self.balance)
        t3 = HhMm(time_stamp)
        print(f'last-login: {t1}, balance before: {t2}, time stamp: {t3}')
        self.balance = str(t2 + (t3 - t1))
        print(f'Balance after. {self.balance}')
        self.events += [[time_stamp, 'out', self.balance]]
        self.dump_working_day()
        self.show_working_day()

    def get_latest_login(self):
        '''
        Returns the time stamp of the latest login. The important thing
        is not to return the last time stamp of the current day but
        rather the last time stamp of the current day with "in" as
        the direction. Bug fix 2.3.2019 by Jari M.
        '''
        indx = -1
        while self.events[indx][1] != "in": #events[][1] contains the direction
            indx -= 1
        return self.events[indx][0] # events[][0] contains the time stamp

    def increment(self, time_s):
        '''
        Increments the Current Balance by time_s. time_s is a string in the
        format '02:34'
        '''
        self.load_working_day()
        self.balance = str(HhMm(self.balance) + HhMm(time_s))
        self.events += [[time_s, 'inc', self.balance]]
        self.dump_working_day()
        self.show_working_day()

    def decrement(self, time_s):
        '''
        Decrements the Current Balance by time_s. time_s is a string in the
        format '02:34'
        '''
        self.load_working_day()
        self.balance = str(HhMm(self.balance) - HhMm(time_s))
        self.events += [[time_s, 'dec', self.balance]]
        self.dump_working_day()
        self.show_working_day()


if __name__ == '__main__':
    # Testing
    wd = WorkingDay()
    #wd.dump_working_day()
    #print(wd)
    #wd.login()
    wd.logout()
    #wd.increment('02:30')
    #print(wd)
    #wd.decrement('01:20')
    #print(wd)
