

# username = input("username:")
# password = input("password:")

# users = ['bob', 'ann', 'mike', 'liz']
# passwords =['123', 'pass123', 'password123', 'pass123']

# abc = True

# while abc:
#     username = input("username:")
#     if username in users:
#         index = users.index(username)
#         password = input('Enter the password: ')

#         if username in ((users)[index]) and password in ((passwords)[index]):
#             print('Welcome')
#             abc = False
#         else:
#             print('The password you have entered is incorrect')
#             continue
#     else:
#         print('The username does not exist')
#         continue
#     break



# sequence = [1, 21, 5, 3, 5, 8, 321, 1, 2, 2, 32, 6, 9, 1, 4, 6, 3, 1, 2]

# counts = dict()

# for cislo in sequence:
#     if cislo not in counts:
#         counts[cislo] = 1
#     else:
#         counts[cislo] = counts[cislo] + 1


# for key, value in sorted(counts.items()):
#     print("key: ", key, "value:", value)
        
# vysledek = list()
# zadana_cisla = '1, 2, 3, 4, 5'

# cisla = zadana_cisla.split(",")

# for cislo in cisla:
#     ocistene_cislo = int(cislo.strip())
#     vysledek.append(ocistene_cislo)

# print("List: ", vysledek)


# veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'

# samohlasky = "aeiouy"
# vysledek = {"souhlasky": 0,"samohlasky": 0}

# for znak in veta:
#     if znak in samohlasky:
#         vysledek["samohlasky"] += 1
#     elif znak.isalpha() and  znak not in samohlasky:
#         vysledek["souhlasky"] += 1
#     else:
#         continue

# print("Pocet souhlasek: ", vysledek["souhlasky"], " | ", "Pocet samohlasek: ", vysledek["samohlasky"])


# for cislo in range (1, 101):
#     if (cislo % 15) == 0:
#         print("FizzBuzz")
#     elif (cislo % 3) == 0:
#         print("Fizz")
#     elif (cislo % 5) == 0:
#         print("Buzz")
#     else:
#         print(cislo)

# vysledek = list()
# start = 3
# stop = 9
# delitel = 3


# result = isinstance((start, stop, delitel), int)
# print(result)

# if isinstance(start, int) and isinstance(stop, int) and isinstance(delitel, int):
#     print("Zadany rozsah <", start, ",", stop, ">.", sep = "")
#     for cislo in range(start, stop + 1):
#         if (cislo % delitel) == 0:
#             vysledek.append(cislo)
#     print(vysledek)
            

# else:
#     print("Zadane vstupy nejsou cisla.")

# seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]
# delky_slov = 

# velikost = 10
# symboly = ['#',' ']
# sachovnice = []

# rada = "# # "
# sachovnice.append(rada)
# sachovnice.append(rada)


# print ('\n'.join(sachovnice))

# Iteruj přes řádky šachovnice a vytvoř proměnnou "rada"

# for radek in range(velikost):

#     rada = []

#     # Iteruj přes jednotlivé buňky v každém řádku

#     for bunka in range(velikost):

#         # Vytvoř index, který vybere jednu z hodnot v proměnné "symboly"

#         index = (radek + bunka) % len(symboly)

#         rada.append(symboly[index])

#     # Přidej hotové buňky do proměnné "sachovnice"

#     sachovnice.append(''.join(rada)) # spaja rady do stringu

# # Vypiš výslednou šachovnici

# print('\n'.join(sachovnice))

# a = ["OXOXOX", "XOXOXO", "OXOXOX"]

# b = ["X","O","X","O","X","O"]

# a.append(''.join(b))

# print(a)


# seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]
# delky_slov = {slovo: len(slovo) for slovo in seznam_slov}
# print(delky_slov)

# slova = list()

# while True:
#     odpoved = input("Zadej slovo ze ctyr: ")
    
#     if odpoved.isalpha and (len(odpoved) == 4) and odpoved not in slova:
#         slova.append(odpoved)
#         if (len(slova) == 3):
#             print("Uz mam ulozene tri slova.")
#             break
#     elif odpoved.isalpha and (len(odpoved) != 4):
#         print("Slovo neni dlouhe ctyri znaky")
#     elif odpoved in slova:
#         print("Slovo je jiz ulozene")


# ovoce = ("jablko", "banan", "citron", "pomeranc")



# print("Dostupné ovoce:", ovoce)

# dotazovani = True
# while dotazovani:
#     vybrane_ovoce = input("Vyber z dostupného ovoce: ")
#     if vybrane_ovoce in ovoce:
#         print("Bezva, toto ovoce je v nabídce.")
#         dotazovani = False
#     else:
#         print("Ovoce není v nabídce")
#         continue
    


