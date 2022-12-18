import json
import socket
from json_estados import gravajson

def socket_central(host_rec: str, port_rec:int, msg:str):
    
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (host_rec, port_rec)
    tcp.connect(dest)
    tcp.send (msg.encode())
    received = json.loads(tcp.recv(8192).decode("utf-8"))
    tcp.close()
    gravajson(received)
    
    
