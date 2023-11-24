import random

nevhodne_cislo = True

while nevhodne_cislo:
    cislo_nahodne = str(random.randint(1000, 9999))
    duplikat = False

    for i in range(len(cislo_nahodne)):
        for j in range(i+1, len(cislo_nahodne)):
            if cislo_nahodne[i] == cislo_nahodne[j]:
                duplikat = True
                break
    if duplikat == False:
        nevhodne_cislo = False
        
print(cislo_nahodne)