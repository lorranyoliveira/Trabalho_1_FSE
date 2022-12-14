import json
from threading import Thread
import sys

from socket_distribuido import socket_distribuido

if __name__ == '__main__':
     
    #lê o arquivo de configuração mandado via parametro na linha de comando
    with open(sys.argv[1]) as file:
        data = json.load(file)
        ip= str(data["ip_servidor_distribuido"])
        port= int(data["porta_servidor_distribuido"])
    
    # se comunica via socket como servidor central    
    socket_menu = Thread(target=socket_distribuido, args=(ip,port, data))
    socket_menu.start()
    
    
   
   