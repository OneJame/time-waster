import random
import sys
import os

def cls():
    os.system('cls' if os.name =='nt' else 'clear')

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
    diceTotal = dice1 + dice2 + dice3
    print(f"you rolled... {diceTotal}")
    print('')
    print('Save roll?') 
    start = input('[Y/N] ').lower()
    print('_______________________________________________________')
    if start == 's':
        if diceTotal == goal:
            print('PROGRAM STARTING...')
            break
        else:
            sys.exit('Wrong number buddy')
    if start != 'y':
        roll = input('Press enter to roll')
    elif start == 'y':
        sys.exit('Read the instructions next time')

# CAPTHA
cls()
print('_______________________________________________________')
print('ARE YOU HUMAN?')
CAPTCHA1 = input('[Y/N] ').lower()

if CAPTCHA1 == 'y':
    print('Why do you follow instructions so well then?')
    sys.exit('ROBOT DETECTED')
elif CAPTCHA1 == 'n':
    sys.exit('ROBOT DETECTED')
else:
    print('hmm alright, solve the following equation  to prove you are human')

# math
math1 = random.randint(100, 999)
math2 = random.randint(1000, 9999)
mathTotal = math1 * math2

print(f'what is {math1} multiplied by {math2} equal to?')

while True:
    try:
        mathAnswer = int(input('INPUT ANSWER: '))
        break
    except ValueError:
        print('That is not a number bro')


if mathAnswer == mathTotal:
    print('No human is that good at math')
    sys.exit('ROBOT DETECTED')

else:
    cls()
    print("That's so extremely wrong... very human of you")


rickOptions = ['give you up', 'let you down', 'run around and desert you', 'make you cry', 'say goodbye', 'tell a lie and hurt you']
rickCorrect = random.choice('rickOptions')
print('')