import json
import socket

def socket_central(host_rec: str, port_rec:int, msg:str):
    
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (host_rec, port_rec)
    tcp.connect(dest)
    tcp.send (msg.encode())
    received = json.loads(tcp.recv(8192).decode("utf-8"))
    tcp.close()
    gravajson(received)
    
    
def gravajson(data_estados: any):
    file_estados = open("../json/estados.json", 'w')
    json.dump(data_estados, file_estados)
    file_estados.close()
    