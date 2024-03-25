"""
Řetězce se dají sčítat. Dají se i násobit? Dělit? Odečítat? (Odpověz slovně.)
"""

# násobit ne, potřebuje čísla pro násobení
# >>> 'ABX' * 'A'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can't multiply sequence by non-int of type 'str'
  
# dělit ne
# 'AAA' / 'A'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for /: 'str' and 'str'
    
# odečítat ne
# 'AAA' - 'A'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
# >>>

# ----------------
"""
Co se stane, když se pokusím sečíst číslo a řetězec? (Můžeš vložit výsledek z příkazové řádky, ale odpověz i slovně)
"""

# TypeError - chyba typu, nelze sčítat 

# >>> 'A' + 2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str

# ----------------
"""
A vynásobit? (Můžeš vložit výsledek z příkazové řádky, ale odpověz i slovně)
"""

# >>> 'ABX' * 3
# 'ABXABXABX'
# Třikrát se napíše za sebe




"""Jaká chyba nastane, když zkusíš podělit řetězec řetězcem?"""
# TypeError

# >>> 'ABX' / 'A'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for /: 'str' and 'str'

"""
Jaká chyba nastane, když zkusíš použít proměnnou předtím, než do ní něco přiřadíš?"""


# >>> q + 1
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'q' is not defined

"""
Ne všechno se dá použít jako jméno proměnné. Fungují pro proměnné následující jména? Pokud ne, proč asi?

x
tlacitko4
34
3e4
krůta
$i
druha-odmocnina
readme.txt
kratsiStrana
POCET_BODU
_ (podtržítko)
π (pí)
True
_cache
__name__
while
"""
# 34, 3e4 - ne, jsou to čísla
# $i - ne, invalid syntax
# druha-odmocnina - je to výraz, nesmí být název proměnné 
# readme.txt - readme is not defined
# True - nejde, logická proměnná
# while - nejde, rezervované na příkaz
