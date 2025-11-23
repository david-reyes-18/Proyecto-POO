#LIbrerias nesesarias

import customtkinter as ctk
from Utils.utils import MIN_ANCHO, MIN_ALTO, x, y, ANCHO, ALTO
from Utils.funcions import cargar_jsons, eliminar_datos_alumno, eliminar_datos_profesor
from Utils.paths import ADMINISTRADORES, ALUMNOS, ASIGNATURAS, PROFESORES
from Clases.administrador import Admin
from Clases.asignatura import Asignatura
from Ventanas.ventanas_top import VentanaDatosAlumno, VentanaMatricula, VentanaAñadirAsignatura, VisualizarAlumnosProfes, VentanaDatosProfesor, VentanaAñadirProfe, VentanaAsignacion
from Utils.fonts import Fonts

#La ventana que verá el administrador después de haber iniciado sesión
class VentanaAdmin(ctk.CTkToplevel):
    def __init__(self, email, master):
        super().__init__(master)
        
        #Configuración de la pantalla
        self.master = master
        self.email = email
        self.title("Administración del Instituto Epsilon")
        self.geometry(f"{MIN_ANCHO}x{MIN_ALTO}+{x}+{y}")
        self.minsize(MIN_ANCHO, MIN_ALTO)
        
        #Se cargar las fuentes para el texto
        Fonts.cargar()
        
        #Se llama a la función que tiene la ventana de inicio que verá el administrador
        self.ventana_principal()
        
    #       Ventana de inicio del administrador (para visualizar, crear y eliminar estudiantes, profesores y asigaturas)
    def ventana_principal(self):
        
        #Se limpia la ventana
        self.limpiar()
        
        #Se cargan los datos del administrador
        datos = cargar_jsons(ADMINISTRADORES)
        info = datos[self.email]
        
        #Creando al administrador
        admin = Admin(self.email, info["nombre"], info["rut"], info["contrasena"])
        
        #Creando el frame superior (Datos del admin)
        self.frame_superior = ctk.CTkFrame(self, fg_color="#2b2b2b", height=ALTO*0.1)
        self.frame_superior.pack(fill="both", expand=True)

        #Información que irá en la parte superior
        ctk.CTkLabel(self.frame_superior, text=f"Bienvenido admin {admin.nombre}", font=Fonts.m2bold).place(relx=0.02, rely=0.15)
        ctk.CTkLabel(self.frame_superior, text=f"{admin.rut}", font=Fonts.i3).place(relx=0.02, rely=0.6)
        
        
        #       Creando el frame inferior (En donde se verá las pestañas de alumnos, profesores y asignaturas)
        self.frame_inferior = ctk.CTkScrollableFrame(self, width=ANCHO, height=ALTO*0.9, fg_color="#1b1b1b", border_width=2, border_color="#000000")
        self.frame_inferior.pack(fill="both", expand=True)
        
        #       Frame de los alumnos
        frame_alumnos = ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.4, height=ALTO*0.45, border_width=2, border_color="#ffffff")
        frame_alumnos.grid(row=0, column=0, padx=20, pady=120)
            
        ctk.CTkLabel(frame_alumnos, text="Estudiantes", font=Fonts.m2).place(relx=0.5, rely=0.2, anchor="center")
        ctk.CTkLabel(frame_alumnos, text="Aquí se podrá visualizar la información de todos los estudiantes matriculados dentro del instituto.", wraplength=ANCHO*0.17, font=Fonts.i3, justify="center").place(relx=0.5, rely=0.5, anchor="center")
            
        ctk.CTkButton(frame_alumnos, text="Ver Alumnos", command=self.mostrar_alumnos, font=Fonts.m3).place(relx=0.5, rely= 0.8, anchor="center")
            
        #       Frame de los profesores
        frame_profes = ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.4, height=ALTO*0.45, border_width=2, border_color="white")
        frame_profes.grid(row=0, column=1, padx=20, pady=120)
            
        ctk.CTkLabel(frame_profes, text="Profesores", font=Fonts.m2).place(relx=0.5, rely=0.2, anchor="center")
        ctk.CTkLabel(frame_profes, text="Aquí se podrá visualizar la información de todos los profesores que imparten clases dentro del instituto.", wraplength=ANCHO*0.17, font=Fonts.i3).place(relx=0.5, rely=0.5, anchor="center")
            
        ctk.CTkButton(frame_profes, text="Ver Profesores", command=self.mostrar_profesores, font=Fonts.m3).place(relx=0.5, rely= 0.8, anchor="center")
            
        #       Frame de las asignaturas
        frame_asignaturas = ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.4, height=ALTO*0.45, border_width=2, border_color="white")
        frame_asignaturas.grid(row=0, column=2, padx=20, pady=120)
            
        ctk.CTkLabel(frame_asignaturas, text="Asignaturas", font=Fonts.m2).place(relx=0.5, rely=0.2, anchor="center")
        ctk.CTkLabel(frame_asignaturas, text="Aquí se podrá visualizar todas las asignaturas que se imparten dentro del instituto.", wraplength=ANCHO*0.17, font=Fonts.i3).place(relx=0.5, rely=0.5, anchor="center")
            
        ctk.CTkButton(frame_asignaturas, text="Ver Asignaturas", command=self.mostrar_asignaturas, font=Fonts.m3).place(relx=0.5, rely= 0.8, anchor="center")
            
        #Configurar los frames y hacerlos responsive
        for c in range(3):
            self.frame_inferior.columnconfigure(c, weight=1)
        self.frame_inferior.rowconfigure(0, weight=1)
            
        self.protocol("WM_DELETE_WINDOW", self.cerrar)


    #Ventana que mostrará a los alumnos de todo el instituto en orden alfabetico, además permite ver datos, eliminar y matricular estudiante
    def mostrar_alumnos(self):
        
        #Se limpia el frame
        self.limpiar_widgets()
        
        #Cargar datos de todos los estudiantes
        datos_alumnos = cargar_jsons(ALUMNOS)
        
        #Boton de matricular
        ctk.CTkButton(self.frame_superior, text="Matricular", command=VentanaMatricula, font=Fonts.m3).place(relx=0.85, rely=0.3)
        
        #       Listado de alumnos
        ctk.CTkLabel(self.frame_inferior, text="Listado de Alumnos", font=Fonts.m2).place(relx=0.5, rely=0.1, anchor="center")
        
        self.frame = ctk.CTkFrame(self.frame_inferior, fg_color="#2b2b2b", width=ANCHO*0.6, height=ALTO*0.4)
        self.frame.pack(pady=100)
        
        #Se ordenan los alumnos en orden alfabetico
        total_alumnos = sorted(datos_alumnos.items(), key=lambda x: x[1]["nombre"])
        #Se guarda la informacion de cada estudiante en una tupla de (nombre estudiante, email estudiante)
        total_alumnos = [(info["nombre"], email) for email, info in total_alumnos]

        #Boton para volver a la ventana principal
        ctk.CTkButton(self.frame_inferior, text="Volver", command=self.volver).place(relx=0.01, rely=0.05)
        
        #Se hace el listado de los alumnos
        for i, (nombre, email) in enumerate(total_alumnos, start=1):
            
            #Por cada alumno se crea un contenedor nuevo que contiene la información de los alumnos
            contenedor = ctk.CTkFrame(self.frame, height=ALTO*0.05, width=ANCHO*0.68, border_width=1, border_color="black")
            contenedor.pack(fill="x")
            
            #información de los alumnos
            ctk.CTkLabel(contenedor, text=f"{i}.-", font=Fonts.i3).place(relx=0.01, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{nombre}", font=Fonts.i3).place(relx=0.03, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{email}", font=Fonts.i3).place(relx=0.3, rely=0.2)
            
            #Botones de ver datos y eliminar alumnos
            ctk.CTkButton(contenedor, text="Ver Datos", command=lambda e=email: VentanaDatosAlumno(e), font=Fonts.m3).place(relx=0.7, rely=0.2)
            ctk.CTkButton(contenedor, text="Eliminar", command=lambda e=email: self.recargar_alumnos(e), font=Fonts.m3).place(relx=0.85, rely=0.2)

    #Ventana que muestra todos los prodesores, en el cual se puede añadir profesores, eliminar, ver datos y asignar a un profesor una asignatura
    def mostrar_profesores(self):
        
        #Se limpia el frame principal
        self.limpiar_widgets()
        
        #Se cargan todos los datos de los profesores de la base de datos para mostrarlos
        datos_profesores = cargar_jsons(PROFESORES)
        
        #Se crean los botones para añadir y asignar profesores
        ctk.CTkButton(self.frame_superior, text="Añadir Profesor", command=VentanaAñadirProfe, font=Fonts.m3).place(relx=0.7, rely=0.3)
        ctk.CTkButton(self.frame_superior, text="Asignar Profesor", command=VentanaAsignacion, font=Fonts.m3).place(relx=0.85, rely=0.3)
        
        #Listado de profesores
        ctk.CTkLabel(self.frame_inferior, text="Listado de Profesores", font=Fonts.m2).place(relx=0.5, rely=0.1, anchor="center")
        
        self.frame = ctk.CTkFrame(self.frame_inferior, fg_color="#2b2b2c", width=ANCHO*0.6, height=ALTO*0.4)
        self.frame.pack(pady=100)
        
        #Se ordenan los profesores en orden alfabetico
        total_profesores = sorted(datos_profesores.items(), key=lambda x: x[1]["nombre"])
        
        #Se guarda una tupla con (nombre profesor, email profesor) para cada profesor
        total_profesores = [(info["nombre"], email) for email, info in total_profesores]

        #Boton para volver a la ventana principal
        ctk.CTkButton(self.frame_inferior, text="Volver", command=self.volver).place(relx=0.01, rely=0.05)
        
        #Se hace el listado de profesores
        for i, (nombre, email) in enumerate(total_profesores, start=1):
            
            #Por cada profesor se creará un nuevo contenedor
            contenedor = ctk.CTkFrame(self.frame, height=ALTO*0.05, width=ANCHO*0.68, border_width=1, border_color="black")
            contenedor.pack(fill="x")
            
            #Se muestra la información básica del profesor
            ctk.CTkLabel(contenedor, text=f"{i}.-", font=Fonts.i3).place(relx=0.01, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{nombre}", font=Fonts.i3).place(relx=0.03, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{email}", font=Fonts.i3).place(relx=0.3, rely=0.2)
            
            #Botones par ver información y eliminar profesores del sistema
            ctk.CTkButton(contenedor, text="Ver Datos", command=lambda e=email: VentanaDatosProfesor(e), font=Fonts.m3).place(relx=0.7, rely=0.2)
            ctk.CTkButton(contenedor, text="Eliminar", command=lambda e=email: self.recargar_profesores(e), font=Fonts.m3).place(relx=0.85, rely=0.2)
    
    #Funcion la cual al cerrar una CTkTopLevel cierra todo el programa
    def cerrar(self):
        self.master.destroy()
    
    #Función que regresa a la ventana principal del administrador
    def volver(self):
        self.ventana_principal()
    
    #Función que limpia toda la ventana
    def limpiar(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    #Función que limpia el frame inferior
    def limpiar_widgets(self):
        for widget in self.frame_inferior.winfo_children():
            widget.destroy()

    
    def recargar_alumnos(self, email):
        eliminar_datos_alumno(email)
        self.mostrar_alumnos()
        
    def recargar_profesores(self, email):
        eliminar_datos_profesor(email)
        self.mostrar_profesores()
    
    def mostrar_asignaturas(self):
        self.limpiar_widgets()
        datos = cargar_jsons(ASIGNATURAS)
        asignaturas = [asignatura for asignatura in datos]
            
        ctk.CTkButton(self.frame_superior, text="Añadir Asignatura", command=VentanaAñadirAsignatura).place(relx=0.8, rely=0.3)
        
        ctk.CTkButton(self.frame_inferior, text="Volver", command=self.volver).place(relx=0.01, rely=0.01)
        
        for i, asignatura in enumerate(asignaturas):
            ramo = Asignatura(asignatura, datos[asignatura]["estudiantes"], datos[asignatura]["profesores"], datos[asignatura]["cantidad_estudiantes"])
            
            filas = i // 3
            columnas = i % 3
            
            frame_asignatura = ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.2, height=ALTO*0.5, fg_color="#ffffff")
            frame_asignatura.grid(row=filas, column=columnas, sticky="nsew", padx=20, pady=50)
            ctk.CTkLabel(frame_asignatura, text=ramo.nombre).place(relx = 0.3, rely=0.1)
            ctk.CTkLabel(frame_asignatura, text=f"Cantidad Alumnos: {ramo.cantidad_estudiantes}").place(relx = 0.3, rely=0.3)
            ctk.CTkButton(frame_asignatura, text="Ver Alumnos", command=lambda: VisualizarAlumnosProfes("alumno")).place(relx=0.6, rely=0.8)
            ctk.CTkButton(frame_asignatura, text="Ver Profesores", command=lambda: VisualizarAlumnosProfes("profesor")).place(relx=0.8, rely=0.8)
        
        num_filas = (len(datos) + 2) // 3 
        for f in range(num_filas):
            self.frame_inferior.rowconfigure(f, weight=1)
        for c in range(3):
            self.frame_inferior.columnconfigure(c, weight=1)
        
    
    