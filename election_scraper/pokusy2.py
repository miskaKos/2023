import sys
sys.argv
import csv
import json
import requests
import bs4 
from bs4 import BeautifulSoup as bs
import traceback
import pandas as pd 


url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"

def zpracuj_odpoved_serveru(url: str) -> bs:
    r = requests.get(url)
    return bs(r.text, features="html.parser")


def najdi_tabulku(soup: bs) -> bs4.element.Tag:
    return soup.find("div", {"id": "inner"})
    

def najdi_nazvy_cisla_obci(obec_seznam: bs4.element.Tag) -> list:
    nazvy_obci = []
    cisla_obci = []

    nazvy_obci_podklad = obec_seznam.find_all("td", {"class": "overflow_name"})
    for i in nazvy_obci_podklad:
        nazvy_obci.append(i.text.strip())    

    cisla_obci_podklad = obec_seznam.find_all("td", {"class": "cislo"})
    for k in cisla_obci_podklad:
        cisla_obci.append(k.text.strip())
      
    return nazvy_obci, cisla_obci
    

def vytvor_odkazy_obce_jednotlive(obec_seznam: bs4.element.Tag) -> list:
    podklady_odkazy = obec_seznam.select('.cislo a')
    return ["https://volby.cz/pls/ps2017nss/" + obec_seznam['href'] for obec_seznam in podklady_odkazy]


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

    nazvy_stran = []

    nazvy_stran_podklad = nazvy_stran_seznam.find_all("td", {"class":"overflow_name"})

    for i in nazvy_stran_podklad:
        nazvy_stran.append(i.text.strip())
    
    return nazvy_stran


def vytvor_list_fin_cast_1(cisla_obci, nazvy_obci, registred, envelopes, valid: list) -> list:
    fin_cast_1 = []
    for index in range(0, len(cisla_obci)):
        p = [cisla_obci[index], nazvy_obci[index], registred[index], envelopes[index], valid[index]]
        fin_cast_1.append(p)
    return fin_cast_1

def vytvor_list_fin_cast_2(fin_cast_1, platne_hlasy_strany: list) -> list:
    # fin_cast_2 = []
    for index in range(0, len(fin_cast_1)):
        # r = [fin_cast_1[index], platne_hlasy_strany[index]]
        fin_cast_1[index].extend(platne_hlasy_strany[index])
        # fin_cast_2.append(r)
    return fin_cast_1

#  def uloz_seznam_do_json(udaje: list):
#     with open("vysledek.json", mode="w", encoding="utf-8") as f:
#         json.dump(udaje, f)

# json_soubor = open("vysledek.json", mode="w")
# json.dump(d_pole, json_soubor)
# json_soubor.close()

# zapis_json = uloz_seznam_do_json(d_pole)
# print(zapis_json)

def zapis_data(hlavicka, fin_cast_2: list, jmeno_souboru: str) -> str:
    """
    Zkus zapsat udaje z par. 'data' do souboru formatu .csv.
    """
    try:
        csv_soubor = open(jmeno_souboru, mode="w", encoding="utf-8")
        sloupce = hlavicka
    except FileExistsError:
        return traceback.format_exc()
    except IndexError:
        return traceback.format_exc()
    else:
        zapis = csv.DictWriter(csv_soubor, dialect="excel", fieldnames = sloupce)
        zapis.writeheader()      
        zapis.writerows(fin_cast_2)
        return "Saved"
    finally:
        csv_soubor.close()

    return zapis_data(hlavicka, fin_cast2, jmeno_souboru)
        
def main(url: str):
    soup = zpracuj_odpoved_serveru(url) 
    obec_seznam = najdi_tabulku(soup)
    nazvy_obci, cisla_obci = najdi_nazvy_cisla_obci(obec_seznam)
    odkazy = vytvor_odkazy_obce_jednotlive(obec_seznam)
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

    nazvy_stran_test = ['Občanská demokratická strana', 'Řád národa - Vlastenecká unie', 'CESTA ODPOVĚDNÉ SPOLEČNOSTI', 'Česká str.sociálně demokrat.', 'Radostné Česko', 'STAROSTOVÉ A NEZÁVISLÍ', 'Komunistická str.Čech a Moravy', 'Strana zelených', 'ROZUMNÍ-stop migraci,diktát.EU', 'Strana svobodných občanů', 'Blok proti islam.-Obran.domova', 'Občanská demokratická aliance', 'Česká pirátská strana', 'Referendum o Evropské unii', 'TOP 09', 'ANO 2011', 'Dobrá volba 2016', 'SPR-Republ.str.Čsl. M.Sládka', 'Křesť.demokr.unie-Čs.str.lid.', 'Česká strana národně sociální', 'REALISTÉ', 'SPORTOVCI', 'Dělnic.str.sociální spravedl.', 'Svob.a př.dem.-T.Okamura (SPD)', 'Strana Práv Občanů']
    hlavicka = ['code', 'location', 'registred', 'envelopes', 'valid']
    hlavicka.extend(nazvy_stran_test)
    # print(hlavicka)
    fin_cast_1 = vytvor_list_fin_cast_1(cisla_obci, nazvy_obci, registred, envelopes, valid)
    fin_cast_2 = vytvor_list_fin_cast_2(fin_cast_1, platne_hlasy_strany)
    # print(fin_cast_2[:2])

    with open("prostejov.csv", "w", encoding='UTF8', newline='' ) as f:
        write = csv.writer(f, delimiter = "|", dialect="excel-tab")

        write.writerow(hlavicka)
        write.writerows(fin_cast_2)
        
    # zapis_csv = zapis_data(hlavicka, fin_cast_2, "vysledky_prostejov.csv")
    
                  
if __name__ == "__main__":
    url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
    main(url)   