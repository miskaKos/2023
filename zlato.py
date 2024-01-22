import requests
from bs4 import BeautifulSoup

bi_url = "https://markets.businessinsider.com/commodities/gold-price"

# odpoved = requests.get(bi_url)

"""

* odpoved.text - objekt typu 'str',

* feature - argument, který upřesní typ rozdělovače.

"""

# rozdelene_html = BeautifulSoup(odpoved.text, features="html.parser")
# print(rozdelene_html)

def ziskej_cenu_zlata(url: str) -> str:
    odpoved_serveru = requests.get(url)
    rozdelene_html = BeautifulSoup(odpoved_serveru.content, features="html.parser")

    cena_zlata = rozdelene_html.find(
        "span",
        {"class": "price-section__current-value"}
    ).get_text()
    
    return cena_zlata

cena = ziskej_cenu_zlata(bi_url)

print(cena)
