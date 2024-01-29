<!-- Engeto-pa-3-projekt -->
Election_scraper je třetím projektem do Engeto Online Python Akademie

## Popis projektu
Tento projekt slouží k získání výsledků z parlamentních voleb uskutečněných v roce 2017, odkaz k nahlédnutí naleznete [zde](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103).

## Instalace knihoven
Knihovny, které jsou použité v kódu projektu, jsou uložené v souboru requirements.txt. 
Pro jejich instalaci je vhodné použít nové virtuální prostředí a s nainstalovaným manažerem spustit dle níže uvedeného postupu:

$ pip3 --version                         # overim verzi manazeru
$ pip3 install -r requirements.txt       # nainstalujeme knihovny

## Spuštění projektu
Pro správné spuštění souboru election_scraper.py v příkazovém řádku jsou potřebné dva povinné argumenty, a to:

**python election_scraper.py <odkaz-uzemniho-celku> <vysledny-soubor>**

Následně budou staženy výsledky voleb zvolené obce jako "csv" soubor.

Pro správné otevření csv souboru v MS Excel byl použitý k zapisování dat do "csv" delimiter ";" [election_scraper.py řádek 153]

## Ukázka projektu
Výsledky hlasování pro okres Prostějov:
- je potřebné zadat dva povinné argumenty, a to:
1. argument: "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
2. argument: vysledky_prostejov.csv

Spouštění programu
election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky_prostejov.csv

Průběh stahování
STAHUJI DATA Z VYBRANEHO URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
UKLADAM DO SOUBORU vysledky_prostejov.csv
UKONCUJI election_scraper

Částečný výstup:
code;location;registred;envelopes;valid;Občanská demokratická strana;Řád národa - Vlastenecká unie;CESTA ODPOVĚDNÉ SPOLEČNOSTI;Česká str.sociálně demokrat.;Radostné Česko;STAROSTOVÉ A NEZÁVISLÍ;Komunistická str.Čech a Moravy;Strana zelených;ROZUMNÍ-stop migraci,diktát.EU;Strana svobodných občanů;Blok proti islam.-Obran.domova;Občanská demokratická aliance;Česká pirátská strana;Referendum o Evropské unii;TOP 09;ANO 2011;Dobrá volba 2016;SPR-Republ.str.Čsl. M.Sládka;Křesť.demokr.unie-Čs.str.lid.;Česká strana národně sociální;REALISTÉ;SPORTOVCI;Dělnic.str.sociální spravedl.;Svob.a př.dem.-T.Okamura (SPD);Strana Práv Občanů
506761;Alojzov;205;145;144;29;0;0;9;0;5;17;4;1;1;0;0;18;0;5;32;0;0;6;0;0;1;1;15;0
589268;Bedihošť;834;527;524;51;0;0;28;1;13;123;2;2;14;1;0;34;0;6;140;0;0;26;0;0;0;0;82;1
589276;Bílovice-Lutotín;431;279;275;13;0;0;32;0;8;40;1;0;4;0;0;30;0;3;83;0;0;22;0;0;0;1;38;0
589284;Biskupice;238;132;131;14;0;0;9;0;5;24;2;1;1;0;0;10;2;0;34;0;0;10;0;0;0;0;19;0
589292;Bohuslavice;376;236;236;20;0;0;23;0;3;22;3;4;6;0;1;17;0;4;53;1;1;39;0;0;3;0;36;0
589306;Bousín;107;67;67;5;0;0;4;0;3;14;0;2;0;0;0;7;0;2;10;0;0;9;0;0;0;0;11;0
...
