import pickle
import socket
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Funções
def buttonClick():
    entryGet = entryPesquisar.get()
    if entryGet != '':
        socket.send(str.encode(entryGet))
        verificacao = socket.recv(1024).decode()
        if verificacao == 'Linha Inválida.':
            messagebox.showinfo("Busca Bus Fortaleza", "Linha do ônibus requisitado:\nSem resultados para a busca.")
            entryPesquisar.delete(0, END)
            entryPesquisar.focus()
        else:
            dataNomeByte = socket.recv(4096)
            socket.send(str.encode('Lista dos Nomes recebido.'))
            dataNumeroByte = socket.recv(4096)
            dataNome = pickle.loads(dataNomeByte)
            dataNumero = pickle.loads(dataNumeroByte)
            stringComNomes = ''
            for x in range(len(dataNumero)):
                if x == (len(dataNumero) - 1):
                    stringComNomes = stringComNomes + f'{dataNumero[x]} : {dataNome[x]}.'
                    break
                stringComNomes = stringComNomes + f'{dataNumero[x]} : {dataNome[x]}\n'
            messagebox.showinfo("Busca Bus Fortaleza", "Linha do ônibus requisitado:\n%s" %(stringComNomes))
            entryPesquisar.delete(0, END)
            entryPesquisar.focus()
    elif entryGet == '':
        messagebox.showinfo("Busca Bus Fortaleza", "Preencha os dois campos obrigatórios.")
        entryPesquisar.focus()

def buttonClick2():
    entryGet = entryPesquisar.get()
    entryGet2 = entryPesquisar2.get()
    if entryGet != '' and entryGet2 != '':
        socket.send(str.encode('PesquisaDupla'))
        socket.send(str.encode(entryGet))
        socket.recv(1024).decode()
        socket.send(str.encode(entryGet2))
        verificacao = socket.recv(1024).decode()
        if verificacao == 'Linha Inválida.':
            messagebox.showinfo("Busca Bus Fortaleza", "Linha do ônibus requisitado:\nSem resultados para a busca.")
            entryPesquisar2.delete(0, END)
            entryPesquisar.delete(0, END)
            entryPesquisar2.focus()
        elif verificacao == 'Linha Existente.':
            dataNomeByte2 = socket.recv(5470)
            socket.send(str.encode('Lista dos Nomes recebido.'))
            dataNumeroByte2 = socket.recv(5470)
            dataNome2 = pickle.loads(dataNomeByte2)
            dataNumero2 = pickle.loads(dataNumeroByte2)
            stringComNomes = ''
            for x in range(len(dataNome2)):
                if x == (len(dataNome2) - 1):
                    stringComNomes = stringComNomes + f'{dataNumero2[x]} : {dataNome2[x]}.'
                    break
                stringComNomes = stringComNomes + f'{dataNumero2[x]} : {dataNome2[x]}\n'
            messagebox.showinfo("Busca Bus Fortaleza", "Linha do ônibus requisitado:\n%s" %(stringComNomes))
            entryPesquisar2.delete(0, END)
            entryPesquisar.delete(0, END)
            entryPesquisar2.focus()
    elif entryGet == '' or entryGet2 == '':
        messagebox.showinfo("Busca Bus Fortaleza", "Preencha os dois campos obrigatórios.")
        entryPesquisar2.focus()

def menuInicio():
    esconderTudo()
    label_image.place(x=0, y=0)

def menuPesquisar():
    esconderTudo()
    labelPesquisar.place(x=67.5, y=50)
    entryPesquisar.place(x=87.5, y=150)
    buttonPesquisar.place(x=101.5, y=172)
    entryPesquisar.focus()

def menuPesquisarDuplo():
    esconderTudo()
    labelPesquisar.place(x=67.5, y=50)
    labelInicio.place(x=0, y=120)
    labelDestino.place(x=0, y=145)
    entryPesquisar2.place(x=87.5, y=125)
    entryPesquisar.place(x=87.5, y=150)
    buttonPesquisar2.place(x=101.5, y=172)
    entryPesquisar2.focus()

def menuSobre():
    esconderTudo()
    root.focus()
    labelNomeDoPrograma.place(x=67, y=0)
    labelDescricao.place(x=1, y=50)
    labelAutor.place(x=1, y=285)

def connectionQuit():
    socket.send(str.encode('breakConnection'))
    data = socket.recv(1024).decode()
    messagebox.showinfo("Busca Bus Fortaleza", "%s" % (data))
    root.quit()

def esconderTudo():
    label_image.place_forget()
    labelPesquisar.place_forget()
    labelInicio.place_forget()
    labelDestino.place_forget()
    entryPesquisar.place_forget()
    entryPesquisar2.place_forget()
    buttonPesquisar.place_forget()
    buttonPesquisar2.place_forget()
    labelNomeDoPrograma.place_forget()
    labelDescricao.place_forget()
    labelAutor.place_forget()

