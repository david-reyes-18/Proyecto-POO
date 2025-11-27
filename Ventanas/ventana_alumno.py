#Ventana que el alumno verá al iniciar sesión correctamente

#Librerias y modulos usados
import customtkinter as ctk
from Utils.utils import MIN_ANCHO, MIN_ALTO, x, y, ANCHO, ALTO
from Utils.funcions import cargar_jsons
from Utils.paths import ALUMNOS
from Utils.fonts import Fonts
from Clases.alumnos import Alumno
from Ventanas.ventanas_top import VentanaInscribir

#Creación de la ventana que verá el alumno
class VentanaAlumno(ctk.CTkToplevel):
    def __init__(self, email, master):
        super().__init__(master)
        
        #Configuración de la ventana
        self.master = master
        self.email = email
        self.title("Instituto Epsilon")
        self.geometry(f"{MIN_ANCHO}x{MIN_ALTO}+{x}+{y}")
        self.minsize(MIN_ANCHO, MIN_ALTO)
        
        #Cargar los datos del estudiante y guardarlos en la clase Alumno
        datos = cargar_jsons(ALUMNOS)
        info = datos[email]
        alumno = Alumno(email, info["nombre"], info["rut"],info["carrera"],info["asignaturas"],info["contrasena"], info["profesores"])
        
        
        #Creando el frame superior (Datos del estudiante)
        frame_superior = ctk.CTkFrame(self, fg_color="#2b2b2b", height=ALTO*0.1)
        frame_superior.pack(fill="both", expand = True)
        
        #Información que irá en la parte superior
        ctk.CTkLabel(frame_superior, text=f"Bienvenido, {alumno.nombre}", font=Fonts.m2bold).place(relx=0.02, rely=0.15)
        ctk.CTkLabel(frame_superior, text=f"{alumno.rut}", font=Fonts.i2).place(relx=0.02, rely=0.6)
        ctk.CTkLabel(frame_superior, text=f"{alumno.carrera}", font=Fonts.i2).place(relx=0.3, rely=0.6)
        
        ctk.CTkButton(frame_superior, text="Inscribir Asignatura", command=lambda: VentanaInscribir(email, self), font=Fonts.m2).place(relx=0.75, rely=0.3)
        
        #Creando el frame inferior (Donde se mostrará las asignaturas del alumno)
        self.frame_inferior = ctk.CTkScrollableFrame(self, width=ANCHO, height=ALTO*0.9, fg_color="#1b1b1b")
        self.frame_inferior.pack(fill="both", expand=True)
        
        self.mostrar_asignaturas(email)

        self.protocol("WM_DELETE_WINDOW", self.cerrar)


    def mostrar_asignaturas(self, email):
        #Cargar los datos del estudiante y guardarlos en la clase Alumno
        datos = cargar_jsons(ALUMNOS)
        info = datos[email]
        alumno = Alumno(email, info["nombre"], info["rut"],info["carrera"],info["asignaturas"],info["contrasena"], info["profesores"])
        #Se crea un contenedor por cada asignatura que tenga el estudiante
        for i, asignatura in enumerate(alumno.asignaturas):
            
            #Iran 3 asignaturas por cada fila
            filas = i // 3
            #Sirve para saber en que columa poner la asignatura
            columnas = i % 3
            frame_asignatura = ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.1, height=ALTO*0.25, fg_color="#2b2b2b")
            frame_asignatura.grid(row=filas, column=columnas, sticky="nsew", padx=20, pady=60)
            
            ctk.CTkLabel(frame_asignatura, text=asignatura, font=Fonts.m2bold, wraplength=ANCHO*0.2).place(relx = 0.1, rely=0.15)
            ctk.CTkLabel(frame_asignatura, text=f"Profesor/a: {alumno.profesores[i]}", font=Fonts.i3).place(relx = 0.1, rely=0.5)
            
        num_filas = (len(alumno.asignaturas) + 2) // 3 
        for f in range(num_filas):
            self.frame_inferior.rowconfigure(f, weight=1)
        for c in range(3):
            self.frame_inferior.columnconfigure(c, weight=1)
    
    def cerrar(self):
        self.master.destroy()
