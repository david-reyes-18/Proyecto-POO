import customtkinter as ctk
from Utils.utils import TOPLEVEL_ANCHO, TOPLEVEL_ALTO, x, y
from Utils.funcions import cargar_jsons, correo_institucional, contrasena, guardar_datos, profesores_totales, asignaturas_totales
from Utils.paths import ADMINISTRADORES, ALUMNOS, ASIGNATURAS, PROFESORES
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
            correo = correo_institucional(nombres, apellidos, "alumno")
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

class VentanaInscribir(ctk.CTkToplevel):
    def __init__(self, email):
        super().__init__()
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Inscribir Asignatura")
        
        datos_alumnos = cargar_jsons(ALUMNOS)
        datos_asignaturas = cargar_jsons(ASIGNATURAS)
        
        opciones = [asignatura for asignatura in datos_asignaturas if datos_alumnos[email]["nombre"] not in datos_asignaturas[asignatura]["estudiantes"]]
        
        ctk.CTkLabel(self, text="Seleccione el ramo a inscribir: ").pack()
        
        menu_asignaturas = ctk.CTkOptionMenu(self, values=opciones)
        menu_asignaturas.set("Seleccione una asignatura")
        menu_asignaturas.pack()
        
        def inscribir():
            asignatura = menu_asignaturas.get()
            
            datos_alumnos[email]["asignaturas"].append(asignatura)
            datos_asignaturas[asignatura]["estudiantes"].append(datos_alumnos[email]["nombre"])
            
            guardar_datos(ALUMNOS, datos_alumnos)
            guardar_datos(ASIGNATURAS, datos_asignaturas)
            
            self.destroy()
        
        ctk.CTkButton(self, text="Inscribir", command=inscribir).pack()


class VentanaAñadirAsignatura(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Añadir Asignatura")
        
        ctk.CTkLabel(self, text ="Añada el nombre de la asignatura que desee agregar:").pack(fill="x")
        nueva_asignatura = ctk.CTkEntry(self)
        nueva_asignatura.pack()
        
        def añadir_asignatura():
            ramo_nuevo = nueva_asignatura.get()
            
            datos = cargar_jsons(ASIGNATURAS)
            
            datos[ramo_nuevo] = {
                "nombre": ramo_nuevo,
                "estudiantes": [],
                "profesores": [],
                "cantidad_estudiantes": 0
            }
            guardar_datos(ASIGNATURAS, datos)
            
            self.destroy()
        
        ctk.CTkButton(self, text="Añadir", command=añadir_asignatura).pack()


class VisualizarAlumnosProfes(ctk.CTkToplevel):
    def __init__(self, rol: str):
        super().__init__()
        self.rol = rol
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        
        if rol == "alumno":
            datos_alumnos = cargar_jsons(ALUMNOS)
            self.frame = ctk.CTkScrollableFrame(self, fg_color="#195e28", width=TOPLEVEL_ANCHO, height=TOPLEVEL_ALTO)
            self.frame.pack(pady=20)
            
            total_alumnos = sorted(datos_alumnos.items(), key=lambda x: x[1]["nombre"])
            total_alumnos = [(info["nombre"], email) for email, info in total_alumnos]

            for i, (nombre, email) in enumerate(total_alumnos, start=1):
                
                contenedor = ctk.CTkFrame(self.frame)
                contenedor.pack(padx= 10,pady = 10, fill="x")
                
                ctk.CTkLabel(contenedor, text=f"{i}.-").place(relx=0.01, rely=0.2)
                ctk.CTkLabel(contenedor, text=f"{nombre}").place(relx=0.03, rely=0.2)
                ctk.CTkLabel(contenedor, text=f"{email}").place(relx=0.27, rely=0.2)
        elif rol == "profesor":
            datos_profesor = cargar_jsons(PROFESORES)
            self.frame = ctk.CTkScrollableFrame(self, fg_color="#195e28", width=TOPLEVEL_ANCHO, height=TOPLEVEL_ALTO)
            self.frame.pack(pady=20)
            
            total_profesores = sorted(datos_profesor.items(), key=lambda x: x[1]["nombre"])
            total_profesores = [(info["nombre"], email) for email, info in total_profesores]

            for i, (nombre, email) in enumerate(total_profesores, start=1):
                
                contenedor = ctk.CTkFrame(self.frame)
                contenedor.pack(padx= 10,pady = 10, fill="x")
                
                ctk.CTkLabel(contenedor, text=f"{i}.-").place(relx=0.01, rely=0.2)
                ctk.CTkLabel(contenedor, text=f"{nombre}").place(relx=0.03, rely=0.2)
                ctk.CTkLabel(contenedor, text=f"{email}").place(relx=0.27, rely=0.2)
        

class VentanaDatosAlumno(ctk.CTkToplevel):
    def __init__(self, email):
        super().__init__()
        self.email = email
        
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)


