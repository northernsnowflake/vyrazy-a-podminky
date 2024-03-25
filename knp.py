#Vytvoř hru Kámen nůžky papír  

import random
seznam = ['kámen','nůžky','papír']

tah_pocitace = random.choice(seznam)
tah_hrace = input('kámen, nůžky, papír?')

print('tah pocitace je', tah_pocitace)
print('tah hrace je', tah_hrace)

if tah_hrace == 'kámen':
    if tah_pocitace == 'kámen':
        print('Remíza.')
    elif tah_pocitace == 'nůžky':
        print('Vyhrál jsi!')
    elif tah_pocitace == 'papír':
        print('Prohrál jsi!')

elif tah_hrace == 'nůžky':
    if tah_pocitace == 'kámen':
        print('Prohrál jsi!')
    elif tah_pocitace == 'nůžky':
        print('Remíza.')
    elif tah_pocitace == 'papír':
        print('Vyhrál jsi!')

elif tah_hrace == 'papír':
    if tah_pocitace == 'kámen':
        print('Vyhrál jsi!')
    elif tah_pocitace == 'nůžky':
        print('Prohrál jsi!')
    elif tah_pocitace == 'papír':
        print('Remíza.')
else:
    print('Pardon, znám jen tři slova - kámen, nůžky, papír')
