import random
import slova
from figurka import hangman

random.seed(0)
slovo = random.choice(slova.random_words)
tajenka = ["_"] * len(slovo)

hra_bezi = True
zivoty = 7

while hra_bezi and (zivoty > 0):
    print(tajenka)
    print(hangman[7 - zivoty])
    hadani = input("Hadej pismeno/slovo:")
    if hadani == slovo:
        hra_bezi = False
    elif hadani in slovo and len(hadani) == 1:
        for idx, symbol in enumerate(slovo):
            if symbol == hadani:
                tajenka[idx] = hadani
        hra_bezi = False if "_" not in tajenka else True

    else: 
        zivoty -= 1    
if not hra_bezi:
    print("Gratulace")

else:
    print(f"Tajenka: {slovo}. Prohral si.")

