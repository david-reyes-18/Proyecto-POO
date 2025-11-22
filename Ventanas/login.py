#Librerias y modulos que usaremos
import customtkinter as ctk
from Utils.utils import x, y, MIN_ANCHO, MIN_ALTO
from Utils.paths import ALUMNOS, PROFESORES, ADMINISTRADORES
from Utils.funcions import cargar_jsons
from Ventanas.ventana_alumno import VentanaAlumno
from Ventanas.ventana_admin import VentanaAdmin
from Ventanas.ventana_profe import VentanaProfe

#Creacion de la ventana de Inicio de sesión con customtkinter
class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        #Configuracion de la ventana
        self.title("Iniciar Sesión")
        self.geometry(f"{MIN_ANCHO}x{MIN_ALTO}+{x}+{y}")
        self.minsize(MIN_ANCHO, MIN_ALTO)
        
        #               Iniciar sesión
        
        #   Label inicio de sesión
        label_inicio = ctk.CTkLabel(self, text="Iniciar sesión", font=('Arial', 30))
        label_inicio.place(relx=0.1, rely=0.1)
        
        #    Sección de email
        
        label_email = ctk.CTkLabel(self, text="Ingrese su email", font=('Arial', 20))
        label_email.place(relx=0.1, rely=0.2)
        
        entrada_email = ctk.CTkEntry(self)
        entrada_email.place(relx=0.1, rely=0.3)
        
        #    Sección contraseña
        
        label_contrasena = ctk.CTkLabel(self, text="Ingrese su contraseña", font=('Arial', 20))
        label_contrasena.place(relx=0.1, rely=0.4)
        
        entrada_contrasena = ctk.CTkEntry(self, show='*')
        entrada_contrasena.place(relx=0.1, rely=0.5)
        
        #                  Boton iniciar sesión
        
        #Funcion que verifica el inicio de sesión, verifica si el correo y la contraseña estan correctos
        def iniciar_sesion():
            #Obtener la informacion que entrego el usuario
            email = entrada_email.get()
            contrasena = entrada_contrasena.get()
            
            #cargar los datos que se tienen en la base de datos
            datos_alumnos = cargar_jsons(ALUMNOS)
            datos_profesor = cargar_jsons(PROFESORES)
            datos_administradores = cargar_jsons(ADMINISTRADORES)
            
            #    Verificar el email y la contraseña
            
            #Verificar si es alumno
            if email in datos_alumnos:
                if contrasena == datos_alumnos[email]["contrasena"]:
                    ventanita = VentanaAlumno(email)
                    self.destroy()
                    ventanita.mainloop()
            
            #Verificar si es profesor
            elif email in datos_profesor:
                if contrasena == datos_profesor[email]["contrasena"]:
                    ventanita = VentanaProfe(email)
                    self.destroy()
                    ventanita.mainloop()
                    
            #Verificar si es administrador
            elif email in datos_administradores:
                if contrasena == datos_administradores[email]["contrasena"]:
                    ventanita = VentanaAdmin(email, master=self)
                    self.withdraw()
        
        #Boton de inicio de sesión
        boton_sesion = ctk.CTkButton(self, text="Iniciar sesion", command=iniciar_sesion)
        boton_sesion.place(relx = 0.1, rely=0.6)
