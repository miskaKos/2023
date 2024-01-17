import sys
sys.argv
import csv
import json
import requests
import bs4 
from bs4 import BeautifulSoup as bs
import pandas 

# tables = pandas.read_html("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103")
# print(tables)


url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"

r = requests.get(url)
soup = bs(r.text, features="html.parser")
# print(soup.prettify)

obec_seznam = soup.find("div", {"id": "inner"})
# print(obec_seznam)

# vsechny_tr = obec_seznam.find_all("tr")
# for tr in vsechny_tr[1:]:
#     td_na_radku = tr.find_all("td")
    # print((td_na_radku))

# list = []
# for i in vsechny_tr:
#     if i:
#         list.append(i.text.strip())

# print(list)



# list = [r.replace("\n", " ") for r in list]

# x = ", ".join(list)
# y = x.split()
# print((y))

# nazvy_obci = []
# cisla_obci = []
# for polozka in y:
#     if polozka.isdigit():
#         cisla_obci.append(polozka)
# for polozka in y:
#     if polozka.istitle() :
#         nazvy_obci.append(polozka)

# print(cisla_obci)
# print(nazvy_obci)

#  novy pokus td

vsechny_tr = obec_seznam.find_all("td")
list = []
for i in vsechny_tr:
    if i:
        list.append(i.text.strip())

# print(list)

nazvy_obci = []
cisla_obci = []
for polozka in list:
    if polozka.isdigit():
        cisla_obci.append(polozka)
print(cisla_obci)

for polozka in list:
    if polozka.istitle() and len(polozka) > 1:
        nazvy_obci.append(polozka)
print(nazvy_obci)


podklady_odkazy = obec_seznam.select('.center a')
# print(podklady_odkazy)
odkazy = ["https://volby.cz/pls/ps2017nss/" + obec_seznam['href'] for obec_seznam in podklady_odkazy]
# print(odkazy)

for index in range(0, len(nazvy_obci)):
    d = {"cislo_obce": cisla_obci[index], "nazev_obce": nazvy_obci[index], "odkaz": odkazy[index]}
    print(d)