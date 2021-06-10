import pickle
import socket
import threading
from tkinter import *
from tkinter import ttk, messagebox

# --------------------------------------------------------- #
# Funções

def menu_inicio():
    esconder_tudo()
    labelImage.place(x=0,y=0)

def button_click():
    global cartela, cartelaCopy
    msg = 'request'
    client.send(msg.encode())
    cartelaBytes = client.recv(1024)
    cartela = pickle.loads(cartelaBytes)
    cartelaCopy = pickle.loads(cartelaBytes)

    primeiroMenu.delete(2,4)
    mostrar_cartela(cartela)
    alterar_comando()
    menu_cartela()

def menu_cartela():
    esconder_tudo()
    labelBingo.place(x=10, y=10)
    buttonIniciar.place(x=216, y=250)

def mostrar_cartela(cartela):
    labelBingo['text'] =    '%2s\t%2s\t%2s\t%2s\t%2s\n' % tuple('BINGO') +\
                            '\n%2s\t%2s\t%2s\t%2s\t%2s\n' % (str(cartela['B'][0]),str(cartela['I'][0]),str(cartela['N'][0]),str(cartela['G'][0]), str(cartela['O'][0])) +\
                            '\n%2s\t%2s\t%2s\t%2s\t%2s\n' % (str(cartela['B'][1]),str(cartela['I'][1]),str(cartela['N'][1]),str(cartela['G'][1]), str(cartela['O'][1])) +\
                            '\n%2s\t%2s\t%2s\t%2s\t%2s\n' % (str(cartela['B'][2]),str(cartela['I'][2]),str(cartela['N'][2]),str(cartela['G'][2]), str(cartela['O'][2])) +\
                            '\n%2s\t%2s\t%2s\t%2s\t%2s\n' % (str(cartela['B'][3]),str(cartela['I'][3]),str(cartela['N'][3]),str(cartela['G'][3]), str(cartela['O'][3])) +\
                            '\n%2s\t%2s\t%2s\t%2s\t%2s\n' % (str(cartela['B'][4]),str(cartela['I'][4]),str(cartela['N'][4]),str(cartela['G'][4]), str(cartela['O'][4])) +\
                            '\nID: %s' % ID

def mostrar_cartela_inicial():
    global cartelaCopy
    esconder_tudo()
    labelBingoInicial.place(x=10, y=10)
    labelBingoInicial['text'] =    '%2s\t%2s\t%2s\t%2s\t%2s\n' % tuple('BINGO') +\
                            '\n%2s\t%2s\t%2s\t%2s\t%2s\n' % (str(cartelaCopy['B'][0]),str(cartelaCopy['I'][0]),str(cartelaCopy['N'][0]),str(cartelaCopy['G'][0]), str(cartelaCopy['O'][0])) +\
                            '\n%2s\t%2s\t%2s\t%2s\t%2s\n' % (str(cartelaCopy['B'][1]),str(cartelaCopy['I'][1]),str(cartelaCopy['N'][1]),str(cartelaCopy['G'][1]), str(cartelaCopy['O'][1])) +\
                            '\n%2s\t%2s\t%2s\t%2s\t%2s\n' % (str(cartelaCopy['B'][2]),str(cartelaCopy['I'][2]),str(cartelaCopy['N'][2]),str(cartelaCopy['G'][2]), str(cartelaCopy['O'][2])) +\
                            '\n%2s\t%2s\t%2s\t%2s\t%2s\n' % (str(cartelaCopy['B'][3]),str(cartelaCopy['I'][3]),str(cartelaCopy['N'][3]),str(cartelaCopy['G'][3]), str(cartelaCopy['O'][3])) +\
                            '\n%2s\t%2s\t%2s\t%2s\t%2s\n' % (str(cartelaCopy['B'][4]),str(cartelaCopy['I'][4]),str(cartelaCopy['N'][4]),str(cartelaCopy['G'][4]), str(cartelaCopy['O'][4])) +\
                            '\nID: %s' % ID

def alterar_comando():
    global cartelaCopy
    segundoMenu.delete(0)
    segundoMenu.add_command(label="Minha Cartela", command=menu_cartela)
    segundoMenu.add_command(label="Cartela Inicial", command=mostrar_cartela_inicial)

