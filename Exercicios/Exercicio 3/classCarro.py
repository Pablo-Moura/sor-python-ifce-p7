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

class Carro():
    def __init__(self, consumo):
        self.consumo = consumo
        self.litrosAbastecidos = float(input('Quantos litros você deseja abastecer? '))
        self.gInicial = 0

    def andar(self):
        global distanciaPercorrida, gasolinaAtual
        distanciaPercorrida = int(input('Quantos km você deseja andar? '))
        gasolinaTemporaria = gasolinaAtual - (distanciaPercorrida / self.consumo)
        if gasolinaTemporaria < 0:
            print('Não é possivel percorrer a distancia fornecida, tente novamente.')
        else:
            gasolinaAtual = gasolinaAtual - (distanciaPercorrida / self.consumo)
            print(f'Você andou {distanciaPercorrida} km, gastando 1 litro por cada {self.consumo} km percorridos.')

    def adicionarGasolina(self):
        global gasolinaAtual
        gasolinaAtual = self.gInicial + self.litrosAbastecidos
        return print(f'Você adicionou {self.litrosAbastecidos} litros de gasolina ao tanque.')

    def obterGasolina(self):
        if gasolinaAtual == 1:
            print(f'Você possui: {gasolinaAtual} litro de gasolina no tanque.')
        else:
            print(f'Você possui: {gasolinaAtual} litros de gasolina no tanque.')

Chevette = Carro(20)
Chevette.adicionarGasolina()
Chevette.andar()
Chevette.obterGasolina()

