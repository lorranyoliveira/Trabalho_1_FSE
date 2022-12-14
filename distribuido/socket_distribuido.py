import socket

from luz import acende_luz

def socket_distribuido(_host: str,_port:int, data:any):
    HOST = _host              # Endereco IP do Servidor
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
            print ('mensagem:', msg.decode())
            if msg.decode()=='1': 
                acende_luz(int(data["outputs"][0]["gpio"]))
            
        print ('Finalizando conexao do cliente', cliente)
        con.close()

        
    