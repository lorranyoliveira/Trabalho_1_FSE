from datetime import datetime
import json
import signal
from threading import Thread
from socket_central import  socket_central
import sys
from signal import signal, SIGPIPE, SIG_DFL

opcao = -1
sala = -1


def escreverLog(text: str):
    log = open('log.csv', 'a')
    log.write(f"{datetime.now()}, {text}\n")
    log.close()

def fraseLog(opcao: str, sala: int):
    if opcao == 'a': 
        escreverLog("Alterar estado Lampada 01 na sala " + str(sala))
    elif opcao == 'b': 
        escreverLog("Alterar estado Lampada 02 na sala " + str(sala))
    elif opcao == 'c': 
        escreverLog("Alterar estado Ar condicionado na sala " + str(sala))
    elif opcao == 'd': 
        escreverLog("Alterar estado Projetor Multimidia na sala " + str(sala))
    elif opcao == 'e': 
        escreverLog("Ligar modo de segurança via sensor de Presença " + str(sala))
    elif opcao == 'f': 
        escreverLog("Ligar modo anti incendio " + str(sala))
    elif opcao == 'g': 
        escreverLog("Ligar modo de segurança via sensor Janela " + str(sala))
    elif opcao == 'h': 
        escreverLog("Ligar modo de segurança via sensor Porta" + str(sala))



def display():
    
    file = open('../json/estados.json')
    data = json.load(file)
    file.close()
    
            
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
    
    while opcao!='s': 
        print('----------- MENU PRINCIPAL ---------------')
        print('Escolha uma opcao:')
        print('a - Alterar estado Lampada 01')
        print('b - Alterar estado Lampada 02')
        print('c - Alterar estado Ar condicionado')
        print('d - Alterar estado Projetor Multimidia')
        print('e - Ligar modo de segurança via sensor de Presença')
        print('f - Ligar modo anti incendio')
        print('g - Ligar modo de segurança via sensor Janela')
        print('h - Ligar modo de segurança via sensor Porta')
        print('i - Visualizar status salas')
        print('s - sair')
        opcao = input()
        temp = opcao
        if temp!='s' and temp!='i':
            temp = 's'
            print('Informe a sala 1 ou 2:')
            sala = int(input())
            while sala != 1 and int(sala) !=2:
                print('Informe a sala 1 ou 2:')
                sala = int(input())
                
            socket_central(str(sys.argv[1]),int(sys.argv[2]), str(sala)+str(opcao))
            fraseLog(opcao, sala)
        elif temp=='i':
            display()
            
            
            
if __name__ == '__main__':
    
    
    signal(SIGPIPE,SIG_DFL)
    
    
    socketMenu = Thread(target=menu)
    socketMenu.start()  
    
   
   