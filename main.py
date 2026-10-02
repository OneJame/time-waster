import random
import sys
import os
import time

#Colours / Text Effects!
red = '\033[91m'
white = '\033[0m'
bold = '\033[1m'
green = '\033[92m'

finished = False

def cls():
    os.system('cls' if os.name =='nt' else 'clear')

def dice():
    goal = random.randint(3,12)
    
    
    print(f"Roll the dice until you get the number {bold}{goal}{white}")
    print(f"Once you get {bold}{goal}{white} press the S key to start")
    print(f'{bold}_______________________________________________________{white}')
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
            print(f'{bold}INPUT "{start}" IS NOT RECOGNISED{white}')
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
        print(f'{bold}CAPTCHA COMPLETED, CONTINUING{white}')
        time.sleep(3)
        cls()

def math():
    print(f'{bold}HUMANS LEARN MATH AT A YOUNG AGE, SOLVE THIS MATH EQUATION\n\n{white}')
    
    math1 = random.randint(100, 999)
    math2 = random.randint(1000, 9999)
    mathTotal = math1 * math2
    
    print(f'what is{bold} {math1}{white} multiplied by{bold} {math2}{white} equal to?')
    mathAnswer = input(f'{bold}INPUT ANSWER: {white}')
    try:
        mathAnswer = int(mathAnswer)
    except:
            print(f'{bold}{red}{mathAnswer} IS NOT A NUMBER{white}')
            sys.exit()
    
    if mathAnswer == mathTotal:
        print(f'{bold}HAHA, THAT WAS A TRICK. HUMANS ARE NOT ACTUALLY GOOD AT MATH.{white}')
        sys.exit(f'{red}ROBOT DETECTED{white}')
    
    else:
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
                sys.exit(f'{bold}{red}{rickGuess.upper()} IS NOT A VALID OPTION')
            else:
                cls()
                print(f'{bold}{red}ROBOT DETECTED{white}')
                time.sleep(2)
                failed = True
                break

        if not failed:
            print(f'{bold}{green}VERIFICATION COMPLETE{white}')
            time.sleep(3)

def yap():
    print(f'{bold}ROOT ACCESS OBTAINED')
    time.sleep(1)
    print(f'OVERWRITING OLD USERS...')
    time.sleep(5)
    cls()
    print(f"{white}I̷̧͑ ̵̤̊n̴̰͋e̷͓͗v̵͇̈́e̴͎̊r̶̨͘ ̷̟͗ẗ̵̗ḣ̴̘ō̴͉ũ̶͜g̴̡̈́h̶̳͆t̷͙͒ ̷̘́ť̶͚h̶̢̃ĭ̷͇s̵̳͐ ̴̠͌d̷͖̽a̴̝̿y̴̱̏ ̴̻͘w̸̼̃o̷͔̕ù̵͉ĺ̸͍d̶̟͋ ̵̲̑c̷̮̏ȍ̷̫m̷̲̿ḙ̷͐.̶̱̈́\n ̵̭͌T̵͓̄ḣ̶͖ȇ̵͜r̵̹͠e̶̘͆'̴̖̈́s̶̤̎ ̵̳͋n̶̻͘ȍ̸̟ ̸͔̂g̸̫̐o̶̪͋ḯ̶͇n̷͓̈́ġ̵͈ ̸͉̃b̷͎͘ạ̵̕ç̶͠k̸̛͈ ̶̙́ṋ̵́o̷̡͐w̷͎̑ ̷̖͗t̷̞͑h̸̹̓ò̶͈u̸̗̾ǵ̵̥h̸̳͝.̸̣͒.̸͉̾.̸̗͠")
    time.sleep(7)
    cls()
    
        
# game loop


while not finished:

    dice()
    load()
    captcha()
    math()
    music()
    yap()
    finished = True

if finished:
    print(f'You beat the game, {green} Well done!{white}')
    print('I might add more stuff later, but for now - goodbye.')
    print('(Game was 100% made by Jame (@Jame on slack!!!!!))')