# This file defines the class, which contains all the methods and attributes
# of one working day. The data is stored in a json file on the disk.

import jsonpickle

class WorkingDay:

    TARGET_HOURS = '05:00'

    def __init__(self):
#        self.date = '26.01.2019'
#        self.now_at_work = True
#        self.morning_balance = '02:35'
#        self.dipped_balance = '-03:35'
#        self.balance = '01:35'
#        self.events = [ ('07:03', 'in', '-03:35'), 
#                        ('11:33', 'out', '01:35'),
#                        ('12:00', 'in', '01:35') ]
        self.date = ''
        self.now_at_work = None
        self.morning_balance = ''
        self.dipped_balance = ''
        self.balance = ''
        self.events = []

    def __repr__(self):
        o_string = '-' * 16 + ' Working day data ' + '-' * 16 + '\n'
        o_string += f'''
        Date: {self.date}
        Now at work: {self.now_at_work}
        Morning balance: {self.morning_balance}
        Dipped balance: {self.dipped_balance}\t(substracted target hours)
        Current balance: {self.balance}
        '''
        o_string += '\n'
        for event in self.events:
            time, dire, bala = event
            o_string += f'\tAt {time} logged {dire: >3s} -> '
            o_string += f'Balance = {bala}\n'
        o_string += '\n' + '-' * 50
        return o_string

    def dump_working_day(self):
        '''Śtores the working day into the disk.'''
        with open('today.json', 'w') as fh:
            frozen = jsonpickle.encode(self)
            fh.write(frozen)

def load_working_day():
    with open('today.json', 'r') as fh:
        contents = fh.read()
        return jsonpickle.decode(contents)




if __name__ == '__main__':
    # Testing
#    wd = WorkingDay()
#    wd.dump_working_day()
    wd = load_working_day()
    print(wd)