def temaDark():
    root['bg'] = 'black'
    label_image['image'] = logoBranco
    labelPesquisar['bg'] = 'black'
    labelPesquisar['fg'] = 'white'
    labelInicio['bg'] = 'black'
    labelInicio['fg'] = 'white'
    labelDestino['bg'] = 'black'
    labelDestino['fg'] = 'white'
    labelNomeDoPrograma['bg'] = 'black'
    labelNomeDoPrograma['fg'] = 'white'
    labelDescricao['bg'] = 'black'
    labelDescricao['fg'] = 'white'
    labelAutor['bg'] = 'black'
    labelAutor['fg'] = 'white'
    primeiroMenu['bg'] = '#212121'
    primeiroMenu['fg'] = 'white'
    segundoMenu['bg'] = '#212121'
    segundoMenu['fg'] = 'white'

def temaLight():
    root['bg'] = 'white'
    label_image['image'] = logoPreto
    labelPesquisar['bg'] = 'white'
    labelPesquisar['fg'] = 'black'
    labelInicio['bg'] = 'white'
    labelInicio['fg'] = 'black'
    labelDestino['bg'] = 'white'
    labelDestino['fg'] = 'black'
    labelNomeDoPrograma['bg'] = 'white'
    labelNomeDoPrograma['fg'] = 'black'
    labelDescricao['bg'] = 'white'
    labelDescricao['fg'] = 'black'
    labelAutor['bg'] = 'white'
    labelAutor['fg'] = 'black'
    primeiroMenu['bg'] = '#f0f0f0'
    primeiroMenu['fg'] = 'black'
    segundoMenu['bg'] = '#f0f0f0'
    segundoMenu['fg'] = 'black'

# Conexão com o Servidor
HOST = 'localhost'
PORT = 50000
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

# Janela de Interface
root = Tk()
root.title('BuscaBus Fortaleza')
root['bg'] = 'white'
root.geometry('300x300') # +479+220
root.resizable(width=False, height=False)

# Barra de Menus
barraDeMenus = Menu(root)
primeiroMenu = Menu(barraDeMenus, tearoff=0, bd=1)
primeiroMenu.add_command(label="Inicio", command=menuInicio)
primeiroMenu.add_command(label="Pesquisar Linha Unica", command=menuPesquisar)
primeiroMenu.add_command(label="Pesquisar Linha Dupla", command=menuPesquisarDuplo)
primeiroMenu.add_command(label="Sobre", command=menuSobre)
primeiroMenu.add_separator()
primeiroMenu.add_command(label="Fechar", command=connectionQuit)
segundoMenu = Menu(barraDeMenus, tearoff=0, bd=1)
segundoMenu.add_command(label="Dark", command=temaDark)
segundoMenu.add_command(label="Light", command=temaLight)
barraDeMenus.add_cascade(label="Menu", menu=primeiroMenu)
barraDeMenus.add_cascade(label="Tema", menu=segundoMenu)

# Widgets
logoPreto = PhotoImage(file="buscaBusPreto.png")
logoBranco = PhotoImage(file="buscaBusBranco.png")
label_image = Label(root, image=logoPreto, bd=0)
labelPesquisar = Label(root, text='Digite o nome\nda linha desejada:', font=('Segoe UI Symbol', 15), fg='black', bg='white')
labelInicio = Label(root, text='Local Atual:', font=('Segoe UI Symbol', 12), fg='black', bg='white')
labelDestino = Label(root, text='Local Final:', font=('Segoe UI Symbol', 12), fg='black', bg='white')
entryPesquisar2 = ttk.Entry(root, width=20)
entryPesquisar = ttk.Entry(root, width=20)
buttonPesquisar = ttk.Button(root, text='Pesquisar', command=buttonClick, width=15)
buttonPesquisar2 = ttk.Button(root, text='Pesquisar', command=buttonClick2, width=15)
labelNomeDoPrograma = Label(root, text='BuscaBus Fortaleza', font=('Segoe UI Symbol', 13), fg='black', bg='white')
labelDescricao = Label(root, text="Olá, seja bem vindo ao BuscaBus Fortaleza!\n"
                                    "Este é um programa que visa ajudar aqueles\n"
                                    "que não possuem tantas informações sobre\n"
                                    "as linhas de ônibus em Fortaleza.\n"
                                    "O Programa é bem simples de usar, basta\n"
                                    "escolher uma das opções de pesquisa na aba\n"
                                    "'Menu' da parte superior esquerda da tela.\n"
                                    "Após realizar a consulta, você receberá\n"
                                    "uma messagebox com as linhas de ônibus\n"
                                    "referentes a sua pesquisa.\n", font=('Segoe UI Symbol', 10), fg='black', bg='white', justify=LEFT)
labelAutor = Label(root, text='© Copyright: Pablo Silva de Moura, 2021.', font=('Arial', 7), fg='black', bg='white')

# Layout
label_image.place(x=0, y=0)
labelPesquisar.place(x=5000, y=5000)
labelInicio.place(x=5000, y=5000)
labelDestino.place(x=5000, y=5000)
entryPesquisar.place(x=5000, y=5000)
entryPesquisar2.place(x=5000, y=5000)
buttonPesquisar.place(x=5000, y=5000)
buttonPesquisar2.place(x=5000, y=5000)
labelNomeDoPrograma.place(x=5000, y=5000)
labelDescricao.place(x=5000, y=5000)
labelAutor.place(x=5000, y=5000)

# Main
root.config(menu=barraDeMenus)
root.mainloop()
