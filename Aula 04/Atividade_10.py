from tkinter import *

def mesFormatado(mes):
    global mesForm

    if mes == 1:
        mesForm = 'janeiro'
    elif mes == 2:
        mesForm = 'fevereiro'
    elif mes == 3:
        mesForm = 'março'
    elif mes == 4:
        mesForm = 'abril'
    elif mes == 5:
        mesForm = 'maio'
    elif mes == 6:
        mesForm = 'junho'
    elif mes == 7:
        mesForm = 'julho'
    elif mes == 8:
        mesForm = 'agosto'
    elif mes == 9:
        mesForm = 'setembro'
    elif mes == 10:
        mesForm = 'outubro'
    elif mes == 11:
        mesForm = 'novembro'
    elif mes == 12:
        mesForm = 'dezembro'
    return mesForm

def buttonClick():
    global ano
    ano = int(ed.get())

    lbAno.pack_forget()
    buttonAndEdForget()
    lbMes.pack()
    buttonAndEdPack()

    bt['command'] = buttonClick2

def buttonClick2():
    global mes
    mes = int(ed.get())
    mesFormatado(mes)

    lbMes.pack_forget()
    buttonAndEdForget()
    lbDia.pack()
    buttonAndEdPack()

    bt['command'] = buttonClick3

def buttonClick3():
    global ano, mesForm
    dia = int(ed.get())

    lbDia.pack_forget()
    buttonAndEdForget()

    lbData = Label(window, text=f'Data Formatada: {dia} de {mesForm} de {ano}', fg='white', bg='black', font= fonte)
    lbDataInicial = Label(window, text=f'Data Inicial: {dia}/{mes}/{ano}', fg='white', bg='black', font=fonte)

    lbData.pack()
    lbDataInicial.pack()

def buttonAndEdForget():
    bt.pack_forget()
    ed.pack_forget()

def buttonAndEdPack():
    ed.pack()
    bt.pack()

window = Tk()

window['bg'] = 'black'
fonte = ('Arial', '9', 'italic')
mesInicial = 1
mesLimite = 31

lb1 = Label(window, text='Este programa irá formatar uma data.', fg='white', bg='black', font=fonte)
lbMes = Label(window, text='Por favor, digite um mês do ano.', fg='white', bg='black', font=fonte)
lbDia = Label(window, text='Por favor, digite um dia do mês.', fg='white', bg='black', font=fonte)
lbAno = Label(window, text='Por favor, digite um ano.', fg='white', bg='black', font=fonte)
lbLinha = Label(window, text='-'*30, fg='white', bg='black', font=fonte)
#

ed = Entry(window)
bt = Button(window, width=10, text='Ok', command=buttonClick)

lb1.pack(side=TOP)
lbLinha.pack()
lbAno.pack()
buttonAndEdPack()

window.geometry('300x110')
window.mainloop()