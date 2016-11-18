import os
import copy
import sys
import random
import time
import tty
import invent
from invent import inv
from termcolor import cprint, colored


dark_green = '\33[32m'
bright_green = '\33[92m'
dark_groundish = '\33[36m'
bright_groundish = '\33[96m'
white = '\33[97m'
blue = '\33[94m'
gold = '\33[33m'
end_color = '\33[0m'
red = '\33[91m'

blood = red + "≡" + end_color
cure = dark_groundish + "●" + end_color
supercure = bright_groundish + "♥" + end_color
goldenegg = gold + "Q" + end_color
magicweed = dark_green + "♣" + end_color
pitchfork = red + "Ψ" + end_color
zombie = "💀"
roof = gold + "▤" + end_color
door = gold + "▦" + end_color
fence = gold + "▐" + end_color

difficulty = 10
thanksgiving_egg_amount = difficulty * 2
weed_counter = 0


def game_intro():
    """INTRO WITH SPECIAL EFFECTS"""
    f = open("effect.txt", 'r')
    colorlist = ("red", "yellow", "white", "red")
    effect_list = [line[:-1] for line in f]
    f.close()
    maxlen = len(effect_list[0])
    for i in range(round(maxlen/2)):
        os.system('clear')
        for z in range(len(effect_list)):
            cprint(effect_list[z][:i+3] + (" " * ((maxlen-i*2)-3)) + effect_list[z][maxlen-i:],
            random.choice(colorlist))
        time.sleep(0.05)


def game_rules():
    """START SCREEN. RULES, HELP GAME"""
    cprint('Welcome to the Grand Game ZOMBIE CHICKEN FARM!', 'red', attrs=['bold'], file=sys.stderr)
    time.sleep(2)
    print('old macdonald had a farm....')
    print('''                           _.-^-._    .--.
                        .-'   _   '-. |__|
                       /     |_|     \|  |
                      /               \  |
                     /|     _____     |\ |
                      |    |==|==|    |  |
  |---|---|---|---|---|    |--|--|    |  |
  |---|---|---|---|---|    |==|==|    |  |
 ^jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ''')
    time.sleep(2)
    os.system('clear')
    print('\n\n... but after a nuclear holocaust chickens on your farm turned into bloodthirsty zombies...')
    print('now you need to heal your chickens! remember! everywhere rises radioactive mist.')
    cprint('''if you dont want to die too quickly
     hide in abandoned barns & clear infected blood.
     then you gain more time.''', 'red')
    time.sleep(2)
    cprint('\n\nINSTRUCTION: ', 'red', attrs=['bold'], file=sys.stderr)
    print('\nzombie chicken ', zombie, "\t you can cure the zombie using the cure")
    print('\ncure', cure, "\t\t\t cure chickens. you can have only 1 in inventory")
    print('\nsupercure', supercure, "\t\t russian roulette. you can gain 15 cures or... die!")
    print('\nmagic weed', magicweed, "\t\t improves mood before the big fight")
    print('\ngolden egg', goldenegg, "\t\t trophy")
    print('\npitchfork', pitchfork, "\t\t be careful! pitchforks can kill you")
    print('\nblood', blood, "\t\t clear infected blood. than you can heal more chickens")
    print("\nCONTROL:\nA - move left\nS - move down\nD - move right\nW - move up\n")


def credits():
    """PRINT CREDITS"""
    print('''
                                                 _______________________
       _______________________-------------------                       `\
     /:--__                                                              |
    ||< > |                                   ___________________________/
    | \__/_________________-------------------                         |
    |                                                                  |
     |                                                                 |
     |           DESIGNED    &                                          |
     |                       PROGRAMMED                                  |
      |                   BY                                               |
      |                                                                   |
      |   💀 MATEUSZ KACZMARCZYK 💀 MICHAŁ KACZKOWSKI  💀 IKA GRABOŃ         |
      |                                                                   |
       |                                                                  |
       |                                                                  |
       |                                                                  |
      |                                              ____________________|_
      |  ___________________-------------------------                      `\
      |/`--_                                                                 |
      ||[ ]||                                            ___________________/
       \===/___________________--------------------------
        ''')


