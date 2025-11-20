import os

#Ruta en donde se encuentra el archivo base
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#Rutas en donde se encuentran los archivos json
ALUMNOS = os.path.join(BASE_DIR, "Utils", "alumnos.json")
PROFESORES = os.path.join(BASE_DIR, "Utils", "profesores.json")
ADMINISTRADORES = os.path.join(BASE_DIR, "Utils", "administradores.json")
