import os

#Ruta en donde se encuentra el archivo base
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#Rutas en donde se encuentran los archivos json
ALUMNOS = os.path.join(BASE_DIR, "Jsons", "alumnos.json")
PROFESORES = os.path.join(BASE_DIR, "Jsons", "profesores.json")
ADMINISTRADORES = os.path.join(BASE_DIR, "Jsons", "administradores.json")
ASIGNATURAS = os.path.join(BASE_DIR, "Jsons", "asignaturas.json")

MONTSERRAT = os.path.join(BASE_DIR, "Fonts", "Montserrat.ttf")
INTER = os.path.join(BASE_DIR, "Fonts", "Inter.ttf")