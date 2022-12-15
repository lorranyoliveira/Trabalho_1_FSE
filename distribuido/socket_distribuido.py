import socket

from input import muda_estado_input

def socket_distribuido(_host: str,_port:int, data:any, data2:any):
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
            if temp[0]=='1':
                if temp[1]=='a':
                    muda_estado_input(int(data["outputs"][0]["gpio"]))
                elif temp[1]=='b':
                    muda_estado_input(int(data["outputs"][1]["gpio"]))
                elif temp[1]=='c':
                    muda_estado_input(int(data["outputs"][3]["gpio"]))
                elif temp[1]=='d':
                    muda_estado_input(int(data["outputs"][2]["gpio"]))
                elif temp[1]=='e':
                    muda_estado_input(int(data["outputs"][4]["gpio"]))
            elif temp[0]=='2':
                if temp[1]=='a':
                    muda_estado_input(int(data2["outputs"][0]["gpio"]))
                elif temp[1]=='b':
                    muda_estado_input(int(data2["outputs"][1]["gpio"]))
                elif temp[1]=='c':
                    muda_estado_input(int(data2["outputs"][3]["gpio"]))
                elif temp[1]=='d':
                    muda_estado_input(int(data2["outputs"][2]["gpio"]))
                elif temp[1]=='e':
                    muda_estado_input(int(data2["outputs"][4]["gpio"]))
        
        print ('Finalizando conexao do cliente', cliente)
        con.close()

        
    