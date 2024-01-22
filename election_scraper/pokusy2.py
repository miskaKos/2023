import sys
sys.argv
import csv
import json
import requests
import bs4 
from bs4 import BeautifulSoup as bs
import traceback

url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"

def zpracuj_odpoved_serveru(url: str) -> bs:
    r = requests.get(url)
    return bs(r.text, features="html.parser")

# zrusit funkciu?

def najdi_tabulku(soup: bs) -> bs4.element.Tag:
    return soup.find("div", {"id": "inner"})
     

def najdi_td(obec_seznam: bs4.element.Tag) -> bs4.element.ResultSet:
    return obec_seznam.find_all("td")

def najdi_nazvy_cisla_obci(vsechny_td: bs4.element.ResultSet) -> list:
    list = []
    for i in vsechny_td:
        if i:
            list.append(i.text.strip())

    nazvy_obci = []
    cisla_obci = []
    for polozka in list:
        if polozka.istitle() and len(polozka) > 1:
            nazvy_obci.append(polozka)
            
    for polozka in list:
        if polozka.isdigit():
            cisla_obci.append(polozka)
    return nazvy_obci, cisla_obci

def vytvor_odkazy_obce_jednotlive(obec_seznam: bs4.element.Tag) -> list:
    # podklady_odkazy = obec_seznam.find_all("td", {"class":"cislo", "headers":("t1sa1")})
    podklady_odkazy = obec_seznam.select('.cislo a')
    # return podklady_odkazy
    return ["https://volby.cz/pls/ps2017nss/" + obec_seznam['href'] for obec_seznam in podklady_odkazy]


def vytvor_dict_nazvy_cisla_obci(cisla_obci, nazvy_obci: list) -> dict:
    d_pole = []
    for index in range(0, len(nazvy_obci)):
        d = {"code": cisla_obci[index], "location": nazvy_obci[index]}
        d_pole.append(d)
    return d_pole

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
        
        
def vytvor_pocty_seznam_list(r2: requests.models.Response) -> list:
    location_soup = bs(r2.text, features="html.parser")
    cisla_seznam = location_soup.find("table", {"id": "ps311_t1"})
    cisla_seznam_td = cisla_seznam.find_all("td")
    cisla_seznam_list = []
    for j in cisla_seznam_td:
        cisla_seznam_list.append(j.text.strip())
    cisla_seznam_list = [r.replace("\xa0", "") for r in cisla_seznam_list]
    return cisla_seznam_list


def najdi_seznam_platne_hlasy(r2: requests.models.Response) -> list:
    location_soup = bs(r2.text, features="html.parser")
    strany_seznam = location_soup.find("div", {"id": "inner"})

    platne_hlasy_podklad_1 = strany_seznam.find_all("td", {"class":"cislo", "headers": ("t1sb3")})
    platne_hlasy_podklad_2 = strany_seznam.find_all("td", {"class":"cislo", "headers": ("t2sb3")})
    
    platne_hlasy_1 = []
    platne_hlasy_2 = []

    for i in platne_hlasy_podklad_1:
        platne_hlasy_1.append(i.text.strip())

    platne_hlasy_1 = [r.replace("\xa0", "") for r in platne_hlasy_1]
   
    for i in platne_hlasy_podklad_2:
        platne_hlasy_2.append(i.text.strip())

    platne_hlasy_2 = [r.replace("\xa0", "") for r in platne_hlasy_2]

    return platne_hlasy_1 + platne_hlasy_2   
 

def najdi_seznam_pol_stran(r2: requests.models.Response) -> list:
    nazvy_stran_soup = bs(r2.text, features="html.parser")
    nazvy_stran_seznam = nazvy_stran_soup.find("div", {"id": "inner"})

    nazvy_stran_1 = []
    nazvy_stran_2 = []

    nazvy_stran_podklad_1 = nazvy_stran_seznam.find_all("td", {"class":"overflow_name", "headers": "t1sa1"})
    nazvy_stran_podklad_2 = nazvy_stran_seznam.find_all("td", {"class":"overflow_name", "headers": "t2sa1"})

    for i in nazvy_stran_podklad_1:
        nazvy_stran_1.append(i.text.strip())

    # print(nazvy_stran_1)

    for i in nazvy_stran_podklad_2:
        nazvy_stran_2.append(i.text.strip())
    return nazvy_stran_1 + nazvy_stran_2


def main(url: str):
    soup = zpracuj_odpoved_serveru(url) 
    obec_seznam = najdi_tabulku(soup)
    vsechny_td = najdi_td(obec_seznam)
    nazvy_obci, cisla_obci = najdi_nazvy_cisla_obci(vsechny_td)
    odkazy = vytvor_odkazy_obce_jednotlive(obec_seznam)
    dict_fin = vytvor_dict_nazvy_cisla_obci(cisla_obci, nazvy_obci)

    nazvy_stran = najdi_seznam_pol_stran(requests.get(odkazy[0]))

    registred = []
    envelopes = []
    valid = []
    platne_hlasy_strany = []

    for odkaz in odkazy:
        r2 = requests.get(odkaz)
        cisla_seznam_list = vytvor_pocty_seznam_list(r2)
        registred.append(cisla_seznam_list[3])
        envelopes.append(cisla_seznam_list[4])
        valid.append(cisla_seznam_list[7])
        platne_hlasy_strany.append(najdi_seznam_platne_hlasy(r2))
    
    print(registred)
                  
if __name__ == "__main__":
    url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
    main(url)   