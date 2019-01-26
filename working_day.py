# This file defines the class, which contains all the methods and attributes
# of one working day. The data is stored in a json file on the disk.

class WorkingDay:

    TARGET_HOURS = '05:00'

    def __init__(self):
        self.date = '26.01.2019'
        self.now_at_work = False
        self.morning_balance = '02:35'
        self.dipped_balance = '-03:35'