def getch():
    """BLACK MAGIC, DO NOT TOUCH. FOR IMPUT WITHOUT ENTER"""
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def gameboard(x=31, y=31):
    """ MAKE PURE GAMEBOARD WITHOUT OBSTACLES"""
    lista = []
    for row in range(x):
        lista.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1:
                lista[row].append('X')
            else:
                lista[row].append(' ')
    return lista


def display_board(lista):
    """PRINT LIST FROM GAMEBOARD DEF"""
    for i in lista:
        print('  '.join(i))


def random_building(lista, a, b, c=1):
    """BUILDINGS: RANDOM GENERATOR"""
    ran1 = random.randint(3, 15)
    ran2 = random.randint(7, 12)

    for row in range(ran1, ran1 + ran2):
        for column in range(a, b):
            lista[row][column] = "▦"
        for column in range(a, b, c):
            lista[row][column] = "▤"


def random_fence(lista, lista2):
    """OBSTACLES: RANDOM GENERATOR"""
    for idx, val in enumerate(lista2):
        rand1 = random.randint(4, 6)
        rand2 = random.randint(23, 25)
        zakres_1 = list(range(1, rand1))
        zakres_2 = list(range(rand2, 30))
        for row in zakres_1 + zakres_2:
            lista[row][val] = "+"


def level_board(lista, level=1):
    """DIFFCULTY OF LEVELS. RANDOM OBSTACLES"""
    random_building(lista, 5, 10, 2)
    random_building(lista, 13, 18, 2)
    random_building(lista, 21, 26, 2)
    border_list = [3, 11, 19, 27]
    random_fence(lista, border_list)
    return lista


def house_board(lista):
    """MINI GAME AT BARN - CLEANING BLOOD. USER MUST CLEAN RED OBJECTS AT BOARD"""
    lista_copied = copy.deepcopy(lista)
    for row in range(1, len(lista_copied)-1):
        for column in range(1, len(lista_copied)-1):
            lista_copied[row][column] = " "
    for i in range(2):
        ran1 = random.randint(1, len(lista_copied)-11)
        ran2 = random.randint(3, 10)
        zakres_1 = list(range(ran1, ran1+ran2))
        ran3 = random.randint(1, len(lista_copied)-11)
        ran4 = random.randint(3, 10)
        zakres_2 = list(range(ran3, ran3+ran4))
        blood = red + "☃" + end_color
        for row in zakres_2:
            for column in zakres_1:
                lista_copied[row][column] = blood
    for row in list(range(1, 8)) + list(range(len(lista_copied)-8, len(lista_copied)-1)):
        for column in range(1, len(lista_copied)-1):
            lista_copied[row][column] = "X"
    y = 15
    x = 2
    lista_copied[y][x] = "@"
    var = True
    while var:
        os.system('clear')
        display_board(lista_copied)
        key = getch()
        if key == "x":
            exit()

        should_exit = True
        for row in range(30):
            for column in range(30):
                if lista_copied[row][column] == blood:
                    should_exit = False
        if should_exit:
            os.system('clear')
            boss_fight()
            success = guess(number_generator())
            var = False

        if key == "d" and lista_copied[y][x+1] not in ["X"]:
            lista_copied[y][x] = ' '
            x += 1
            lista_copied[y][x] = "@"
            continue
        elif key == "a" and lista_copied[y][x-1] not in ["X"]:
            lista_copied[y][x] = ' '
            x -= 1
            lista_copied[y][x] = "@"
            continue
        elif key == "w" and lista_copied[y-1][x] not in ["X"]:
            lista_copied[y][x] = ' '
            y -= 1
            lista_copied[y][x] = "@"
            continue
        elif key == "s" and lista_copied[y+1][x] not in ["X"]:
            lista_copied[y][x] = ' '
            y += 1
            lista_copied[y][x] = "@"
            continue


