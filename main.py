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
    
    
    print(f"Roll the dice until you get the number {bold}{goal}{white} to start the program")
    print(f"Once you get {bold}{goal}{white} press the S key to start")
    print('_______________________________________________________')
    roll = input(f'Press enter to roll{white}')
    
    # roll to start
    while True:
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        dice3 = random.randint(1, 4)
        diceTotal = dice1 + dice2 + dice3
        print(f"{bold}you rolled... {diceTotal}{white}")
        print('')
        print(f'{white}Save roll?') 
        start = input(f'{bold}[Y/N] {white}').lower()
        print('_______________________________________________________')
        if start == 's':
            if diceTotal == goal:
                print(f'{bold}PROGRAM STARTING...{white}')
                break
            else:
                print(f'{bold}{diceTotal} DOES NOT MATCH {goal}{white}')
                sys.exit('')
        elif start == 'y':
            print(f'{bold}{red}ERROR: DO BETTER NEXT TIME{white}')
            sys.exit('')

        elif start == 'n':
            roll = input(f'Press enter to roll{white}')

        else:
            print(f'{bold}{start} IS NOT RECOGNISED{white}')
            sys.exit('')

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
        print('Loading....')
        time.sleep(1)
        loadCurrent += 1

    cls()
    print('Starting program!')
    time.sleep(3)

def captcha():
    cls()
    print(f'_______________________________________________________')
    print(f'ARE YOU HUMAN?')
    CAPTCHA1 = input(f'{bold}[Y/N]: {white}').lower()

    if CAPTCHA1 in ['y', 'n']:
        sys.exit(f'{red}INSTRUCTIONS FOLLOWED TOO WELL\nROBOT DETECTED.{white}')
    else:
        print(f'{bold}CAPTCHA COMPLETED{white}')
        cls()

def math():
    print(f'{bold}HUMANS LEARN MATH AT A YOUNG AGE, SOLVE THIS MATH EQUATION\n\n{white}')
    
    math1 = random.randint(100, 999)
    math2 = random.randint(1000, 9999)
    mathTotal = math1 * math2
    
    print(f'what is{bold} {math1}{white} multiplied by{bold} {math2}{white} equal to?')
    
    mathAnswer = input(f'{bold}INPUT ANSWER: {white}')
    
    if mathAnswer == mathTotal:
        print(f'{bold}HAHA, THAT WAS A TRICK. HUMANS ARE NOT ACTUALLY GOOD AT MATH.{white}')
        sys.exit(f'{red}ROBOT DETECTED{white}')
    
    else:
        try:
            mathAnswer = int(mathAnswer)
        except:
            print(f'{bold}{red}{mathAnswer} IS NOT A NUMBER{white}')
            sys.exit()
        cls()
        print(f"{bold}HUMAN LEVEL MATH SKILLS DETECTED, CONTINUING VERIFICATION.{white}")
        time.sleep(3)

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

    while True:
        availableOptions = list(lyrics.keys())
        cls()
        print(f'{bold}HUMANS ENJOY MUSIC, SELECT THE CORRECT FOLLOWING LYRICS. {white}')
        failed = False
        for i, correctAnswer in enumerate(rickSequence):
            print('"Never gonna..."')

            for letter in sorted(availableOptions):
                print(f'{letter.upper()}. {lyrics[letter]}')
            print()
            rickGuess = input(f'{bold}CHOOSE FROM: {white}{', '.join([str(x).upper() for x in sorted(availableOptions)])}: ').lower()
    
            if rickGuess == correctAnswer:
                cls()
                if correctAnswer in availableOptions:
                    availableOptions.remove(correctAnswer)

                if i < len(rickSequence):
                    print(f'{bold}A ROBOT COULD HAVE GOTTEN THAT, TRY ANOTHER...{white}')

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

    #dice()
    #load()
    #captcha()
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