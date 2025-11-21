import json

def cargar_jsons(archivo):
    with open(archivo, "r") as file:
        datos = json.load(file)
    return datos
