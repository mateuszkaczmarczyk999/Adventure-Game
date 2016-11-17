import os
import copy
import sys
import random
import time
import tty
import invent                       ##### MK import inventory_game
from invent import inv              ##### MK import inventory_game

#lista naszych kolorów
dark_green = '\33[32m'
bright_green = '\33[92m'
dark_groundish = '\33[36m'
bright_groundish = '\33[96m'
white = '\33[97m'
blue = '\33[94m'
gold = '\33[33m'
end_color = '\33[0m'
red = '\33[91m'


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def gameboard(x=31, y=31):
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
    for i in lista:
        print('  '.join(i))


def move_on_board(lista):
    start_time = time.time()
    actual_time = 0
    y = 15
    x = 2
    lista[y][x] = "@"
    inv["thanksgiving egg"] = 0

    #actual_time < 90 and inv["thanksgiving egg"] < 20

    while actual_time < 90 and inv["thanksgiving egg"] < 20:
        os.system('clear')
        real_time = time.time()
        actual_time = real_time - start_time
        display_board(lista)
        #print(start_time)
        invent.print_table(inv, "count,desc")   ### MK print tabelki
        key = getch()
        if key == "x":
            exit()
        if key == "d" and lista[y][x+1] not in ["I", "X", "▤", "+"]:
            if lista[y][x+1] not in ["Q", "💀", "♣", "●", "♥", "Ψ"]:
                lista[y][x] = ' '
                x += 1
                lista[y][x] = "@"
            elif lista[y][x+1] in ["Q", "💀", "♣", "●", "♥", "Ψ"]:
                add_to_inventory(lista, y, x +1)
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
                add_to_inventory(lista, y, x -1)
                lista[y][x] = ' '
                x -= 1
                lista[y][x] = "@"
            continue

        elif key == "w" and lista[y-1][x] not in ["I", "X", "▤", "+"]:
            if lista[y-1][x] not in ["Q", "💀", "♣", "●", "♥", "Ψ"]:
                lista[y][x] = ' '
                y -= 1
                lista[y][x] = "@"
            elif lista[y-1][x] in ["Q", "💀", "♣", "●", "♥", "Ψ"]:
                add_to_inventory(lista, y-1, x)
                lista[y][x] = ' '
                y -= 1
                lista[y][x] = "@"
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
                house_board(lista)
            continue
    if actual_time >= 90:
        print("\33[91mNO TIME TO LOOSE. IT'S TIME TO DIE\33[0m")
    elif inv["thanksgiving egg"] == 20:
        print("\33[92mIT'S YOUR LUCKY DAY\33[0m")


def random_building(lista, a, b, c=1):
    ran1 = random.randint(3, 15)
    ran2 = random.randint(7, 12)

    for row in range(ran1, ran1 + ran2):
        for column in range(a, b):
            #roof = bright_groundish + "=" + end_color
            lista[row][column] = "▦"
        for column in range(a, b, c):
            #roof2 = bright_groundish + "I" + end_color
            lista[row][column] = "▤"

def random_fence(lista, lista2):
    for idx, val in enumerate(lista2):
        rand1 = random.randint(4, 6)
        rand2 = random.randint(23, 25)
        zakres_1 = list(range(1, rand1))
        zakres_2 = list(range(rand2,30))
        for row in zakres_1 + zakres_2:
            #fence = dark_green + "+" + end_color
            lista[row][val] = "+"

def level_board(lista, level=1):
    random_building(lista, 5, 10, 2)
    random_building(lista, 13, 18, 2)
    random_building(lista, 21, 26, 2)
    border_list = [3, 11, 19, 27]
    random_fence(lista, border_list)
    return lista

def house_board(lista):
    lista_copied = copy.deepcopy(lista)
    for row in range(1, len(lista_copied)-1):
        for column in range(1, len(lista_copied)-1):
            lista_copied[row][column] = " "
    for i in range(5):
        ran1 = random.randint(1, len(lista_copied)-11)
        ran2 = random.randint(3,10)
        zakres_1 = list(range(ran1, ran1+ran2))
        ran3 = random.randint(1, len(lista_copied)-11)
        ran4 = random.randint(3,10)
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
            var = False

        if key == "d" and lista_copied[y][x+1] not in ["X", "▤"]:
            lista_copied[y][x] = ' '
            x += 1
            lista_copied[y][x] = "@"
            continue
        elif key == "a" and lista_copied[y][x-1] not in ["X", "▤"]:
            lista_copied[y][x] = ' '
            x -= 1
            lista_copied[y][x] = "@"
            continue
        elif key == "w" and lista_copied[y-1][x] not in ["X", "▤"]:
            lista_copied[y][x] = ' '
            y -= 1
            lista_copied[y][x] = "@"
            continue
        elif key == "s" and lista_copied[y+1][x] not in ["X", "▤"]:
            lista_copied[y][x] = ' '
            y += 1
            lista_copied[y][x] = "@"
            continue



        #if blood not in lista_copied:
            #return False

    #move_on_board(lista)








def add_to_inventory(lista, y, x):

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
            exit()

    elif lista[y][x] == "♣":
        if "magic weed" not in inv.keys():
            inv["magic weed"] = 1
        else:
            inv["magic weed"] += 1

    elif lista[y][x] == "●":
        if "cure" not in inv.keys():
            inv["cure"] = 1
        else:
            del inv["cure"]

    elif lista[y][x] == "♥":
        live_or_die_number = random.randint(1,6)
        if live_or_die_number == 1:
            print("\33[91mIT WASN'T THE GREATEST IDEA TO EAT IT ALL. YOU DIE\33[0m")
            exit()
        elif "super cure" not in inv.keys():
            inv["cure"] = 15

    elif lista[y][x] == "Ψ":
        print('\33[91mNICE AND SHARP (YOU DIE)\33[0m')
        exit()

def items(lista):
    difficulty = 10
    level_difficulty = difficulty
    items_place = []

    golden_egg = int(difficulty * 0.1) * ["Q"]
    zombie_chicken = int(difficulty * 2) * ["💀"]
    magic_weed = int(difficulty * 2) * ["♣"]
    cure = int(difficulty * 2.2) * ["●"]
    super_cure = 1 * ["♥"]
    pitchfork= int(difficulty * 2) * ["Ψ"]

    all_items = golden_egg + zombie_chicken + magic_weed + cure + super_cure + pitchfork

    while len(all_items) > 0:
        for item in all_items:
            x = random.randint(1,28)
            y = random.randint(1,28)
            if lista[y][x] not in ["X", "I", "▤", "+"] and lista[y][x] == ' ':
                lista[y][x] = item
                all_items.remove(item)
            else:
                continue

    return lista




#display_board(gameboard(10, 25))
level = items(level_board(gameboard(), 10))

move_on_board(level)
