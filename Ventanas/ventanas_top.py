import customtkinter as ctk
from Utils.utils import TOPLEVEL_ANCHO, TOPLEVEL_ALTO, x, y
from Utils.funcions import cargar_jsons, correo_institucional, contrasena, guardar_datos
from Utils.paths import ADMINISTRADORES, ALUMNOS
from Clases.administrador import Admin

class VentanaMatricula(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Mtricula Alumno Nuevo")
        
        frame_interno = ctk.CTkScrollableFrame(self)
        frame_interno.pack(fill="both", expand=True)
        
        ctk.CTkLabel(frame_interno, text="Formulario de matricula").pack(fill="x")
        ctk.CTkLabel(frame_interno, text="Ingrese adecuadamente los datos del estudiante a matricular, indicando sus nombres, apellidos, rut y la carrera en la cual se va a matricular. Posterior a la matricula al alumno se le asignará un correo institucional y una contraseña para ingresar a visualizar sus asignaturas, después podrá cambiar la contraseña a voluntas.", wraplength=TOPLEVEL_ANCHO* 0.7).pack(fill="x")
        
        ctk.CTkLabel(frame_interno, text="Nombres: ").pack(fill="x")
        nombres_alumnos = ctk.CTkEntry(frame_interno)
        nombres_alumnos.pack()
        
        ctk.CTkLabel(frame_interno, text="Apellidos: ").pack(fill="x")
        apellidos_alumnos = ctk.CTkEntry(frame_interno)
        apellidos_alumnos.pack()
        
        ctk.CTkLabel(frame_interno, text="Ingrese su rut: ").pack(fill="x")
        rut_alumnos = ctk.CTkEntry(frame_interno)
        rut_alumnos.pack()
        
        ctk.CTkLabel(frame_interno, text="Ingrese la carrera: ").pack(fill="x")
        carrera_alumno = ctk.CTkEntry(frame_interno)
        carrera_alumno.pack()
        
        def matricular():
            nombres = nombres_alumnos.get()
            apellidos = apellidos_alumnos.get()
            rut = rut_alumnos.get()
            carrera = carrera_alumno.get()
            
            nombre_completo = f"{nombres} {apellidos}"
            correo = correo_institucional(nombres, apellidos)
            contra = contrasena(rut)
            asignaturas = []
            
            datos = cargar_jsons(ALUMNOS)
            
            datos[correo] = {
                "nombre": nombre_completo,
                "rut": rut,
                "carrera": carrera,
                "asignaturas": asignaturas,
                "contrasena": contra
            }
            
            guardar_datos(ALUMNOS, datos)
            
            self.destroy()
            
        
        ctk.CTkButton(frame_interno, text="Matricular Alumno", command=matricular).pack()
        
class VentanaDatosAlumno(ctk.CTkToplevel):
    def __init__(self, email):
        super().__init__()
        self.email = email
        
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)