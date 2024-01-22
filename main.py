# print ("We are starting with Git")
# print("Second line")

# print ("Third print")


# users = {
#     'admin': {'password': 'adm1n'},
#     'man': {'password': 'thing'},
#     'cool': {'password': 'guy'}
# }

# while True:
#     user_input = input('Enter your username: ')

#     if user_input in users:
#         password = input('Enter the password: ')

#         if password == users[user_input]['password']:
#             print('Welcome')
#         else:
#             print('The password you have entered is incorrect')
#             continue
#     else:
#         print('The username does not exist')
#         continue
#     break



# def zobraz_slova(txt: list) -> list:
#     zadana_slova = open(txt, "r")
#     data = zadana_slova.read()
#     txt = data.split()
#     hledane_slova = list()
#     for slovo in txt:
#         if len(slovo) >= 7:
#             hledane_slova.append(slovo)

#     return hledane_slova

# if __name__== "__main__":
#     print(zobraz_slova("slova.txt"))


# prvni_radek = "První řádek v souboru,\n"
# druhy_radek = "druhý řádek v souboru,\n"
# treti_radek = "třetí řádek v souboru."

# txt_soubor = open("txt_soubor.txt", mode = "w")
# txt_soubor.write(prvni_radek)
# txt_soubor.write(druhy_radek)
# txt_soubor.write(treti_radek)
# txt_soubor.close()

# cteni_txt = open("txt_soubor.txt")
# obsah_txt = cteni_txt.readlines()

# print(obsah_txt)

# kombinace = 1.234
# presnost_str = "Hello"
# presnost_cisla = 123.4567

# formatovana_presnost = (f"|{(presnost_cisla):.2e}|{round(presnost_cisla, 1)}|{round(presnost_cisla, 2)}|")
# print(f"Naformatovana presnost: {formatovana_presnost},")

# formatovana_kombinace = (f"|{kombinace}$|")
# print(f"Naformatovana kombinace:{formatovana_kombinace},")

# formatovana_presnost_str = (f" |{presnost_str[:4]}|")
# print(f"Naformanovany string:{formatovana_presnost_str}.")

# print("Zapisuji do souboru.")

# txt_soubor = open("vysledek.txt", mode = "w")
# txt_soubor.write(formatovana_presnost)
# txt_soubor.write(formatovana_kombinace)
# txt_soubor.write(formatovana_presnost_str)
# txt_soubor.close()

# cteni_txt = open("vysledek.txt")
# obsah_txt = cteni_txt.readlines()

# print(obsah_txt)

# print(f"""\
# Naformátovaná přesnost: \t{formatovana_presnost},
# Naformátovaná kombinace: \t{formatovana_kombinace},
# Naformátovaný string: \t\t{formatovana_presnost_str}.""")

# print("Zapisuji do souboru.")

# with open("vysledek.txt", mode="w") as txt:

#     txt.write("\n".join(

#         (formatovana_presnost, formatovana_kombinace, formatovana_presnost_str)

#         )

#     )


# def nacti_radky(txt):
#     try:
#         cteni_txt = open(txt)
#         vysledek = cteni_txt.readlines()
#     except FileNotFoundError:
#         print(f"Soubor {txt} neexistuje!")
#     else:   
#         print(vysledek)

# print(nacti_radky("jazykzy.txt"))

# 10. ukol 1

# def nacti_radky(cesta_k_souboru: str):
#     try:
#         soubor = open(cesta_k_souboru)
#         # cteni_txt = open(txt)
#         # vysledek = cteni_txt.readlines()
#     except FileNotFoundError:
#         print(f"Soubor {cesta_k_souboru} neexistuje!")
#         obsah = []
#     else:  
#         obsah = soubor.read()
#         soubor.close()
#     finally:
#         return obsah

# vysledek = nacti_radky("jazyky.txt")
# print(vysledek)


# 10. ukol 2
# def secti_hodnoty(udaje):
#     vysledek = 0.0

#     for hodnota in udaje:
#         try:
#             cislo = float(hodnota)
#         except Exception:
#             print(f"Hodnota {hodnota} není číselný údaj.")
#         else:
#             vysledek += cislo
#     return vysledek
    

