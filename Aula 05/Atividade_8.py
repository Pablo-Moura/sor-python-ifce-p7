"""
8.Repita o exemplo anterior para inteiros de 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10
"""

import sys

lista = []
print(sys.getsizeof(lista))

for numero in range(1, 11):
    lista.append(numero)
    print(lista)
    print(sys.getsizeof(lista))