import customtkinter as ctk
from Utils.utils import MIN_ANCHO, MIN_ALTO, x, y, ANCHO, ALTO
from Utils.funcions import cargar_jsons
from Utils.paths import ADMINISTRADORES
from Clases.administrador import Admin

class VentanaAdmin(ctk.CTk):
    def __init__(self, email):
        self.email = email
        self.title("Administración de Escuelita")
        self.config(background="#2b2b2b")
        self.geometry(f"{MIN_ANCHO}x{MIN_ALTO}+{x}+{y}")
        self.minsize(MIN_ANCHO, MIN_ALTO)
        
        datos = cargar_jsons(ADMINISTRADORES)
        info = datos[email]
        admin = Admin(email, info["nombre"], info["rut"], info["contrasena"])
        
        #Creando el frame superior (Datos del estudiante)
        frame_superior = ctk.CTkFrame(self, fg_color="#F90808", height=ALTO*0.1)
        frame_superior.pack(fill="both", expand = True)
        
        #Información que irá en la parte superior
        ctk.CTkLabel(frame_superior, text=f"Bienvenido admin {admin.nombre}", font=("Arial", 20)).place(relx=0.02, rely=0.25)
        ctk.CTkLabel(frame_superior, text=f"{admin.rut}", font=("Arial", 15)).place(relx=0.02, rely=0.6)
        
        #Creando el frame inferior (DOnde se mostrará las asignaturas del alumno)
        frame_inferior = ctk.CTkScrollableFrame(self, width=ANCHO, height=ALTO*0.9, fg_color="#999999")
        frame_inferior.pack(fill="both", expand=True)
    
    def iniciar(self):
        self.mainloop()