#Ventana que el alumno verá al iniciar sesión correctamente

#Librerias y modulos usados
import customtkinter as ctk
from Utils.utils import MIN_ANCHO, MIN_ALTO, x, y, ANCHO, ALTO
from Utils.funcions import cargar_jsons
from Utils.paths import ALUMNOS
from Clases.alumnos import Alumno
from Ventanas.ventanas_top import VentanaInscribir

#Creación de la ventana que verá el alumno
class VentanaAlumno(ctk.CTkToplevel):
    def __init__(self, email, master):
        super().__init__(master)
        
        #Configuración de la ventana
        self.master = master
        self.email = email
        self.title("Escuelita")
        self.geometry(f"{MIN_ANCHO}x{MIN_ALTO}+{x}+{y}")
        self.minsize(MIN_ANCHO, MIN_ALTO)
        
        #Cargar los datos del estudiante y guardarlos en la clase Alumno
        datos = cargar_jsons(ALUMNOS)
        info = datos[email]
        alumno = Alumno(email, info["nombre"], info["rut"],info["carrera"],info["asignaturas"],info["contrasena"], info["profesores"])
        
        
        #Creando el frame superior (Datos del estudiante)
        frame_superior = ctk.CTkFrame(self, fg_color="#F90808", height=ALTO*0.1)
        frame_superior.pack(fill="both", expand = True)
        
        #Información que irá en la parte superior
        ctk.CTkLabel(frame_superior, text=f"Bienvenido, {alumno.nombre}", font=("Arial", 20)).place(relx=0.02, rely=0.25)
        ctk.CTkLabel(frame_superior, text=f"{alumno.rut}", font=("Arial", 15)).place(relx=0.02, rely=0.6)
        ctk.CTkLabel(frame_superior, text=f"{alumno.carrera}", font=("Arial", 15)).place(relx=0.5, rely=0.4)
        
        ctk.CTkButton(frame_superior, text="Inscribir Asignatura", command=lambda: VentanaInscribir(email)).place(relx=0.8, rely=0.3)
        
        #Creando el frame inferior (DOnde se mostrará las asignaturas del alumno)
        frame_inferior = ctk.CTkScrollableFrame(self, width=ANCHO, height=ALTO*0.9, fg_color="#999999")
        frame_inferior.pack(fill="both", expand=True)
        
        for i in range(len(alumno.asignaturas)):
            filas = i // 3
            columnas = i % 3
            ctk.CTkFrame(frame_inferior, width=ANCHO*0.2, height=ALTO*0.5, fg_color="#ffffff").grid(row=filas, column=columnas, sticky="nsew", padx=20, pady=20)
        
        num_filas = (len(alumno.asignaturas) + 2) // 3 
        for f in range(num_filas):
            frame_inferior.rowconfigure(f, weight=1)
        for c in range(3):
            frame_inferior.columnconfigure(c, weight=1)
        self.protocol("WM_DELETE_WINDOW", self.cerrar)

    def cerrar(self):
        self.master.destroy()