def add_to_inventory(lista, y, x):
    """ADD ITEMS TO INVENTORY"""
    global inv

    if lista[y][x] == "Q":
        if "golden egg" not in inv.keys():
            inv["golden egg"] = 1
        else:
            inv["golden egg"] += 1

    elif lista[y][x] == "💀":
        if "cure" in inv.keys() and inv["cure"] == 1:
            del inv["cure"]
            if "thanksgiving egg" not in inv.keys():
                inv["thanksgiving egg"] = 1
            else:
                inv["thanksgiving egg"] += 1
        elif "cure" in inv.keys() and inv["cure"] > 1:
            inv["cure"] -= 1
            if "thanksgiving egg" not in inv.keys():
                inv["thanksgiving egg"] = 1
            else:
                inv["thanksgiving egg"] += 1
        else:
            print('\33[91mNO CURE NO CHANCES. BYE BYE (YOU DIE)\33[0m')
            time.sleep(3)
            main()

    elif lista[y][x] == "♣":
        global weed_counter
        if "magic weed" not in inv.keys():
            inv["magic weed"] = 1
            weed_counter = 1
        else:
            inv["magic weed"] += 1
            weed_counter += 1

    elif lista[y][x] == "●":
        if "cure" not in inv.keys():
            inv["cure"] = 1
        else:
            del inv["cure"]

    elif lista[y][x] == "♥":
        live_or_die_number = random.randint(1, 6)
        if live_or_die_number == 1:
            print("\33[91mIT WASN'T THE GREATEST IDEA TO EAT IT ALL. YOU DIE\33[0m")
            time.sleep(3)
            main()
        elif "super cure" not in inv.keys():
            inv["cure"] = 15

    elif lista[y][x] == "Ψ":
        print('\33[91mNICE AND SHARP (YOU DIE)\33[0m')
        time.sleep(3)
        main()


def items(lista):
    """INVENTORY GENERATOR"""
    # global difficulty
    # difficulty = 10
    # level_difficulty = difficulty
    items_place = []

    golden_egg = int(difficulty * 0.1) * ["Q"]
    zombie_chicken = int(difficulty * 2) * ["💀"]
    magic_weed = int(difficulty * 2) * ["♣"]
    cure = int(difficulty * 2.2) * ["●"]
    super_cure = 1 * ["♥"]
    pitchfork = int(difficulty * 2) * ["Ψ"]

    all_items = golden_egg + zombie_chicken + magic_weed + cure + super_cure + pitchfork

    while len(all_items) > 0:
        for item in all_items:
            x = random.randint(1, 28)
            y = random.randint(1, 28)
            if lista[y][x] not in ["X", "I", "▤", "+"] and lista[y][x] == ' ':
                lista[y][x] = item
                all_items.remove(item)
            else:
                continue

    return lista


