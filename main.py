import random
import sys
import os
import time

def cls():
    os.system('cls' if os.name =='nt' else 'clear')

def dice():
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
            print('read the instructions, bucko')
            break

def load():
    # loading cycle
    loadTime = random.randint(5, 10)
    loadCurrent = 0

    while loadCurrent != loadTime:
        cls()
        print('Loading')
        time.sleep(1)
        cls()
        print('Loading.')
        time.sleep(1)
        cls()
        print('Loading..')
        time.sleep(1)
        cls()
        print('Loading...')
        time.sleep(1)
        cls()
        print('Loading....\n (Password:1752764)')
        time.sleep(1)
        loadCurrent += 1

    cls()
    print('Starting program!')
    time.sleep(3)

def captcha():
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
        cls()

def math():
    print('hmm alright, solve the following equation to prove you are human')
    
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

def music():
    rickOptions = ['a', 'b', 'c', 'd', 'e', 'f',]
    rickCorrect = random.choice(rickOptions)
    print('Finish the lyrics if you really are that human')
    print('')
    print('"Never gonna..."')
    print('A. Give you up')
    print('B. Let you down')
    print('C. Run around and desert you')
    print('D. Make you cry')
    print('E. Say goodbye')
    print('F. Tell a lie and hurt you')
    
    rickGuess = input('A, B, C, D, E or F? ').lower()
    lives = 3
    
    while rickGuess != rickCorrect:
        if rickGuess in ['a', 'b', 'c', 'd', 'e', 'f']:
            lives -= 1
            print(f'INCORRECT {lives} ATTEMPTS REMAINING')

        else:
            print('It is not this difficult bro...')

        rickGuess = input('A, B, C, D, E or F? ').lower()
    while lives < 1:
        print('ROBOT DETECTED, HUMANS ENJOY MUSIC...')
        break
    
        

finished = False

while not finished:

    dice()
    load()
    captcha()
    math()
    music()

    print( 'HUMAN VERIFICATION COMPLETE...')
    print('ENTER PASSWORD...')
    password = 1752764
    pw_attempt = input('>').lower()
    if pw_attempt:
        if pw_attempt != password:
            print('FRUADULANT ACTIVITY DETECTED...')
        else:
            print('PERMISSIONS GRANTED')
            pass
    print('Why havent you given up yet?')
    print('Most give up by now')
    print('You were never meant to have access to THE PROGRAM')
    print('SO JUST STOP TRYING!!')