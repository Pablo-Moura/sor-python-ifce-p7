# -*- encoding: utf-8 -*-
# This Python file uses the following encoding: utf-8

import sqlite3
import requests, bs4

banco = sqlite3.connect('linhas_de_onibus.db')
cursor = banco.cursor()

def createTable():
    cursor.execute('CREATE TABLE IF NOT EXISTS linhas (numero_da_linha TEXT, nome_da_linha TEXT, destino_um TEXT,'
                   'destino_dois TEXT, destino_tres TEXT, destino_quatro TEXT)')

def entryValues(numeroDaLinha, nomeDaLinha, destinoUm, destinoDois, destinoTres, destinoQuatro):
    cursor.execute("INSERT INTO linhas (numero_da_linha, nome_da_linha, destino_um, destino_dois, destino_tres, "
                   "destino_quatro)"
                   "VALUES (?,?,?,?,?,?)",(numeroDaLinha, nomeDaLinha, destinoUm, destinoDois, destinoTres, destinoQuatro))
    banco.commit()

def pegarTudoPeloTexto(textoUsado1):
    sqlPegarNumero = "SELECT numero_da_linha FROM linhas WHERE ? IN (numero_da_linha, nome_da_linha, destino_um, destino_dois, destino_tres," \
                     "destino_quatro)"
    for numero in cursor.execute(sqlPegarNumero, ((textoUsado1,))):
        for y in range(len(numero)):
            if numero[y] != None:
                linhasNumero.append(numero[y])

    sqlPegarNome = "SELECT nome_da_linha FROM linhas WHERE ? IN (numero_da_linha, nome_da_linha, destino_um, destino_dois, destino_tres," \
                     "destino_quatro)"
    for nome in cursor.execute(sqlPegarNome, ((textoUsado1,))):
        for y in range(len(numero)):
            if nome[y] != None:
                linhasNome.append(nome[y])

def pegarTudoPeloTexto2(textoUsado1, textoUsado2):
    sqlPegarNumero = "SELECT numero_da_linha FROM linhas WHERE ? IN (numero_da_linha, nome_da_linha, destino_um, destino_dois, destino_tres," \
                     "destino_quatro) AND ? IN (numero_da_linha, nome_da_linha, destino_um, destino_dois, destino_tres," \
                     "destino_quatro)"
    for numero in cursor.execute(sqlPegarNumero, ((textoUsado1, textoUsado2))):
        for y in range(len(numero)):
            if numero[y] != None:
                linhasNumero.append(numero[y])

    sqlPegarNome = "SELECT nome_da_linha FROM linhas WHERE ? IN (numero_da_linha, nome_da_linha, destino_um, destino_dois, destino_tres," \
                     "destino_quatro) AND ? IN (numero_da_linha, nome_da_linha, destino_um, destino_dois, destino_tres," \
                     "destino_quatro)"
    for nome in cursor.execute(sqlPegarNome, ((textoUsado1, textoUsado2))):
        for y in range(len(numero)):
            if nome[y] != None:
                linhasNome.append(nome[y])

def limpaLista():
    linhasNome.clear()
    linhasNumero.clear()

def criarBancoDeDados():
    createTable()
    res = requests.get("https://moovitapp.com/index/pt-br/transporte_p%C3%BAblico-lines-Fortaleza-983-9809")

    res.raise_for_status()
    objectSoup = bs4.BeautifulSoup(res.text, features="lxml")
    linhasMoovit = objectSoup.select('.line-title-wrapper')
    for x in range(len(linhasMoovit)):
        linhaText = linhasMoovit[x].getText()  # Pega o texto da linha indicada
        linhaText = linhaText.replace('\n', '')  # Remove as \n do texto
        rotaCompleta = linhaText[4:]  # Separa em uma nova lista, o texto completo para servir como rota
        rotaSplit = rotaCompleta.split(" / ")  # Separa em uma nova lista, o texto completo com split pela barra
        rotaNumero = linhaText[:3]
        try:
            entryValues(rotaNumero, rotaCompleta, rotaSplit[0], rotaSplit[1], rotaSplit[2], rotaSplit[3])
        except:
            try:
                entryValues(rotaNumero, rotaCompleta, rotaSplit[0], rotaSplit[1], rotaSplit[2], None)
            except:
                try:
                    entryValues(rotaNumero, rotaCompleta, rotaSplit[0], rotaSplit[1], None, None)
                except:
                    entryValues(rotaNumero, rotaCompleta, rotaSplit[0], None, None, None)

linhasNome = []
linhasNumero = []
linhasDestinos = []