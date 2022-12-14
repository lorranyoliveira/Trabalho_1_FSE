from threading import Thread
from socket_central import socket_central
import sys

opcao = -1

def menu():
    global opcao
    print('----------- MENU PRINCIPAL ---------------')
    print('Escolha uma opcao:')
    print('1 - Lampada 01')
    print('2 - Lampada 02')
    print('3 - Ar condicionado')
    print('4 - Projetor Multimidia')
    print('5 - Sensor de temperatura')
    print('0 - sair')
    opcao = int(input())
    print(opcao)
    

if __name__ == '__main__':
    
    socketMenu = Thread(target=menu)
    socketMenu.start()  
    socketMenu.join()
    
    print(opcao)

    if opcao==1: 
        socketThread = Thread(target=socket_central, args=(str(sys.argv[1]),int(sys.argv[2]), str(opcao)))
        socketThread.start()        
    
    
   
   