class VentanaDatosProfesor(ctk.CTkToplevel):
    def __init__(self, email):
        super().__init__()
        self.email = email
        
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)

class VentanaAñadirProfe(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Ingresar nuevo profesor")
        
        frame_interno = ctk.CTkScrollableFrame(self)
        frame_interno.pack(fill="both", expand=True)
        
        ctk.CTkLabel(frame_interno, text="Ingresar nuevo Profesor").pack(fill="x")
        ctk.CTkLabel(frame_interno, text="Ingrese adecuadamente los datos del profesor", wraplength=TOPLEVEL_ANCHO* 0.7).pack(fill="x")
        
        ctk.CTkLabel(frame_interno, text="Nombres: ").pack(fill="x")
        nombres_profe = ctk.CTkEntry(frame_interno)
        nombres_profe.pack()
        
        ctk.CTkLabel(frame_interno, text="Apellidos: ").pack(fill="x")
        apellidos_profe = ctk.CTkEntry(frame_interno)
        apellidos_profe.pack()
        
        ctk.CTkLabel(frame_interno, text="Ingrese su rut: ").pack(fill="x")
        rut_profe = ctk.CTkEntry(frame_interno)
        rut_profe.pack()
        
        def añadir_profesor():
            nombres = nombres_profe.get()
            apellidos = apellidos_profe.get()
            rut = rut_profe.get()
            
            nombre_completo = f"{nombres} {apellidos}"
            correo = correo_institucional(nombres, apellidos, "profesor")
            contra = contrasena(rut)
            asignaturas = []
            
            datos = cargar_jsons(PROFESORES)
            
            datos[correo] = {
                "nombre": nombre_completo,
                "rut": rut,
                "asignaturas": asignaturas,
                "contrasena": contra
            }
            
            guardar_datos(PROFESORES, datos)
            self.destroy()
            
        
        ctk.CTkButton(frame_interno, text="Matricular Alumno", command=añadir_profesor).pack()

class VentanaAsignacion(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Ingresar nuevo profesor")
        
        ctk.CTkLabel(self, text="Asignar Profesor a una asignatura").pack()
        ctk.CTkLabel(self, text="Elija al profesor: ").pack()
        
        total_profesores = profesores_totales()
        
        self.menu_profes = ctk.CTkOptionMenu(self, values=total_profesores, command=self.actualizar_asignaturas)
        self.menu_profes.set("Escoger profesor")
        self.menu_profes.pack()
        
        ctk.CTkLabel(self, text="Elija la asignatura: ").pack()
        
        self.menu_asignaturas = ctk.CTkOptionMenu(self, state="disabled")
        self.menu_asignaturas.set("Escoger asignatura")
        self.menu_asignaturas.pack()
        
        def asignacion():
            profesor = self.menu_profes.get()
            asignatura = self.menu_asignaturas.get()
            
            datos_profesores = cargar_jsons(PROFESORES)
            datos_asignaturas = cargar_jsons(ASIGNATURAS)
            
            for profe in datos_profesores:
                if datos_profesores[profe]["nombre"] == profesor:
                    datos_profesores[profe]["asignaturas"].append(asignatura)
            
            
            datos_asignaturas[asignatura]["profesores"].append(profesor)
            
            guardar_datos(PROFESORES, datos_profesores)
            guardar_datos(ASIGNATURAS, datos_asignaturas)
            
            self.destroy()
        
        ctk.CTkButton(self, text="Asignar asignatura",command=asignacion).pack()
        
    def actualizar_asignaturas(self, profesor):
        asignaturas = asignaturas_totales()
        
        datos = cargar_jsons(ASIGNATURAS)
        
        ramo = [asignatura for asignatura in asignaturas if profesor not in datos[asignatura]["profesores"]]
        self.menu_asignaturas.configure(values = ramo, state="normal")