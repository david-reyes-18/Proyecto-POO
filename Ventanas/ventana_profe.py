#Ventana que el alumno verá al iniciar sesión correctamente

#Librerias y modulos usados
import customtkinter as ctk
from Utils.utils import MIN_ANCHO, MIN_ALTO, x, y, ANCHO, ALTO, img_epsilon, COLOR_AZUL, COLOR_FONDO, COLOR_FONTS
from Utils.functions import cargar_jsons
from Utils.paths import PROFESORES
from Utils.fonts import Fonts
from Clases.profesor import Profesor
from Ventanas.ventanas_top import VentanaVerAlumnos

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
        nombre_profe = f"{info['nombre'].split(" ")[0]} {info['nombre'].split(" ")[2]}" if len(info['nombre'].split(" ")) == 4 else f"{info['nombre'].split(" ")[0]} {info['nombre'].split(" ")[3]}"
        
        profesor = Profesor(email, info["nombre"], info["rut"], info["asignaturas"], info["contrasena"], info["alumnos"])
        
        
        #Creando el frame superior (Datos del estudiante)
        frame_superior = ctk.CTkFrame(self, fg_color=COLOR_FONDO, height=ALTO*0.16, border_color=COLOR_FONTS, border_width=2)
        frame_superior.pack(fill="both", expand = True)
        
        ctk.CTkLabel(frame_superior, image=img_epsilon, text="", fg_color="transparent").place(relx=0.95, rely=0.5, anchor="center")
        
        #Información que irá en la parte superior
        ctk.CTkLabel(frame_superior, text=f"Bienvenido Profe {nombre_profe}", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.02, rely=0.15)
        ctk.CTkLabel(frame_superior, text=f"{profesor.rut}", font=Fonts.i1, text_color=COLOR_FONTS).place(relx=0.02, rely=0.6)
        
        
        #Creando el frame inferior (Donde se mostrará las asignaturas que imparte el profesor)
        self.frame_inferior = ctk.CTkScrollableFrame(self, width=ANCHO, height=ALTO*0.85, fg_color=COLOR_AZUL)
        self.frame_inferior.pack(fill="both", expand=True)
        
        self.frame_superior1 = ctk.CTkFrame(self.frame_inferior, fg_color=COLOR_AZUL, height=MIN_ALTO*0.1)
        self.frame_superior1.pack(fill="x", expand=True)

        ctk.CTkLabel(self.frame_superior1, text="Mis asignaturas impartidas", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.5, rely=0.5, anchor="center")
        
        self.frame_inferior1 = ctk.CTkFrame(self.frame_inferior, fg_color=COLOR_AZUL, height=MIN_ALTO*0.9)
        self.frame_inferior1.pack(fill="x", expand=True)
        
        self.mostrar_asignaturas(email)

        self.protocol("WM_DELETE_WINDOW", self.cerrar)


    def mostrar_asignaturas(self, email):
        #Cargar los datos del estudiante y guardarlos en la clase Alumno
        datos = cargar_jsons(PROFESORES)
        info = datos[email]
        profe = Profesor(email, info["nombre"], info["rut"], info["asignaturas"], info["contrasena"], info["alumnos"])
        #Se crea un contenedor por cada asignatura que tenga el estudiante
        for i, asignatura in enumerate(profe.asignaturas):
            #Iran 3 asignaturas por cada fila
            filas = i // 3
            #Sirve para saber en que columa poner la asignatura
            columnas = i % 3
            
            cantidad_alumnos = 0
            
            for alumno in profe.alumnos:
                if alumno.split(",")[1] == asignatura:
                    cantidad_alumnos += 1
            
            frame_asignatura = ctk.CTkFrame(self.frame_inferior1, width=ANCHO*0.1, height=ALTO*0.2, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
            frame_asignatura.grid(row=filas, column=columnas, sticky="nsew", padx=20, pady=60)
            
            ctk.CTkLabel(frame_asignatura, text=asignatura, font=Fonts.m2bold, wraplength=ANCHO*0.2, text_color=COLOR_FONTS).place(relx = 0.1, rely=0.15)
            ctk.CTkLabel(frame_asignatura, text=f"Alumnos Inscritos: {cantidad_alumnos}", font=Fonts.i3, text_color=COLOR_FONTS).place(relx = 0.1, rely=0.5)
            ctk.CTkButton(frame_asignatura, text="Ver Alumnos", font=Fonts.m3, command=lambda e=email, a=asignatura: VentanaVerAlumnos(e, a), fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS, text_color=COLOR_FONTS, hover_color=COLOR_AZUL).place(rely=0.7, relx=0.6)
            
        num_filas = (len(profe.asignaturas) + 2) // 3 
        for f in range(num_filas):
            self.frame_inferior1.rowconfigure(f, weight=1)
        for c in range(3):
            self.frame_inferior1.columnconfigure(c, weight=1)
                
    def cerrar(self):
        self.master.destroy()
