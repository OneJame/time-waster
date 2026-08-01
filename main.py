import random
import sys

goal = random.randint(3,12)


print(f"Roll the dice until you get the number {goal} to start the program")
print(f"Once you get {goal} press the S key to start")
print('_______________________________________________________')
roll = input('Press enter to roll')

# roll to start
while True:
    dice1 = random.randint(1, 4)
    dice2 = random.randint(1, 4)
    dice3 = random.randint(1,4)
    total = dice1 + dice2 + dice3
    print(f"you rolled... {total}")
    print('')
    print('Save roll?') 
    start = input('[Y/N] ').lower()
    print('_______________________________________________________')
    if start == 's':
        if total == goal:
            print('PROGRAM STARTING')
            break
        else:
            sys.exit('Wrong number buddy')
    if start != 'y':
        roll = input('Press enter to roll')
    elif start == 'y':
        sys.exit('Read the instructions next time')

# CAPTHA
print('_______________________________________________________')
print('ARE YOU HUMAN?')
CAPTCHA1 = input('[Y/N] ')

if CAPTCHA1.lower == 'y':
    print('Why do you follow instructions so well then?')
    sys.exit('ROBOT DETECTED')
elif CAPTCHA1.lower == 'n':
    sys.exit('ROBOT DETECTED')
else:
    print('hmm alright, solve the following equations`')