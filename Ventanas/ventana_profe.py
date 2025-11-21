import tkinter as tk
from Utils.utils import MIN_ANCHO, MIN_ALTO, x, y, ANCHO, ALTO
from Utils.funcions import cargar_jsons
from Utils.paths import PROFESORES
from Clases.profesor import Profesor

class VentanaProfe:
    def __init__(self, email):
        self.email = email
        self.root = tk.Tk()
        self.root.title("Escuelita")
        self.root.config(background="#2b2b2b")
        self.root.geometry(f"{MIN_ANCHO}x{MIN_ALTO}+{x}+{y}")
        self.root.minsize(MIN_ANCHO, MIN_ALTO)
        
        datos = cargar_jsons(PROFESORES)
        info = datos["profesores"][email]
        profe = Profesor(email, info["nombre"], info["rut"], info["asignaturas"], info["contrasena"])
        
        #Creando el lienzo superior
        lienzo_superior = tk.Canvas(self.root, width=ANCHO, height=ALTO*0.1, background="#3b3b3b")
        lienzo_superior.place(relx=0, rely=0)
        
        #Texto del lienzo superior
        tk.Label(lienzo_superior, text=f"Bienvenido Profesor {profe.nombre}", font=("Arial", 20)).place(relx=0.02, rely=0.25)
        tk.Label(lienzo_superior, text=f"{profe.rut}", font=("Arial", 15)).place(relx=0.02, rely=0.6)
        
        
        
        #Creando el lienzo inferior
        lienzo_inferior = tk.Canvas(self.root, width=ANCHO, height=ALTO*0.9, background="#0059FF")
        lienzo_inferior.place(relx= 0, y=ALTO*0.1)
    
    def iniciar(self):
        self.root.mainloop()