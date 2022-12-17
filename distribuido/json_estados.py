import json
import socket


def lerjson():
    file_estados = open("../json/estados.json", 'r')
    data_estados = json.load(file_estados)
    file_estados.close()
    return data_estados
        
    