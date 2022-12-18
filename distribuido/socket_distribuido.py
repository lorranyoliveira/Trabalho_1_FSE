import json
import pprint
import socket
import socketserver
from json_estados import lerjson, gravajson
from input import muda_estado_input
from output import muda_estado_output
from dht22_sensor_temp import sensor_temp

retorno = True

def socket_distribuido(_host: str,_port:int, data:any, data2:any):
    global retorno
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (_host, _port)
    tcp.bind(orig)
    tcp.listen()
    while True:
        con, cliente = tcp.accept()
        print ('Concetado por', cliente)
        while True:
            msg = con.recv(8192)
            if not msg: break
            temp = msg.decode()
            data_estados = verificaEscolha(temp[0], temp[1], data, data2)
            con.sendall(bytes(json.dumps(data_estados), encoding="UTF-8"))
        print ('Finalizando conexao do cliente', cliente)
            


def verificaEscolha(sala: str, opcao: str, data: any, data2: any):
    global retorno
    
    data_estados = lerjson()
    
   
    if sala=='1':
        
        if opcao=='a':
            retorno = muda_estado_output(int(data["outputs"][0]["gpio"]))
            data_estados["sala_01"][0]["outputs"][0]['status'] = retorno
        elif opcao=='b':
            retorno = muda_estado_output(int(data["outputs"][1]["gpio"]))
            data_estados["sala_01"][0]["outputs"][1]['status'] = retorno
        elif opcao=='c':
            retorno = muda_estado_output(int(data["outputs"][3]["gpio"]))
            data_estados["sala_01"][0]["outputs"][3]['status'] = retorno
        elif opcao=='d':
            retorno = muda_estado_output(int(data["outputs"][2]["gpio"]))
            data_estados["sala_01"][0]["outputs"][2]['status'] = retorno
        elif opcao=='e':
            retorno = muda_estado_input(int(data["inputs"][0]["gpio"]), int(data["outputs"][4]["gpio"]))
        elif opcao=='f':
            retorno = muda_estado_input(int(data["inputs"][1]["gpio"]), int(data["outputs"][4]["gpio"]))
        elif opcao=='g':
            retorno = muda_estado_input(int(data["inputs"][2]["gpio"]), int(data["outputs"][4]["gpio"]))
        elif opcao=='h':
            retorno = muda_estado_input(int(data["inputs"][3]["gpio"]), int(data["outputs"][4]["gpio"]))
        elif opcao=='j':
            sensor_temp(data["sensor_temperatura"][0]["gpio"])
    elif sala=='2':        
        if opcao=='a':
            retorno = muda_estado_output(int(data2["outputs"][0]["gpio"]))
            data_estados["sala_02"][0]["outputs"][0]['status'] = retorno
        elif opcao=='b':
            retorno = muda_estado_output(int(data2["outputs"][1]["gpio"]))
            data_estados["sala_02"][0]["outputs"][1]['status'] = retorno
        elif opcao=='c':
            retorno = muda_estado_output(int(data2["outputs"][3]["gpio"]))
            data_estados["sala_02"][0]["outputs"][3]['status'] = retorno
        elif opcao=='d':
            retorno = muda_estado_output(int(data2["outputs"][2]["gpio"]))
            data_estados["sala_02"][0]["outputs"][2]['status'] = retorno
        elif opcao=='e':
            retorno = muda_estado_input(int(data2["inputs"][0]["gpio"]), int(data2["outputs"][4]["gpio"]))
        elif opcao=='f':
            retorno = muda_estado_input(int(data2["inputs"][1]["gpio"]), int(data2["outputs"][4]["gpio"]))
        elif opcao=='g':
            retorno = muda_estado_input(int(data2["inputs"][2]["gpio"]), int(data2["outputs"][4]["gpio"]))
        elif opcao=='h':
            retorno = muda_estado_input(int(data2["inputs"][3]["gpio"]), int(data2["outputs"][4]["gpio"]))
        elif opcao=='j':
            sensor_temp(data2["sensor_temperatura"][0]["gpio"])
            
        gravajson(data_estados)

        data_estados_atualizado = lerjson()

    return data_estados_atualizado