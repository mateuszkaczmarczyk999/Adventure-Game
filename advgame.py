import os
import copy
import sys
import random
import invent                       ##### MK import inventory_game
from invent import inv              ##### MK import inventory_game


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
        if key == "d" and lista[y][x+1] not in ["I", "X"]:
            lista[y][x] = ' '
            x += 1
            lista[y][x] = "@"
            continue
        elif key == "a" and lista[y][x-1] not in ["I", "X"]:
            lista[y][x] = ' '
            x -= 1
            lista[y][x] = "@"
            continue
        elif key == "w" and lista[y-1][x] not in ["I", "X"]:
            lista[y][x] = ' '
            y -= 1
            lista[y][x] = "@"
            continue
        elif key == "s" and lista[y+1][x] not in ["I", "X"]:
            lista[y][x] = ' '
            y += 1
            lista[y][x] = "@"
            continue


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


#def house_board(lista, level=1):
    #for row in enumerate(lista):
        #random.choice(lista) = "I"
        #for column in range(5, 10):
            #lista[row][column] = "H"

    #return lista


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
level = items(level_board(gameboard(30, 30)))

move_on_board(level)
