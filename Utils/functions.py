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
    
    #Por cada asignatura que este en los datos
    for asignatura in datos:
        #Si el nombre del alumno esta en una asignatura
        if nombre_alumno in datos[asignatura]["estudiantes"]:
            #Se elimina de la asignatura
            datos[asignatura]["estudiantes"].remove(nombre_alumno)
            #Se actualizan los estudiantes
            datos[asignatura]["cantidad_estudiantes"] = len(datos[asignatura]["estudiantes"])
    
    #Se guardan los datos
    guardar_datos(ASIGNATURAS, datos)
    
    #Se cargan los datos de los profesores
    datos =cargar_jsons(PROFESORES)
    
    #Por cada profesor en los datos
    for profe in datos:
        #Si el nombre del alumno eliminado se encuentra en profesores
        if nombre_alumno in datos[profe]["alumnos"]:
            #Se elimina el alumno de ahi
            datos[profe]["estudiantes"].remove(nombre_alumno)
    
    #Se guardan los datos
    guardar_datos(PROFESORES, datos)

#Elimina todos los datos de un profesor
def eliminar_datos_profesor(email):
    #Se cargan los datos de los profesores, asiganturas y alumnos
    datos_profe = cargar_jsons(PROFESORES)
    datos_asignatura = cargar_jsons(ASIGNATURAS)
    datos_alumno = cargar_jsons(ALUMNOS)
    
    #Se guarda el nombre del profesor
    nombre_profesor = datos_profe[email]["nombre"]
    
    #Se eliminan todos los datos del profesor
    del datos_profe[email]
    
    #Por cada asignatura que se encuentre en los datos
    for asignatura in datos_asignatura:
        
        #Si el nombre del profesor se encuentra dentro de dicha asignatura se elimina
        if nombre_profesor in datos_asignatura[asignatura]["profesores"]:
            datos_asignatura[asignatura]["profesores"].remove(nombre_profesor)
    
    #Por cada alumno que este en los datos
    for alumno in datos_alumno:
        
        #Si el profesor se encuentra en los datos de cierto alumno
        if nombre_profesor in datos_alumno[alumno]["profesores"]:
            #Se guarda el nombre del alumno
            nombre_alumno = datos_alumno[alumno]["nombre"]
            #Se guarda el indice en donde esta el profesor
            indice = datos_alumno[alumno]["profesores"].index(nombre_profesor)
            #Se elimina el profesor del alumno
            datos_alumno[alumno]["profesores"].remove(nombre_profesor)
            #Se obtiene la materia del alumno en donde aparece el profe
            asig_impartida = datos_alumno[alumno]["asignaturas"][indice]
            datos_asignatura[asig_impartida]["estudiantes"].remove(nombre_alumno)
            datos_asignatura[asig_impartida]["cantidad_estudiantes"] = len(datos_asignatura[asig_impartida]["estudiantes"])
            #Se elimina la materia que impartia
            del datos_alumno[alumno]["asignaturas"][indice]

            
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
                    datos_profesores[profe]["alumnos"].remove(f"{datos_alumnos[alumno]['nombre']},{asignatura}")
    for profe in datos_profesores:
        if asignatura in datos_profesores[profe]["asignaturas"]:
            datos_profesores[profe]["asignaturas"].remove(asignatura)

    guardar_datos(ALUMNOS, datos_alumnos)
    guardar_datos(PROFESORES, datos_profesores)

#Funcion que entrega un correo institucional según el rol
def correo_institucional(nombres: str, apellidos: str, rol: str):
    #Se separan los nombres y los apellidos
    lista_nombre = nombres.split()
    lista_apellidos = apellidos.split()
    #Si es un alumno tendrá la siguiente estructura: nombre1nombre2.apellido1@alumnos.epsilon.cl
    if rol == "alumno":
        return f"{lista_nombre[0].lower()}{lista_nombre[1].lower()}.{lista_apellidos[0].lower()}@alumnos.epsilon.cl"
    #Si es un profesor tendrá la siguiente estructura: nombre1nombre2.apellido1@profe.epsilon.cl
    elif rol == "profesor":
        return f"{lista_nombre[0].lower()}{lista_nombre[1].lower()}.{lista_apellidos[0].lower()}@profe.epsilon.cl"

