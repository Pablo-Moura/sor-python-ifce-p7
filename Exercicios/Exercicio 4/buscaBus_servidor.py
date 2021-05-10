# -*- encoding: utf-8 -*-
# This Python file uses the following encoding: utf-8

from bancoDeDados import *
import socket
import pickle

HOST = 'localhost'
PORT = 50000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen()
print('Aguardando conexão do cliente...\n')

while True:
    conn, ender = socket.accept()
    print('Conectado em:', ender)
    while True:
        data = conn.recv(1024).decode()
        if data == 'breakConnection':
            conn.send(str.encode("Obrigado por utilizar o\nBuscaBus Fortaleza."))
            conn.close()
            break
        elif data == 'PesquisaDupla':
            pesquisar = conn.recv(1024).decode()
            conn.send(str.encode('Recebi'))
            pesquisar2 = conn.recv(1024).decode()
            pegarTudoPeloTexto2(pesquisar, pesquisar2)
            if len(linhasNome) == 0:
                conn.send(str.encode("Linha Inválida."))
            else:
                conn.send(str.encode("Linha Existente."))
                linhasNomeByte = pickle.dumps(linhasNome)
                linhasNumeroByte = pickle.dumps(linhasNumero)
                conn.send(linhasNomeByte)
                recebido = conn.recv(1024).decode()
                conn.send(linhasNumeroByte)
                limpaLista()
        elif data != '':
            pegarTudoPeloTexto(data)
            if len(linhasNome) == 0:
                conn.send(str.encode("Linha Inválida."))
            else:
                conn.send(str.encode("Linha Existente."))
                linhasNomeByte = pickle.dumps(linhasNome)
                linhasNumeroByte = pickle.dumps(linhasNumero)
                conn.send(linhasNomeByte)
                recebido = conn.recv(1024).decode()
                conn.send(linhasNumeroByte)
                limpaLista()
        else:
            conn.close()
            break