import customtkinter as ctk
from Utils.utils import MIN_ANCHO, MIN_ALTO, x, y, ANCHO, ALTO
from Utils.funcions import cargar_jsons
from Utils.paths import PROFESORES
from Clases.profesor import Profesor

class VentanaProfe(ctk.CTkToplevel):
    def __init__(self, email, master):
        super().__init__(master)
        self.master = master
        self.email = email
        self.title("Escuelita")
        self.config(background="#2b2b2b")
        self.geometry(f"{MIN_ANCHO}x{MIN_ALTO}+{x}+{y}")
        self.minsize(MIN_ANCHO, MIN_ALTO)
        
        datos = cargar_jsons(PROFESORES)
        info = datos[email]
        profe = Profesor(email, info["nombre"], info["rut"], info["asignaturas"], info["contrasena"])
        