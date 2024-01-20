import sys
sys.argv
import csv
import json
import requests
import bs4 
from bs4 import BeautifulSoup as bs
import traceback

url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"

r = requests.get(url)
soup = bs(r.text, features="html.parser")
# print(soup.prettify)

obec_seznam = soup.find("div", {"id": "inner"})
# print(obec_seznam)


#  novy pokus td
vsechny_td = obec_seznam.find_all("td")
list = []
for i in vsechny_td:
    if i:
        list.append(i.text.strip())

nazvy_obci = []
cisla_obci = []
for polozka in list:
    if polozka.istitle() and len(polozka) > 1:
        nazvy_obci.append(polozka)
# print(nazvy_obci)
        
for polozka in list:
    if polozka.isdigit():
        cisla_obci.append(polozka)
# print(cisla_obci)

podklady_odkazy = obec_seznam.select('.center a')
# print(podklady_odkazy)
odkazy = ["https://volby.cz/pls/ps2017nss/" + obec_seznam['href'] for obec_seznam in podklady_odkazy]
# print(odkazy)

d_pole = []
for index in range(0, len(nazvy_obci)):
    d = {"code": cisla_obci[index], "location": nazvy_obci[index]}
    d_pole.append(d)

# print(type(d_pole))

# def uloz_seznam_do_json(udaje: list):
#     with open("vysledek.json", mode="w", encoding="utf-8") as f:
#         json.dump(udaje, f)

# json_soubor = open("vysledek.json", mode="w")
# json.dump(d_pole, json_soubor)
# json_soubor.close()

# zapis_json = uloz_seznam_do_json(d_pole)
# print(zapis_json)

def zapis_data(data: list, jmeno_souboru: str) -> str:
    """
    Zkus zapsat udaje z par. 'data' do souboru formatu .csv.
    """
    try:
        csv_soubor = open(jmeno_souboru, mode="w", encoding="utf-8")
        nazvy_sloupcu = ["code", "location"]
        # sloupce = data[0].keys()   
    except FileExistsError:
        return traceback.format_exc()
    except IndexError:
        return traceback.format_exc()
    else:
        zapis = csv.DictWriter(csv_soubor, fieldnames = nazvy_sloupcu)
        zapis.writeheader()
        zapis.writerows(data)
        return "Saved"
    finally:
        csv_soubor.close()

# zapis_csv = zapis_data(d_pole, "vysledky_prostejov.csv")
# print(zapis_csv)
        

for odkaz in range(2): #odkazy:
    r2 = requests.get(odkazy[odkaz])
    location_soup = bs(r2.text, features="html.parser")
    cisla_seznam = location_soup.find("table", {"id": "ps311_t1"})


# r2 = requests.get(odkaz)
# location_soup = bs(r2.text, features="html.parser")
# cisla_seznam = location_soup.find("table", {"id": "ps311_t1"})
# print(cisla_seznam)
# # break

    cisla_seznam_td = cisla_seznam.find_all("td")
    # print(cisla_seznam_td)
    cisla_seznam_list = []
    for j in cisla_seznam_td:
        cisla_seznam_list.append(j.text.strip())


    registred = cisla_seznam_list[3]
    envelopes = cisla_seznam_list[4]
    valid = cisla_seznam_list[7]

    # cisla = cisla_seznam.select("td", {"class":"cislo", "headers": "sa2"})

    # print(registred)
    # print(envelopes)
    # print(valid)

    strany_seznam = location_soup.find("div", {"id": "inner"})

    platne_hlasy_podklad_1 = strany_seznam.find_all("td", {"class":"cislo", "headers": ("t1sb3")})
    platne_hlasy_podklad_2 = strany_seznam.find_all("td", {"class":"cislo", "headers": ("t2sb3")})
    
    platne_hlasy_1 = []
    platne_hlasy_2 = []

    for i in platne_hlasy_podklad_1:
        platne_hlasy_1.append(i.text.strip())

    for i in platne_hlasy_podklad_2:
        platne_hlasy_2.append(i.text.strip())

    platne_hlasy = platne_hlasy_1 + platne_hlasy_2
    print(platne_hlasy)

# print(strany_seznam)
# strany_seznam_td = strany_seznam.find_all("td")
# strany_seznam_list = []
# for k in strany_seznam_td:
#     if k:
#         strany_seznam_list.append(k.text.strip())

    nazvy_stran_1 = []
    nazvy_stran_2 = []
 
# Nefunguje --> proc????
for odkaz in range(1): #odkazy:
    r2 = requests.get(odkazy[odkaz])
    nazvy_stran_soup = bs(r2.text, features="html.parser")
    nazvy_stran_seznam = nazvy_stran_soup.find("div", {"id": "inner"})

    nazvy_stran_podklad_1 = strany_seznam.find_all("td", {"class":"overflow_name", "headers": "t1sa1"})
    nazvy_stran_podklad_2 = strany_seznam.find_all("td", {"class":"overflow_name", "headers": "t2sa1"})


    for i in nazvy_stran_podklad_1:
        nazvy_stran_1.append(i.text.strip())

    # print(nazvy_stran_1)

    for i in nazvy_stran_podklad_2:
        nazvy_stran_2.append(i.text.strip())
        
    # print(nazvy_stran_2)

        nazvy_stran = nazvy_stran_1 + nazvy_stran_2
        print(nazvy_stran)

    # while i <= len(strany_seznam_list):
    #     nazvy_stran.append(strany_seznam_list[i])
    #     i = i + 5
    # print(nazvy_stran)
    


    # j = 2                
    # while j <= len(strany_seznam_list):
    #     platne_hlasy.append(strany_seznam_list[j])
    #     j = j + 5
    # print(platne_hlasy)


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