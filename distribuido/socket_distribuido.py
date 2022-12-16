import json
import socket
from input import muda_estado_input

from output import muda_estado_output

retorno = True

def socket_distribuido(_host: str,_port:int, data:any, data2:any):
    global retorno
    HOST = _host           # Endereco IP do Servidor
    PORT = _port           # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)
    while True:
        con, cliente = tcp.accept()
        print ('Concetado por', cliente)
        while True:
            msg = con.recv(1024)
            if not msg: break

            temp = msg.decode()
            verificaEscolha(temp[0], temp[1], data, data2)
        print ('Finalizando conexao do cliente', cliente)
        con.close()

def gravajson(pino: int, sala: int):
    file_estados = open("../json/estados.json", 'r')
    data_estados = json.load(file_estados)
    file_estados.close()
        
def verificaEscolha(sala: str, opcao: str, data: any, data2: any):
    global retorno
   
    if sala=='1':
        if opcao=='a':
            retorno = muda_estado_output(int(data["outputs"][0]["gpio"]))
        elif opcao=='b':
            retorno = muda_estado_output(int(data["outputs"][1]["gpio"]))
        elif opcao=='c':
            retorno = muda_estado_output(int(data["outputs"][3]["gpio"]))
        elif opcao=='d':
            retorno = muda_estado_output(int(data["outputs"][2]["gpio"]))
        elif opcao=='e':
            retorno = muda_estado_input(int(data["inputs"][0]["gpio"]), int(data["outputs"][4]["gpio"]))
        elif opcao=='f':
            retorno = muda_estado_input(int(data["inputs"][1]["gpio"]), int(data["outputs"][4]["gpio"]))
        elif opcao=='g':
            retorno = muda_estado_input(int(data["inputs"][2]["gpio"]), int(data["outputs"][4]["gpio"]))
        elif opcao=='h':
            retorno = muda_estado_input(int(data["inputs"][3]["gpio"]), int(data["outputs"][4]["gpio"]))
    elif sala=='2':
        if opcao=='a':
            retorno = muda_estado_output(int(data2["outputs"][0]["gpio"]))
        elif opcao=='b':
            retorno = muda_estado_output(int(data2["outputs"][1]["gpio"]))
        elif opcao=='c':
            retorno = muda_estado_output(int(data2["outputs"][3]["gpio"]))
        elif opcao=='d':
            retorno = muda_estado_output(int(data2["outputs"][2]["gpio"]))
        elif opcao=='e':
            retorno = muda_estado_input(int(data2["inputs"][0]["gpio"]), int(data2["outputs"][4]["gpio"]))
        elif opcao=='f':
            retorno = muda_estado_input(int(data2["inputs"][1]["gpio"]), int(data2["outputs"][4]["gpio"]))
        elif opcao=='g':
            retorno = muda_estado_input(int(data2["inputs"][2]["gpio"]), int(data2["outputs"][4]["gpio"]))
        elif opcao=='h':
            retorno = muda_estado_input(int(data2["inputs"][3]["gpio"]), int(data2["outputs"][4]["gpio"]))
