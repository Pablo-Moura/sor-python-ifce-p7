"""
2.Escrever um programa em Python que encontre a palavra mais longa em um arquivo.
"""

arquivo = open('arquivo.txt')
linhas = arquivo.readlines()

maiorPalavra = ''
for linha in linhas:
    palavras = linha.split()
    for palavra in palavras:
        if len(palavra) > len(maiorPalavra):
            maiorPalavra = palavra

print(maiorPalavra)