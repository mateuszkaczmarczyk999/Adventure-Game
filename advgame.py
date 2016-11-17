import os
import copy
import sys
import random
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
    y = 15
    x = 2
    lista[y][x] = "@"
    while True:
        os.system('clear')
        display_board(lista)
        invent.print_table(inv, "count,desc")   ### MK print tabelki
        key = getch()
        if key == "x":
            exit()
        if key == "d" and lista[y][x+1] not in ["I", "X", "+"]:
            lista[y][x] = ' '
            x += 1
            lista[y][x] = "@"
            continue
        elif key == "a" and lista[y][x-1] not in ["I", "X", "+"]:
            lista[y][x] = ' '
            x -= 1
            lista[y][x] = "@"
            continue
        elif key == "w" and lista[y-1][x] not in ["I", "X", "+"]:
            if lista[y-1][x] in ["="]:
                print("AAAAAAAAA")
                for row in range(1, len(lista)-1):
                    for column in range(1, len(lista)-1):
                        lista = gameboard()


            lista[y][x] = ' '
            y -= 1
            lista[y][x] = "@"
            continue
        elif key == "s" and lista[y+1][x] not in ["I", "X", "+"]:
            lista[y][x] = ' '
            y += 1
            lista[y][x] = "@"
            continue

def random_building(lista, a, b, c=1):
    ran1 = random.randint(2, 13)
    ran2 = random.randint(10, 16)

    for row in range(ran1, ran1 + ran2):
        for column in range(a, b):
            #roof = bright_groundish + "=" + end_color
            lista[row][column] = "▤"
        for column in range(a, b, c):
            #roof2 = bright_groundish + "I" + end_color
            lista[row][column] = "▤"

def random_fence(lista, lista2):
    for idx, val in enumerate(lista2):
        rand1 = random.randint(6, 15)
        rand2 = random.randint(16, 25)
        for row in list(range(1, rand1)) + list(range(rand2,30)):
            #fence = dark_green + "+" + end_color
            lista[row][val] = "+"

def level_board(lista, level=1):
    random_building(lista, 5, 10, 2)
    random_building(lista, 13, 18, 2)
    random_building(lista, 21, 26, 2)
    border_list = [3, 11, 19, 27]
    random_fence(lista, border_list)
    return lista

    """
    #ran_list = []
    #i = 0
    #while i != level:
        r = random.randint(2, (len(lista)-2))
        ran_list.append(r)
        i = len(set(ran_list))
        ran_list = list(set(ran_list))
    ran_list.extend([1, (len(lista)-2)])
    ran_list = sorted(ran_list)

    for row in range(1, (len(lista)-1)):
        for column in range(1, (len(lista)-1)):
            lista[row][column] = "I"

    #for row in range(1, (len(lista)-1)):
        #for column in ran_list:
            #lista[row][column] = " "

    combs = []
    for idx, val in enumerate(ran_list):
        if idx < (len(ran_list)-1):
            combs.append((ran_list[idx], ran_list[idx + 1]))
    print(combs)
    print(combs[0])
    print(combs[0][0], combs[0][1])

    for i, v in enumerate(combs):
        random_place(lista, combs[i][0], combs[i][1])
"""


"""
    for row in range(random.randrange(2, 10), random.randrange(17, 25)):
        for column in range(1, 5):
            lista[row][column] = " "
    r = random.randrange(2, 10)
    for row in range(r, random.randrange(17, 25)):
        for column in range(5, 9):
            lista[row][column] = " "
            lista[r-1][7] = "."
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
"""

"""
def house_board(lista, level=1):
    for row in enumerate(lista):
        #random.choice(lista) = "I"
        for column in range(5, 10):
            lista[row][column] = "H"
    return lista
"""


def items(lista):                           ### MK funkcja generowania przedmiotów
    difficulty = 10
    level_difficulty = difficulty
    items_place = []
    #lista[20][20] = 'G'
    gold_egg = int(difficulty * 0.1) * ["Q"]
    feather = int(difficulty * 0.5) * ["f"]
    egg = int(difficulty * 0.7) * ["o"]
    pitchfork = int(difficulty * 0.1) * ["Y"]
    magic_weed = int(difficulty * 2) * ["w"]
    all_items = gold_egg + feather + egg + pitchfork + magic_weed
    counter = len(all_items)
    while counter > 0:
        for item in range(len(all_items)):
            x = random.randint(1,20)
            y = random.randint(1,20)
            if lista[y][x] not in ["X", "I"]:
                lista[y][x] = all_items[item]
                counter -= 1
            else:
                continue
    return lista





#display_board(gameboard(10, 25))
level = level_board(gameboard(), 10)

move_on_board(level)
