"""

Čím se liší program:

if pocet_tykadel > 12:
    print("Odkud jste přiletěli?")
if pocet_tykadel > 6:
    print("Že by pavouček?")
else:
    print("Tak málo tykadel mě nezajímá!")
od programu:

if pocet_tykadel > 12:
    print("Odkud jste přiletěli?")
elif pocet_tykadel > 6:
    print("Že by pavouček?")
else:
    print("Tak málo tykadel mě nezajímá!")
"""
# V prvním se provede if, až se vyhodnotí, tak se provede druhé if a 
# když je druhé if splněno, else se přeskočí.
# V drhuhém se provede if a je-li splněno, zbytek se přeskočí
