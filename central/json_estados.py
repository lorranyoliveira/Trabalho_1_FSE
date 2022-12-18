import json


def gravajson(data_estados: any):
    file_estados = open("../json/estados.json", 'w')
    json.dump(data_estados, file_estados)
    file_estados.close()
    