def alterar_comando2():
    global cartelaCopy
    segundoMenu.delete(0)
    segundoMenu.add_command(label="Minha Cartela", command=menu_cartela2)

def button_confirmar():
    thread_confirm = threading.Thread(target=button_confirmar_thread, args=())
    thread_confirm.start()

def button_confirmar_thread():
    global confirmarB
    if confirmarB == 0:
        client.send(str.encode('CONFIRM'))
        confirmarB = 1
        recv()
    else:
        messagebox.showinfo("Bin-Go!", f"Só é possível confirmar uma vez por partida.")

def recv():
    global cartela, confirmarB
    recv = client.recv(100).decode()
    if recv == 'BINGO!!!':
        confirmarB = 0
        messagebox.showinfo("Bin-Go!", f"{recv}")
        recv2 = client.recv(1024).decode()
        messagebox.showinfo("Bin-Go!", f"{recv2}")

        buttonIniciar.place_forget()
        alterar_comando2()
        primeiroMenu.add_separator()
        primeiroMenu.add_command(label="Fechar", command=menu_fechar)
    else:
        confirmarB = 0
        messagebox.showinfo("Bin-Go!", f"Número Sorteado: {recv}")
        verificar_numero(int(recv))
        verificar_bingo()

def verificar_numero(numero):
    for x in cartela:
        for y in range(0, 5):
            if cartela[x][y] == numero:
                cartela[x][y] = 'X'
                mostrar_cartela(cartela)

def verificar_bingo():
    global cartela
    if cartela == {'B': ['X', 'X', 'X', 'X', 'X'], 'I': ['X', 'X', 'X', 'X', 'X'], 'N': ['X', 'X', 'X', 'X', 'X'], 'G': ['X', 'X', 'X', 'X', 'X'], 'O': ['X', 'X', 'X', 'X', 'X']}:
        buttonIniciar['text'] = 'Bingo!'
        buttonIniciar['command'] = bingo_button
    else:
        pass

def bingo_button():
    client.send(str('BINGO').encode())
    client.send(str(ID).encode())
    recv()

def esconder_tudo():
    labelImage.place_forget()
    labelNomeDoPrograma.place_forget()
    labelAutor.place_forget()
    labelDescricao.place_forget()
    labelBingo.place_forget()
    labelBingoInicial.place_forget()
    buttonCriarCartela.place_forget()
    buttonIniciar.place_forget()

def menu_cartela2():
    esconder_tudo()
    labelBingo.place(x=10, y=10)

def menu_sobre():
    esconder_tudo()
    windows.focus()
    labelNomeDoPrograma.place(x=110, y=0)
    labelDescricao.place(x=1, y=50)
    labelAutor.place(x=1, y=285)

def menu_jogar():
    esconder_tudo()
    labelNomeDoPrograma.place(x=117, y=30)
    buttonCriarCartela.place(x=97.5, y=150)

def menu_fechar():
    msg = 'connectionBreak'
    client.send(msg.encode())
    messagebox.showinfo("Bin-Go!", "Obrigado por utilizar o Bin-Go!")
    windows.quit()

def tema_dark():
    color_1 = 'white'
    color_2 = '#1c1c1c'

    labelImage['image'] = logoBranco
    labelImage['bg'] = '#1c1c1c'

    labelNomeDoPrograma['fg'] = color_1
    labelDescricao['fg'] = color_1
    labelAutor['fg'] = color_1
    labelBingo['fg'] = color_1
    labelBingoInicial['fg'] = color_1
    primeiroMenu['fg'] = color_1
    segundoMenu['fg'] = color_1
    terceiroMenu['fg'] = color_1

    windows['bg'] = color_2
    labelNomeDoPrograma['bg'] = color_2
    labelDescricao['bg'] = color_2
    labelAutor['bg'] = color_2
    labelBingo['bg'] = color_2
    labelBingoInicial['bg'] = color_2
    primeiroMenu['bg'] = '#212121'
    segundoMenu['bg'] = '#212121'
    terceiroMenu['bg'] = '#212121'

