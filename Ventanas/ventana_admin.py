#LIbrerias nesesarias

import customtkinter as ctk
from Utils.utils import MIN_ANCHO, MIN_ALTO, x, y, ANCHO, ALTO, COLOR_FONDO, COLOR_AZUL, COLOR_FONTS, img_epsilon, img_volver
from Utils.functions import cargar_jsons, eliminar_datos_alumno, eliminar_datos_profesor, eliminar_datos_asignatura
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
        self.frame_superior = ctk.CTkFrame(self, fg_color=COLOR_FONDO, height=ALTO*0.16, border_width=2, border_color=COLOR_FONTS)
        self.frame_superior.pack(fill="x", expand=True)

        #Información que irá en la parte superior
        ctk.CTkLabel(self.frame_superior, text=f"Bienvenido admin {admin.nombre}", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.02, rely=0.12)
        ctk.CTkLabel(self.frame_superior, text=f"{admin.rut}", font=Fonts.i2, text_color=COLOR_FONTS).place(relx=0.02, rely=0.6)
        
        
        ctk.CTkLabel(self.frame_superior, text="", image=img_epsilon).place(relx=0.95, rely=0.5, anchor="center")
        
        
        #       Creando el frame inferior (En donde se verá las pestañas de alumnos, profesores y asignaturas)
        self.frame_inferior = ctk.CTkScrollableFrame(self, width=ANCHO, height=ALTO*0.84, border_width=2, border_color=COLOR_FONTS, fg_color=COLOR_AZUL, scrollbar_button_color=COLOR_FONTS, scrollbar_button_hover_color=COLOR_FONDO)
        self.frame_inferior.pack(fill="both", expand=True)
        
        #       Frame de los alumnos
        frame_alumnos = ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.4, height=MIN_ALTO*0.7, border_width=2, border_color=COLOR_FONTS, fg_color=COLOR_FONDO, corner_radius=15)
        frame_alumnos.grid(row=0, column=0, padx=20, pady=40)
            
        ctk.CTkLabel(frame_alumnos, text="Estudiantes", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.5, rely=0.2, anchor="center")
        ctk.CTkLabel(frame_alumnos, text="Aquí se podrá visualizar la información de todos los estudiantes matriculados dentro del instituto.", wraplength=ANCHO*0.17, font=Fonts.i2, justify="center", text_color=COLOR_FONTS).place(relx=0.5, rely=0.5, anchor="center")
            
        ctk.CTkButton(frame_alumnos, text="Ver Alumnos", command=self.mostrar_alumnos, font=Fonts.m2bold, corner_radius=15, border_width=2, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, text_color=COLOR_FONTS, hover_color=COLOR_AZUL).place(relx=0.5, rely= 0.8, anchor="center")
            
        #       Frame de los profesores
        frame_profes = ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.4, height=MIN_ALTO*0.7, border_width=2, border_color=COLOR_FONTS, fg_color=COLOR_FONDO, corner_radius=15)
        frame_profes.grid(row=0, column=1, padx=20, pady=40)
            
        ctk.CTkLabel(frame_profes, text="Profesores", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.5, rely=0.2, anchor="center")
        ctk.CTkLabel(frame_profes, text="Aquí se podrá visualizar la información de todos los profesores que imparten clases dentro del instituto.", wraplength=ANCHO*0.17, font=Fonts.i2, text_color=COLOR_FONTS).place(relx=0.5, rely=0.5, anchor="center")
            
        ctk.CTkButton(frame_profes, text="Ver Profesores", command=self.mostrar_profesores, font=Fonts.m2bold, corner_radius=15, border_width=2, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, text_color=COLOR_FONTS, hover_color=COLOR_AZUL).place(relx=0.5, rely= 0.8, anchor="center")
            
        #       Frame de las asignaturas
        frame_asignaturas = ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.4, height=MIN_ALTO*0.7, border_width=2, border_color=COLOR_FONTS, fg_color=COLOR_FONDO, corner_radius=15)
        frame_asignaturas.grid(row=0, column=2, padx=20, pady=40)
            
        ctk.CTkLabel(frame_asignaturas, text="Asignaturas", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.5, rely=0.2, anchor="center")
        ctk.CTkLabel(frame_asignaturas, text="Aquí se podrá visualizar todas las asignaturas que se imparten dentro del instituto.", wraplength=ANCHO*0.17, font=Fonts.i2, text_color=COLOR_FONTS).place(relx=0.5, rely=0.5, anchor="center")
            
        ctk.CTkButton(frame_asignaturas, text="Ver Asignaturas", command=self.mostrar_asignaturas, font=Fonts.m2bold, corner_radius=15, border_width=2, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, text_color=COLOR_FONTS, hover_color=COLOR_AZUL).place(relx=0.5, rely= 0.8, anchor="center")
            
        #Configurar los frames y hacerlos responsive
        for c in range(3):
            self.frame_inferior.columnconfigure(c, weight=1)
        self.frame_inferior.rowconfigure(0, weight=1)
        
        def scroll(event):
            try:
                #Accerder al scroll
                canvas =    self.frame_inferior._parent_canvas  

                #       Scroll tanto para Windows, MacOS y Linux
                
                #Si el scroll es positivo (en caso de Linux el scroll hacia arriba se considera el boton 4), se realiza el scroll
                if event.num == 4 or event.delta > 0:
                    canvas.yview_scroll(-1, "units")
                    
                #Si el scroll es negativo (en caso de Linux el scroll hacia abajo se considera el boton 5), se realiza el scroll
                elif event.num == 5 or event.delta < 0:
                    canvas.yview_scroll(1, "units")
            except Exception:
                pass
                
        
        #Scroll para Windows y MacOS
        self.frame_inferior.bind_all("<MouseWheel>", scroll)
        
        #Scroll para Linux
        self.frame_inferior.bind_all("<Button-4>", scroll)
        self.frame_inferior.bind_all("<Button-5>", scroll)  
            
        self.protocol("WM_DELETE_WINDOW", self.cerrar)


    #Ventana que mostrará a los alumnos de todo el instituto en orden alfabetico, además permite ver datos, eliminar y matricular estudiante
    def mostrar_alumnos(self):
        
        #Se limpia el frame
        self.limpiar_widgets()
        
        #Cargar datos de todos los estudiantes
        datos_alumnos = cargar_jsons(ALUMNOS)
        
        #Boton de matricular
        ctk.CTkButton(self.frame_superior, text="Matricular", command=lambda: VentanaMatricula(master=self), font=Fonts.m2bold, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, hover_color=COLOR_AZUL, border_width=2, border_spacing=3, border_color=COLOR_FONTS).place(relx=0.75, rely=0.3)
        
        #       Listado de alumnos
        ctk.CTkLabel(self.frame_inferior, text="Listado de Alumnos", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.5, rely=0.07, anchor="center")
        
        self.frame = ctk.CTkFrame(self.frame_inferior, fg_color=COLOR_FONDO, width=ANCHO*0.6, height=ALTO*0.4)
        self.frame.pack(pady=120)
        
        #Se ordenan los alumnos en orden alfabetico
        total_alumnos = sorted(datos_alumnos.items(), key=lambda x: x[1]["nombre"])
        #Se guarda la informacion de cada estudiante en una tupla de (nombre estudiante, email estudiante)
        total_alumnos = [(info["nombre"], email) for email, info in total_alumnos]

        #Boton para volver a la ventana principal
        ctk.CTkButton(self.frame_inferior, text="", command=self.volver, image=img_volver, fg_color="transparent", hover_color=COLOR_AZUL).place(relx=0.01, rely=0.02)
        
        #Se hace el listado de los alumnos
        for i, (nombre, email) in enumerate(total_alumnos, start=1):
            
            #Por cada alumno se crea un contenedor nuevo que contiene la información de los alumnos
            contenedor = ctk.CTkFrame(self.frame, height=ALTO*0.05, width=ANCHO*0.68, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
            contenedor.pack(fill="x")
            
            #información de los alumnos
            ctk.CTkLabel(contenedor, text=f"{i}.-", font=Fonts.i3, text_color=COLOR_FONTS).place(relx=0.01, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{nombre}", font=Fonts.i3, text_color=COLOR_FONTS).place(relx=0.035, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{email}", font=Fonts.i3, text_color=COLOR_FONTS).place(relx=0.31, rely=0.2)
            
            #Botones de ver datos y eliminar alumnos
            ctk.CTkButton(contenedor, text="Ver Datos", command=lambda e=email: VentanaDatosAlumno(e), font=Fonts.m3, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, border_width=2, hover_color=COLOR_AZUL).place(relx=0.7, rely=0.2)
            ctk.CTkButton(contenedor, text="Eliminar", command=lambda e=email: self.recargar_alumnos(e), font=Fonts.m3, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, border_width=2, hover_color=COLOR_AZUL).place(relx=0.85, rely=0.2)


    #Ventana que muestra todos los prodesores, en el cual se puede añadir profesores, eliminar, ver datos y asignar a un profesor una asignatura
    def mostrar_profesores(self):
        
        #Se limpia el frame principal
        self.limpiar_widgets()
        
        #Se cargan todos los datos de los profesores de la base de datos para mostrarlos
        datos_profesores = cargar_jsons(PROFESORES)
        
        #Se crean los botones para añadir y asignar profesores
        ctk.CTkButton(self.frame_superior, text="Añadir Profesor", command=lambda: VentanaAñadirProfe(master=self), font=Fonts.m3).place(relx=0.7, rely=0.3)
        ctk.CTkButton(self.frame_superior, text="Asignar Profesor", command=VentanaAsignacion, font=Fonts.m3).place(relx=0.85, rely=0.3)
        
        #Listado de profesores
        ctk.CTkLabel(self.frame_inferior, text="Listado de Profesores", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.5, rely=0.07, anchor="center")
        
        self.frame = ctk.CTkFrame(self.frame_inferior, fg_color=COLOR_FONDO, width=ANCHO*0.6, height=ALTO*0.4)
        self.frame.pack(pady=120)
        
        #Se ordenan los profesores en orden alfabetico
        total_profesores = sorted(datos_profesores.items(), key=lambda x: x[1]["nombre"])
        
        #Se guarda una tupla con (nombre profesor, email profesor) para cada profesor
        total_profesores = [(info["nombre"], email) for email, info in total_profesores]

        #Boton para volver a la ventana principal
        ctk.CTkButton(self.frame_inferior, text="", command=self.volver, image=img_volver, fg_color="transparent", hover_color=COLOR_AZUL).place(relx=0.01, rely=0.02)  
        
        #Se hace el listado de profesores
        for i, (nombre, email) in enumerate(total_profesores, start=1):
            
            #Por cada profesor se creará un nuevo contenedor
            contenedor = ctk.CTkFrame(self.frame, height=ALTO*0.05, width=ANCHO*0.68, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
            contenedor.pack(fill="x")
            
            #Se muestra la información básica del profesor
            ctk.CTkLabel(contenedor, text=f"{i}.-", font=Fonts.i3, text_color=COLOR_FONTS).place(relx=0.01, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{nombre}", font=Fonts.i3, text_color=COLOR_FONTS).place(relx=0.035, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{email}", font=Fonts.i3, text_color=COLOR_FONTS).place(relx=0.31, rely=0.2)
            
            #Botones par ver información y eliminar profesores del sistema
            ctk.CTkButton(contenedor, text="Ver Datos", command=lambda e=email: VentanaDatosProfesor(e), font=Fonts.m3, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, border_width=2, hover_color=COLOR_AZUL).place(relx=0.7, rely=0.2)
            ctk.CTkButton(contenedor, text="Eliminar", command=lambda e=email: self.recargar_profesores(e), font=Fonts.m3, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, border_width=2, hover_color=COLOR_AZUL).place(relx=0.85, rely=0.2)
    
    
    #Ventana que mostrará las asignaturas totales que se imparten en el instituto, donde se podrá visualizar, añadir y eliminar asignaturas
    def mostrar_asignaturas(self):
        
        #Se limpia el espacio donde se verán las asignaturas
        self.limpiar_widgets()
        
        #Se cargan los datos de todas las asignaturas
        datos = cargar_jsons(ASIGNATURAS)
        
        #Enlistar todas las asignaturas que estan en el sistema
        asignaturas = [asignatura for asignatura in datos]
            
        #Boton para añadir asignaturas
        ctk.CTkButton(self.frame_superior, text="Añadir Asignatura", command=lambda: VentanaAñadirAsignatura(master=self), font=Fonts.m3).place(relx=0.8, rely=0.3)
        #Boton para volver a la ventana principal
        ctk.CTkButton(self.frame_inferior, text="Volver", command=self.volver).place(relx=0.01, rely=0.01)
        
        #Se crea un contenedor por cada asignatura en la lista
        for i, asignatura in enumerate(asignaturas):
            #Por cada asignatura se crea un objeto asignatura
            ramo = Asignatura(asignatura, datos[asignatura]["estudiantes"], datos[asignatura]["profesores"], datos[asignatura]["cantidad_estudiantes"])
            
            #Irán 3 asignaturas por fila
            filas = i // 3
            #Sabe en que columna poner
            columnas = i % 3
            
            #Contenedor de la información 
            frame_asignatura = ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.1, height=ALTO*0.3, fg_color="#2b2b2b")
            frame_asignatura.grid(row=filas, column=columnas, sticky="nsew", padx=20, pady=60)
            
            #Información de la asignatura del alumno
            ctk.CTkLabel(frame_asignatura, text=ramo.nombre, font=Fonts.m2bold, wraplength=ANCHO*0.2).place(relx = 0.1, rely=0.15)
            ctk.CTkLabel(frame_asignatura, text=f"Cantidad Alumnos: {ramo.cantidad_estudiantes}", font=Fonts.i2).place(relx = 0.1, rely=0.5)
            
            #Boton para ver alumnos de la asignatura, para ver
            ctk.CTkButton(frame_asignatura, text="Ver Alumnos", command=lambda a=asignatura: VisualizarAlumnosProfes("alumno", a), font=Fonts.m4).place(relx=0.05, rely=0.8)
            ctk.CTkButton(frame_asignatura, text="Ver Profesores", command=lambda a=asignatura: VisualizarAlumnosProfes("profesor", a), font=Fonts.m4).place(relx=0.34, rely=0.8)
            ctk.CTkButton(frame_asignatura, text="Eliminar", command=lambda a=asignatura: self.recargar_asignaturas(a), font=Fonts.m4).place(relx=0.72, rely=0.8)
        
        num_filas = (len(datos) + 2) // 3 
        for f in range(num_filas):
            self.frame_inferior.rowconfigure(f, weight=1)
        for c in range(3):
            self.frame_inferior.columnconfigure(c, weight=1)
            
        def scroll(event):
            #Accerder al scroll
            canvas = self.frame_inferior._parent_canvas  

            #       Scroll tanto para Windows, MacOS y Linux
            
            #Si el scroll es positivo (en caso de Linux el scroll hacia arriba se considera el boton 4), se realiza el scroll
            if event.num == 4 or event.delta > 0:
                canvas.yview_scroll(-1, "units")
                
            #Si el scroll es negativo (en caso de Linux el scroll hacia abajo se considera el boton 5), se realiza el scroll
            elif event.num == 5 or event.delta < 0:
                canvas.yview_scroll(1, "units")
        
        #Scroll para Windows y MacOS
        self.frame_inferior.bind_all("<MouseWheel>", scroll)
        
        #Scroll para Linux
        self.frame_inferior.bind_all("<Button-4>", scroll)
        self.frame_inferior.bind_all("<Button-5>", scroll)  
    
    
    
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

    #Se eliminan los datos del alumnno y se recarga la ventana de alumnos
    def recargar_alumnos(self, email):
        eliminar_datos_alumno(email)
        self.mostrar_alumnos()
    
    #Se eliminan los datos de lo profesore y se recarga la ventana de profesores 
    def recargar_profesores(self, email):
        eliminar_datos_profesor(email)
        self.mostrar_profesores()
    
    #Se eliminan los datos de la asignatura y se recarga la ventana de asignaturas
    def recargar_asignaturas(self, asignatura):
        eliminar_datos_asignatura(asignatura)
        self.mostrar_asignaturas()
    
    