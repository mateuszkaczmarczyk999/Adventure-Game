import os
import sys
import tty
import random

"""KOLORY POWINNY BYĆ JAKO ZMIENNE NA POCZĄTKU GRY. ODWOŁUJEMY SIĘ DO NICH JAK DO ZMIENNEJ.
np jeśli chcemy krwi odnosimy się do blood - poniżej przykłady"""

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

#lista NAZW kolorowych ITEMÓW
blood = red + "≡" + end_color
cure = dark_groundish + "●" + end_color
supercure = bright_groundish + "♥" + end_color
goldenegg = gold + "Q" + end_color
magicweed = bright_green + "♣" + end_color
killer = bright_groundish + "○" + end_color
pitchfork = blue + "Ψ" + end_color

lista=[]

print(blood)
for column in range(5, 10):
    lista = blood
    print(lista)

print(cure)
print(goldenegg)
print(supercure)
print(magicweed)
print(killer)
print(blood)
print(pitchfork)
