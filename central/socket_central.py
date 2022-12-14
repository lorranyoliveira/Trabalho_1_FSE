import socket

def socket_central(host_rec: str, port_rec:int, msg:str):
    HOST = host_rec         # Endereco IP do Servidor
    PORT = port_rec    # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    print ('Para sair use CTRL+X\n')
    tcp.send (msg.encode())
    tcp.close()