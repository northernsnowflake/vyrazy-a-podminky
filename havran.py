'''
Napiš program, který po zadání správného hesla vypíše nějakou „tajnou informaci“.

Vhodné tajemství je třeba: V pátek jsem viděl černého havrana.
'''

heslo = str(input('Zadej heslo a vypíšu tajnou informaci:'))
while heslo != 'havran':
    heslo = str(input('Zadej heslo a vypíšu tajnou informaci:'))
else:
    print('V pátek jsem viděl černého havrana.')
