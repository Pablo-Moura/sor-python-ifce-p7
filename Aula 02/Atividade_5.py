# Escrever um programa em Python em que dada uma lista com números inteiros, retorna uma nova lista com os números ímpares (ou pares) contidos nesta lista.

lista = [1,5,8,2,9,4,10,6,3,7]
listaPar = []
listaImpar = []
    
print(lista)
listaS = sorted(lista)

for x in listaS:
    if x % 2 == 0:
        listaPar.append(x)
    else:
        listaImpar.append(x)
        
print(f'Lista Impar: {listaImpar}\nLista Par: {listaPar}')
