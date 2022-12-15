import datetime
import json
from threading import Thread
from socket_central import socket_central
import sys

opcao = -1
sala = -1

def escreverLog(text: str):
    log = open('log.csv', 'a')
    log.write(f"{datetime.now()}, {text}\n")
    log.close()


def display():
    
    with open('../json/estados.json') as file:
        data = json.load(file)
            
    print('----------- ESTADO SALA 01 ---------------')
    print('Lampada 01:         ' , data["sala_01"][0]["outputs"][0]["status"])
    print('Lampada 02:          ' + data["sala_01"][0]["outputs"][1]["status"])
    print('Ar condicionado:     ' + data["sala_01"][0]["outputs"][3]["status"])
    print('Projetor Multimidia: ' + data["sala_01"][0]["outputs"][2]["status"])
    print('Alarme:              ' + data["sala_01"][0]["outputs"][4]["status"])
    print('------------------------------------------')
    print('----------- ESTADO SALA 02 ---------------')
    print('Lampada 01:         ' , data["sala_02"][0]["outputs"][0]["status"])
    print('Lampada 02:          ' + data["sala_02"][0]["outputs"][1]["status"])
    print('Ar condicionado:     ' + data["sala_02"][0]["outputs"][3]["status"])
    print('Projetor Multimidia: ' + data["sala_02"][0]["outputs"][2]["status"])
    print('Alarme:              ' + data["sala_02"][0]["outputs"][4]["status"])
    

def menu():
    global opcao
    global sala
    
    while opcao!='f' and opcao!='a' and opcao!='b' and opcao!='c' and opcao!='d' and opcao!='e': 
        display()
        print('----------- MENU PRINCIPAL ---------------')
        print('Escolha uma opcao:')
        print('a - Alterar estado Lampada 01')
        print('b - Alterar estado Lampada 02')
        print('c - Alterar estado Ar condicionado')
        print('d - Alterar estado Projetor Multimidia')
        print('e - Alterar estado do Alarme')
        print('f - sair')
        opcao = input()
        temp = opcao
        if temp!='f':
            temp = 'f'
            print('Informe a sala 1 ou 2:')
            sala = int(input())
            while sala != 1 and int(sala) !=2:
                print('Informe a sala 1 ou 2:')
                sala = int(input())
                
            socket_central(str(sys.argv[1]),int(sys.argv[2]), str(sala)+str(opcao))
            if opcao == 'a': 
                escreverLog("Alterar estado Lampada 01 na sala " + sala)
            elif opcao == 'b': 
                escreverLog("Alterar estado Lampada 02 na sala " + sala)
            elif opcao == 'c': 
                escreverLog("Alterar estado Ar condicionado na sala " + sala)
            elif opcao == 'd': 
                escreverLog("Alterar estado Projetor Multimidia na sala " + sala)
            elif opcao == 'f': 
                escreverLog("Alterar estado Alarme na sala " + sala)
            

if __name__ == '__main__':
    
    socketMenu = Thread(target=menu)
    socketMenu.start()  
    
    print(opcao)

    socketThread = Thread(target=socket_central, args=(str(sys.argv[1]),int(sys.argv[2]), str(opcao)))
    socketThread.start()         
    socketMenu.join()
   
   