def gameplay(lista):
    """MAIN LOOP: MOVE, TIME, COUNTER"""
    global weed_counter
    global max_time
    global thanksgiving_egg_amount

    max_time = 90
    start_time = time.time()
    actual_time = 0
    y = 15
    x = 2
    lista[y][x] = "@"
    inv["thanksgiving egg"] = 0
    global difficulty

    # actual_time < 90 and inv["thanksgiving egg"] < 20

    while actual_time < max_time and inv["thanksgiving egg"] < thanksgiving_egg_amount:
        os.system('clear')
        real_time = time.time()
        actual_time = real_time - start_time
        display_board(lista)
        # print(start_time)
        invent.print_table(inv, "count,desc")   # MK print tabelki
        print("approx TIME to die: ", int(max_time-actual_time))
        key = getch()
        if weed_counter in [5, 15, 25]:
            os.system('clear')
            chick()
            rock_game()
        if weed_counter in [10, 20, 30]:
            os.system('clear')
            mini_intro()
            time.sleep(2)
            game_start()
        if key == "x":
            exit()
        if key == "d" and lista[y][x+1] not in ["I", "X", "▤", "+"]:
            if lista[y][x+1] not in ["Q", "💀", "♣", "●", "♥", "Ψ"]:
                lista[y][x] = ' '
                x += 1
                lista[y][x] = "@"
            elif lista[y][x+1] in ["Q", "💀", "♣", "●", "♥", "Ψ"]:
                add_to_inventory(lista, y, x + 1)
                lista[y][x] = ' '
                x += 1
                lista[y][x] = "@"
            continue

        elif key == "a" and lista[y][x-1] not in ["I", "X", "▤", "+"]:
            if lista[y][x-1] not in ["Q", "💀", "♣", "●", "♥", "Ψ"]:
                lista[y][x] = ' '
                x -= 1
                lista[y][x] = "@"
            elif lista[y][x-1] in ["Q", "💀", "♣", "●", "♥", "Ψ"]:
                add_to_inventory(lista, y, x - 1)
                lista[y][x] = ' '
                x -= 1
                lista[y][x] = "@"
            continue

        elif key == "w" and lista[y-1][x] not in ["I", "X", "▤", "+"]:
            if lista[y-1][x] not in ["Q", "💀", "♣", "●", "♥", "Ψ", "▦"]:
                lista[y][x] = ' '
                y -= 1
                lista[y][x] = "@"
            elif lista[y-1][x] in ["Q", "💀", "♣", "●", "♥", "Ψ"]:
                add_to_inventory(lista, y-1, x)
                lista[y][x] = ' '
                y -= 1
                lista[y][x] = "@"
            elif lista[y-1][x] in ["▦"]:
                max_time += 120
                house_board(lista)
            continue

        elif key == "s" and lista[y+1][x] not in ["I", "X", "▤", "+"]:
            if lista[y+1][x] not in ["Q", "💀", "♣", "●", "♥", "Ψ", "▦"]:
                lista[y][x] = ' '
                y += 1
                lista[y][x] = "@"
            elif lista[y+1][x] in ["Q", "💀", "♣", "●", "♥", "Ψ"]:
                add_to_inventory(lista, y+1, x)
                lista[y][x] = ' '
                y += 1
                lista[y][x] = "@"
            elif lista[y+1][x] in ["▦"]:
                max_time += 120
                house_board(lista)
            continue
    if actual_time >= max_time:
        print("\33[91mNO TIME TO LOOSE. IT'S TIME TO DIE\33[0m")
        time.sleep(3)
        main()
    if inv["thanksgiving egg"] == thanksgiving_egg_amount:
        print("\33[92mIT'S YOUR LUCKY DAY. TIME TO NEW CHAPTER\33[0m")
        time.sleep(4)
        difficulty += 5
        items(lista)
        gameplay(lista)


def win():
    """ADD THANKSGIVING EGG TO INVENTORY. ITS A TROPHY."""
    global inv
    os.system('clear')
    print("YOU WON !!!")
    time.sleep(2)

    if "golden egg" not in inv.keys():
        inv["golden egg"] = 1
    else:
        inv["golden egg"] += 1


def rock_game():
    """SIMPLE GAME ROCK, PAPER, SCISSORS"""
    global weed_counter
    player = False
    weed_counter += 1
    while player is False:
        cprint("CHOOSE ROCK, PAPER OR SCISSORS OR DIE!\n", "yellow")
        hand = ['ROCK', 'PAPER', 'SCISSORS']
        computer_choice = hand[random.randint(0, 2)]

        player = input("'ROCK', 'PAPER', 'SCISSORS'? ")
        player = player.upper()
        if player == computer_choice:
            print('TIE! ' + player + ' ' + computer_choice)
            player = False
            computer_choice = hand[random.randint(0, 2)]
        elif player == 'PAPER':
            print('☑')
            time.sleep(1)
            if computer_choice == 'SCISSORS':
                os.system('clear')
                print('YOU LOOSE!☠ ' + computer_choice + ' CUT ' + player)
                time.sleep(2)
                player = True
            else:
                print('YOU WIN!✌ ' + player + ' COVERS ' + computer_choice)
                win()
        elif player == 'ROCK':
            print('☁')
            time.sleep(1)
            if computer_choice == 'PAPER':
                os.system('clear')
                print('YOU LOOSE!☠ ' + computer_choice + ' COVERS ' + player)
                time.sleep(2)
                player = True
            else:
                print('YOU WIN!✌ ' + player + ' SMASHES ' + computer_choice)
                win()
        elif player == 'SCISSORS':
            print('✄')
            time.sleep(1)
            if computer_choice == 'ROCK':
                os.system('clear')
                print('YOU LOOSE!☠ ' + computer_choice + ' SMASHES ' + player)
                time.sleep(2)
                player = True
            else:
                print('YOU WIN!✌ ' + player + ' CUT ' + computer_choice)
                win()
        else:
            print('TRY AGAIN')
            player = False
            computer_choice = hand[random.randint(0, 2)]


