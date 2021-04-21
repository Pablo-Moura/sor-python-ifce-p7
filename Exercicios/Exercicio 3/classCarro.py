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
from tkinter import *

class Carro():
    def __init__(self, consumo):
        self.consumo = consumo
        self.gInicial = 0

    def andar(self):
        global gasolinaAtual
        distanciaPercorrida = float(ed.get())
        gasolinaTemporaria = gasolinaAtual - (distanciaPercorrida / self.consumo)
        if gasolinaTemporaria < 0:
            print('Não é possivel percorrer a distancia fornecida, tente novamente.')
        else:
            gasolinaAtual = gasolinaAtual - (distanciaPercorrida / self.consumo)
            print(f'Você andou {distanciaPercorrida} km, gastando 1 litro por cada {self.consumo} km percorridos.')

    def adicionarGasolina(self):
        global gasolinaAtual
        litrosAbastecidos = float(ed.get())
        gasolinaAtual = self.gInicial + litrosAbastecidos
        return print(f'Você adicionou {litrosAbastecidos}L de gasolina ao tanque.')

    def obterGasolina(self):
        print('Você possui: {:.1f}L de gasolina no tanque.'.format(gasolinaAtual))

def buttonClick1():
    global lbTemporaria
    Chevette.adicionarGasolina()

    lb1['text'] = f'Você adicionou {ed.get()}L de gasolina'
    lb3['text'] = 'Quantos quilometros você deseja percorrer?'
    lbTemporaria = lbTemporaria + lb1['text']

    btConfirm1.destroy()
    ed.pack_forget()
    passoAPasso()

    lbLinha.pack(side=TOP)
    ed.pack(side=TOP)
    lb3.pack(side=TOP)
    btConfirm2.pack(side=TOP)

def buttonClick2():
    global lbTemporaria
    Chevette.andar()

    lb1['text'] = f'Você andou {ed.get()}km, consumindo 1L a cada {Chevette.consumo}km'
    lb3['text'] = 'Você deseja ver a quantidade de gasolina no tanque?'
    lbTemporaria = lbTemporaria + f'\n2 - ' + lb1['text']

    ed.destroy()
    btConfirm2.destroy()
    passoAPasso()

    lbLinha.pack(side=TOP)
    lb3.pack(side=TOP)
    btConfirm3.pack(side=TOP)

def buttonClick3():
    global lbTemporaria, gasolinaAtual
    Chevette.obterGasolina()

    lb1['text'] = 'Gasolina Atual: {:.1f}L no tanque'.format(gasolinaAtual)
    lbTemporaria = lbTemporaria + f'\n3 - ' + lb1['text']

    lb3.destroy()
    btConfirm3.destroy()
    passoAPasso()

def passoAPasso():
    lb2['text'] = f'Passo a Passo:\n1 - ' + lbTemporaria
    lb2.pack(side=BOTTOM)

window = Tk()
window['bg'] = 'black'
window.title = 'Gasolina do Carro - Calculator'

fonte = ('Arial', '9', 'italic')
fonteFg = 'white'
fonteBg = 'black'

lb1 = Label(window, text='Quantos litros de gasolina você deseja adicionar?', font=fonte, bg=fonteBg, fg=fonteFg)
lb2 = Label(window, font=fonte, bg=fonteBg, fg=fonteFg)
lb3 = Label(window, font=fonte, bg=fonteBg, fg=fonteFg)
lbLinha = Label(window, text='-' * 40, font=fonte, fg=fonteFg, bg=fonteBg)
lbTemporaria = ''

btConfirm1 = Button(window, width=10, text='Confirm', command=buttonClick1)
btConfirm2 = Button(window, width=10, text='Confirm', command=buttonClick2)
btConfirm3 = Button(window, width=10, text='Confirm', command=buttonClick3)

ed = Entry(window)

lb1.pack(side=TOP)
ed.pack(side=TOP)
btConfirm1.pack(side=TOP)

Chevette = Carro(15)

window.geometry('300x200')
window.mainloop()