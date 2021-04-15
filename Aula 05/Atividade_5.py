"""
5.Qual o tamanho ocupado na memória por um inteiro? Uma String vazia? Uma string de um único
caractere? E por um Byte de um caractere?
"""

import sys

numeroInteiro = 11
stringVazia = ''
stringQualquer = 'a'
byte = b'b'

print(sys.getsizeof(numeroInteiro))
print(sys.getsizeof(stringVazia))
print(sys.getsizeof(stringQualquer))
print(sys.getsizeof(byte))