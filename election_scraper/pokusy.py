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
print(type(obec_seznam))


#  novy pokus td
vsechny_td = obec_seznam.find_all("td")
# print(type(vsechny_td))
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
print(type(odkazy))

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
        

for odkaz in range(3): #odkazy:
    r2 = requests.get(odkazy[odkaz])
    try: 
        location_soup = bs(r2.text, features="html.parser")
        cisla_seznam = location_soup.find("table", {"id": "ps311_t1"})
        cisla_seznam_td = cisla_seznam.find_all("td")
        cisla_seznam_list = []
        for j in cisla_seznam_td:
            cisla_seznam_list.append(j.text.strip())


        registred = int(cisla_seznam_list[3])
        envelopes = int(cisla_seznam_list[4])
        valid = int(cisla_seznam_list[7])

    # cisla = cisla_seznam.select("td", {"class":"cislo", "headers": "sa2"})

        print((registred))
        print(envelopes)
        print(valid)

        strany_seznam = location_soup.find("div", {"id": "inner"})

        platne_hlasy_podklad_1 = strany_seznam.find_all("td", {"class":"cislo", "headers": ("t1sb3")})
        platne_hlasy_podklad_2 = strany_seznam.find_all("td", {"class":"cislo", "headers": ("t2sb3")})
        
        platne_hlasy_1 = []
        platne_hlasy_2 = []

        for i in platne_hlasy_podklad_1:
            platne_hlasy_1.append(int(i.text.strip()))

        for i in platne_hlasy_podklad_2:
            platne_hlasy_2.append(int(i.text.strip()))

        platne_hlasy = platne_hlasy_1 + platne_hlasy_2
        print(platne_hlasy)
    
    except AttributeError:
        location_soup_okrsky = bs(r2.text, features="html.parser")
        okrsky_table = location_soup_okrsky.find("table", {"class", "table"})
        table_odkazy = okrsky_table.select('.cislo a')
        odkazy_okrsky = ["https://volby.cz/pls/ps2017nss/" + okrsky_table['href'] for okrsky_table in table_odkazy]
        print(odkazy_okrsky)


    nazvy_stran_1 = []
    nazvy_stran_2 = []
 
obsah_seznamu = True
for odkaz in odkazy: 
    r2 = requests.get(odkaz)
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
        
    if obsah_seznamu:
        if (len(nazvy_stran_1) > 0) and (len(nazvy_stran_2) > 0):
            nazvy_stran = nazvy_stran_1 + nazvy_stran_2
            obsah_seznamu = False
            print(nazvy_stran)

