import random

class CriandoBingo():
    Id = 0

    def __init__(self):
        CriandoBingo.Id += 1
        self.criar_cartela()

    def criar_cartela(self):
        nome = 'BINGO'
        self.cartela = dict()
        for i, letra in enumerate(nome):
            lista = list(range(i * 15 + 1, i * 15 + 16))
            numeros = random.sample(lista, 5)
            self.cartela[letra] = numeros
        self.checar_cartela()
        return self.cartela

    def checar_cartela(self):
        with open('Castelas_BinGO.json', 'r') as file:
            nomes = file.readlines()
            cartela_string = f'{self.cartela}\n'
            if cartela_string not in nomes:
                self.salvar_cartela()
            else:
                self.criar_cartela()

    def salvar_cartela(self):
        with open('Castelas_BinGO.json', 'a') as arq:
            cartela_string = f'{self.cartela}\n'
            arq.write(cartela_string)

    def getId(self):
        return CriandoBingo.Id