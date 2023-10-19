text1 = """
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.
"""

text2 = """
At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.
"""

text3 = """
The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.
"""


text_number = input("Enter a number btw. 1 and 3 select: ")

#if not text_number.isnumeric():
#    print("Once more") 
#    quit()
#elif text_number not in ["1", "2", "3"]:
#    print("Your choice is not in list")
#    quit()
#else:
    
    
if text_number == '1':
    vycistena_slova = []

    for slovo in text1.split():
        cislo_slovo = slovo.strip('.,:;!?_')
        vycistena_slova.append(cislo_slovo)

    pocet_slov = 0

    for slovo in vycistena_slova:
        pocet_slov += 1
    
    print("There are", pocet_slov, "words in the selected text.")

    slova_velke = []

    for slovo in text1.split():
        prvni_velke = slovo.istitle()
        slova_velke.append(prvni_velke)

    pocet_velke = 0

    for slovo in slova_velke:
        if slovo == True:
            pocet_velke += 1
    
    print("There are", pocet_velke, "words in the selected text.")

elif text_number == '2':
    vycistena_slova = []

    for slovo in text2.split():
        cislo_slovo = slovo.strip('.,:;!?_')
        vycistena_slova.append(cislo_slovo)

    pocet_slov = 0

    for slovo in vycistena_slova:
        pocet_slov += 1
    
    print("There are", pocet_slov, "words in the selected text.")

    slova_velke = []

    for slovo in text2.split():
        prvni_velke = slovo.istitle()
        slova_velke.append(prvni_velke)

    pocet_velke = 0

    for slovo in slova_velke:
        if slovo == True:
            pocet_velke += 1
    
    print("There are", pocet_velke, "words in the selected text.")

elif text_number == '3':
    vycistena_slova = []

    for slovo in text3.split():
        cislo_slovo = slovo.strip('.,:;!?_')
        vycistena_slova.append(cislo_slovo)

    pocet_slov = 0

    for slovo in vycistena_slova:
        pocet_slov += 1
    
    print("There are", pocet_slov, "words in the selected text.")

    slova_velke = []

    for slovo in text3.split():
        prvni_velke = slovo.istitle()
        slova_velke.append(prvni_velke)

    pocet_velke = 0

    for slovo in slova_velke:
        if slovo == True:
            pocet_velke += 1
    
    print("There are", pocet_velke, "words in the selected text.")

elif not text_number.isnumeric():
    print("Once more") 
    quit()
elif text_number not in ["1", "2", "3"]:
    print("Your choice is not in list")
    quit()
else:
    quit()