# Escrever um programa que Informe ao usuário o maior e o menor elemento de uma lista e o valor médio dos elementos da lista, Utilize uma lista com 10 números.

import random

# Criando uma lista vazia
lista = []

# Adicionando valores aleatórios para a lista
for x in range (0, 10):
    ale = random.randrange(1, 11)
    print(f'O numero {ale} entrou na lista.')
    lista.append(ale)

# Reorganizando a lista do menor número para o maior
listaS = sorted(lista)

# Exibindo o menor e o maior valor da lista
print(f'Lista atual: {lista}')
print(f'\nO maior numero da lista é: {listaS[-1]}\nO menor numero da lista é: {listaS[0]}')

# Calculando e exibindo o valor médio da lista
valor_medio = (listaS[4] + listaS[5]) / 2
print(f'O valor médio é: {valor_medio}')
