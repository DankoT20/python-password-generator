import string
import random
import numpy as np

szamok = np.arange(0,10)
str_szamok = ""

for z in szamok:
   str_szamok += str(z)

def jelszo():
    generalt_jelszo = ""
    lehetosegek = string.ascii_lowercase + string.ascii_uppercase + str_szamok
    while True:
        hossz = int(input("Kérem adja meg a jelszó hosszát: "))
        if type(hossz) == int:
            break
        else:
            print("Kérem számot adjon meg")
    for i in range(hossz):
        randomChar = lehetosegek[random.randint(0, len(lehetosegek))]
        generalt_jelszo += randomChar

    print(f"A generált jelszava: {generalt_jelszo}")


jelszo()

