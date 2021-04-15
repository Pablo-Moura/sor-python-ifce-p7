def calcularFatorial():
    if num >= 0:
        numAux = 1
        for x in range (1, num+1):
            numAux *= x
        return print(f'O fatorial do número {num} é {numAux}')
    else:
        print('O numero digitado não possui um auxiliar, por favor, digite um numero positivo.')

num = int(input('Digite um numero positivo para calcular o seu fatorial: '))
calcularFatorial()