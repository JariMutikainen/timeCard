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

    def take_action(self):
        action = self.actions[self.answ]
        action()


            def login,
            def logout,
            def show_day,
            def show_history,
            def add_hours,
            def subtract_hours,
            def quit


if __name__ == '__main__':
    # Testing
    m1 = Menu()
    m1.get_user_input()
    m1.take_action()
