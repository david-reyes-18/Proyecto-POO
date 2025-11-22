import customtkinter as ctk
from Utils.utils import TOPLEVEL_ANCHO, TOPLEVEL_ALTO, x, y
from Utils.funcions import cargar_jsons
from Utils.paths import ADMINISTRADORES, ALUMNOS
from Clases.administrador import Admin


class VentanaDatosAlumno(ctk.CTkToplevel):
    def __init__(self, email):
        super().__init__()
        self.email = email
        
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)