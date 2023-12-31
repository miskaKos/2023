"""
project_2.py: druhy projekt do Engeto Online Python Akademie

author: Michaela Kosova

email: kosova.m@outlook.cz

discord: miskaKos

"""
# Program pozdraví užitele a vypíše úvodní text
# Program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)

oddelovac = ("-" * 30)


print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
print(oddelovac)

import random

cislo = random.randint(1000, 10000)


cislo_1 = random.randint(1, 9)
cislo_2 = random.randint(0, 9)
cislo_3 = random.randint(0, 9)
cislo_4 = random.randint(0, 9)



while cislo_1 == cislo_2:       
    cislo_2 = random.randint(0, 9)

while cislo_3 == cislo_1 or cislo_3 == cislo_2:
    cislo_3 = random.randint(0, 9)

while cislo_4 == cislo_1 or cislo_4 == cislo_2 or cislo_4 == cislo_3:
    cislo_4 = random.randint(0, 9)

cislo_generovane = str(cislo_1) + str(cislo_2) + str(cislo_3) + str(cislo_4)
print(cislo_generovane)

# Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, 
# pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky

hra_bezi = True
pocet_hadani = 0

while hra_bezi: 
    dotazovani = True
        
    if hra_bezi == True:
        pocet_hadani += 1
        
    while dotazovani: 
        sameNumbers = False
        zadane_cislo = input("Enter a number: ")
        if not zadane_cislo.isnumeric():
            print("Once more")
            continue
        elif len(zadane_cislo) != 4:
            print("Number has wrong length")
            continue
        elif zadane_cislo[0] == "0":
            print("First number has not be 0. ")
            continue
        for i in range (len(zadane_cislo)):
            for j in range (i+1,len(zadane_cislo)):
                if zadane_cislo[i] == zadane_cislo[j]:
                    print("Same numbers")
                    sameNumbers = True
                    break
        if sameNumbers == False:
            dotazovani = False           

# Program vyhodnotí tip uživatele
# Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), 
# příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění).
# Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows).    
    bulls = 0
    cows = 0     
    
    for a in range(len(cislo_generovane)):
        if cislo_generovane[a] == zadane_cislo[a]:
            bulls += 1
        for b in range (len(zadane_cislo)):
            if a != b and cislo_generovane[a] == zadane_cislo[b]:
                cows += 1
            else:
                continue
    

    if bulls == 1:
        tvar_bulls = "bull"
    else:
        tvar_bulls = "bulls"

    if cows == 1:
        tvar_cows = "cow"
    else:
        tvar_cows = "cows"
    
    if pocet_hadani == 1:
        tvar_guess = "guess"
    else:
        tvar_guess = "guesses"
    
    
    if bulls == 4:
        print(oddelovac)
        print(f"Correct, you've guessed the right number in {pocet_hadani} {tvar_guess}!")
        print(oddelovac)
        
        if pocet_hadani == (1 or 2):
            print("That's amazing!")
        elif pocet_hadani in range(3, 6):
            print("That's avarage.")
        else:
            print("That's not so good.")

        hra_bezi = False
    else:
        print(oddelovac)
        print(f"{bulls} {tvar_bulls}, {cows} {tvar_cows}")
        print(oddelovac)

    


