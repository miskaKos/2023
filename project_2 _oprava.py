"""
project_2_fin_oprava.py: druhy projekt do Engeto Online Python Akademie

author: Michaela Kosova

email: kosova.m@outlook.cz

discord: miskaKos

"""
import random

# def
def vyhodnot_zadane_cislo(zadane_cislo):
    stejne_cisla = False  
    if not zadane_cislo.isnumeric():
        Pokračuj = True
        Text = "Once more"
        return  Pokračuj, Text
    elif len(zadane_cislo) != 4:
        Pokračuj = True
        Text = "Number has wrong length"
        return  Pokračuj, Text
    elif zadane_cislo[0] == "0":
        Pokračuj = True
        Text = "First number has not be 0."
        return  Pokračuj, Text
    for i in range(len(zadane_cislo)):
        for j in range (i+1,len(zadane_cislo)):
            if zadane_cislo[i] == zadane_cislo[j]:
                stejne_cisla = True
                Pokračuj = True
                Text = "Same numbers"
                return  Pokračuj, Text                
    if stejne_cisla == False:
        Pokračuj = False
        Text = ""
        return  Pokračuj, Text

# Pozdrav
oddelovac = ("-" * 30)

print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
print(oddelovac)

# Generovani nahodneho cisla

nevhodne_cislo = True

while nevhodne_cislo:
    cislo_nahodne = str(random.randint(1000, 9999))
    duplikat = False

    for i in range(len(cislo_nahodne)):
        for j in range(i+1, len(cislo_nahodne)):
            if cislo_nahodne[i] == cislo_nahodne[j]:
                duplikat = True
                break
    if duplikat == False:
        nevhodne_cislo = False

# Kontrola spravnosti zadaneho cisla

hra_bezi = True
pocet_hadani = 0

while hra_bezi: 
    dotazovani = True
    pocet_hadani += 1
      
    while dotazovani: 
        zadane_cislo = input("Enter a number: ")
        Pokračuj, Text = vyhodnot_zadane_cislo(zadane_cislo)
        dotazovani = Pokračuj
        if dotazovani == True:
            print(Text)
   

# Vyhodnocovani tipu uzivatele

    bulls = 0
    cows = 0     
    
    for a in range(len(cislo_nahodne)):
        if cislo_nahodne[a] == zadane_cislo[a]:
            bulls += 1
        elif cislo_nahodne[a] in zadane_cislo:
            cows += 1
    

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

    


