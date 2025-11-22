import customtkinter as ctk
from Utils.utils import MIN_ANCHO, MIN_ALTO, x, y, ANCHO, ALTO
from Utils.funcions import cargar_jsons
from Utils.paths import ADMINISTRADORES, ALUMNOS
from Clases.administrador import Admin

class VentanaAdmin(ctk.CTk):
    def __init__(self, email):
        super().__init__()
        self.email = email
        self.title("Administración de Escuelita")
        self.config(background="#2b2b2b")
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
        
        ctk.CTkButton(frame_profes, text="Ver Profesores").place(relx=0.5, rely= 0.7, anchor="center")
        
        #       Frame de las asignaturas
        frame_asignaturas = ctk.CTkFrame(self.frame_inferior, width=ANCHO*0.4, height=ALTO*0.45, corner_radius=100)
        frame_asignaturas.grid(row=0, column=2, padx=20, pady=120)
        
        ctk.CTkLabel(frame_asignaturas, text="Asignaturas").place(relx=0.5, rely=0.2, anchor="center")
        ctk.CTkLabel(frame_asignaturas, text="Aquí se podrá visualizar todas las asignaturas que se imparten dentro del instituto.", wraplength=ANCHO*0.2).place(relx=0.5, rely=0.5, anchor="center")
        
        ctk.CTkButton(frame_asignaturas, text="Ver Asignaturas").place(relx=0.5, rely= 0.7, anchor="center")
        
        #Configurar los frames y hacerlos responsive
        for c in range(3):
            self.frame_inferior.columnconfigure(c, weight=1)
        self.frame_inferior.rowconfigure(0, weight=1)
    
    
    def limpiar_widgets(self):
        for widget in self.frame_inferior.winfo_children():
            widget.destroy()
    
    def mostrar_alumnos(self):
        self.limpiar_widgets()
        
        datos_alumnos = cargar_jsons(ALUMNOS)
        
        frame = ctk.CTkFrame(self.frame_inferior, fg_color="#195e28", width=ANCHO*0.6, height=ALTO*0.4)
        frame.pack(pady=20)
        
        i = 1
        total_alumnos = [ y for y in datos_alumnos.items()]
        
        print(total_alumnos)
        for alumno in total_alumnos:
            
            contenedor = ctk.CTkFrame(frame, height=ALTO*0.05, width=ANCHO*0.6)
            contenedor.pack(padx= 10,pady = 10, fill="x")
            
            #ctk.CTkLabel(contenedor, text=f"{i}.-").place(relx=0.1, rely=0.5, anchor="center")
            #ctk.CTkLabel(contenedor, text=f"{alumno}").place(relx=0.2, rely=0.5, anchor="center")
            #ctk.CTkLabel(contenedor, text=f"{datos_alumnos[alumno]['rut']}").place(relx=0.4, rely=0.5, anchor="center")
            