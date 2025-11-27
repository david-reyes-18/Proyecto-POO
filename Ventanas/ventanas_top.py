#Librerias nesesarias
import customtkinter as ctk
from Utils.utils import TOPLEVEL_ANCHO, TOPLEVEL_ALTO, x, y
from Utils.funcions import cargar_jsons, correo_institucional, contrasena, guardar_datos, profesores_totales, asignaturas_totales
from Utils.paths import ADMINISTRADORES, ALUMNOS, ASIGNATURAS, PROFESORES
from Clases.administrador import Admin
from Utils.fonts import Fonts
from Clases.alumnos import Alumno
from Clases.profesor import Profesor

#       Aquí se encuentran todas las ventanas TopLevel que el sistema usa, ya sea para la creacion, visualización o eliminación de datos

#Ventana que sirve para matricular un alumno nuevo, de esta manera se le entrega un correo y contraseña institucionales
class VentanaMatricula(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__()
        
        #Configuracción de la ventana
        self.master = master
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
            if len(apellidos.split()) > 3 or len(apellidos.split()) < 2:
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
            carrera_alumno.configure(border_color="green")

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
                "contrasena": contra,
                "profesores": []
            }
            
            #Se guarda en la base de datos
            guardar_datos(ALUMNOS, datos)
            
            #Muetra nuevamente la pantalla de los alumnos, actualizando asi su contenido
            master.mostrar_alumnos()
            
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



#Ventana para la inscripción de asignaturas
class VentanaInscribir(ctk.CTkToplevel):
    def __init__(self, email, ventana_alumno):
        super().__init__()
        
        #Configuración de la ventana
        self.email = email
        self.ventana_alumnos = ventana_alumno
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Inscribir Asignatura")
        
        #Cargar datos
        datos_alumnos = cargar_jsons(ALUMNOS)
        datos_asignaturas = cargar_jsons(ASIGNATURAS)
        
        #Se guardan en una lista las opciones de asignaturas que puede optar el estudiante
        opciones_asignaturas = [asignatura for asignatura in datos_asignaturas if datos_alumnos[email]["nombre"] not in datos_asignaturas[asignatura]["estudiantes"]]
        
        #Texto de inicio
        ctk.CTkLabel(self, text="Inscripción de Asignatura", font=Fonts.m2bold).pack(fill="x", pady=30)
        ctk.CTkLabel(self, text="Seleccione el ramo a inscribir:", font=Fonts.i1, width=TOPLEVEL_ANCHO*0.8, anchor="w").pack(pady=30)
        
        #Funcion que se actualiza al pinchar un ramo, busca los profesores que imparten el ramo elegido
        def actualizar_profes(asignatura):
            profes = [profe for profe in datos_asignaturas[asignatura]["profesores"]]
            menu_profes.configure(values =profes, state="normal")
        
        #Menú desplegable para ver las asignaturas que puede inscribit
        menu_asignaturas = ctk.CTkOptionMenu(self, values=opciones_asignaturas, command=actualizar_profes, font=Fonts.m3, dropdown_font=Fonts.i2, width=TOPLEVEL_ANCHO*0.5)
        menu_asignaturas.set("Seleccione una asignatura")
        menu_asignaturas.pack()
        
        #Label para el profesor
        ctk.CTkLabel(self, text="Seleccione el profesor:", font=Fonts.i1, width=TOPLEVEL_ANCHO*0.8, anchor="w").pack(pady=30)
        
        #Menú desplegable para ver los profesores que imparten dicha materia (estará desabilitado hasta que el alumno escoja una materia)
        menu_profes = ctk.CTkOptionMenu(self, state="disabled", font=Fonts.m3, dropdown_font=Fonts.i2, width=TOPLEVEL_ANCHO*0.5)
        menu_profes.set("Seleccione a un profesor")
        menu_profes.pack()
        

        #Función que se ejecutará al presionar un botón de inscribir
        def inscribir():
            
            #Se toman los valores de la asignatura y el profesor
            asignatura = menu_asignaturas.get()
            profesor = menu_profes.get()
            
            #Se verifica que se haya seleccionado un profesor, sino el botón no funciona
            if profesor == "Seleccione a un profesor":
                return
            
            #Se cargan los datos de los profesores
            datos_profesor = cargar_jsons(PROFESORES)
            
            #Se añade la asignatura a la base de datos del alumno
            datos_alumnos[email]["asignaturas"].append(asignatura)
            #SE añade el profesor que eligió el alumno para su asignatura en la base de datos
            datos_alumnos[email]["profesores"].append(profesor)
            #En la asignatura elegida se guarda el nombre del estudiante
            datos_asignaturas[asignatura]["estudiantes"].append(datos_alumnos[email]["nombre"])
            
            #Se busca al profesor que el alumno eligio en la base de datos
            for profe in datos_profesor:
                #Si lo encuentra se agregara el nombre del alumno y la asignatura que eligió en la base de datos del profesor
                if datos_profesor[profe]["nombre"] == profesor:
                    datos_profesor[profe]["alumnos"].append(f"{datos_alumnos[email]["nombre"]},{asignatura}")
            
            #Se actualiza la cantidad de alumnos que hay en la asigantura elegida
            datos_asignaturas[asignatura]["cantidad_estudiantes"] = len(datos_asignaturas[asignatura]["estudiantes"])
            
            #Se guardan los datos
            guardar_datos(ALUMNOS, datos_alumnos)
            guardar_datos(ASIGNATURAS, datos_asignaturas)
            guardar_datos(PROFESORES,datos_profesor)
            
            #Se actualiza la ventana de alumnos, para que muestre la asigantura recien elegida
            self.ventana_alumnos.mostrar_asignaturas(email)
            #SE destruye la ventana de inscipción
            self.destroy()
        
        #Botón para inscribir
        ctk.CTkButton(self, text="Inscribir", command=inscribir, font=Fonts.m2).pack(pady=60)


