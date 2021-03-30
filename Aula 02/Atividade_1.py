# Escrever um programa para somar todos os elementos de uma lista de números

soma = 0
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in range(len(lista)):
    soma = soma + lista[x]
print(f'O valor da soma é {soma}')