# while True:
#     print("Scitani: '+' \nOdcitani: '-'\n")
#     operation = input("Vyber si operaci: ")
#     if operation not in ('+', '-'):
#         print("Nezadali jste platný operátor, zkuste to znovu")
#         continue
#     number_1 = int(input("Zadej prvni cislo: "))
#     number_2 = int(input("Zadej druhe cislo: "))
#     if operation == '+':                                                        #proc je tady opet if a ne elif???
#         print("Vysledek:", (number_1 + number_2))
#     elif operation == '-':
#         print("Vysledek:", (number_1 - number_2))
#     opakovat = input("Chcete pokracovat v pokracovat v pocitani? Pokud ano, stisknete 'y':")
#     if opakovat == "y":
#         continue
#     else:
#         print("Ukoncuji kalkulacku.")
#         break


# 2. Napište kód, který zkontroluje, zda je jméno přítomno ve slovníku a pokud ano, vypište přidružený věk.
# data = {"Jan": 30, "Marie": 25, "Petr": 35}

# for value in data:              ----> slo by tisknout hodnoty??
#     print(value)

# 5. Máte seznam slov. Najděte a vypište nejdelší slovo v seznamu.
# slova = ["jabko", "hory", "kočka", "programování", "knihovna"]                    # vysvetlit
# nejdelsi_slovo = ''

# for slovo in slova:
#     if len(nejdelsi_slovo) < len(slovo):
#         nejdelsi_slovo = slovo
# print(nejdelsi_slovo)

# pismena = ['a', 'a', 'b', 'c', 'd', 'a', 'e', 'g', 'm', 'e']

# # 1. zeptat se uzivatele
# # 2. smazat pismenko
# # ..(pokracovat)

# while pismena:
#     input_user = input("Ktere pismeno chces vyhodit? ")
#     while input_user in pismena:
#         pismena.remove(input_user)
#     print(pismena)

# import random
# moznosti = ["kamen", "nuzky", "papir"]
# hrac = "kamen"
# pocitac = random.choice(moznosti)



# print(f"Hrac: {hrac}")
# print(f"Pocitat: {pocitac}")
# if pocitac == "nuzky":
#     print("Vyhral jsi")
# elif pocitac == "papir":
#     print("Prohral jsi")
# else:
#     print("Nerozhodne")


# import random

# min_hodnota = 1
# max_hodnota = 6

# kostka_hodnota = random.randint(min_hodnota, max_hodnota)

# while True:
#     print("Hazim kostkou..")
#     print(f"Na kostce je: {kostka_hodnota}")
#     if kostka_hodnota == 6:
#         continue
#     else:
#         break

# def scitej_dve_hodnoty(cislo_1, cislo_2):
#     """Vraci soucet dvou hodnot uvnitr parametru"""
#     return cislo_1 + cislo_2

# soucet_1 = scitej_dve_hodnoty(5, 6)
# soucet_2 = scitej_dve_hodnoty(15, 8)

# print(soucet_1, soucet_2, sep="\n")

# prvni_cislo = 5
# druhe_cislo = 5

# def vynasob(num1, num2):
#     """Vraci nasobek dvou hodnot uvnitr parametru"""
#     return num1 * num2

# vysledek = vynasob(prvni_cislo, druhe_cislo)

# print(f"Vysledek je: {vysledek}")

# sekvence_cisel = [35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30]

# def spocitej_prumer(list):
#     """Vraci prumernou hodnotu listu"""
#     return sum(list) / len(list)

# vysledek = spocitej_prumer(sekvence_cisel)

# print(vysledek)
    

# vstup = 'Ahoj všem'

# def zdvojnasob_vsechny_znaky(zadani):
#     zdvojene = [pismeno * 2 for pismeno in zadani]
#     return "".join(zdvojene)                               #----> dovysvetlit join

# vysledek = zdvojnasob_vsechny_znaky(vstup)

# print(vysledek)


# prvni_cislo = 12
# druhe_cislo = 16

# def najdi_gcd(x1: int, x2: int) -> int:
#     mensi = x1
#     vetsi = x2
#     if x2 < mensi:
#         mensi = x2
#         vetsi = x1
#     for delitel in range(mensi, 2, -1):
#             if vetsi % delitel == 0 and mensi % delitel == 0:
#                 gcd = delitel
#                 break
#     return gcd


# vysledek = najdi_gcd(prvni_cislo, druhe_cislo)
# print(vysledek)


# import sys

# def je_os_windows():
#     if sys.platform.startswith("win"): 
#         return True
#     else:
#         return False 

# print(je_os_windows()) 


