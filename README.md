# timeCard
This is a Python 3.7 based timeCard program. It keeps track of the working 
hours of an employee. When the emplyee comes to work he logs in and when
he leaves he logs out. The program creates and stores the time stamps of 
these events. The target number of the daily hours is a configurable
parameter to the program. The program maintains a 'balance of the working 
hours' by comparing the number of the actual daily working hours to the 
target number of the daily working hours. If the actual is smaller than
the target, the difference is substracted from the balance. If the actual
is larger than the target the difference is added to the balance. 
The balance can be either negative or positive. Normally the boss of the 
office insists, that the balance should be kept positive.
