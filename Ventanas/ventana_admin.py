import customtkinter as ctk
from Utils.utils import MIN_ANCHO, MIN_ALTO, x, y, ANCHO, ALTO
from Utils.funcions import cargar_jsons, eliminar_datos
from Utils.paths import ADMINISTRADORES, ALUMNOS, ASIGNATURAS, PROFESORES
from Clases.administrador import Admin
from Clases.asignatura import Asignatura
from Ventanas.ventanas_top import VentanaDatosAlumno, VentanaMatricula, VentanaAñadirAsignatura, VisualizarAlumnosProfes, VentanaDatosProfesor, VentanaAñadirProfe, VentanaAsignacion

class VentanaAdmin(ctk.CTkToplevel):
    def __init__(self, email, master):
        super().__init__(master)
        self.master = master
        self.email = email
        self.title("Administración de Escuelita")
        self.geometry(f"{MIN_ANCHO}x{MIN_ALTO}+{x}+{y}")
        self.minsize(MIN_ANCHO, MIN_ALTO)
        
        datos = cargar_jsons(ADMINISTRADORES)
        info = datos[email]
        admin = Admin(email, info["nombre"], info["rut"], info["contrasena"])
        
        #Creando el frame superior (Datos del admin)
        self.frame_superior = ctk.CTkFrame(self, fg_color="#F90808", height=ALTO*0.1)
        self.frame_superior.pack(fill="both", expand = True)
        
        #Información que irá en la parte superior
        ctk.CTkLabel(self.frame_superior, text=f"Bienvenido admin {admin.nombre}", font=("Arial", 20)).place(relx=0.02, rely=0.25)
        ctk.CTkLabel(self.frame_superior, text=f"{admin.rut}", font=("Arial", 15)).place(relx=0.02, rely=0.6)
        
        
        #       Creando el frame inferior (En donde se verá las pestañas de alumnos, profesores y asignaturas)
        self.frame_inferior = ctk.CTkScrollableFrame(self, width=ANCHO, height=ALTO*0.9, fg_color="#999999")
        self.frame_inferior.pack(fill="both", expand=True)
        
        #       Frame de los alumnos
        frame_alumnos = ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.4, height=ALTO*0.45, corner_radius=100)
        frame_alumnos.grid(row=0, column=0, padx=20, pady=120)
        
        ctk.CTkLabel(frame_alumnos, text="Estudiantes").place(relx=0.5, rely=0.2, anchor="center")
        ctk.CTkLabel(frame_alumnos, text="Aquí se podrá visualizar la información de todos los estudiantes matriculados dentro del instituto.", wraplength=ANCHO*0.2).place(relx=0.5, rely=0.5, anchor="center")
        
        ctk.CTkButton(frame_alumnos, text="Ver Alumnos", command=self.mostrar_alumnos).place(relx=0.5, rely= 0.7, anchor="center")
        
        #       Frame de los profesores
        frame_profes = ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.4, height=ALTO*0.45, corner_radius=100)
        frame_profes.grid(row=0, column=1, padx=20, pady=120)
        
        ctk.CTkLabel(frame_profes, text="Profesores").place(relx=0.5, rely=0.2, anchor="center")
        ctk.CTkLabel(frame_profes, text="Aquí se podrá visualizar la información de todos los profesores que imparten clases dentro del instituto.", wraplength=ANCHO*0.2).place(relx=0.5, rely=0.5, anchor="center")
        
        ctk.CTkButton(frame_profes, text="Ver Profesores", command=self.mostrar_profesores).place(relx=0.5, rely= 0.7, anchor="center")
        
        #       Frame de las asignaturas
        frame_asignaturas = ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.4, height=ALTO*0.45, corner_radius=100)
        frame_asignaturas.grid(row=0, column=2, padx=20, pady=120)
        
        ctk.CTkLabel(frame_asignaturas, text="Asignaturas").place(relx=0.5, rely=0.2, anchor="center")
        ctk.CTkLabel(frame_asignaturas, text="Aquí se podrá visualizar todas las asignaturas que se imparten dentro del instituto.", wraplength=ANCHO*0.2).place(relx=0.5, rely=0.5, anchor="center")
        
        ctk.CTkButton(frame_asignaturas, text="Ver Asignaturas", command=self.mostrar_asignaturas).place(relx=0.5, rely= 0.7, anchor="center")
        
        #Configurar los frames y hacerlos responsive
        for c in range(3):
            self.frame_inferior.columnconfigure(c, weight=1)
        self.frame_inferior.rowconfigure(0, weight=1)
        
        self.protocol("WM_DELETE_WINDOW", self.cerrar)

    def cerrar(self):
        self.master.destroy()
    
    
    def limpiar_widgets(self):
        for widget in self.frame_inferior.winfo_children():
            widget.destroy()
    
    def mostrar_alumnos(self):
        self.limpiar_widgets()
        
        datos_alumnos = cargar_jsons(ALUMNOS)
        ctk.CTkButton(self.frame_superior, text="Matricular", command=VentanaMatricula).place(relx=0.8, rely=0.3)
        self.frame = ctk.CTkFrame(self.frame_inferior, fg_color="#195e28", width=ANCHO*0.6, height=ALTO*0.4)
        self.frame.pack(pady=20)
        
        total_alumnos = sorted(datos_alumnos.items(), key=lambda x: x[1]["nombre"])
        total_alumnos = [(info["nombre"], email) for email, info in total_alumnos]

        for i, (nombre, email) in enumerate(total_alumnos, start=1):
            
            contenedor = ctk.CTkFrame(self.frame, height=ALTO*0.05, width=ANCHO*0.6)
            contenedor.pack(padx= 10,pady = 10, fill="x")
            
            ctk.CTkLabel(contenedor, text=f"{i}.-").place(relx=0.01, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{nombre}").place(relx=0.03, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{email}").place(relx=0.27, rely=0.2)
            
            ctk.CTkButton(contenedor, text="Ver Datos", command=lambda e=email: VentanaDatosAlumno(e)).place(relx=0.7, rely=0.2)
            ctk.CTkButton(contenedor, text="Eliminar", command=lambda e=email: self.recargar_alumnos(e)).place(relx=0.8, rely=0.2)
    
    def recargar_alumnos(self, email):
        eliminar_datos(ALUMNOS, email)
        self.mostrar_alumnos()
        
    def recargar_profesores(self, email):
        eliminar_datos(PROFESORES, email)
        self.mostrar_profesores()
    
    def mostrar_asignaturas(self):
        self.limpiar_widgets()
        datos = cargar_jsons(ASIGNATURAS)
        asignaturas = [asignatura for asignatura in datos]
            
        ctk.CTkButton(self.frame_superior, text="Añadir Asignatura", command=VentanaAñadirAsignatura).place(relx=0.8, rely=0.3)
        
        for i, asignatura in enumerate(asignaturas):
            ramo = Asignatura(asignatura, datos[asignatura]["estudiantes"], datos[asignatura]["profesores"], datos[asignatura]["cantidad_estudiantes"])
            
            filas = i // 3
            columnas = i % 3
            
            frame_asignatura = ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.2, height=ALTO*0.5, fg_color="#ffffff")
            frame_asignatura.grid(row=filas, column=columnas, sticky="nsew", padx=20, pady=20)
            ctk.CTkLabel(frame_asignatura, text=ramo.nombre).place(relx = 0.3, rely=0.1)
            ctk.CTkLabel(frame_asignatura, text=f"Cantidad Alumnos: {ramo.cantidad_estudiantes}").place(relx = 0.3, rely=0.3)
            ctk.CTkButton(frame_asignatura, text="Ver Alumnos", command=lambda: VisualizarAlumnosProfes("alumno")).place(relx=0.6, rely=0.8)
            ctk.CTkButton(frame_asignatura, text="Ver Profesores", command=lambda: VisualizarAlumnosProfes("profesor")).place(relx=0.8, rely=0.8)
        
        num_filas = (len(datos) + 2) // 3 
        for f in range(num_filas):
            self.frame_inferior.rowconfigure(f, weight=1)
        for c in range(3):
            self.frame_inferior.columnconfigure(c, weight=1)
        
    
    def mostrar_profesores(self):
        self.limpiar_widgets()
        
        datos_profesores = cargar_jsons(PROFESORES)
        ctk.CTkButton(self.frame_superior, text="Añadir Profesor", command=VentanaAñadirProfe).place(relx=0.7, rely=0.3)
        ctk.CTkButton(self.frame_superior, text="Asignar Profesor", command=VentanaAsignacion).place(relx=0.9, rely=0.3)
        self.frame = ctk.CTkFrame(self.frame_inferior, fg_color="#195e28", width=ANCHO*0.6, height=ALTO*0.4)
        self.frame.pack(pady=20)
        
        total_alumnos = sorted(datos_profesores.items(), key=lambda x: x[1]["nombre"])
        total_alumnos = [(info["nombre"], email) for email, info in total_alumnos]

        for i, (nombre, email) in enumerate(total_alumnos, start=1):
            
            contenedor = ctk.CTkFrame(self.frame, height=ALTO*0.05, width=ANCHO*0.6)
            contenedor.pack(padx= 10,pady = 10, fill="x")
            
            ctk.CTkLabel(contenedor, text=f"{i}.-").place(relx=0.01, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{nombre}").place(relx=0.03, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{email}").place(relx=0.27, rely=0.2)
            
            ctk.CTkButton(contenedor, text="Ver Datos", command=lambda e=email: VentanaDatosProfesor(e)).place(relx=0.7, rely=0.2)
            ctk.CTkButton(contenedor, text="Eliminar", command=lambda e=email: self.recargar_profesores(e)).place(relx=0.8, rely=0.2)