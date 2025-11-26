#Ventana que el alumno verá al iniciar sesión correctamente

#Librerias y modulos usados
import customtkinter as ctk
from Utils.utils import MIN_ANCHO, MIN_ALTO, x, y, ANCHO, ALTO
from Utils.funcions import cargar_jsons
from Utils.paths import PROFESORES
from Utils.fonts import Fonts
from Clases.profesor import Profesor
from Ventanas.ventanas_top import VentanaInscribir

#Creación de la ventana que verá el alumno
class VentanaProfe(ctk.CTkToplevel):
    def __init__(self, email, master):
        super().__init__(master)
        
        #Configuración de la ventana
        self.master = master
        self.email = email
        self.title("Instituto Epsilon")
        self.geometry(f"{MIN_ANCHO}x{MIN_ALTO}+{x}+{y}")
        self.minsize(MIN_ANCHO, MIN_ALTO)
        
        #Cargar los datos del estudiante y guardarlos en la clase Alumno
        datos = cargar_jsons(PROFESORES)
        info = datos[email]
        profesor = Profesor(email, info["nombre"], info["rut"], info["asignaturas"], info["contrasena"], info["alumnos"])
        
        
        #Creando el frame superior (Datos del estudiante)
        frame_superior = ctk.CTkFrame(self, fg_color="#2b2b2b", height=ALTO*0.1)
        frame_superior.pack(fill="both", expand = True)
        
        #Información que irá en la parte superior
        ctk.CTkLabel(frame_superior, text=f"Bienvenido Profe {profesor.nombre}", font=Fonts.m2bold).place(relx=0.02, rely=0.15)
        ctk.CTkLabel(frame_superior, text=f"{profesor.rut}", font=Fonts.i2).place(relx=0.02, rely=0.6)
        
        
        #Creando el frame inferior (Donde se mostrará las asignaturas del alumno)
        self.frame_inferior = ctk.CTkScrollableFrame(self, width=ANCHO, height=ALTO*0.9, fg_color="#1b1b1b")
        self.frame_inferior.pack(fill="both", expand=True)
        
        self.mostrar_asignaturas(email)

        self.protocol("WM_DELETE_WINDOW", self.cerrar)


    def mostrar_asignaturas(self, email):
        #Cargar los datos del estudiante y guardarlos en la clase Alumno
        datos = cargar_jsons(PROFESORES)
        info = datos[email]
        profe = Profesor(email, info["nombre"], info["rut"], info["asignaturas"], info["contrasena"], info["alumnos"])
        #Se crea un contenedor por cada asignatura que tenga el estudiante
        for i in range(len(profe.asignaturas)):
            
            #Iran 3 asignaturas por cada fila
            filas = i // 3
            #Sirve para saber en que columa poner la asignatura
            columnas = i % 3
            ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.1, height=ALTO*0.35, fg_color="#2b2b2b").grid(row=filas, column=columnas, sticky="nsew", padx=20, pady=60)
        
        num_filas = (len(profe.asignaturas) + 2) // 3 
        for f in range(num_filas):
            self.frame_inferior.rowconfigure(f, weight=1)
        for c in range(3):
            self.frame_inferior.columnconfigure(c, weight=1)
    
    def cerrar(self):
        self.master.destroy()
