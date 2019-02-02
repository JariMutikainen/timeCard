'''
This file contains the base class Day for the class WorkingDay. 
'''
class Day:
    '''
    Day is an image of a WorkingDay stored in the history file
    on te disk. 

    '''

    # The expected number of workin hours per day:
    TARGET_HOURS = '05:00'

    def __init__(self):
        # Fill in some dummy data 
        self.date = '01.01.2000'
        self.now_at_work = False
        self.morning_balance = '06:00'
        self.dipped_balance = '01:00'
        self.balance = '06:00'
        self.events = [
            ['07:00', 'in', '01:00'],
            ['12:00', 'out', '06:00'],
            
        ]

    def __repr__(self):
        o_string = '-' * 16 + ' Single day data ' + '-' * 16 + '\n'
        dp = self.dipped_balance
        th = Day.TARGET_HOURS
        o_string += f'''
        Date: {self.date}
        Now at work: {self.now_at_work}
        Morning Balance: {self.morning_balance}
        Dipped Balance: {dp}\t(= Morning Balance - {th} hours)
        '''
        o_string += '\n'
        if self.events:
            for event in self.events:
                time, direction, balance = event
                if direction == 'inc':
                    o_string += f'\tAdded manually {time}. -> '
                    o_string += f'Balance = {balance}\n'
                elif direction == 'dec':
                    o_string += f'\tSubtracted manually {time}. -> '
                    o_string += f'Balance = {balance}\n'
                else:
                    o_string += f'\tAt {time} logged {direction: >3s} -> '
                    o_string += f'Balance = {balance}\n'

            o_string += f'\n\tCurrent Balance: {self.balance}\n'
            o_string += '\n' + '-' * 50
        else:
            o_string += "\tNo recorded events were found for today.\n"
        return o_string

    def show_working_day(self):
        '''Prints out the data of the working day.'''
        print(self)

    def dict_to_day(self, working_day):
        ''' Converts a dictionary of a working day into
        an object of the class Day. More often than not this dictionary
        has been loaded from an external .json-file.
        '''
        self.date            = working_day['date']
        self.now_at_work     = working_day['now_at_work']
        self.morning_balance = working_day['morning_balance']
        self.dipped_balance  = working_day['dipped_balance']
        self.balance         = working_day['balance']
        self.events          = working_day['events'][:]
        return self

    def day_to_dict(self):
        ''' Converts an object of the class Day into a dictionary of a 
        working day. More often than not this dictionary
        will be dumped into an external .json-file next.
        '''
        working_day = {}
        working_day['date']              = self.date
        working_day['now_at_work']       = self.now_at_work
        working_day['morning_balance']   = self.morning_balance
        working_day['dipped_balance']    = self.dipped_balance
        working_day['balance']           = self.balance
        working_day['events']            = self.events
        return working_day

if __name__ == '__main__':
    # Testing
    d1 = Day()
    print(d1)
    d_dict = d1.day_to_dict()
    print(d_dict)
    d_dict['date'] = '22.33.4444'
    d2 = Day()
    d2.dict_to_day(d_dict)
    print(d2)
