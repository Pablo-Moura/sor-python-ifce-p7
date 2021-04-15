"""
4.Defina uma variável inteira, um float e um decimal atribuindo valores a cada um deles. Qual a
quantidade de memória utilizada por cada um deles?
"""

numeroInteiro = 1
numeroReal = 3.2
numeroDecimal = 0.1

print(numeroInteiro.__sizeof__())
print(numeroReal.__sizeof__())
print(numeroDecimal.__sizeof__())