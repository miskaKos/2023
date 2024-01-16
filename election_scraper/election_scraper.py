import sys
sys.argv
import csv
import json
import requests
import bs4 
from bs4 import BeautifulSoup as bs


# url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"

def zpracuj_odpoved_serveru(url: str) -> bs:
    odpoved_serveru = requests.get(url)
    return bs(odpoved_serveru.text, features="html.parser")

def najdi_tabulku(rozdelene_html: bs) -> bs4.element.ResultSet:
    tabulky = rozdelene_html.find("div", {"id": "inner"}, )
    # return tabulky
    # return tabulky.find_all("table", {"class": "table"})
    return tabulky.find_all("tr")

def zpracuj_tr(tr: bs4.element.Tag) -> dict:
    radky = (tr.get_text).splitlines()
    # radky = [r.('') for r in radky]
    d = {
        "cislo": ,
        "nazev":
    }
    print(radky)

# def najdi_sloupce_obec(vsechny_tabulky: bs) -> bs4.element.ResultSet:
#     # vsechny_tr = vsechny_tabulky.find_all("tr")
#     seznam = list()
#     for tr in vsechny_tabulky[2:]:
#         td_na_radku = tr.find_all("td")
#         data_obce = (td_na_radku[0].text, td_na_radku[1].text, td_na_radku[2].text)
#         seznam.append(data_obce)
#         return seznam
#         # return (td_na_radku[0].text, td_na_radku[1].text, td_na_radku[2].text)
    
#     # data_hrace = vyber_atributy_z_radku(td_na_radku)
#     # vysledky.append(data_hrace)

def main(url: str):
    rozdelene_html = zpracuj_odpoved_serveru(url)
    vsechny_tabulky = najdi_tabulku(rozdelene_html)
    for tr in vsechny_tabulky[2: -2]:
        zpracuj_tr(tr)
    # print(vsechny_tabulky[2:])
    # sloupce_obec = najdi_sloupce_obec(vsechny_tabulky)
    # print(sloupce_obec)


if __name__ == "__main__":
    url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
    main(url)


    

# odpoved_serveru = requests.get(url)

# rozdelene_html = bs(odpoved_serveru.text, features="html.parser")
# print(rozdelene_html.prettify())
# print(rozdelene_html.head)
# print(rozdelene_html.body)

# a = rozdelene_html.find_all("a")
# print(a)

# najit vsechny radky tabulky ze stranky
# table_tag_top = rozdelene_html.find("table", {"class": "table"})
# vsechny_tr = table_tag_top.find_all("tr")

# # najit vybrane sloupce z tabulky
# for tr in vsechny_tr[2:]:
#     td_na_radku = tr.find_all("td")
#     print(td_na_radku[0].text, td_na_radku[1].text)

# table_tag_top = soup.find("table", {"class": "tab_top"})  # <table></table>
# vsechny_tr = table_tag_top.find_all("tr")
# vysledky = []  # list[dict]
# for tr in vsechny_tr[1:]:
#     td_na_radku = tr.find_all("td")
#     data_hrace = vyber_atributy_z_radku(td_na_radku)
#     vysledky.append(data_hrace)
    
# def vyber_atributy_z_radku(td_na_radku: "bs4.element.ResultSet"):
#     """
#     Z kazdeho radku (tr) vyber urcite bunky (td)[index])
#     a zabal je do slovniku
    
#     :return: dict
#     """
#     return {
#         "cislo_obce": td_na_radku[0].text,
#         "nazev_obce": td_na_radku[1].text
#     }



# precte obsah stranky 
# print(rozdelene_html.body.contents)
# for string in rozdelene_html.strings:
#     if string == "\n":
#         continue
#     print(string)


    
# print(rozdelene_html.body.children)

# for child in rozdelene_html.body.children:
#     print(child)

# boxes = soup.find_all


# write.csv(volby, "prostejov.csv")

