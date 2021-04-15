from ladosDoTriangulo import *

class Triangulo():
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def areaDoTriangulo(self):
        print((self.ladoA * self.ladoB) / 2)

    def perimetroDoTriangulo(self):
        print(self.ladoA + self.ladoB + self.ladoC)

trianguloExemplo = Triangulo(verticeA, verticeB, verticeC)
trianguloExemplo.areaDoTriangulo()
trianguloExemplo.perimetroDoTriangulo()