# test = [1, 'asda', {'zvire': 'kocka'}, '3.0', 2.0, [], '\\n', 4]
# print("Vysledek:", secti_hodnoty(test))

# muj_slovnik = {
#     'jmeno':'Pepa',
#     'prijmeni': 'Novak',
#     'rok_narozeni': 1990
# }

# def obsahuje_klic_a_hodnotu(klic: str, hodnota: str, slovnik: dict):
#     try:
#         udaj = slovnik[klic]
#     except KeyError:
#         print(f"Klíč:  {klic}, nenalezen.")
#         vysledek = False
#     else:
#         print(f"Klíč: {klic}, nalezen.")
#         if udaj == hodnota:
#             vysledek = True
#         else:
#             print(f"Hodnota: {hodnota}, nenalezena.")
#             vysledek = False
#     finally:
#         return vysledek

# print(obsahuje_klic_a_hodnotu("jmeno", "Pepa", muj_slovnik))

# import json

# def najdi_zadane_klice(jmeno_souboru: str) -> list:
#     with open(jmeno_souboru) as json_soubor:
#         obsah_jsonu = json.load(json_soubor)
#     return [
#             slovnik.get("jmeno") for slovnik in obsah_jsonu
#     ]

# if __name__ == "__main__":
#     print(najdi_zadane_klice("udaje.json"))


# import json



# def zapis_serazene_klice(jmeno_souboru: str, data: dict):
#     with open(jmeno_souboru, mode = "w") as json_soubor:
#         json.dump(data, json_soubor, sort_keys=True)


# def vypis_obsah_souboru(jmeno_souboru):
#     with open(jmeno_souboru, mode = "r") as json_soubor:
#         return json.load(json_soubor)
    

# jmeno_souboru = "serazene.json"
# data = {'4': 5, '6': 7, '1': 3, '2': 4}

# zapis_serazene_klice(jmeno_souboru, data)
# print(vypis_obsah_souboru(jmeno_souboru))

# import csv

# hlavicka = ["jmeno", "prijmeni", "vek"]
# osoba_1 = ["Matous", "Pokoj", "28"]
# osoba_2 = ["Petr", "Svetr", "27"]

# nove_csv = open("prvni_tabulkovy_soubor.csv", mode="w")

# # ... vytvoříš zapisovací objekt, který do souboru zapíše údaje

# zapisovac = csv.writer(nove_csv)

# # ... nejprve zapíšeš záhlaví

# zapisovac.writerow(hlavicka)

# # ... potom první údaj

# zapisovac.writerow(osoba_1)

# # ... druhý údaj

# zapisovac.writerow(osoba_2)

# # ... nakonec objekt a soubor uzavřeš

# nove_csv.close()

# import csv

# data = [
#     [10,'a1', 1],
#     [12,'a2', 3],
#     [14, 'a3', 5],
#     [16, 'a4', 7],
#     [18, 'a5', 9]
# ]

# with open("nove.csv", mode="w") as nove_csv:
#     zapisovac = csv.writer(nove_csv)
#     zapisovac.writerows(
#         (
#             data
#         )
#     )
    
    
# with open("nove.csv") as csv_data: 
#     cteni = csv.reader(csv_data)
#     for row in cteni:
#         print(row)

# import sys

# print(sys.argv[0])

adresa = "https://cs.wikipedia.org/wiki/Hlavn%C3%AD_strana"


# import requests

# from requests import get

# adresa = "https://cs.wikipedia.org/wiki/Hlavn%C3%AD_strana"
# odpoved = get(adresa)

# print(odpoved.text)

# print(odpoved.text[:15])
# print(odpoved.text[94:141])



from requests import get
from bs4 import BeautifulSoup as bs

adresa = "https://cs.wikipedia.org/wiki/Hlavn%C3%AD_strana"
odpoved = get(adresa)

"""
* odpoved.text - objekt typu 'str',
* feature - argument, který upřesní typ rozdělovače.
"""
rozdelene_html = bs(odpoved.text, features="html.parser")

print(rozdelene_html)