# def je_anagram(*args) -> bool:
# #     vzor = sorted(args[0])
# #     for slovo in args:
# #         if sorted(slovo) != vzor:
# #             return False
# #     else:                               ---------------------> preco neni else na urovni if??
# #         return True

# # print(je_anagram("ship", "hips", "hisp"))
# # print(je_anagram("ship", "hips", "duck"))


# adresy = [
#    "matous@holinka.com",
#    "danek11@seznam.cz",
#    "rennud15@gmail.com",
#    "pepa@centrum.cz"
# ]

# def filtruj_adresy_s_cisly(emaily: list) -> list:
#     vyfiltrovane = []
#     for email in emaily:
#         for znak in email:
#                 if not znak.isnumeric():
#                      continue
#                 vyfiltrovane.append(email)
#                 break    
                
#     return vyfiltrovane

# vysledek = filtruj_adresy_s_cisly(adresy)
# print(vysledek)


# import os

# jmena_slozek = ["obrazky", "texty", "gify"]

# for nazev in jmena_slozek:
#     if not os.path.exists(nazev):
#         os.mkdir(nazev)
#         print(f"Tvorim novou slozku {nazev}")
#     else:
#         print(f"Slozka jiz existuje.")
# print("Vsechny slozky jiz existuji.")


# jmeno_souboru = "novy_soubor.txt"
# pozdrav = "Ahoj, toto je první zápis do textového souboru"
# txt_soubor = open(jmeno_souboru, mode = "w")
# txt_soubor.write(pozdrav)
# txt_soubor.close()
# txt_soubor = open(novy_soubor.txt, mode = "r")

# Vytvoř funkci je_prvocislo, s parametrem cislo, který vezme samotné číslo a jako druhý parametr prvocisla,

def je_prvocislo(cislo: int, prvocisla: tuple) -> bool:

    return cislo in prvocisla

# vytvoř funkci generuj_interval_prvocisel, která nejprve vytvoří interval všech čísel od nuly až po parametr stop (včetně této hodnoty),
# prochází interval a všechny jeho hodnoty. Pokud narazí na 0 nebo 1, přeskoč je,
# vytvoř zanořený cyklus, který prochází hodnoty v rozsahu range(2, cislo),
# pokud platí, že hodnota z vnějšího cyklu cislo je dělitelná beze zbytku hodnotou z vnitřního cyklu filtr_cislo, přeruš vnitřní cyklus. Nakonec ulož hodnotu v filtr_cislo do proměnné vysledek,

def generuj_interval_prvocisel(stop: int) -> bool:
    vysledek = list()
    for cislo in tuple(range(stop + 1)):
        if cislo == 0 or cislo == 1:
            continue
        for filtr_cislo in range(2, cislo):
            if cislo % filtr_cislo == 0:
                break
        else:
            vysledek.append(cislo)

# získané údaje vrať jako tuple
    return tuple(vysledek)

# vyzkoušej tvoji úlohu na těchto voláních: 
print(

    je_prvocislo(23, generuj_interval_prvocisel(30)),

    je_prvocislo(233, generuj_interval_prvocisel(300)),

    je_prvocislo(146, generuj_interval_prvocisel(300)),

    sep="\n"

)


text = """'Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc tristique
fringilla congue. Donec ante diam cnn@info.com, dapibus
lacinia vulputate vitae, ullamcorper in justo. Maecenas
massa purus, ultricies a dictum ut, dapibus vitae massa.
Cras abc@gmail.com vel libero felis. In augue elit, porttitor
nec molestie quis, auctor a quam. Quisque b2b@money.fr
pretium dolor et tempor feugiat. Morbi libero lectus,
porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
Pellentesque id dui viverra, auctor enim ut, fringilla est.
Maecenas gravida turpis nec ultrices aliquet."""

# text2 = """Lorem ipsum dolor sit amet, consectetud
# tiger123@email.cz auctor massa molestie at.nec ultrices aliquet."""

# def vytvor_emailove_adresy(text: str) -> list:
#     emaily = list()
#     for slovo in text.split():
#         if "@" in slovo:
#             emaily.append(slovo)
        
                
#     return emaily

# vysledek = vytvor_emailove_adresy(text)

# print(vysledek)


           


# def uloz_emailove_adresy(text: str) -> list:
#     return [
#         slovo.strip(",.:;")
#         # for slovo in text.split()
#         # if "@" in slovo
#     ]
    
# vysledek = uloz_emailove_adresy(text)  

# seznam = []
# for slovo in text.split():
#     orezane_slovo = slovo.strip(",.:;")
#     seznam.append(orezane_slovo)

# print(seznam)


# prvni_radek = "První řádek v souboru,\n"
# druhy_radek = "druhý řádek v souboru,\n"
# treti_radek = "třetí řádek v souboru."


