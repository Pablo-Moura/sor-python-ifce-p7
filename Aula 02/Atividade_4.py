# Escrever um programa em Python que remove os elementos duplicados de uma lista
import random

lista = []
rand = 0
for x in range (0, 10):
    rand = random.randrange(0, 10)
    print(f'O numero {rand} foi adicionado a lista.')
    lista.append(rand)
    
print(f'{lista}')
print(f'\nRemovendo Duplicados...\n')
print(set(lista))
