#Aqui se encuentran funciones importantes que se usarán dentro de sistema
import json
from Utils.paths import ALUMNOS, PROFESORES, ASIGNATURAS

#Funcion que carga los datos de un archivo json y entrega esos datos
def cargar_jsons(archivo):
    with open(archivo, "r", encoding="utf-8") as file:
        datos = json.load(file)
    return datos

#Guarda los datos que se le entreguen en un archivo json
def guardar_datos(archivo, datos):
    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4)

#Elimina todos los datos de un alumno
def eliminar_datos_alumno(email):
    #cargar datos del los alumnos
    datos = cargar_jsons(ALUMNOS)
    #guardar el nombre del alumno
    nombre_alumno = datos[email]["nombre"]
    #eliminar todos los datos del alumno
    del datos[email]
    #se guardan los cambios
    guardar_datos(ALUMNOS, datos)
    
    #Se elimina de todas las asignaturas en la que estaba el alumno
    datos = cargar_jsons(ASIGNATURAS)
    
    for asignatura in datos:
        if nombre_alumno in datos[asignatura]["estudiantes"]:
            datos[asignatura]["estudiantes"].remove(nombre_alumno)
    
    guardar_datos(ASIGNATURAS, datos)
    
    datos =cargar_jsons(PROFESORES)
    
    for profe in datos:
        if nombre_alumno in datos[profe]["alumnos"]:
            datos[profe]["estudiantes"].remove(nombre_alumno)
    
    guardar_datos(PROFESORES, datos)

#Elimina todos los datos de un profesor
def eliminar_datos_profesor(email):
    #Se cargan los datos de los profesores, asiganturas y alumnos
    datos_profe = cargar_jsons(PROFESORES)
    datos_asignatura = cargar_jsons(ASIGNATURAS)
    datos_alumno = cargar_jsons(ALUMNOS)
    
    #Se guarda ek nombre del profesor
    nombre_profesor = datos_profe[email]["nombre"]
    
    #Se eliminan todos los datos del profesor
    del datos_profe[email]
    
    #Se elimina el nombre del profesor de todas las asignaturas en las que imparte
    for asignatura in datos_asignatura:
        if nombre_profesor in datos_asignatura[asignatura]["profesores"]:
            datos_asignatura[asignatura]["profesores"].remove(nombre_profesor)
    
    
    for alumno in datos_alumno:
        if nombre_profesor in datos_alumno[alumno]["profesores"]:
            nombre_alumno = datos_alumno[alumno]["nombre"]
            indice = datos_alumno[alumno]["profesores"].index(nombre_profesor)
            datos_alumno[alumno]["profesores"].remove(nombre_profesor)
            del datos_alumno[alumno]["asignaturas"][indice]
            
    #Se elimina el nombre del profesor de todas las asignaturas en las que imparte
    for asignatura in datos_asignatura:
        if nombre_profesor in datos_asignatura[asignatura]["profesores"]:
            datos_asignatura[asignatura]["profesores"].remove(nombre_profesor)
            datos_asignatura[asignatura]["alumnos"].remove(nombre_alumno)
    
            
    guardar_datos(PROFESORES, datos_profe)
    guardar_datos(ASIGNATURAS, datos_asignatura)
    guardar_datos(ALUMNOS, datos_alumno)

def eliminar_datos_asignatura(asignatura):
    
    datos_asignatura = cargar_jsons(ASIGNATURAS)
    
    del datos_asignatura[asignatura]
    
    guardar_datos(ASIGNATURAS, datos_asignatura)
    
    datos_alumnos = cargar_jsons(ALUMNOS)
    datos_profesores = cargar_jsons(PROFESORES)
    
    for alumno in datos_alumnos:
        if asignatura in datos_alumnos[alumno]["asignaturas"]:
            indice = datos_alumnos[alumno]["asignaturas"].index(asignatura)
            datos_alumnos[alumno]["asignaturas"].remove(asignatura)
            profesor = datos_alumnos[alumno]["profesores"][indice]
            del datos_alumnos[alumno]["profesores"][indice]
            for profe in datos_profesores:
                if datos_profesores[profe]["nombre"] == profesor:
                    datos_profesores[profe]["alumnos"].remove(datos_alumnos[alumno]["nombre"])
    for profe in datos_profesores:
        if asignatura in datos_profesores[profe]["asignaturas"]:
            datos_profesores[profe]["asignaturas"].remove(asignatura)

    guardar_datos(ALUMNOS, datos_alumnos)
    guardar_datos(PROFESORES, datos_profesores)


def correo_institucional(nombres: str, apellidos: str, rol: str):
    lista_nombre = nombres.split()
    lista_apellidos = apellidos.split()
    if rol == "alumno":
        return f"{lista_nombre[0].lower()}{lista_nombre[1].lower()}.{lista_apellidos[0].lower()}@alumnos.epsilon.cl"
    elif rol == "profesor":
        return f"{lista_nombre[0].lower()}{lista_nombre[1].lower()}.{lista_apellidos[0].lower()}@profe.epsilon.cl"
    
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
