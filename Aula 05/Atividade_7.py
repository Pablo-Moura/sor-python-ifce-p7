"""

7.Criar um script que exiba a quantidade de memória ocupada por uma lista vazia, lista com
apenas um elemento de 1 caractere, com dois caracteres, três, até 10 caracteres.

"""

import sys

lista = []
print(sys.getsizeof(lista))
letra = ''

for elemento in range(1, 11):
    for caractere in range(1, elemento+1):
        letra += 'o'
    lista.append(letra)
    letra = ''
    print(lista)
    print(sys.getsizeof(lista))