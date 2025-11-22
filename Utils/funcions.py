import json
from Utils.paths import ALUMNOS, PROFESORES

def cargar_jsons(archivo):
    with open(archivo, "r") as file:
        datos = json.load(file)
    return datos

def guardar_datos(archivo, datos):
    with open(archivo, "w") as file:
        json.dump(datos, file, indent=4)

def eliminar_alumno(email):
    datos = cargar_jsons(ALUMNOS)
    del datos[email]
    with open(ALUMNOS, "w") as file:
        json.dump(datos, file, indent=4)

def correo_institucional(nombres: str, apellidos: str):
    lista_nombre = nombres.split()
    lista_apellidos = apellidos.split()
    
    return f"{lista_nombre[0].lower()}{lista_nombre[1].lower()}.{lista_apellidos[0].lower()}@alumnos.escuelita.cl"

def contrasena(rut: str):
    rut_sin_punto = [char for char in rut if char != '.' and char != '-' ]
    rut_string = "".join(rut_sin_punto)
    contrasena = rut_string[0:5]
    return contrasena
