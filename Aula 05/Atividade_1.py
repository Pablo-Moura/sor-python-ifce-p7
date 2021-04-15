"""
1.Escrever um programa em Python para informar ao usuário a quantidade de linhas e caracteres
de um arquivo texto.
"""

arquivo = open('arquivo.txt')
linhas = arquivo.readlines()

print(f'O número de linhas lidas nesse arquivo é {len(linhas)}')

arquivo.seek(0)
terminarDeLer = 0
caracteresLidos = 0

while terminarDeLer < 1:
    caractereAtual = arquivo.read(1)
    caracteresLidos += 1
    if caractereAtual == '':
        terminarDeLer = 1

print(f'O número de caracteres lidos nesse arquivo é {caracteresLidos}')