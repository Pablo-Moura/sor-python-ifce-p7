import math

def raizQuadrada():
    if num > 0:
        print(math.sqrt(num))
    else:
        print('Esse não é um número válido.')

num = int(input('Digite um número inteiro maior que 0: '))
raizQuadrada()