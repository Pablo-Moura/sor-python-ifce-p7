# Escrever um programa para somar todos os elementos de uma lista de números (Aula 02 - Atividade 01)

# Implementar uma mini aplicação com Interface gráfica. Exemplos: cálculo do IMC, conversão de unidades, etc.
# Utilizar algum exercício das aulas para criar a interface gráfica.

from tkinter import *

def buttonClick():
    try:
        global soma

        Lista.append(ed.get())
        soma += int(ed.get())

        lb2.pack(anchor=W)
        lb3.pack(anchor=W)

        lb2['text'] = f'Lista: {Lista}'
        lb3['text'] = f'Soma da Lista: {soma}'

    except ValueError:
        lb2['text'] = 'Somente números são aceitos, tente novamente.'
        Lista.pop()

window = Tk()
window.title('Pablin List Calculator')
window['bg'] = 'black'

Lista = []
soma = 0
fonte = ('Arial', '10', 'italic')

lb1 = Label(window, text='Por favor, insira um número.', bg='black', fg='white', font=(fonte))
lb2 = Label(window,  bg='black', fg='white', font=(fonte))
lb3 = Label(window,  bg='black', fg='white', font=(fonte))
ed = Entry(window)
bt = Button(window, width=10, text='OK', command=buttonClick)

lb1.pack(side = TOP)
ed.pack(side = TOP)
bt.pack(side = TOP)

window.geometry('300x130+100+100')
window.mainloop()