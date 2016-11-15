import os
import copy
import sys

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


def gameboard(x=5, y=5):
    lista = []
    for rzad in range(x):
        lista.append([])
        for kolumn in range(y):
            if rzad == 0 or rzad == x-1 or kolumn == 0 or kolumn == y-1:
                lista[rzad].append('x')
            else:
                lista[rzad].append(' ')
    return lista


def display_board(lista):
    for i in lista:
        print('  '.join(i))


def move_on_board(lista):
    y = len(lista) - 3
    x = 2
    lista[y][x] = "@"
    while True:
        os.system('clear')
        display_board(lista)
        key = getch()
        if key == "x":
            exit()
        if key == "d" and x < (len(lista[0]) - 2):
            lista[y][x] = ' '
            x += 1
            lista[y][x] = "@"
            continue
        elif key == "a" and x > 1:
            lista[y][x] = ' '
            x -= 1
            lista[y][x] = "@"
            continue
        elif key == "w" and y > 1:
            lista[y][x] = ' '
            y -= 1
            lista[y][x] = "@"
            continue
        elif key == "s" and y < (len(lista) - 2):
            lista[y][x] = ' '
            y += 1
            lista[y][x] = "@"
            continue


display_board(gameboard(25, 25))
move_on_board(gameboard(25, 25))
