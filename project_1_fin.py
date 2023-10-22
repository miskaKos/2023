"""

projekt_1_fin.py: první projekt do Engeto Online Python Akademie

author: Michaela Kosova

email: kosova.m@outlook.cz

discord: miskaKos

"""
oddelovac = ("-" * 30)

users = ['bob', 'ann', 'mike', 'liz']
passwords =['123', 'pass123', 'password123', 'pass123']

prihlasovani = True

while prihlasovani:
    username = input("username:")
    if username in users:
        index = users.index(username)
        password = input('password: ')

        if username in ((users)[index]) and password in ((passwords)[index]):
            print('Welcome')
            prihlasovani = False
        else:
            print('The password you have entered is incorrect')
            continue
    else:
        password = input('password: ')
        print('unregistered user, terminating the program..')
        quit()
    break


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

print(oddelovac)

print("Welcome to the app,", username)
print(f'We have {len(TEXTS)} texts to be analyzed.')

print(oddelovac)

text_number = input(f'Enter a number btw. 1 and {len(TEXTS)} select: ')

if not text_number.isnumeric():
    print("Once more") 
    quit()
else:
    text_number = int(text_number)

if text_number < 1 or text_number > len(TEXTS):
    print("Your choice is not in list")
    quit()

elif text_number > 1 or text_number < len(TEXTS):

    text = TEXTS[int(text_number) - 1]

    print(oddelovac)

    vycistena_slova = []
    slova_velke = []
    slova_vse_velke = []
    slova_vse_male = []
    cisla_v_textu = []
    delky_slov = []

    for slovo in text.split():
        # pocet slov
        cislo_slovo = slovo.strip('.,:;!?_')
        vycistena_slova.append(cislo_slovo)
        
        # prvni velke
        prvni_velke = slovo.istitle()
        slova_velke.append(prvni_velke)

        # vse velke
        vse_velke = slovo.isupper() and slovo.isalpha()
        slova_vse_velke.append(vse_velke)

        #  vse male
        vse_male = slovo.islower()
        slova_vse_male.append(vse_male)

        #  cisla v textu
        cisla = slovo.isnumeric()
        cisla_v_textu.append(cisla)

        # delky slov
        cislo_slovo = slovo.strip('.,:;!?_')
        delky_slov.append(len(cislo_slovo)) 

    pocet_slov = 0

    for slovo in vycistena_slova:
        pocet_slov += 1
        
    print("There are", pocet_slov, "words in the selected text.")

    pocet_velke = 0

    for slovo in slova_velke:
        if slovo == True:
            pocet_velke += 1
        
    print("There are", pocet_velke, "titlecase words.")

    pocet_vse_velke = 0

    for slovo in slova_vse_velke:
        if slovo == True:
            pocet_vse_velke += 1

    print("There are", pocet_vse_velke, "uppercase words.")

    pocet_vse_male = 0

    for slovo in slova_vse_male:
        if slovo == True:  
            pocet_vse_male += 1

    print("There are", pocet_vse_male, "lowercase words.")

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

    counts = dict()

    for cislo in delky_slov:
        if cislo not in counts:
            counts[cislo] = 1
            
        else: 
            counts[cislo] = counts[cislo] + 1

    values = counts.values()
    pocet_znaku_max = max(values)
    
    print("LEN", "|", "OCCURENCES".center(pocet_znaku_max), "|", "NR.")

    print(oddelovac)
            
    for key, value in sorted(counts.items()):

        print(str(key).rjust(3), "|", ("*" * value), "|".rjust(pocet_znaku_max - value + 1), value)

    print(oddelovac)
   
else:
    quit()


