import requests
import bs4

def posli_pozadavek_get(url: str) -> str:
    odpoved_serveru = requests.get(url)
    return odpoved_serveru.text

def ziskej_parsovanou_odpoved(odpoved_serveru: str) -> bs4.BeautifulSoup:
    return bs4.BeautifulSoup(odpoved_serveru.content, features="html.parser")

def vyber_tr_tagy(odpoved_serveru: bs4.BeautifulSoup) -> bs4.element.ResultSet:
    return odpoved_serveru.find_all("tr")
    