#Función que crea una contraseña institucional básica
def contrasena(rut: str):
    rut_sin_punto = [char for char in rut if char != '.' and char != '-' ]
    rut_string = "".join(rut_sin_punto)
    contrasena = rut_string[0:5]
    return contrasena

#Función que entrega el total de alumnos ordenados
def alumnos_totales():
    datos = cargar_jsons(ALUMNOS)
    alumnos = [datos[email]["nombre"] for email in datos]
    alumnos.sort()
    return alumnos

#Función que entrega todos los profesores ordenados
def profesores_totales():
    datos = cargar_jsons(PROFESORES)
    profesores = [datos[email]["nombre"] for email in datos]
    profesores.sort()
    return profesores

#Función que entrega todas las asignaturas ordenadas
def asignaturas_totales():
    datos = cargar_jsons(ASIGNATURAS)
    asignaturas = [dato for dato in datos]
    asignaturas.sort()
    return asignaturas

#Función que verifica que una palabra es un string sin numeros ni caracteres especiales
def es_string(palabra: str):
    #Por cada caracter en la palabra
    for char in palabra:
        #Si no es alphanumerico y ademas no es un espacio se retorna False
        if not char.isalpha() and not char == " ":
            return False
    #Si todos los caracteres son alphanumerico o contiene espacios se retorna True
    return True


#Función para verificar un rut
def verificar_rut(rut: str):
    #Primero se trata de ejecutar la siguiente linea de código
    try:
        #Si no tiene el siguiente formato XX.XXX.XXXX entonces no retorna False
        if not len(rut.split(".")[0]) == 2 or not len(rut.split(".")[1]) == 3 or not len(rut.split(".")[2]) == 5:
            return False
        
        #Además complementando al anterior, si no tiene el siguiente formato XXXXXXXXXX-X retorna False
        if not len(rut.split("-")[0]) == 10 or not len(rut.split("-")[1]) == 1:
            return False
    #Si ocurre algun error entonces no tiene el formato rut, entonces retorna False
    except Exception:
        return False
    
    #Ya verificado el formato XX.XXX.XXX-X quitamos los . y -
    rut = rut.replace(".", "").replace("-", "")

    #Si los primeros 8 no son numeros retorna False
    if not rut[:-1].isdigit():
        return False
    
    #Guardamos el digito verificador
    digito_verificador = rut[-1]
    
    #Ya que comprobamos que todos son numeros estrictamente a excepcion del digito verificador, ahora verificamos que el digito verificador efectivamente sea el correcto
    
    #Se inicia el algoritmo para verificar el digito verificador
    multiplicadores = [2, 3, 4, 5, 6, 7, 2, 3]
    
    #Se guardan los primeros 8 digitos para comenzar con la verificación
    rut = rut[:-1]
    #Se invierte el rut
    rut_inverso = rut[::-1]
    #Variable suma con valor 0
    suma_rut = 0
    
    #Se itera por cada caracter del rut inverso, incluyendo su indice
    for i, char in enumerate(rut_inverso):
        #Se van sumando la multiplicacion de cada digito por los multiplicadores
        suma_rut += int(char) * multiplicadores[i]
    
    #A la suma se le saca modulo 11
    modulo = suma_rut % 11
    
    #Finalmente el digito verificador es la resta de 11 menos el modulo obtenido
    nuevo_digito_verificador = 11 - modulo
    
    #Si da resultado 10 se cambia por una k
    if nuevo_digito_verificador == 10:
        nuevo_digito_verificador = "k"
    
    #Si el resultado es 11 se cambia por un 0
    if nuevo_digito_verificador == 11:
        nuevo_digito_verificador = "0"
    
    #Si el digito resultante no es igual al inicial se retorna False
    if not str(nuevo_digito_verificador) == digito_verificador.lower():
        return False
    
    #Si todo salió bien, entonces efectivamente es un rut correcto
    return True