def chick():
    """PRINT EVIL CHICKEN FOR MINI GAME ROCK, PAPER, SCISSORS"""
    cprint('''
                              .'`  `.      __
                             /      |  ,-'`  `'.
                            ;       '-'         )
                            |              _,.-'
                        _   |_.--.,       (_
                     .'`\`'-'//    \        ''"'-.
                    /  .-\-//`  `\   ;_
                     |   o| o    | __   \   `.
               _,.---'\___.\.__.'    `'. |_   )
           _.-'               _.-""-.   '-.'-'
         ,'                     |   \`.    `.
        /                       ;   |       |
       (_.-'""''---..           /   |      /
                     `'-..___.-'    ;  ,.-'
                           \ 7      ' / |
                           |/_  _  ; /  '
                       .-  /' /` j/ '   |
                       | \|  '   /  |
                       '  `.___.'  ;     '
                       ;          /      |
                        \        /       |
                         `.,__,.'
    ''', 'yellow', attrs=['bold'], file=sys.stderr)
    time.sleep(2)


def mini_intro():
    """INTRO FOR MINI GAME FARM HANGMAN"""
    global life
    global weed_counter
    cprint("Welcome IN FARM HANGMAN!! \n", 'yellow')
    print('''
       __
      /  ('>-
      \__/
       L\_
         ''')
    time.sleep(0.5)
    life = 5
    weed_counter += 1


def load_capital():
    """LOADING TXT FILES WITH LIST OF COUNTRIES AND CAPITALS"""
    capitals_file = open('farm.txt', 'r')
    capitals_array = capitals_file.readlines()
    capitals_file.close()
    return capitals_array[random.randrange(0, len(capitals_array)-1)]


def game_start():
    """INIT GAME, CHANGE LETTERS FOR DASHES"""
    country_capital = load_capital()
    capitaldash = []

    for x in range(len(country_capital)):
        if country_capital[x] == "|":
            country = country_capital[:x-1]
            capital = country_capital[x+2:len(country_capital)-1]
            capitaldash = capital[:]
            break

    for i in range(len(capitaldash)):

        if capitaldash[i] != " ":
            capitaldash = capitaldash[:i] + '_' + capitaldash[i+1:]

    play(country, capital, capitaldash)
    return


def play(country, capital, capitaldash):
    """GUESSING, LOOSE LIFES"""
    global life
    life = 5
    badletters = []

    while life > 0:
        os.system('clear')
        cprint("\n\nSOMETHING FROM " + country + "?", 'cyan', attrs=['bold'], file=sys.stderr)
        print("word: ", capitaldash)
        print("\nBADLETTERS ", badletters, "\nYOUR LIFES", life)
        hangman()
        userinput = input("enter letter or word: ")
        userinput = userinput.upper()

        if len(userinput) > 1:
            if userinput == capital:
                win()
                break
            else:
                badletters.append(userinput)
                life -= 2

        else:
            if userinput in capital:
                for x in range(len(capital)):
                    if capital[x] == userinput:
                        capitaldash = capitaldash[:x] + userinput + capitaldash[x+1:]
                if capital == capitaldash:
                    win()
                    break

            else:
                badletters.append(userinput)
                life -= 1

    return


def hangman():
    """VISUALIZE HANGMAN"""

    if life == 6:
        cprint('''
   ______
  |      |
  |
  |
  |
 _|_          ''', 'blue', attrs=['bold'], file=sys.stderr)

    elif life == 5:
        cprint('''
   ______
  |      |
  |      O
  |
  |
 _|_          ''', 'blue', attrs=['bold'], file=sys.stderr)

    elif life == 4:
        cprint('''
   ______
  |      |
  |      O
  |      |
  |
 _|_          ''', 'blue', attrs=['bold'], file=sys.stderr)

    elif life == 3:
        cprint('''
   ______
  |      |
  |      O
  |     /|
  |
 _|_          ''', 'blue', attrs=['bold'], file=sys.stderr)

    elif life == 2:
        cprint('''
   ______
  |      |
  |      O
  |     /|\\
  |
 _|_          ''', 'blue', attrs=['bold'], file=sys.stderr)

    elif life <= 1:
        cprint('''
   ______
  |      |
  |      O
  |     /|\\
  |     / \\
 _|_          ''', 'blue', attrs=['bold'], file=sys.stderr)


