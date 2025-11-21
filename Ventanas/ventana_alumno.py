import customtkinter as ctk
from Utils.utils import MIN_ANCHO, MIN_ALTO, x, y, ANCHO, ALTO
from Utils.funcions import cargar_jsons
from Utils.paths import ALUMNOS
from Clases.alumnos import Alumno

class VentanaAlumno(ctk.CTk):
    def __init__(self, email):
        super().__init__()
        self.email = email
        self.title("Escuelita")
        self.geometry(f"{MIN_ANCHO}x{MIN_ALTO}+{x}+{y}")
        self.minsize(MIN_ANCHO, MIN_ALTO)
        
        datos = cargar_jsons(ALUMNOS)
        info = datos["alumnos"][email]
        alumno = Alumno(email, info["nombre"], info["rut"],info["carrera"],info["asignaturas"],info["contrasena"])
        
        #Creando el lienzo superior
        frame_superior = ctk.CTkFrame(self, fg_color="#F90808", height=ALTO*0.1)
        frame_superior.pack(fill="both", expand = True)
        #Texto del lienzo superior
        ctk.CTkLabel(frame_superior, text=f"Bienvenido, {alumno.nombre}", font=("Arial", 20)).place(relx=0.02, rely=0.25)
        ctk.CTkLabel(frame_superior, text=f"{alumno.rut}", font=("Arial", 15)).place(relx=0.02, rely=0.6)
        ctk.CTkLabel(frame_superior, text=f"{alumno.carrera}", font=("Arial", 15)).place(relx=0.5, rely=0.4)
        
        #Creando el lienzo inferior
        frame_inferior = ctk.CTkScrollableFrame(self, width=ANCHO, height=ALTO*0.9, fg_color="#999999")
        frame_inferior.pack(fill="both", expand=True)
        
        for i in range(len(alumno.asignaturas)):
            filas = i // 3
            columnas = i % 3
            ctk.CTkFrame(frame_inferior, width=ANCHO*0.2, height=ALTO*0.5, fg_color="#ffffff").grid(row=filas, column=columnas, sticky="nsew", padx=10, pady=10)
        
        num_filas = (len(alumno.asignaturas) + 2) // 3 
        for f in range(num_filas):
            frame_inferior.rowconfigure(f, weight=1)
        for c in range(3):
            frame_inferior.columnconfigure(c, weight=1)
    
    def iniciar(self):
        self.root.mainloop()