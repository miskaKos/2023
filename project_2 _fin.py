"""
project_2_fin.py: druhy projekt do Engeto Online Python Akademie

author: Michaela Kosova

email: kosova.m@outlook.cz

discord: miskaKos

"""
# Pozdrav
oddelovac = ("-" * 30)


print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
print(oddelovac)

# Generovani nahodneho cisla

# L25-L40 - napada te jak tyhle radky sloucit? co treba zkusit vygenerovat cislo mezi 1000 a 9999
# a zkontrolovat jestli je unikatni a nebo lepsi je zamichat posloupnost cisel od 0 do 9 a pripadne 
# osetrit aby prvni nebyla nula - ale takto je to take spravne - jenom ne optimalni


import random


def generovani_cisla() -> int:
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

    cislo_nahodne = str(cislo_1) + str(cislo_2) + str(cislo_3) + str(cislo_4)    
    return cislo_nahodne

cislo_generovane = generovani_cisla()
print(cislo_generovane)

# Kontrola spravnosti zadaneho cisla

hra_bezi = True
pocet_hadani = 0

while hra_bezi: 
    dotazovani = True
        
    if hra_bezi == True:
        pocet_hadani += 1
        
    while dotazovani: 
        stejne_cisla = False
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
        for i in range(len(zadane_cislo)):
            for j in range (i+1,len(zadane_cislo)):
                if zadane_cislo[i] == zadane_cislo[j]:
                    print("Same numbers")
                    stejne_cisla = True
                    break
        if stejne_cisla == False:
            dotazovani = False              
                     

# Vyhodnocovani tipu uzivatele
    bulls = 0
    cows = 0     
    
    for a in range(len(cislo_generovane)):
        if cislo_generovane[a] == zadane_cislo[a]:
            bulls += 1
        for b in range(len(zadane_cislo)):
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

    


