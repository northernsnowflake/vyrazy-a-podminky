#Napiš program, který spočítá povrch a obsah krychle o straně 2852 cm.
#Abys nemusela tolik hledat v učebnici (vlastně Wikipedii): povrch S = 6a*a
#,obsah V = a*a*a
#Změň program tak, aby stranu/poloměr mohl uživatel zadat.

krychle = float(input('Zadej velikost strany krychle: '))
print('Povrch krychle o straně', krychle, 'cm je', 6*krychle*krychle,'cm')
print('Obsah krychle o straně', krychle, 'cm je', krychle*krychle*krychle,'cm')
