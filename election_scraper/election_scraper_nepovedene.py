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

def najdi_radky(rozdelene_html: bs) -> bs4.element.ResultSet:
    radky = rozdelene_html.find("div", {"id": "inner"}, )
    # tabulky = rozdelene_html.select("oveflow_name")
    # tabulky = rozdelene_html.find("table", {"class": "table"})
    # return tabulky
    # return tabulky.find_all("table", {"class": "table"})
    # return radky.find_all("tr")
    return radky.find_all("td")


def zpracuj_sloupce(sloupec: bs4.element.Tag):
#     # sloupce = (sloupec.text).splitlines()
#     sloupce = (sloupec.text).split()
    sloupce = (sloupec.get_text())
#     # sloupce = sloupec.get_text(separator).splitlines()
#     # print(sloupce) 
    return sloupce 

# def urob_list():
#     for sloupec in vsechny_radky:
#         vxa = zpracuj_sloupce(sloupec)
#         vxa2 = vxa[0]
#         listik = "".join(vxa2)
#     return listik

    
   
    # radky = [r.('') for r in radky]
    # d = {
    #     "cislo": sloupce.readlines[0](sloupce[1]),
    #     "nazev": sloupce.readlines[1](sloupce[2])
    # }
    # return d

# def vyber_atributy_z_radku(td_na_radku: "bs4.element.ResultSet") -> dict:
#     """
#     Z kazdeho radku (tr) vyber urcite bunky (td)[index])
#     a zabal je do slovniku
    
#     :return: dict
#     """
#     return {
#         "cislo_obce": td_na_radku[1].text,
#         "nazev_obce": td_na_radku[2].text
    # }

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
    vsechny_radky = najdi_radky(rozdelene_html)
    for sloupec in vsechny_radky:
        vxa = zpracuj_sloupce(sloupec)
        print(vxa)
        # for elem in vxa:
        #     elem.append(listik)
        #     print(listik)


    # for string in vxa:
    #     sloucit = "\n".join(string)
    #     print(sloucit)
    #     # vxa2 = vxa[0]
    #     listik = "\n".join(vxa)
    #     # seznam = []
    #     # for polozka in listik:
    #     #     if polozka.isnumeric:
    #     #         polozka.append(seznam)
        
    #     print(listik)
    #     # print(listik2)

    # seznam = []
    # for tr in vsechny_radky[1:]:
    #     td_na_radku = tr.find_all("td")
    #     print(td_na_radku[2].text)
        # data_obce = vyber_atributy_z_radku(td_na_radku)
        # seznam.append(data_obce)

    # for sloupec in vsechny_radky:
    #     vxa = zpracuj_sloupce(sloupec)
    #     print(vxa)
    # sloupce_obec = zpracuj_sloupce(vsechny_radky)
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
#     

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

#!/bin/env python
# from csv     import reader
# from os.path import isfile
# from sys     import argv, exit

# def quit():
#     print "\nStiskni ENTER pro konec..."
#     raw_input()
#     exit()

# def main():
#     if  len(argv) < 2:
#         print "Zadej CSV soubor jako parametr."
#         quit()

#     csvPath = argv[1]

#     if  not isfile(csvPath):
#         print "Soubor '%s' neexistuje." % csvPath
#         quit()

#     csvFile = open(csvPath, 'rb')
#     parser  = reader(csvFile, dialect='excel', delimiter=';')

#     html = ['<table>']

#     for i, row in enumerate(parser):
#         eo = 'odd' if i % 2 else 'even'
#         html.append('  <tr class="%s row%d">' % (eo, i))
#         for j, cell in enumerate(row):
#             cell = cell.replace('&', '&amp;')
#             cell = cell.replace('<', '&lt;')
#             html.append('    <td class="col%d cell%d-%d">%s</td>' % (j, i, j, cell))
#         html.append('  </tr>')

#     html.append('</table>')

#     htmlTxt = '\n'.join(html)

#     htmlFile = open(csvPath + '.html', 'wt')
#     htmlFile.write(htmlTxt)
#     htmlFile.close()

#     print "\n\nHOTOVO"
#     quit()

# try:
#     print "Konverze csv souboru do html tabulky."
#     print "Copyright (c) 2007, Petr Mach, gsl@seznam.cz"
#     print "Licence: GPL v 2.0, http://www.gnu.org/…gpl-2.0.html"
#     print
#     main()
# except Exception, e:
#     print "\n\nZACHYCENA CHYBA V PROGRAMU:\n"
#     print e
#     quit()