def boss_fight():
    f = open("boss.txt", 'r')
    colorlist = ("red", "white", "red")
    effect_list = [line[:-1] for line in f]
    f.close()
    maxlen = len(effect_list[0])
    for i in range(round(maxlen/2)):
        os.system('clear')
        for z in range(len(effect_list)):
            cprint(effect_list[z][:i+3] + (" " * ((maxlen-i*2)-3)) + effect_list[z][maxlen-i:],
            random.choice(colorlist))
        time.sleep(0.05)


def win2():
    """VICTORY SCREEN"""
    os.system("clear")
    cprint('''


    ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗
    ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
    ██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝
    ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝
     ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║
      ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝


    ''', 'red')
    time.sleep(2)
    if "golden egg" not in inv.keys():
        inv["golden egg"] = 1
    else:
        inv["golden egg"] += 1


def number_generator():
    """NUMBER GENERATOR"""
    numlist = []
    for number in range(0, 10):
        numlist.append(number)
    first_number = random.choice(numlist)
    numlist.remove(first_number)
    second_number = random.choice(numlist)
    numlist.remove(second_number)
    the_number = (first_number, second_number)
    if first_number != second_number:
        return the_number


def guess(the_number):
    """GUESS THE NUMBER MINI GAME"""
    boss()
    cprint("\nGUESS THE NUMBER (2 digit) OR DIE!", "red", attrs=['bold'], file=sys.stderr)
    cprint("COLD        This digit is not correct.", "blue")
    cprint("WARM        This digit is correct in wrong position.", "yellow")
    cprint("HOT         This digit is correct in the right position.", "red")

    # print(the_number)
    try_number = 1
    while True:
        if try_number > 10:
            print("\nYOU LOOSE.\n\n")
            success = "no"
            return False, success
        guessed_number = []
        guess = input("\nGuess № {}: ".format(try_number))

        if len(guess) == 2:
            try:
                for number in guess:
                    guessed_number.append(int(number))

            except ValueError:
                print("TWO NUMBERS YOU VILLAIN!!")
            tuple_number = tuple(guessed_number)
            if the_number == tuple_number:
                success = "yes"
                win2()
                return False, success
            else:
                for index, value in enumerate(tuple_number):
                    if tuple_number[index] == the_number[index]:
                        cprint("HOT", "red")
                    elif tuple_number[index] in the_number:
                        cprint("WARM", "yellow")
                    elif tuple_number[index] not in the_number:
                        cprint("COLD", "blue")
                try_number += 1
        else:
            print("\nTWO NUMBERS YOU VILLAIN!!\n")
    return success


def boss():
    """BOSS FIGHT: GUESSING GAME"""
    cprint('''
           ___
         .';:;'.
        /_' _' /\   __
        ;a/ e= J/-'"  '.
        \ ~_   (  -'  ( ;_ ,.
         L~"'_.    -.  \ ./  )
         ,'-' '-._  _;  )'   (
       .' .'   _.'")  \  \(  |
      /  (  .-'   __\{`', \  |
     / .'  /  _.-'   "  ; /  |
    / /    '-._'-,     / / \ (
 __/ (_    ,;' .-'    / /  /_'-._
    ''', 'red', attrs=['bold'], file=sys.stderr)


def main():
    """MAIN MENU"""
    os.system('clear')
    game_rules()
    time.sleep(2)

    while True:
        cprint("\nMENU:\n1: PLAY \n2: CREDITS \n3: EXIT\n\n", 'red', attrs=['bold'], file=sys.stderr)
        pick = input("PICK THE NUMBER: ")

        if pick == "1":                                                         # main menu
            level = items(level_board(gameboard(), 10))
            gameplay(level)
        elif pick == "3":
            os.system('clear')
            sys.exit()
        elif pick == "2":
            os.system('clear')
            credits()
        else:
            print('INVALID COMMAND')  # errors, invalid command from user
            os.system('clear')

if __name__ == "__main__":
    game_intro()
    time.sleep(2)
    time.sleep(1)
    main()
