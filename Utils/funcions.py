import json
from Utils.paths import ALUMNOS, PROFESORES, ASIGNATURAS

def cargar_jsons(archivo):
    with open(archivo, "r", encoding="utf-8") as file:
        datos = json.load(file)
    return datos

def guardar_datos(archivo, datos):
    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4)

def eliminar_datos(archivo, email):
    datos = cargar_jsons(archivo)
    del datos[email]
    with open(archivo, "w") as file:
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

def alumnos_totales():
    datos = cargar_jsons(ALUMNOS)
    alumnos = [datos[email]["nombre"] for email in datos]
    alumnos.sort()
    return alumnos

def profesores_totales():
    datos = cargar_jsons(PROFESORES)
    profesores = [datos[email]["nombre"] for email in datos]
    profesores.sort()
    return profesores

def asignaturas_totales():
    datos = cargar_jsons(ASIGNATURAS)
    asignaturas = [dato for dato in datos]
    asignaturas.sort()
    return asignaturas
