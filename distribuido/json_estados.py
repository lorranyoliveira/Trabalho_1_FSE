import json
import socket


def lerjson():
    file_estados = open("../json/estados.json", 'r')
    data_estados = json.load(file_estados)
    file_estados.close()
    return data_estados

def gravajson(data_estados: any):
    file_estados = open("../json/estados.json", 'w')
    json.dump(data_estados, file_estados)
    file_estados.close()
        
    