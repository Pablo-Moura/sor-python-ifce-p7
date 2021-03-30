# Escrever um programa que coleta a senha do usuário (previamente ajustada), armazena a senha digitada em uma lista e retorna a quantidade de vezes que o usuário precisou para digitar a senha correta

senha = ''
vezes = 0

while senha != 'bobo':
    senha = input('Digite sua senha: ')
    vezes += 1
if vezes == 1:
    print(f'Você precisou de {vezes} tentativa para acertar sua senha.')
else:
    print(f'Você precisou de {vezes} tentativas para acertar sua senha.')
