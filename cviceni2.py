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
  
    
if text_number == "1":
    text = text1
elif text_number == "2":
    text = text2
elif text_number == "3":
    text = text3

oddelovac = ("-" * 30)


if text_number in ["1","2","3"]:
    vycistena_slova = []

    for slovo in text.split():
        cislo_slovo = slovo.strip('.,:;!?_')
        vycistena_slova.append(cislo_slovo)

    pocet_slov = 0

    for slovo in vycistena_slova:
        pocet_slov += 1
        
    print("There are", pocet_slov, "words in the selected text.")

    slova_velke = []

    for slovo in text.split():
        prvni_velke = slovo.istitle()
        slova_velke.append(prvni_velke)

    pocet_velke = 0

    for slovo in slova_velke:
        if slovo == True:
            pocet_velke += 1
        
    print("There are", pocet_velke, "words in the selected text.")

    slova_vse_velke = []

    for slovo in text.split():
        vse_velke = slovo.isupper() and slovo.isalpha()
        slova_vse_velke.append(vse_velke)


    pocet_vse_velke = 0

    for slovo in slova_vse_velke:
        if slovo == True:
            pocet_vse_velke += 1

    print("There are", pocet_vse_velke, "uppercase words.")

    slova_vse_male = []

    for slovo in text.split():
        vse_male = slovo.islower()
        slova_vse_male.append(vse_male)

    pocet_vse_male = 0

    for slovo in slova_vse_male:
        if slovo == True:  
            pocet_vse_male += 1

    print("There are", pocet_vse_male, "lowercase words.")


    cisla_v_textu = []

    for slovo in text.split():
        cisla = slovo.isnumeric()
        cisla_v_textu.append(cisla)

    pocet_cisla = 0

    for slovo in cisla_v_textu:
        if slovo == True:  
            pocet_cisla += 1

    print("There are", pocet_cisla, "numeric strings.")


    emp_lis = []
    for z in text.split():
        if z.isdigit():
            emp_lis.append(int(z))

    soucet = 0
    for cislo in emp_lis:
        soucet += cislo

    print("The sum of all numbers", soucet)

    print(oddelovac)

    print(f"", "LEN", "|", "OCCURENCES".center(), "|", "NR.")

    print(oddelovac)

    delky_slov = []

    for slovo in text.split():
        cislo_slovo = slovo.strip('.,:;!?_')
        delky_slov.append(len(cislo_slovo)) 

    counts = dict()

    for cislo in delky_slov:
        if cislo not in counts:
            counts[cislo] = 1
            
        else: 
            counts[cislo] = counts[cislo] + 1
        
    for key, value in sorted(counts.items()):

        print(f"", str(key).rjust(3), "|", ("*" * value), "|".rjust(13 - value), value)

    print(oddelovac)

elif not text_number.isnumeric():
    print("Once more") 
    quit()
elif text_number not in ["1", "2", "3"]:
    print("Your choice is not in list")
    quit()
else:
    quit()