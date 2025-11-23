#Librerias nesesarias
import customtkinter as ctk
from Utils.utils import TOPLEVEL_ANCHO, TOPLEVEL_ALTO, x, y
from Utils.funcions import cargar_jsons, correo_institucional, contrasena, guardar_datos, profesores_totales, asignaturas_totales
from Utils.paths import ADMINISTRADORES, ALUMNOS, ASIGNATURAS, PROFESORES
from Clases.administrador import Admin
from Utils.fonts import Fonts

#       Aquí se encuentran todas las ventanas TopLevel que el sistema usa, ya sea para la creacion, visualización o eliminación de datos

#Ventana que sirve para matricular un alumno nuevo, de esta manera se le entrega un correo y contraseña institucionales
class VentanaMatricula(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        
        #Configuracción de la ventana
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Matricula Alumno Nuevo")
        
        #Creación del frame
        frame_interno = ctk.CTkScrollableFrame(self)
        frame_interno.pack(fill="both", expand=True)
        
            #Labeles de cabecera del formulario
        ctk.CTkLabel(frame_interno, text="Formulario de matricula", font=Fonts.m2bold).pack(fill="x", pady=40)
        ctk.CTkLabel(frame_interno, text="Ingrese adecuadamente los datos del estudiante a matricular, indicando sus nombres, apellidos, rut y la carrera en la cual se va a matricular. Posterior a la matricula al alumno se le asignará un correo institucional y una contraseña para ingresar a visualizar sus asignaturas, después podrá cambiar la contraseña a voluntas.", wraplength=TOPLEVEL_ANCHO* 0.75, font=Fonts.i2, justify="left").pack(fill="x")
        
        #Ingresar los nombres
        ctk.CTkLabel(frame_interno, text="Nombres: ", width=TOPLEVEL_ANCHO*0.75, font=Fonts.i1, anchor="w").pack(pady=40)
        
        nombres_alumnos = ctk.CTkEntry(frame_interno, font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, placeholder_text="Ej: Alejandro Ignacio", border_width=2)
        nombres_alumnos.pack()
        
        label_nombres = ctk.CTkLabel(frame_interno, text="", font=Fonts.i3)
        label_nombres.pack()
        
        #Ingresar los apellidos
        ctk.CTkLabel(frame_interno, text="Apellidos: ", font=Fonts.i1, width=TOPLEVEL_ANCHO*0.75, anchor="w").pack(pady=40)
        apellidos_alumnos = ctk.CTkEntry(frame_interno, font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, placeholder_text="Ej: Gonzales Diaz", border_width=2)
        apellidos_alumnos.pack()
        
        label_apellidos = ctk.CTkLabel(frame_interno, text="", font=Fonts.i3)
        label_apellidos.pack()
        
        #Ingresar rut
        ctk.CTkLabel(frame_interno, text="Ingrese su rut: ", width=TOPLEVEL_ANCHO*0.75, font=Fonts.i1, anchor="w", ).pack(pady=40)
        rut_alumnos = ctk.CTkEntry(frame_interno, font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, placeholder_text="Ej: 12.345.678-9", border_width=2)
        rut_alumnos.pack()
        
        label_rut = ctk.CTkLabel(frame_interno, text="", font=Fonts.i3)
        label_rut.pack()
        
        #Ingresar carrera
        ctk.CTkLabel(frame_interno, text="Ingrese la carrera: ", width=TOPLEVEL_ANCHO*0.75, font=Fonts.i1, anchor="w").pack(pady=40)
        carrera_alumno = ctk.CTkEntry(frame_interno, font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, placeholder_text="Ej: Ingenieria Civil en Informatica", border_width=2)
        carrera_alumno.pack()
        
        label_carrera = ctk.CTkLabel(frame_interno, text="", font=Fonts.i3)
        label_carrera.pack()
        
        #Función que ejecuta el botón para matricular
        def matricular():
            
            #Obtener los datos ingresados por el administrador
            nombres = nombres_alumnos.get()
            apellidos = apellidos_alumnos.get()
            rut = rut_alumnos.get()
            carrera = carrera_alumno.get()
            
            #Verificación de que el formato del nombre sea correcto
            if len(nombres.split()) > 3 or len(nombres.split()) < 2:
                label_nombres.configure(text="Nombres invalido", text_color="red")
                nombres_alumnos.configure(border_color="red")
                return

            #Si la verificación del nombre es exitosa se marca verde
            nombres_alumnos.configure(border_color = "green")
            
            #Verificación de los apellidoss
            if len(nombres.split()) > 3 or len(nombres.split()) < 2:
                label_apellidos.configure(text="Apellidos invalido", text_color="red")
                apellidos_alumnos.configure(border_color="red")
                return

            #Si la verificación de los apellidos es correcta se marca verde
            apellidos_alumnos.configure(border_color = "green")
            
            #Verificación del rut
            rut_limpio = rut.replace(".", "").replace("-", "")
            
            if not rut_limpio[:-1].isdigit() or len(rut_limpio) != 9:
                label_rut.configure(text="Rut invalido", text_color="red")
                rut_alumnos.configure(border_color="red")
                return
            
            #Si la verificación del rut es exitosa se marca verde
            rut_alumnos.configure(border_color = "green")
            
            #Verificación de la carrera
            if len(carrera) < 3:
                label_carrera.configure(text="Carrera invalida", text_color="red")
                carrera_alumno.configure(border_color="red")
                return
            
            #Si la verificación de la carrera es correcta se marca verde
            carrera_alumno.configure(border_colr="green")

            #Se le da el formato para poder añadirlo a la base de datos
            nombre_completo = f"{nombres} {apellidos}"
            correo = correo_institucional(nombres, apellidos, "alumno")
            contra = contrasena(rut)
            asignaturas = []
            
            #Se carga el archivo
            datos = cargar_jsons(ALUMNOS)
            
            #Se añade al nuevo alumno
            datos[correo] = {
                "nombre": nombre_completo,
                "rut": rut,
                "carrera": carrera,
                "asignaturas": asignaturas,
                "contrasena": contra
            }
            
            #Se guarda en la base de datos
            guardar_datos(ALUMNOS, datos)
            
            #Se destruye la ventana
            self.destroy()
            
        
        #Boton que ejecuta la función matricula
        ctk.CTkButton(frame_interno, text="Matricular Alumno", command=matricular, font=Fonts.m2).pack(pady=100)

        #Se defune la funcion para mover el frame scrolleable
        def scroll(event):
            #Accerder al scroll
            canvas = frame_interno._parent_canvas  

            #       Scroll tanto para Windows, MacOS y Linux
            
            #Si el scroll es positivo (en caso de Linux el scroll hacia arriba se considera el boton 4), se realiza el scroll
            if event.num == 4 or event.delta > 0:
                canvas.yview_scroll(-1, "units")
                
            #Si el scroll es negativo (en caso de Linux el scroll hacia abajo se considera el boton 5), se realiza el scroll
            elif event.num == 5 or event.delta < 0:
                canvas.yview_scroll(1, "units")
        
        #Scroll para Windows y MacOS
        frame_interno.bind_all("<MouseWheel>", scroll)
        
        #Scroll para Linux
        frame_interno.bind_all("<Button-4>", scroll)
        frame_interno.bind_all("<Button-5>", scroll)  



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