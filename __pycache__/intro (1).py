import os
import random
import time
from termcolor import cprint
import sys
import tty

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
magicweed = bright_green + "♣" + end_color
pitchfork = blue + "Ψ" + end_color
zombie = dark_green + "💀" + end_color

def game_intro():
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
    cprint('if you dont want to die too quickly hide in abandoned barns & clear infected blood. then you gain more time.', 'red')
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


def main():
    """MAIN MENU"""
    os.system('clear')
    game_rules()
    time.sleep(2)


    while True:
        cprint("\nMENU:\n1: PLAY \n2: CREDITS \n3: EXIT\n\n", 'red', attrs=['bold'], file=sys.stderr)
        pick = input("PICK THE NUMBER: ")


        if pick == "1":                                                         # main menu
            game_start()
        elif pick == "3":
            os.system('clear')
            sys.exit()
        elif pick == "2":
            os.system('clear')
            credits()
        else:                                                                   #errors, invalid command from user
            os.system('clear')


if __name__ == "__main__":
    game_intro()
    time.sleep(2)
    time.sleep(1)
    main()
