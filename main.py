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
    lyrics = {
        'a' : 'Give you up',
        'b' : 'Let you down',
        'c' : 'Run around and desert you',
        'd' : 'Make you cry',
        'e' : 'Say goodbye',
        'f' : 'Tell a lie and hurt you'
    }
    rickSequence = ['a', 'b', 'c', 'f', 'e', 'd']
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
    
    if rickGuess == rickSequence[0]:
        cls()
        print('Hmm, alright. That might be a fluke, try again')
        print('"Never gonna..."')
        print('A. Give you up')
        print('B. Let you down')
        print('D. Make you cry')
        print('E. Say goodbye')
        print('F. Tell a lie and hurt you')
    
        rickGuess = input('A, B, D, E or F? ').lower()

        if rickGuess == rickSequence[1]:
            cls()
            print('Robots could still be that good, try again')
            print('"Never gonna..."')
            print('B. Let you down')
            print('D. Make you cry')
            print('E. Say goodbye')
            print('F. Tell a lie and hurt you')

            rickGuess = input('B, D, E or F? ').lower()

            if rickGuess == rickSequence[2]:
                cls()
                print('I still dont belive it, try again')
                print('"Never gonna..."')
                print('D. Make you cry')
                print('E. Say goodbye')
                print('F. Tell a lie and hurt you')

                rickGuess = input('D, E or F? ').lower()

                if rickGuess == rickSequence[3]:
                    cls()
                    print('Hmm, just one more time')

                    print('"Never gonna..."')
                    print('D. Make you cry')
                    print('F. Tell a lie and hurt you')
                    
                    rickGuess = input('D, or F? ').lower()
    else:
        cls()
        print('yeah, nice try at fooling me bucko.')

    
        

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