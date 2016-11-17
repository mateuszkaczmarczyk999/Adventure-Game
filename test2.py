import os
import copy
import sys
import random
import time
from time import sleep
import invent
from invent import inv

#def timer():
"""
    for i in range(0,20):
        #print(10 - i)
        if i == 20:
            print("End")
            exit()
        sleep(1)
"""

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


def gameboard(x=25, y=25):
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
        if key == "d" and lista[y][x+1] not in ["I", "X"]:
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

        elif key == "a" and lista[y][x-1] not in ["I", "X"]:
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

        elif key == "w" and lista[y-1][x] not in ["I", "X"]:
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

        elif key == "s" and lista[y+1][x] not in ["I", "X"]:
            if lista[y+1][x] not in ["Q", "💀", "♣", "●", "♥", "Ψ"]:
                lista[y][x] = ' '
                y += 1
                lista[y][x] = "@"
            elif lista[y+1][x] in ["Q", "💀", "♣", "●", "♥", "Ψ"]:
                add_to_inventory(lista, y+1, x)
                lista[y][x] = ' '
                y += 1
                lista[y][x] = "@"
            continue
    if actual_time >= 90:
        print("\33[91mNO TIME TO LOOSE. IT'S TIME TO DIE\33[0m")
    elif inv["thanksgiving egg"] == 20:
        print("\33[92mIT'S YOUR LUCKY DAY\33[0m")

def level_board(lista, level=1):
    for row in range(1, (len(lista)-1)):
        for column in range(1, (len(lista)-1)):
            lista[row][column] = "I"
    for row in range(random.randrange(2, 10), random.randrange(17, 25)):
        for column in range(1, 5):
            lista[row][column] = " "
    r = random.randrange(2, 10)
    for row in range(r, random.randrange(17, 25)):
        for column in range(5, 9):
            lista[row][column] = " "
            lista[r-1][7] = " "
    for row in range(random.randrange(2, 10), random.randrange(17, 25)):
        for column in range(9, 13):
            lista[row][column] = " "
    for row in range(random.randrange(2, 10), random.randrange(17, 25)):
        for column in range(13, 17):
            lista[row][column] = " "
    for row in range(random.randrange(2, 10), random.randrange(17, 25)):
        for column in range(17, 21):
            lista[row][column] = " "
    for row in range(random.randrange(2, 10), random.randrange(17, 25)):
        for column in range(21, 25):
            lista[row][column] = " "
    for row in range(random.randrange(2, 10), random.randrange(17, 25)):
        for column in range(25, 29):
            lista[row][column] = " "
    return lista

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
            if lista[y][x] not in ["X", "I"] and lista[y][x] == ' ':
                lista[y][x] = item
                all_items.remove(item)
            else:
                continue

    return lista

def house_board(lista):
   for row in enumerate(lista):
       #random.choice(lista) = "I"
       for column in range(5, 10):
           lista[row][column] = "B"
   return lista


level = items(level_board(gameboard(30, 30)))

move_on_board(level)
