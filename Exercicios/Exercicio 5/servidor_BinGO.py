import pickle
import socket
import threading
import random
from BinGO import CriandoBingo

# Socket
IP = '26.209.160.169'
PORT = 5566
ADDR = (IP, PORT)

# Variáveis Globais
CONFIRMAR_CLIENTE = 0
CONFIRMAR_BINGO = 0
CHAMADOS = []
CLIENTES = []
GANHADORES = []

# Funções
def clearJson():
    with open('Castelas_BinGO.json', 'w') as arq:
        arq.write('')

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

def handle_client(conn, addr):
    global conexao
    print('[*] NOVA CONEXÃO: ', addr)
    conexao = threading.activeCount() - 1
    conn.send(str(conexao).encode())
    CLIENTES.append(conn)

    while True:
        try:
            msg = conn.recv(64).decode()
            if msg == 'connectionBreak':
                conn.close()
                break
            elif msg == 'request':
                criarCartela = CriandoBingo()
                cartelaByte = pickle.dumps(criarCartela.cartela)
                conn.send(cartelaByte)
                comecar_bingo(conn)
        except:
            conn.close()
            break

def comecar_bingo(conn):
    while True:
        recv = conn.recv(56).decode()
        if recv == "BINGO":
            global GANHADORES, CONFIRMAR_BINGO
            CONFIRMAR_BINGO += 1
            recvID = conn.recv(100).decode()
            GANHADORES.append(recvID)
            divulgar_ganhadores()
        elif recv == "CONFIRM":
            global CONFIRMAR_CLIENTE
            CONFIRMAR_CLIENTE += 1
            chamar_bingo()

def chamar_bingo():
    global numero, CHAMADOS, CONFIRMAR_CLIENTE, conexao
    if CONFIRMAR_CLIENTE == conexao and CONFIRMAR_CLIENTE >= 2:
        while True:
            numero = random.randrange(1,76)
            if numero not in CHAMADOS:
                CHAMADOS.append(numero)
                broadcast(CLIENTES, str(numero))
                CONFIRMAR_CLIENTE = 0
                break

def divulgar_ganhadores():
    global CONFIRMAR_CLIENTE, CONFIRMAR_BINGO, GANHADORES, conexao
    while True:
        if (CONFIRMAR_CLIENTE+CONFIRMAR_BINGO) == conexao:
            CONFIRMAR_BINGO = 0
            broadcast(CLIENTES, str('BINGO!!!'))
            strGanhadores = ""
            for x in range(0, len(GANHADORES)):
                if x > 0:
                    strGanhadores = strGanhadores + f"\nCartela ID {GANHADORES[x]}"
                else:
                    strGanhadores = strGanhadores + f"Bingo Por: \nCartela ID - {GANHADORES[x]}"
            broadcast(CLIENTES, strGanhadores)
            break

def broadcast(clientes, str):
    for client in clientes:
        client.send(str.encode())

if __name__ == "__main__":
    clearJson()
    main()