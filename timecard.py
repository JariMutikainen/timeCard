'''
This is a Python 3.7 based timeCard program. It keeps track of the working
hours of an employee. When the emplyee comes to work he logs in and when he
leaves he logs out. The program creates and stores the time stamps of these
events. The target number of the daily hours is a configurable parameter to
the program. The program maintains a 'balance of the working hours' by
comparing the number of the actual daily working hours to the target number
of the daily working hours. If the actual is smaller than the target, the
difference is substracted from the balance. If the actual is larger than
the target the difference is added to the balance. The balance can be either
negative or positive. Normally the boss of the office insists, that the
balance should be kept positive.'''

import sys
from history_if import HistoryInterface
from working_day import WorkingDay

class Menu:
    '''Displays the menu actions available. Gets the user input. Invokes
    the action selected by the user.'''

    def __init__(self):
        self.actions = {
            'i': self.login,
            'o': self.logout,
            'd': self.show_day,
            'h': self.show_history,
            'a': self.add_hours,
            's': self.subtract_hours,
            'q': self.quit
        }
        self.answ = 'foo'

    def get_user_input(self):
        '''Prompts the user for next action until a valid answer is given.'''
        while self.answ not in self.actions.keys():
            print('''
                Select one of the following actions:

                Log In           = 'i'
                Log Out          = 'o'
                Show Day         = 'd'
                Show History     = 'h'
                Add Hours        = 'a'
                Subtract Hours   = 's'
                Quit             = 'q'
                --------------------------> ''', end='')
            self.answ = input()
            print('') # An empty line

    def take_action(self):
        '''Turns the user's choice into action.'''
        action = self.actions[self.answ]
        action()
        self.answ = 'foo' # Prevent the program from going crazy.

    def login(self):
        '''Generates a time stamp and logs the user in.'''
        print('\nThe working day summary after the Log In is as follows:')
        WorkingDay().login()

    def logout(self):
        '''Generates a time stamp and logs the user out.'''
        print('\nThe working day summary after the Log Out is as follows:')
        WorkingDay().logout()

    def show_day(self):
        '''Shows the data of the current working day.'''
        print('\nThe working day summary is as follows:')
        WorkingDay().show_working_day()

    def show_history(self):
        '''Shows the data collected into the history file.'''
        HistoryInterface().show_history_data()

    def add_hours(self):
        '''Provides the user with an opportunity to manually increase
           the current working hour balance.'''
        time_s = input('How much time do you want to add to your balance?\n'
                       'Use the format HH:MM - i.e. 01:35 for example: ')
        print('\nThe working day summary after the Addition is as follows:')
        WorkingDay().increment(time_s)

    def subtract_hours(self):
        '''Provides the user with an opportunity to manually decrease
           the current working hour balance.'''
        time_s = input('How much time '
                       'do you want to subtract from your balance?\n'
                       'Use the format HH:MM - i.e. 01:35 for example: ')
        print('\nThe working day summary after the Subtraction is as follows:')
        WorkingDay().decrement(time_s)

    def quit(self):
        '''Quits the program.'''
        sys.exit()

    def run_program(self):
        '''Runs the program in an infinite loop - until the user selects
           to quit.'''
        while True:
            self.get_user_input()
            self.take_action()



if __name__ == '__main__':
    m1 = Menu()
    m1.run_program()
    # Testing
    #m1.get_user_input()
    #m1.take_action()
