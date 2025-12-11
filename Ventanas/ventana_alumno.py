#Ventana que el alumno verá al iniciar sesión correctamente

#Librerias y modulos usados
import customtkinter as ctk
from Utils.utils import MIN_ANCHO, MIN_ALTO, x, y, ANCHO, ALTO, COLOR_FONTS, COLOR_AZUL, COLOR_FONDO, img_epsilon
from Utils.functions import cargar_jsons
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
        nombre_alumno = f"{info['nombre'].split(" ")[0]} {info['nombre'].split(" ")[2]}" if len(info['nombre'].split(" ")) == 4 else f"{info['nombre'].split(" ")[0]} {info['nombre'].split(" ")[3]}"
        alumno = Alumno(email, info["nombre"], info["rut"],info["carrera"],info["asignaturas"],info["contrasena"], info["profesores"], info["semestre"])
        
        
        #Creando el frame superior (Datos del estudiante)
        frame_superior = ctk.CTkFrame(self, fg_color=COLOR_FONDO, height=ALTO*0.16, border_width=1, border_color=COLOR_FONTS)
        frame_superior.pack(fill="both", expand = True)
        
        #Información que irá en la parte superior
        ctk.CTkLabel(frame_superior, text=f"Bienvenido, {nombre_alumno}", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.02, rely=0.15)
        ctk.CTkLabel(frame_superior, text=f"{alumno.rut}", font=Fonts.i2, text_color=COLOR_FONTS).place(relx=0.02, rely=0.6)
        ctk.CTkLabel(frame_superior, text=f"{alumno.carrera}", font=Fonts.i2, text_color=COLOR_FONTS).place(relx=0.5, rely=0.7, anchor="center")
        
        ctk.CTkButton(frame_superior, text="Inscribir Asignatura", command=lambda: VentanaInscribir(email, self), font=Fonts.m2bold, text_color=COLOR_FONTS, border_width=2, border_color=COLOR_FONTS, fg_color=COLOR_FONDO, hover_color=COLOR_AZUL).place(relx=0.65, rely=0.3)
        
        ctk.CTkLabel(frame_superior, image=img_epsilon, text="", fg_color="transparent").place(relx=0.95, rely=0.5, anchor="center")
        
        #Creando el frame inferior (Donde se mostrará las asignaturas del alumno)
        self.frame_inferior = ctk.CTkScrollableFrame(self, width=ANCHO, height=ALTO*0.86, fg_color=COLOR_AZUL, border_width=1, border_color=COLOR_FONTS)
        self.frame_inferior.pack(fill="both", expand=True)
        
        
        self.frame_superior1 = ctk.CTkFrame(self.frame_inferior, fg_color=COLOR_AZUL, height=MIN_ALTO*0.1)
        self.frame_superior1.pack(fill="x", expand=True)

        ctk.CTkLabel(self.frame_superior1, text="Mis asignaturas", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.5, rely=0.5, anchor="center")
        
        self.frame_inferior1 = ctk.CTkFrame(self.frame_inferior, fg_color=COLOR_AZUL, height=MIN_ALTO*0.9)
        self.frame_inferior1.pack(fill="x", expand=True)
        
        
        self.mostrar_asignaturas(email)
        

        self.protocol("WM_DELETE_WINDOW", self.cerrar)


    def mostrar_asignaturas(self, email):
        #Cargar los datos del estudiante y guardarlos en la clase Alumno
        datos = cargar_jsons(ALUMNOS)
        info = datos[email]
        alumno = Alumno(email, info["nombre"], info["rut"],info["carrera"],info["asignaturas"],info["contrasena"], info["profesores"], info["semestre"])
        #Se crea un contenedor por cada asignatura que tenga el estudiante
        for i, asignatura in enumerate(alumno.asignaturas):
            
            #Iran 3 asignaturas por cada fila
            filas = i // 3
            #Sirve para saber en que columa poner la asignatura
            columnas = i % 3
            frame_asignatura = ctk.CTkFrame(self.frame_inferior1, width=ANCHO*0.1, height=ALTO*0.2, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, border_width=2)
            frame_asignatura.grid(row=filas, column=columnas, sticky="nsew", padx=20, pady=60)
            
            ctk.CTkLabel(frame_asignatura, text=asignatura, font=Fonts.m2bold, wraplength=ANCHO*0.2, text_color=COLOR_FONTS).place(relx = 0.1, rely=0.15)
            ctk.CTkLabel(frame_asignatura, text=f"Profesor/a: {alumno.profesores[i]}", font=Fonts.i3, text_color=COLOR_FONTS).place(relx = 0.1, rely=0.5)
            
        num_filas = (len(alumno.asignaturas) + 2) // 3 
        for f in range(num_filas):
            self.frame_inferior1.rowconfigure(f, weight=1)
        for c in range(3):
            self.frame_inferior1.columnconfigure(c, weight=1)
    
    def cerrar(self):
        self.master.destroy()
