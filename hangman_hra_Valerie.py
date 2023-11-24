import random
import slova
from figurka import hangman

random.seed(0)
slovo = random.choice(slova.random_words)
tajenka = ["_"] * len(slovo)  # opakovani  ->  n e r o z h o d

hra_bezi = True 
zivoty = 7
while hra_bezi and zivoty > 0:
    print(tajenka)
    print(hangman[7 - zivoty])
    hadani = input("Hadej pismeno/slovo:")
    if hadani == slovo:  # NE: hadani is slovo
        hra_bezi = False
    elif hadani in slovo and len(hadani) == 1:  
        for idx, symbol in enumerate(slovo):
            if symbol == hadani:
                tajenka[idx] = hadani
        # spatne! tajenka = "".join(tajenka)
        # lepsi: tajenka_str = "".join(tajenka)
        hra_bezi = False if "_" not in tajenka else True
        #                # "_" not in tajenka?
           #         <-- ano              ---->    ne
    else:  # spatne
        zivoty -= 1
    

if not hra_bezi:  # hra_bezi == False
    print("Gratulace...")
else:
    print(f"Tajenka: {slovo}. Prohral jsi.")



############

# database = [
#     ("Jiri", "Novak", 26, "777111222", "PhD"),
#     (...)
# ]

# for idx, (jmeno, prijmeno, vek, cislo, titul) in enumerate(database):
#     ...

# a, b, c, d, e, f = 1, 2, 3, 4, 5, 6