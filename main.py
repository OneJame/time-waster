import random
import sys
import os
import time

#Colours / Text Effects!
red = '\033[91m'
white = '\033[0m'
bold = '\033[1m'

def cls():
    os.system('cls' if os.name =='nt' else 'clear')

def dice():
    goal = random.randint(3,12)
    
    
    print(f"{bold}Roll the dice until you get the number {goal} to start the program")
    print(f"Once you get {goal} press the S key to start")
    print('_______________________________________________________')
    roll = input(f'Press enter to roll{white}')
    
    # roll to start
    while True:
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        dice3 = random.randint(1,4)
        diceTotal = dice1 + dice2 + dice3
        print(f"you rolled... {diceTotal}")
        print('')
        print(f'{bold}Save roll?') 
        start = input(f'[Y/N] {white}').lower()
        print('_______________________________________________________')
        if start == 's':
            if diceTotal == goal:
                print('PROGRAM STARTING...')
                break
            else:
                sys.exit('Wrong number buddy')
        if start != 'y':
            roll = input(f'{bold}Press enter to roll{white}')
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

    comments = [
        'Hmmm, might be a fluke, try another one.',
        'Robots could still be that good, do another one.'
        'I still dont belive it, do it again.',
        'Hmm, just once more',
        'May aswell keep going now, youve come this far',
        'OK, one more for real this time.'

    ]
    rickSequence = ['a', 'b', 'c', 'f', 'e', 'd']

    while True:
        availableOptions = list(lyrics.keys())
        cls()
        print('Finish the lyrics if you really are that human')
        failed = False
        for i, correctAnswer in enumerate(rickSequence):
            print('"Never gonna..."')

            for letter in sorted(availableOptions):
                print(f'{letter.upper()}. {lyrics[letter]}')
            print()
            rickGuess = input(f'Choose from {', '.join([str(x).upper() for x in sorted(availableOptions)])}: ').lower()
    
            if rickGuess == correctAnswer:
                cls()
                if correctAnswer in availableOptions:
                    availableOptions.remove(correctAnswer)

                if i < len(rickSequence):
                    print(comments[min(i, len(comments)-1)])

            elif rickGuess not in availableOptions:
                cls()
                print('not this hard bucko...')
            else:
                cls()
                print('ROBOT DETECTED')
                time.sleep(2)
                failed = True
                break

        if not failed:
            print('hmm, alright then...')
            return


    
        

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