#Ventana para añadir una asignatura al sistema
class VentanaAñadirAsignatura(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__()
        
        #Configuración de la ventana
        self.master = master
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Añadir Asignatura")
        
        #Texto del Inicio
        ctk.CTkLabel(self, text ="Añadir Asignatura", font=Fonts.m2bold).pack(fill="x", pady=60)
        ctk.CTkLabel(self, text ="Al momento de añadir una asignatura, esta quedará registrada en el sistema, por lo tanto se le deberá asignar al menos un profesor a cargo y será liberada para que los alumnos puedan inscribir dicha asignatura.", font=Fonts.i3, wraplength=TOPLEVEL_ANCHO*0.75, justify="left").pack(fill="x")
        ctk.CTkLabel(self, text ="Añada la asignatura:", font=Fonts.m3, anchor="w", width=TOPLEVEL_ANCHO*0.75).pack(pady=40)
        
        
        nueva_asignatura = ctk.CTkEntry(self, placeholder_text="Asignatura", width=TOPLEVEL_ANCHO*0.5, font=Fonts.m3, border_width=2)
        nueva_asignatura.pack()
        
        confirmacion = ctk.CTkLabel(self, text="", font=Fonts.i4)
        confirmacion.pack(fill="x", pady=20)
        
        def añadir_asignatura():
            ramo_nuevo = nueva_asignatura.get()
            
            if len(ramo_nuevo) < 3:
                confirmacion.configure(text="Asignatura Inválida", text_color="red")
                nueva_asignatura.configure(border_color="red")
                return
            
            datos = cargar_jsons(ASIGNATURAS)
            
            datos[ramo_nuevo] = {
                "nombre": ramo_nuevo,
                "estudiantes": [],
                "profesores": [],
                "cantidad_estudiantes": 0
            }
            guardar_datos(ASIGNATURAS, datos)
            master.mostrar_asignaturas()
            self.destroy()
        
        ctk.CTkButton(self, text="Añadir", command=añadir_asignatura, font=Fonts.m2).pack(pady=50)


#Ventana que permite ver todos los alumnos o profesores, dependiendo el rol que  se le de a la ventana, del instituto que estan inscritos a dicha asignatura
class VisualizarAlumnosProfes(ctk.CTkToplevel):
    def __init__(self, rol: str, asignatura: str):
        super().__init__()
        
        #Se configura la ventana
        self.rol = rol
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        
        #Si es un alumno entonces se le mostrará todos los alumnos que estan inscritos a la asignatura
        if rol == "alumno":
            #Se configura el titulo de la ventana
            self.title("Alumnos")
            
            #Se cargan los datos de todos los alumnos
            datos_alumnos = cargar_jsons(ALUMNOS)
            
            #Titulo
            ctk.CTkLabel(self, text="Listado de Alumnos", font=Fonts.m2bold).pack(fill="x", pady=10)
            
            #Se crea el frame scrolleable
            self.frame = ctk.CTkScrollableFrame(self, fg_color="#2b2b2b", width=TOPLEVEL_ANCHO*0.9, height=TOPLEVEL_ALTO*0.9)
            self.frame.pack()
            
            #Se ordenan los datos de los estudiantes por el nombre
            total_alumnos = sorted(datos_alumnos.items(), key=lambda x: x[1]["nombre"])
            #Se crea una tupla con los valores de (nombre, email) si el alumno tiene inscrita dicha asignatura
            total_alumnos = [(info["nombre"], email) for email, info in total_alumnos if asignatura in info["asignaturas"]]

            
            #Se crea el listado de alumnos iterando en cada alumno
            for i, (nombre, email) in enumerate(total_alumnos, start=1):
                
                #Frame que contendrá la información de cada alumno
                contenedor = ctk.CTkFrame(self.frame, border_width=1, border_color="black", height=TOPLEVEL_ALTO*0.15)
                contenedor.pack(fill="x")
                
                #Información del estudiante
                ctk.CTkLabel(contenedor, text=f"{i}.-", font=Fonts.i3).place(relx=0.01, rely=0.2)
                ctk.CTkLabel(contenedor, text=f"{nombre}", font=Fonts.i3).place(relx=0.03, rely=0.2)
                ctk.CTkLabel(contenedor, text=f"{datos_alumnos[email]['rut']}", font=Fonts.i3).place(relx=0.6, rely=0.2)
        
        #Si es un profesor entonces se le mostrará todos los profesores que imparten dicha asigantura
        elif rol == "profesor":
            #Se configura el titulo de la ventana
            self.title("Profesores")
            
            #Se cargan los datos de todos los profesores
            datos_profesores = cargar_jsons(PROFESORES)
            
            #Titulo
            ctk.CTkLabel(self, text="Listado de Profesores", font=Fonts.m2bold).pack(fill="x", pady=10)
            
            #Se crea el frame scrolleable
            self.frame = ctk.CTkScrollableFrame(self, fg_color="#2b2b2b", width=TOPLEVEL_ANCHO*0.9, height=TOPLEVEL_ALTO*0.9)
            self.frame.pack()
            
            #Se ordenan los datos de los profesores por el nombre
            total_profesores = sorted(datos_profesores.items(), key=lambda x: x[1]["nombre"])
            #Se crea una tupla con los valores de (nombre, email) si el alumno tiene inscrita dicha asignatura
            total_profesores = [(info["nombre"], email) for email, info in total_profesores if asignatura in info["asignaturas"]]

            
            #Se crea el listado de los profesores iterando en cada profesor
            for i, (nombre, email) in enumerate(total_profesores, start=1):
                
                #Frame que contendrá la información de cada profesor
                contenedor = ctk.CTkFrame(self.frame, border_width=1, border_color="black", height=TOPLEVEL_ALTO*0.15)
                contenedor.pack(fill="x")
                
                #Información del estudiante
                ctk.CTkLabel(contenedor, text=f"{i}.-", font=Fonts.i3).place(relx=0.01, rely=0.2)
                ctk.CTkLabel(contenedor, text=f"{nombre}", font=Fonts.i3).place(relx=0.03, rely=0.2)
                ctk.CTkLabel(contenedor, text=f"{datos_profesores[email]['rut']}", font=Fonts.i3).place(relx=0.6, rely=0.2)
        

class VentanaDatosAlumno(ctk.CTkToplevel):
    def __init__(self, email):
        super().__init__()
        self.email = email
        
        self.title("Datos Alumno")
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        
        datos_estudiante = cargar_jsons(ALUMNOS)
        asignaturas_alumno = datos_estudiante[email]["asignaturas"]
        profes_alumno = datos_estudiante[email]["profesores"]
        
        #Titulo
        ctk.CTkLabel(self, text="Asignaturas/Profesores", font=Fonts.m2bold).pack(fill="x", pady=10)
            
        #Se crea el frame scrolleable
        self.frame = ctk.CTkScrollableFrame(self, fg_color="#2b2b2b", width=TOPLEVEL_ANCHO*0.9, height=TOPLEVEL_ALTO*0.9)
        self.frame.pack()
        
        #Se crea el listado de alumnos iterando en cada alumno
        for i in range(len(asignaturas_alumno)):
                
            #Frame que contendrá la información de cada alumno
            contenedor = ctk.CTkFrame(self.frame, border_width=1, border_color="black", height=TOPLEVEL_ALTO*0.15)
            contenedor.pack(fill="x")
                
            #Información del estudiante
            ctk.CTkLabel(contenedor, text=f"{i + 1}.-", font=Fonts.i3).place(relx=0.01, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{asignaturas_alumno[i]}", font=Fonts.i3).place(relx=0.03, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{profes_alumno[i]}", font=Fonts.i3).place(relx=0.6, rely=0.2)


class VentanaDatosProfesor(ctk.CTkToplevel):
    def __init__(self, email):
        super().__init__()
        self.email = email
        
        self.title("Datos Profesores")
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        
        datos_profes = cargar_jsons(PROFESORES)
        asignaturas_profes = datos_profes[email]["asignaturas"]
        
        #Titulo
        ctk.CTkLabel(self, text="Asignatura impartidas", font=Fonts.m2bold).pack(fill="x", pady=10)
            
        #Se crea el frame scrolleable
        self.frame = ctk.CTkScrollableFrame(self, fg_color="#2b2b2b", width=TOPLEVEL_ANCHO*0.9, height=TOPLEVEL_ALTO*0.9)
        self.frame.pack()
        
        #Se crea el listado de alumnos iterando en cada alumno
        for i in range(len(asignaturas_profes)):
                
            #Frame que contendrá la información de cada alumno
            contenedor = ctk.CTkFrame(self.frame, border_width=1, border_color="black", height=TOPLEVEL_ALTO*0.15)
            contenedor.pack(fill="x")
                
            #Información del estudiante
            ctk.CTkLabel(contenedor, text=f"{i + 1}.-", font=Fonts.i3).place(relx=0.01, rely=0.2)
            ctk.CTkLabel(contenedor, text=f"{asignaturas_profes[i]}", font=Fonts.i3).place(relx=0.03, rely=0.2)


#Ventana para añadir profesores
class VentanaAñadirProfe(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__()
        
        #Configuración de la ventana
        self.master = master
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Añadir nuevo profesor")
        
        #Creación del frame scrolleable interno
        frame_interno = ctk.CTkScrollableFrame(self)
        frame_interno.pack(fill="both", expand=True)
        
        #Textos que aparecen al inicio
        ctk.CTkLabel(frame_interno, text="Añadir nuevo Profesor", font=Fonts.m2bold).pack(fill="x", pady=40)
        ctk.CTkLabel(frame_interno, text="Ingrese adecuadamente los datos del profesor", wraplength=TOPLEVEL_ANCHO* 0.7, font=Fonts.i1).pack(fill="x")
        
        #Ingresar nombres del profesor
        ctk.CTkLabel(frame_interno, text="Ingrese los nombres:", font=Fonts.i1, anchor="w", width=TOPLEVEL_ANCHO*0.75).pack(pady=40)
        nombres_profe = ctk.CTkEntry(frame_interno, width=TOPLEVEL_ANCHO*0.5, border_width=2, font=Fonts.m3, placeholder_text="Ej: Alejandro Ignacio")
        nombres_profe.pack()
        label_nombre = ctk.CTkLabel(frame_interno, text="", font=Fonts.i3)
        label_nombre.pack(fill="x")
        
        #Ingresar los apellidos del profesor
        ctk.CTkLabel(frame_interno, text="Ingrese los apellidos:", font=Fonts.i1, anchor="w", width=TOPLEVEL_ANCHO*0.75).pack(pady=40)
        apellidos_profe = ctk.CTkEntry(frame_interno, width=TOPLEVEL_ANCHO*0.5, border_width=2, font=Fonts.m3, placeholder_text="Ej: Gonzalo Diaz")
        apellidos_profe.pack()
        label_apellido = ctk.CTkLabel(frame_interno, text="", font=Fonts.i3)
        label_apellido.pack(fill="x")
        
        #Ingresar el rut del profesor
        ctk.CTkLabel(frame_interno, text="Ingrese su rut: ", font=Fonts.i1, anchor="w", width=TOPLEVEL_ANCHO*0.75).pack(pady=40)
        rut_profe = ctk.CTkEntry(frame_interno, width=TOPLEVEL_ANCHO*0.5, border_width=2, font=Fonts.m3, placeholder_text="Ej: 12.345.678-9")
        rut_profe.pack()
        label_rut = ctk.CTkLabel(frame_interno, text="", font=Fonts.i3)
        label_rut.pack(fill="x")
        
        
        #Función que se ejecutará al presionar el boton para añadir al profesor
        def añadir_profesor():
            #Obtener datos que ingreso el admin
            nombres = nombres_profe.get()
            apellidos = apellidos_profe.get()
            rut = rut_profe.get()
            
            #Comprobar que los nombres estan correctos
            if len(nombres.split()) > 3 or len(nombres.split()) < 2:
                label_nombre.configure(text="Nombres invalido", text_color="red")
                nombres_profe.configure(border_color="red")
                return
            #Si pasa la verificación se pondrá de color verde el entry de los nombres
            else:
                label_nombre.configure(text="", text_color="green")
                nombres_profe.configure(border_color="green")
            
            #Comprobar que los apellidos estan correctos
            if len(apellidos.split()) > 3 or len(apellidos.split()) < 2:
                label_apellido.configure(text="Nombres invalido", text_color="red")
                apellidos_profe.configure(border_color="red")
                return
            #Si pasa la verificación se pondrá verde el entry de los apellidos
            else:
                label_apellido.configure(text="", text_color="green")
                apellidos_profe.configure(border_color="green")
            
            #El rut sin puntos ni guión
            rut_limpio = rut.replace(".", "").replace("-", "")
            
            #Verificae si el rut tiene el formato correcto
            if not rut_limpio[:-1].isdigit() or len(rut_limpio) != 9:
                label_rut.configure(text="Rut Invalido", text_color="red")
                rut_profe.configure(border_color="red")
            #Si tiene el formato correcto se pondra verde el entry
            else:
                label_rut.configure(text="", text_color="green")
                rut_profe.configure(border_color="green")
            
            #Se preparan los datos que serán guardados en la base de datos
            nombre_completo = f"{nombres} {apellidos}"
            correo = correo_institucional(nombres, apellidos, "profesor")
            contra = contrasena(rut)
            asignaturas = []
            alumnos = []
            
            #Se abre el archivo de los profesores
            datos = cargar_jsons(PROFESORES)
            
            #Se añade el profesor con el formato de antes
            datos[correo] = {
                "nombre": nombre_completo,
                "rut": rut,
                "asignaturas": asignaturas,
                "contrasena": contra,
                "alumnos": alumnos
            }
            
            #Se guarda en la base de datos de los profesores
            guardar_datos(PROFESORES, datos)
            
            #Se actualiza la ventana de los profesores con el nuevo profesor
            master.mostrar_profesores()
            #Se destruye la ventana de añadir profesores
            self.destroy()
            
        
        #Botón añadir profe
        ctk.CTkButton(frame_interno, text="Añadir Profesor", command=añadir_profesor, font=Fonts.m2bold).pack(pady=50)
        
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


#Ventana de Asignación de profesores
class VentanaAsignacion(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        
        #Configuración de la ventana
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Asignar Profesor")
        
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



class VentanaVerAlumnos(ctk.CTkToplevel):
    def __init__(self, email, asignatura):
        super().__init__()
        #Configuración de la ventana
        self.email = email
        self.asignatura = asignatura
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Alumnos")
        
        datos_profes = cargar_jsons(PROFESORES)
        info = datos_profes[email]
        
        profe = Profesor(email, info["nombre"], info["rut"], info["asignaturas"], info["contrasena"], info["alumnos"])
        
        #Titulo
        ctk.CTkLabel(self, text="Asignatura impartidas", font=Fonts.m2bold).pack(fill="x", pady=10)
            
        #Se crea el frame scrolleable
        self.frame = ctk.CTkScrollableFrame(self, fg_color="#2b2b2b", width=TOPLEVEL_ANCHO*0.9, height=TOPLEVEL_ALTO*0.9)
        self.frame.pack()
        
        #Se crea el listado de alumnos iterando en cada alumno
        for i in range(len(profe.alumnos)):
                
            #Frame que contendrá la información de cada alumno
            contenedor = ctk.CTkFrame(self.frame, border_width=1, border_color="black", height=TOPLEVEL_ALTO*0.15)
            contenedor.pack(fill="x")
            if profe.alumnos[i].split(",")[1] == asignatura:
                alumno = profe.alumnos[i].split(",")[0]
                #Información del estudiante
                ctk.CTkLabel(contenedor, text=f"{i + 1}.-", font=Fonts.i3).place(relx=0.01, rely=0.2)
                ctk.CTkLabel(contenedor, text=f"{alumno}", font=Fonts.i3).place(relx=0.03, rely=0.2)