def tema_light():
    color_1 = '#1c1c1c'
    color_2 = 'white'

    labelImage['image'] = logoPreto
    labelImage['bg'] = color_2

    labelNomeDoPrograma['fg'] = color_1
    labelDescricao['fg'] = color_1
    labelAutor['fg'] = color_1
    labelBingo['fg'] = color_1
    labelBingoInicial['fg'] = color_1
    primeiroMenu['fg'] = color_1
    segundoMenu['fg'] = color_1
    terceiroMenu['fg'] = color_1

    windows['bg'] = color_2
    labelNomeDoPrograma['bg'] = color_2
    labelDescricao['bg'] = color_2
    labelAutor['bg'] = color_2
    labelBingo['bg'] = color_2
    labelBingoInicial['bg'] = color_2
    primeiroMenu['bg'] = '#f0f0f0'
    segundoMenu['bg'] = '#f0f0f0'
    terceiroMenu['bg'] = '#f0f0f0'

# --------------------------------------------------------- #
# Socket Client

IP = '26.209.160.169'
PORT = 5566
ADDR = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
ID = client.recv(1024).decode()

confirmarB = 0
# --------------------------------------------------------- #
# GUI - Tkinter

# Layout Color
color_1 = 'white'
color_2 = '#1c1c1c'

# Main Window
windows = Tk()
windows.title("Bin-Go!")
windows['bg'] = color_2
windows.geometry('300x320')
windows.resizable(width=False, height=False)

# Menu
barraDeMenus = Menu(windows)
primeiroMenu = Menu(barraDeMenus, tearoff=0, bd=1, bg='#212121', fg=color_1)
primeiroMenu.add_command(label="Inicio", command=menu_inicio)
primeiroMenu.add_command(label="Sobre", command=menu_sobre)
primeiroMenu.add_separator()
primeiroMenu.add_command(label="Fechar", command=menu_fechar)
segundoMenu = Menu(barraDeMenus, tearoff=0, bd=1, bg='#212121', fg=color_1)
segundoMenu.add_command(label="Jogar", command=menu_jogar)
terceiroMenu = Menu(barraDeMenus, tearoff=0, bd=1, bg='#212121', fg=color_1)
terceiroMenu.add_command(label="Dark", command=tema_dark)
terceiroMenu.add_command(label="Light", command=tema_light)
barraDeMenus.add_cascade(label="Menu", menu=primeiroMenu)
barraDeMenus.add_cascade(label="Bingo", menu=segundoMenu)
barraDeMenus.add_cascade(label="Tema", menu=terceiroMenu)

# Label
logoBranco = PhotoImage(file="Images/BinGOBranco.png")
logoPreto = PhotoImage(file="Images/BinGOPreto.png")
labelImage = Label(windows, image=logoBranco, bd=0, bg='#1c1c1c')
labelNomeDoPrograma = Label(windows, text='Bin-Go!', font=('Segoe UI Symbol', 13, 'bold'), fg=color_1, bg=color_2)
labelDescricao = Label(windows, text="Olá, seja bem vindo ao Bin-Go!\n"
                                     "Este é um simulador de bingos online.\n\n"
                                     "Para jogar:\n"
                                     "Clique no menu BINGO e escolha a opção\n"
                                     "JOGAR. Em seguida, clique no botão\n"
                                     "CRIAR CARTELA e aguarde novos jogadores\n"
                                     "para iniciar uma partida.\n", font=('Segoe UI Symbol', 11), fg=color_1, bg=color_2, justify=LEFT)
labelAutor = Label(windows, text='© Copyright: Pablo Silva de Moura, 2021.', font=('Arial', 7), fg=color_1, bg=color_2)
labelBingo = Label(windows, text='', font=('Segoe UI Symbol', 11), fg=color_1, bg=color_2, justify=LEFT)
labelBingoInicial = Label(windows, text='', font=('Segoe UI Symbol', 11), fg=color_1, bg=color_2, justify=LEFT)

# Button
buttonCriarCartela = ttk.Button(windows, text='Criar Cartela', command=button_click, width=15)
buttonIniciar = ttk.Button(windows, text='Iniciar', command=button_confirmar, width=10)

# Layout
labelImage.place(x=0, y=0)
labelNomeDoPrograma.place(x=5000, y=5000)
labelDescricao.place(x=5000, y=5000)
labelAutor.place(x=5000, y=5000)
labelBingo.place(x=5000, y=5000)
buttonCriarCartela.place(x=5000, y=5000)
buttonIniciar.place(x=5000, y=5000)

windows.iconbitmap('images/BinGO_Icon.ico')
windows.config(menu=barraDeMenus)
windows.mainloop()