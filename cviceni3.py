oddelovac = ("-" * 30)

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

slova_vse_velke = []

for slovo in text1.split():
    vse_velke = slovo.isupper() and slovo.isalpha()
    slova_vse_velke.append(vse_velke)


pocet_vse_velke = 0

for slovo in slova_vse_velke:
    if slovo == True:
        pocet_vse_velke += 1

print("There are", pocet_vse_velke, "uppercase words.")

slova_vse_male = []

for slovo in text1.split():
    vse_male = slovo.islower()
    slova_vse_male.append(vse_male)

pocet_vse_male = 0

for slovo in slova_vse_male:
    if slovo == True:  
        pocet_vse_male += 1

print("There are", pocet_vse_male, "lowercase words.")


cisla_v_textu = []

for slovo in text1.split():
    cisla = slovo.isnumeric()
    cisla_v_textu.append(cisla)

pocet_cisla = 0

for slovo in cisla_v_textu:
    if slovo == True:  
        pocet_cisla += 1

print("There are", pocet_cisla, "numeric strings.")


emp_lis = []
for z in text1.split():
   if z.isdigit():
      emp_lis.append(int(z))

soucet = 0
for cislo in emp_lis:
    soucet += cislo

print("The sum of all numbers", soucet)

print(oddelovac)

print(f"", "LEN", "|", "OCCURENCES  ", "|", "NR.")

print(oddelovac)

delky_slov = []

for slovo in text1.split():
    cislo_slovo = slovo.strip('.,:;!?_')
    delky_slov.append(len(cislo_slovo)) # řešit čísla??

counts = dict()

for cislo in delky_slov:
    if cislo not in counts:
        counts[cislo] = 1
        
    else: 
        counts[cislo] = counts[cislo] + 1
    
for key, value in sorted(counts.items()):

    print(f"", str(key).rjust(3), "|", ("*" * value), "|".rjust(13 - value), value)

print(oddelovac)


