'''
Na srazu jsme spolu vytvářeli program, který píše různé nesmysly podle uživatelem zadaného věku.

Zkus napsat program, který píše hlášky podle zadané rychlosti chůze, váhy ulovené ryby, počtu tykadel, teploty vody nebo třeba vzdálenosti od rovníku.

(Pošli ten nejzdařilejší; kdyby ses chtěla pochlubit několika verzemi, dej je všechny do jedné odpovědi.)
'''

vzd = int(input('Jaká je tvoje vzdálenost od rovníku (na sever nebo na jih)? v tis.km Např. 4, 5...'))
if vzd >=5:
    print('Jsi na úrovni Paříže, nebo blíže k pólu')
elif vzd >=4:
    print('Jsi na úrovni New Yorku, Tokya.')
elif vzd >= 3:
    print('Jsi na úrovni Káhiry/Johannesburgu.')
elif vzd >= 2:
    print('Jsi na úrovni neznámého města')
elif vzd >= 1:
    print('Jsi na úrovni Panama City.')
else:
    print('Jsi na úrovni Bornea.')
