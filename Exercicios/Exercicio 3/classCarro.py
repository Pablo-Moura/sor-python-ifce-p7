"""
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
- Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa
    quantidade de combustível no tanque.
- O consumo é especificado no construtor e o nível de combustível inicial é 0.
- Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa
    distância, reduzindo o nível de combustível no tanque de gasolina.
- Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
- Forneça um método adicionarGasolina( ), para abastecer o tanque.
"""
from classCarroInput import *

class Carro():
    def __init__(self, consumo):
        self.consumo = consumo
        self.gInicial = 0

    def andar(self):
        global gasolinaAtual
        gasolinaTemporaria = gasolinaAtual - (distanciaPercorrida / self.consumo)
        if gasolinaTemporaria < 0:
            print('Não é possivel percorrer a distancia fornecida, tente novamente.')
        else:
            gasolinaAtual = gasolinaAtual - (distanciaPercorrida / self.consumo)
            print(f'Você andou {distanciaPercorrida} km, gastando 1 litro por cada {self.consumo} km percorridos.')

    def adicionarGasolina(self):
        global gasolinaAtual
        gasolinaAtual = self.gInicial + litrosAbastecidos
        return print(f'Você adicionou {litrosAbastecidos}L de gasolina ao tanque.')

    def obterGasolina(self):
        print('Você possui: {:.2f}L de gasolina no tanque.'.format(gasolinaAtual))

Chevette = Carro(20)
Chevette.adicionarGasolina()
Chevette.andar()
Chevette.obterGasolina()

