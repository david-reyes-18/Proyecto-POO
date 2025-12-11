#Librerias nesesarias
import customtkinter as ctk
from Utils.utils import *
from Utils.functions import *
from Utils.paths import *
from Utils.fonts import Fonts
from Clases.profesor import Profesor
from Clases.carreras import Carrera

#       Aquí se encuentran todas las ventanas TopLevel que el sistema usa, ya sea para la creacion, visualización o eliminación de datos

#Ventana que sirve para matricular un alumno nuevo, de esta manera se le entrega un correo y contraseña institucionales
class VentanaMatricula(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__()
        
        #Configuracción de la ventana
        self.master = master
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Matrícula Alumno Nuevo")
        
        frame_superior = ctk.CTkFrame(self, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS, height=TOPLEVEL_ALTO*0.2)
        frame_superior.pack(fill="both", expand=True)
        
        ctk.CTkLabel(frame_superior, text="Formulario de Matrícula", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.5, rely=0.5, anchor="center")
        
        #Creación del frame
        frame_interno = ctk.CTkScrollableFrame(self, height=TOPLEVEL_ALTO*0.8, fg_color=COLOR_AZUL, scrollbar_button_color=COLOR_FONTS, scrollbar_button_hover_color=COLOR_FONDO)
        frame_interno.pack(fill="both", expand=True)
        
        frame = ctk.CTkFrame(frame_interno, fg_color=COLOR_FONDO, width=TOPLEVEL_ANCHO*0.95)
        frame.pack(pady=20)
        
            #Labeles de cabecera del formulario
        frame_info = ctk.CTkFrame(frame, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
        frame_info.pack()
            
        ctk.CTkLabel(frame_info, text="Ingrese adecuadamente los datos del estudiante a matricular, indicando sus nombres, apellidos, rut y la carrera en la cual se va a matricular. Posterior a la matricula al alumno se le asignará un correo institucional y una contraseña para ingresar a visualizar sus asignaturas, después podrá cambiar la contraseña a voluntad.", wraplength=TOPLEVEL_ANCHO* 0.75, font=Fonts.i2, justify="left", text_color=COLOR_FONTS).pack(padx=30, pady=30)
        
        #Ingresar los nombres
        frame_nombres = ctk.CTkFrame(frame, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
        frame_nombres.pack(fill="x", expand=True)
        
        
        ctk.CTkLabel(frame_nombres, text="Nombres: ", width=TOPLEVEL_ANCHO*0.75, font=Fonts.i1, anchor="w", text_color=COLOR_FONTS).pack(pady=40)
        
        nombres_alumnos = ctk.CTkEntry(frame_nombres, font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, placeholder_text="Ej: Alejandro Ignacio", border_width=2, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, height=47)
        nombres_alumnos.pack()
        
        label_nombres = ctk.CTkLabel(frame_nombres, text="", font=Fonts.i3)
        label_nombres.pack(pady=10)
        
        #Ingresar los apellidos
        frame_apellidos = ctk.CTkFrame(frame, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
        frame_apellidos.pack(fill="x", expand=True)
        
        ctk.CTkLabel(frame_apellidos, text="Apellidos: ", font=Fonts.i1, width=TOPLEVEL_ANCHO*0.75, anchor="w", text_color=COLOR_FONTS).pack(pady=40)
        apellidos_alumnos = ctk.CTkEntry(frame_apellidos, font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, placeholder_text="Ej: Gonzales Diaz", border_width=2, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, height=47)
        apellidos_alumnos.pack()
        
        label_apellidos = ctk.CTkLabel(frame_apellidos, text="", font=Fonts.i3)
        label_apellidos.pack(pady=10)
        
        #Ingresar rut
        frame_rut = ctk.CTkFrame(frame, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
        frame_rut.pack(fill="x", expand=True)
        
        ctk.CTkLabel(frame_rut, text="Ingrese su rut: ", width=TOPLEVEL_ANCHO*0.75, font=Fonts.i1, anchor="w", text_color=COLOR_FONTS).pack(pady=40)
        rut_alumnos = ctk.CTkEntry(frame_rut, font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, placeholder_text="Ej: 12.345.678-9", border_width=2, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, height=47)
        rut_alumnos.pack()
        
        label_rut = ctk.CTkLabel(frame_rut, text="", font=Fonts.i3)
        label_rut.pack(pady=10)
        
        #Ingresar carrera
        frame_carrera = ctk.CTkFrame(frame, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
        frame_carrera.pack(fill="x", expand=True)
        
        ctk.CTkLabel(frame_carrera, text="Ingrese la carrera: ", width=TOPLEVEL_ANCHO*0.75, font=Fonts.i1, anchor="w", text_color=COLOR_FONTS).pack(pady=40)
        
        datos_carrera = cargar_jsons(CARRERAS)
        
        carreras = [carrera for carrera in datos_carrera if datos_carrera[carrera]["habilitado"]]
        
        carrera_alumno = ctk.CTkOptionMenu(frame_carrera, values=carreras, font=Fonts.i2, width=TOPLEVEL_ANCHO*0.45, height=47, fg_color=COLOR_AZUL, button_color=COLOR_OSCURO, dropdown_font=Fonts.i2, dropdown_fg_color=COLOR_AZUL, dropdown_text_color=COLOR_FONTS)
        carrera_alumno.set("Seleccionar Carrera")
        carrera_alumno.pack()
        
        label_carrera = ctk.CTkLabel(frame_carrera, text="", font=Fonts.i3)
        label_carrera.pack(pady=10)
        
        #Función que ejecuta el botón para matricular
        def matricular():
            
            #Obtener los datos ingresados por el administrador
            nombres = nombres_alumnos.get()
            apellidos = apellidos_alumnos.get()
            rut = rut_alumnos.get()
            carrera = carrera_alumno.get()
            
            #Verificación de que el formato del nombre sea correcto
            if (len(nombres.split()) > 3 or len(nombres.split()) < 2) or (not es_string(nombres)) or not (len(nombres) > 6):
                label_nombres.configure(text="Nombres invalido", text_color="red")
                nombres_alumnos.configure(border_color="red")
                return
            else:
                label_nombres.configure(text="")
                nombres_alumnos.configure(border_color = "green")
            
            #Verificación de los apellidoss
            if not (len(apellidos.split()) == 2 and es_string(apellidos) and len(apellidos) > 6):
                label_apellidos.configure(text="Apellidos invalido", text_color="red")
                apellidos_alumnos.configure(border_color="red")
                return
            else:
                label_apellidos.configure(text="")
                apellidos_alumnos.configure(border_color="green")

            ruts_prueba = ["11.111.111-1", "22.222.222-2", "33.333.333-3", "44.444.444-4", "55.555.555-5", "66.666.666-6", "77.777.777-7", "88.888.888-8", "99.999.999-9", "00.000.000-0"]
            
            #Verificar que tenga el formato
            if not verificar_rut(rut):
                label_rut.configure(text="Rut invalido", text_color="red")
                rut_alumnos.configure(border_color="red")
                return
            #Verificar que no sea un rut de prueba
            elif rut in ruts_prueba:
                label_rut.configure(text="Rut invalido", text_color="red")
                rut_alumnos.configure(border_color="red")
                return
            else:
                label_rut.configure(text="")
                rut_alumnos.configure(border_color="green")
            
            #Verificación de la carrera
            if carrera == "Seleccionar Carrera":
                label_carrera.configure(text="No se ha seleccionado una carrera.", text_color="red")
                return
            else:
                label_carrera.configure(text="")
            
            
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
                "profesores": [],
                "semestre": 1
            }
            
            #Se guarda en la base de datos
            guardar_datos(ALUMNOS, datos)
            
            #Muetra nuevamente la pantalla de los alumnos, actualizando asi su contenido
            master.mostrar_alumnos()
            
            #Se destruye la ventana
            self.destroy()
            
        
        #Boton que ejecuta la función matricula
        ctk.CTkButton(frame_interno, text="Matricular Alumno", command=matricular, font=Fonts.m2bold, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, hover_color=COLOR_AZUL, border_width=2, border_color=COLOR_FONTS).pack(pady=50)

        #Se defune la funcion para mover el frame scrolleable
        def scroll(event):
            try:
                #Accerder al scroll
                canvas = frame_interno._parent_canvas  

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
        opciones_asignaturas = []
        
        semestre_alumno = datos_alumnos[email]["semestre"]
        carrera_alumno = datos_alumnos[email]["carrera"]
        
        for asig in datos_asignaturas:
            if datos_asignaturas[asig]["semestre"] == semestre_alumno:
                if carrera_alumno in datos_asignaturas[asig]["carreras"]:
                    opciones_asignaturas.append(asig)
        
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
        
        #Frame del titulo
        frame_superior = ctk.CTkFrame(self, height=TOPLEVEL_ALTO*0.16, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_superior.pack(fill="x")
        #Label con el título
        ctk.CTkLabel(frame_superior, text="Añadir Asignatura", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.5, rely=0.5, anchor="center")
        
        #   Frame inferior que contendrá todo el formulario
        frame_inferior = ctk.CTkScrollableFrame(self, height=TOPLEVEL_ALTO*0.84, fg_color=COLOR_AZUL, border_width=2, border_color=COLOR_FONTS)
        frame_inferior.pack(fill="x")
        
        #Frame contenedor que contendrá los datos
        frame_contenedor = ctk.CTkFrame(frame_inferior, fg_color=COLOR_FONDO)
        frame_contenedor.pack(pady=20)
        
        #Frame para la información inicial
        frame_info = ctk.CTkFrame(frame_contenedor, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
        frame_info.pack()
            
        ctk.CTkLabel(frame_info, text="Ingrese el nombre de la asignatura correctamente, rellenando todos los campos. Se le pedirá además que ingrese el área a la que pertenece dicha asignatura.", wraplength=TOPLEVEL_ANCHO* 0.75, font=Fonts.i2, justify="left", text_color=COLOR_FONTS).pack(padx=30, pady=30)
        
        #           Ingresar el nombre de la Asignatura
        
        #Frame que contendrá el nombre de la asignatura
        frame_nombre = ctk.CTkFrame(frame_contenedor, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
        frame_nombre.pack(fill="x", expand=True)
        
        #Label indicativo
        ctk.CTkLabel(frame_nombre, text="Ingrese el nombre de la Asignatura:", width=TOPLEVEL_ANCHO*0.75, font=Fonts.i1, anchor="w", text_color=COLOR_FONTS).pack(pady=40)
        
        #Entrada de texto para el nombre
        nombre_asignatura = ctk.CTkEntry(frame_nombre, font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, placeholder_text="Ej: Programación", border_width=2, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, height=47)
        nombre_asignatura.pack()
        
        #Label por si ocurre un error
        label_nombre = ctk.CTkLabel(frame_nombre, text="", font=Fonts.i3)
        label_nombre.pack(pady=10)
        
        
        #           Especilidades de la Asignatura
        
        #Frame que contendrá la información
        frame_area = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_area.pack(fill="x", expand=True)
        
        ctk.CTkLabel(frame_area, text="Ingrese el área de la asignatura (máx. 2):", width=TOPLEVEL_ANCHO*0.75, font=Fonts.i1, anchor="w", text_color=COLOR_FONTS).pack(pady=40)
        
        areas = [
            "Ciencias Básicas",
            "Ingeniería y Tecnología",
            "Ciencias Sociales",
            "Salud",
            "Educación",
            "Economía y Administración",
            "Arte y Humanidades"
        ]
        
        checks = {}
        
        def estado():
            seleccionadas = sum(var.get() for var in checks.values())
            
            if seleccionadas == 2:
                for box, val in checks.items():
                    if not val.get():
                        box.configure(state="disabled")
            else:
                for box in checks:
                    box.configure(state="normal")
        
        for area in areas:
            valor = ctk.BooleanVar()
            box = ctk.CTkCheckBox(frame_area, text=area, variable=valor, command=estado)
            box.pack(anchor="w", pady=10)
            checks[box] = valor
        
        
        label_area = ctk.CTkLabel(frame_area, text="", font=Fonts.i3)
        label_area.pack(pady=10)
        
        
        frame_semestres = ctk.CTkFrame(frame_contenedor, border_width=2, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
        frame_semestres.pack(fill="x", expand=True)
        
        #Label indicativo
        ctk.CTkLabel(frame_semestres, text="Ingrese el semestre en el que se impartirá:", width=TOPLEVEL_ANCHO*0.75, font=Fonts.i1, anchor="w", text_color=COLOR_FONTS).pack(pady=40)
        
        #Entrada de texto para el nombre
        entry_semestres = ctk.CTkEntry(frame_semestres, font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, placeholder_text="Ej: 2", border_width=2, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, height=47)
        entry_semestres.pack()
        
        #Label por si ocurre un error
        label_semestre = ctk.CTkLabel(frame_semestres, text="", font=Fonts.i3)
        label_semestre.pack(pady=10)
        
        
        #Función para añadir la carrera en la base de datos
        def añadir_asignatura():
            #Se obtienen los valores que se dieron en los campos anteriores
            nombre = nombre_asignatura.get()
            areas = [box.cget("text") for box, var in checks.items() if var.get()]
            semestre = entry_semestres.get()
            
            #Se verifica que el nombre sea válido
            if len(nombre) < 4 or not es_string(nombre):
                nombre_asignatura.configure(border_color="red")
                label_nombre.configure(text="Nombre Inválido", text_color="red")
                return
            else:
                nombre_asignatura.configure(border_color="green")
                label_nombre.configure(text="")
            
            #Se verifica que se haya seleccionado un área
            if area == []:
                label_area.configure(text="No se ha seleccionado un área.", text_color="red")
                return
            else:
                label_area.configure(text="")
            
            #Verificar los semestres
            if not semestre.isdigit():
                entry_semestres.configure(border_color = "red")
                label_semestre.configure(text="Sólo se permiten números.", text_color="red")
                return
            elif not (1 <= int(semestre) <= 14):
                entry_semestres.configure(border_color = "red")
                label_semestre.configure(text="Número Inválido.", text_color="red")
                return
            else:
                entry_semestres.configure(border_color = "green")
                label_semestre.configure(text="")
            
            #Cargar los datos que hay en las carreras
            datos_asignatura = cargar_jsons(ASIGNATURAS)
            
            #Se agregan los datos de la carrrera
            datos_asignatura[nombre] = {
                "nombre": nombre,
                "estudiantes": [],
                "profesores": [],
                "cantidad_estudiantes": 0,
                "prerequisitos": [],
                "carreras": [],
                "especialidad": areas,
                "semestre": int(semestre)
            }
            
            #Se guardan los datos de la nueva asignatura
            guardar_datos(ASIGNATURAS, datos_asignatura)
            
            #Se actualiza la pantalla
            master.mostrar_asignaturas()
            #Se destruye la ventana
            self.destroy()
        
        ctk.CTkButton(frame_inferior, text="Añadir Carrera", font=Fonts.m2bold, text_color=COLOR_FONTS, border_width=2, border_color=COLOR_FONTS, fg_color=COLOR_FONDO, hover_color=COLOR_AZUL, command=añadir_asignatura).pack(pady=40)
        
        #Se define el scroll para la ventana
        def scroll(event):
            #Accerder al scroll
            canvas = frame_inferior._parent_canvas  

            #       Scroll tanto para Windows, MacOS y Linux
            
            #Si el scroll es positivo (en caso de Linux el scroll hacia arriba se considera el boton 4), se realiza el scroll
            if event.num == 4 or event.delta > 0:
                canvas.yview_scroll(-1, "units")
                
            #Si el scroll es negativo (en caso de Linux el scroll hacia abajo se considera el boton 5), se realiza el scroll
            elif event.num == 5 or event.delta < 0:
                canvas.yview_scroll(1, "units")
        
        #Scroll para Windows y MacOS
        frame_inferior.bind_all("<MouseWheel>", scroll)
        
        #Scroll para Linux
        frame_inferior.bind_all("<Button-4>", scroll)
        frame_inferior.bind_all("<Button-5>", scroll) 




class AñadirPreRequisitos(ctk.CTkToplevel):
    def __init__(self, master, asignatura):
        super().__init__()

        #Se configura la ventana
        self.master = master
        self.asignatura = asignatura
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("PreRequisitos")
        
        #Frame del titulo
        frame_superior = ctk.CTkFrame(self, height=TOPLEVEL_ALTO*0.16, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_superior.pack(fill="x")
        #Label con el título
        ctk.CTkLabel(frame_superior, text="Añadir PreRequisitos", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.5, rely=0.5, anchor="center")
        
        #   Frame inferior que contendrá todo el formulario
        frame_inferior = ctk.CTkFrame(self, height=TOPLEVEL_ALTO*0.84, fg_color=COLOR_AZUL, border_width=2, border_color=COLOR_FONTS)
        frame_inferior.pack(fill="x")
        
        #Frame contenedor que contendrá los datos
        frame_contenedor = ctk.CTkFrame(frame_inferior, fg_color=COLOR_FONDO)
        frame_contenedor.pack(pady=20)
        
        #Frame para la información inicial
        frame_info = ctk.CTkFrame(frame_contenedor, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
        frame_info.pack()
            
        ctk.CTkLabel(frame_info, text="Ingrese el prerequisito de la asignatura correctamente. Sea cuidadoso.", wraplength=TOPLEVEL_ANCHO* 0.75, font=Fonts.i2, justify="left", text_color=COLOR_FONTS).pack(padx=30, pady=30)
        
        #           Ingresar el nombre de la Asignatura
        
        #Frame que contendrá el nombre de la asignatura
        frame_prerequisito = ctk.CTkFrame(frame_contenedor, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
        frame_prerequisito.pack(fill="x", expand=True)
        
        #Label indicativo
        ctk.CTkLabel(frame_prerequisito, text="Ingrese el PreRequisito:", width=TOPLEVEL_ANCHO*0.75, font=Fonts.i1, anchor="w", text_color=COLOR_FONTS).pack(pady=40)
        
        #Entrada de texto para el nombre
        
        datos_asignatura = cargar_jsons(ASIGNATURAS)
        
        especialidad = datos_asignatura[asignatura]["especialidad"]
        
        semestre = datos_asignatura[asignatura]["semestre"]
        
        opciones = []
        
        for asig in datos_asignatura:
            if datos_asignatura[asig]["semestre"] == semestre - 1:
                if any(esp in especialidad for esp in datos_asignatura[asig]["especialidad"]):
                    opciones.append(asig)
        
        if datos_asignatura[asignatura]["prerequisitos"]:
            if len(datos_asignatura[asignatura]["prerequisitos"]) == 2:
                opciones = []
            else:
                for asig in datos_asignatura[asignatura]["prerequisitos"]:
                    if asig in opciones:
                        opciones.remove(asig)
        
        
        
        prerequisito = ctk.CTkOptionMenu(frame_prerequisito, values=opciones)
        prerequisito.set("Seleccione un PreRequisito")
        prerequisito.pack()
        
        #Label por si ocurre un error
        label_prerequisito = ctk.CTkLabel(frame_prerequisito, text="", font=Fonts.i3)
        label_prerequisito.pack(pady=10)
        
        def añadir_prerequisito():
            pre = prerequisito.get()
            
            if pre == "Seleccione un PreRequisito":
                label_prerequisito.configure(text="No se ha seleccionado un prerequisito.", text_color="red")
                return
            
            datos_asignatura[asignatura]["prerequisitos"].append(pre)
            
            guardar_datos(ASIGNATURAS, datos_asignatura)
            
            master.mostrar_asignaturas()
            
            self.destroy()
        
        ctk.CTkButton(frame_inferior, text="Añadir PreRequisito", font=Fonts.m2bold, text_color=COLOR_FONTS, border_width=2, border_color=COLOR_FONTS, fg_color=COLOR_FONDO, hover_color=COLOR_AZUL, command=añadir_prerequisito).pack(pady=40)

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
        
        #Frame para el título
        frame_superior = ctk.CTkFrame(self, height=TOPLEVEL_ALTO*0.16, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_superior.pack(fill="x")
        #Título
        ctk.CTkLabel(frame_superior, text="Añadir Profesor", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.5, rely=0.5,  anchor="center")
        
        #Creación del frame scrolleable interno
        frame_interno = ctk.CTkScrollableFrame(self, height=TOPLEVEL_ALTO*0.84, fg_color=COLOR_AZUL, border_width=2, border_color=COLOR_FONTS)
        frame_interno.pack(fill="x")
        
        #Frame del contenedor
        frame_contenedor = ctk.CTkFrame(frame_interno, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_contenedor.pack(pady=50)
        
        #       Información
        
        #Frame info
        frame_info = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_info.pack(fill="x")
        
        #Textos que aparecen al inicio
        ctk.CTkLabel(frame_info, text="Ingrese adecuadamente los datos del profesor. Coloque los nombres en el campo correspondiente, asi mismo con sus apellidos. Para el rut siga el formato indicado.", wraplength=TOPLEVEL_ANCHO* 0.7, font=Fonts.i3).pack(padx=10, pady=30)
        
        #       Nombres
        
        #Frame nombre
        frame_nombres = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_nombres.pack(fill="x")
        
        #Label nombres
        ctk.CTkLabel(frame_nombres, text="Ingrese los nombres:", font=Fonts.i1, anchor="w", width=TOPLEVEL_ANCHO*0.75).pack(pady=40, padx=20)
        
        #Entry para ingresar los nombres
        nombres_profe = ctk.CTkEntry(frame_nombres, border_width=2, placeholder_text="Ej: Alejandro Ignacio", font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, height=47)
        nombres_profe.pack()
        
        #Label por si ocurre un error
        label_nombre = ctk.CTkLabel(frame_nombres, text="", font=Fonts.i3)
        label_nombre.pack(pady=10)
        
        #       Apellidos
        
        #Frame apellidos
        frame_apellidos = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_apellidos.pack(fill="x")
        
        #Label apellidos
        ctk.CTkLabel(frame_apellidos, text="Ingrese los apellidos:", font=Fonts.i1, anchor="w", width=TOPLEVEL_ANCHO*0.75).pack(pady=40, padx=20)
        
        #Entry para ingresar los nombres
        apellidos_profe = ctk.CTkEntry(frame_apellidos, border_width=2, placeholder_text="Ej: Gallardo Fuentes", font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, height=47)
        apellidos_profe.pack()
        
        #Label por si ocurre un error
        label_apellido = ctk.CTkLabel(frame_apellidos, text="", font=Fonts.i3)
        label_apellido.pack(pady=10)
        
        
        #       Rut
        
        #Frame rut
        frame_rut = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_rut.pack(fill="x")
        
        #Label nombres
        ctk.CTkLabel(frame_rut, text="Ingrese el rut:", font=Fonts.i1, anchor="w", width=TOPLEVEL_ANCHO*0.75).pack(pady=40, padx=20)
        
        #Entry para ingresar los nombres
        rut_profe = ctk.CTkEntry(frame_rut, border_width=2, placeholder_text="Ej: 12.345.678-9", font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, height=47)
        rut_profe.pack()
        
        #Label por si ocurre un error
        label_rut = ctk.CTkLabel(frame_rut, text="", font=Fonts.i3)
        label_rut.pack(pady=10)
        
        
        #       Área
        
        #Frame area
        frame_area = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_area.pack(fill="x")
        
        #Label nombres
        ctk.CTkLabel(frame_area, text="Ingrese sus áreas de conocimiento (máx. 2):", font=Fonts.i1, anchor="w", width=TOPLEVEL_ANCHO*0.75).pack(pady=40, padx=20)
        
        #Áreas disponibles para elegir
        areas = [
            "Ciencias Básicas",
            "Ingeniería y Tecnología",
            "Ciencias Sociales",
            "Salud",
            "Educación",
            "Economía y Administración",
            "Arte y Humanidades"
        ]
        
        #Diccionario que guarda la opcion junto con su valor de verdad
        checks = {}
        
        #Función que no permite más de 2 casillas seleccionadas
        def estado():
            #Cantidad de seleccionadas
            seleccionadas = sum(var.get() for var in checks.values())
            
            #Si hay dos selecciondas pone todas las opciones desabilitadas
            if seleccionadas == 2:
                for box, val in checks.items():
                    if not val.get():
                        box.configure(state="disabled")
            #Sino se vuelve todo a la normalidad
            else:
                for box in checks:
                    box.configure(state="normal")
        
        #Se crean los checkbox por cada área
        for area in areas:
            valor = ctk.BooleanVar()
            box = ctk.CTkCheckBox(frame_area, text=area, variable=valor, command=estado)
            box.pack(anchor="w", pady=10, padx=30)
            checks[box] = valor
        
        #Label por si ocurre un error
        label_area = ctk.CTkLabel(frame_area, text="", font=Fonts.i3)
        label_area.pack(pady=10)
        
        
        #Función que se ejecutará al presionar el boton para añadir al profesor
        def añadir_profesor():
            #Obtener datos que ingreso el admin
            nombres = nombres_profe.get()
            apellidos = apellidos_profe.get()
            rut = rut_profe.get()
            area = [box.cget("text") for box, var in checks.items() if var.get()]
            
            #Comprobar que los nombres estan correctos
            if (len(nombres.split()) > 3 or len(nombres.split()) < 2) or (not es_string(nombres)) or not (len(apellidos) > 6):
                label_nombre.configure(text="Nombres inválidos", text_color="red")
                nombres_profe.configure(border_color="red")
                return
            #Si pasa la verificación se pondrá de color verde el entry de los nombres
            else:
                label_nombre.configure(text="", text_color="green")
                nombres_profe.configure(border_color="green")
            
            #Comprobar que los apellidos estan correctos
            if not (len(apellidos.split()) == 2 and es_string(apellidos) and len(apellidos) > 6):
                label_apellido.configure(text="Apellidos Inválidos", text_color="red")
                apellidos_profe.configure(border_color="red")
                return
            #Si pasa la verificación se pondrá verde el entry de los apellidos
            else:
                label_apellido.configure(text="", text_color="green")
                apellidos_profe.configure(border_color="green")
            
            ruts_prueba = ["11.111.111-1", "22.222.222-2", "33.333.333-3", "44.444.444-4", "55.555.555-5", "66.666.666-6", "77.777.777-7", "88.888.888-8", "99.999.999-9", "00.000.000-0"]
            
            #Verificar si el rut tiene el formato correcto
            if not verificar_rut(rut):
                label_rut.configure(text="Rut Inválido", text_color="red")
                rut_profe.configure(border_color="red")
                return
            #Verificar si está dentro de los ruts de prueba
            elif rut in ruts_prueba:
                label_rut.configure(text="Rut Invalido", text_color="red")
                rut_profe.configure(border_color="red")
                return
            #Si tiene el formato correcto se pondra verde el entry
            else:
                label_rut.configure(text="", text_color="green")
                rut_profe.configure(border_color="green")
            
            #Verificar que se haya seleccionado al menos un área
            if not area:
                label_area.configure(text="Seleccione al menos 1 área.", text_color="red")
                return
            else:
                label_area.configure(text="")
            
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
                "alumnos": alumnos,
                "especialidad": area
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
        
        #Frame para el título
        frame_superior = ctk.CTkFrame(self, height=TOPLEVEL_ALTO*0.16, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_superior.pack(fill="x")
        #Título
        ctk.CTkLabel(frame_superior, text="Asignación de Profesores", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.5, rely=0.5,  anchor="center")
        
        #Creación del frame scrolleable interno
        frame_interno = ctk.CTkScrollableFrame(self, height=TOPLEVEL_ALTO*0.84, fg_color=COLOR_AZUL, border_width=2, border_color=COLOR_FONTS)
        frame_interno.pack(fill="x")
        
        #Frame del contenedor
        frame_contenedor = ctk.CTkFrame(frame_interno, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_contenedor.pack(pady=50)
        
        #       Información
        
        #Frame info
        frame_info = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_info.pack(fill="x")
        
        #Textos que aparecen al inicio
        ctk.CTkLabel(frame_info, text="Para asignar una asignatura a un profesor primero debe escoger el área a la que pertenece. Después seleccione el semestre de dicha asignatura para posteriormente seleccionar la asignatura que será asignada y por último seleccione el profesor que la llevará a cabo.", wraplength=TOPLEVEL_ANCHO* 0.7, font=Fonts.i3).pack(padx=10, pady=30)
        
        #       Área de la asignatura
        
        #Frame para el área
        frame_area = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_area.pack(fill="x")
        
        #Titulo
        ctk.CTkLabel(frame_area, text="Ingrese el área:", font=Fonts.i1, anchor="w", width=TOPLEVEL_ANCHO*0.75).pack(pady=40, padx=20)
        
        #Áreas disponibles para elegir
        areas = [
            "Ciencias Básicas",
            "Ingeniería y Tecnología",
            "Ciencias Sociales",
            "Salud",
            "Educación",
            "Economía y Administración",
            "Arte y Humanidades"
        ]
        
        
        #Option Menu
        self.seccion_area = ctk.CTkOptionMenu(frame_area, fg_color=COLOR_AZUL, font=Fonts.i2, text_color=COLOR_FONTS, button_color=COLOR_OSCURO, dropdown_fg_color=COLOR_AZUL, dropdown_font=Fonts.i2, dropdown_text_color=COLOR_FONTS, dropdown_hover_color=COLOR_FONDO, values=areas, command=self.habilitar_entry)
        self.seccion_area.set("Seleccione el área")
        self.seccion_area.pack()
        
        label_area = ctk.CTkLabel(frame_area, text="", font=Fonts.i3)
        label_area.pack(pady=10)
        
        #       Semestre
        
        #Frame para el semestre
        frame_semestre = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_semestre.pack(fill="x")
        
        #Titulo
        ctk.CTkLabel(frame_semestre, text="Ingrese el semestre:", font=Fonts.i1, anchor="w", width=TOPLEVEL_ANCHO*0.75).pack(pady=40, padx=20)
        
        #Lugra para ingresar el semestre
        self.entry_semestre = ctk.CTkEntry(frame_semestre, font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, placeholder_text="Ej: 2", border_width=2, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, height=47, state="disabled")
        self.entry_semestre.pack()
        
        label_semestre = ctk.CTkLabel(frame_semestre, text="", font=Fonts.i3)
        label_semestre.pack(pady=10)
        
        
        #       Asignatura
        
        #Frame para la asignatura
        frame_asignatura = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_asignatura.pack(fill="x")
        
        #Titulo
        ctk.CTkLabel(frame_asignatura, text="Ingrese la asignatura:", font=Fonts.i1, anchor="w", width=TOPLEVEL_ANCHO*0.75).pack(pady=40, padx=20)
        
        #Lugra para ingresar el semestre
        self.seleccion_asignatura = ctk.CTkOptionMenu(frame_asignatura, fg_color=COLOR_AZUL, font=Fonts.i2, text_color=COLOR_FONTS, button_color=COLOR_OSCURO, dropdown_fg_color=COLOR_AZUL, dropdown_font=Fonts.i2, dropdown_text_color=COLOR_FONTS, dropdown_hover_color=COLOR_FONDO, state="disabled", command=self.actualizar_profes)
        self.seleccion_asignatura.set("Seleccione la asignatura")
        self.seleccion_asignatura.pack()
        
        label_asignatura = ctk.CTkLabel(frame_asignatura, text="", font=Fonts.i3)
        label_asignatura.pack(pady=10)
        
        #       Profesor
        
        #Frame para el profesor
        frame_profesor = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_profesor.pack(fill="x")
        
        #Titulo
        ctk.CTkLabel(frame_profesor, text="Ingrese al profesor:", font=Fonts.i1, anchor="w", width=TOPLEVEL_ANCHO*0.75).pack(pady=40, padx=20)
        
        #Lugra para ingresar el semestre
        self.seleccion_profe = ctk.CTkOptionMenu(frame_profesor, fg_color=COLOR_AZUL, font=Fonts.i2, text_color=COLOR_FONTS, button_color=COLOR_OSCURO, dropdown_fg_color=COLOR_AZUL, dropdown_font=Fonts.i2, dropdown_text_color=COLOR_FONTS, dropdown_hover_color=COLOR_FONDO, state="disabled")
        self.seleccion_profe.set("Seleccione al profesor")
        self.seleccion_profe.pack()
        
        label_profe = ctk.CTkLabel(frame_profesor, text="", font=Fonts.i3)
        label_profe.pack(pady=10)
        
        #Función que se ejecuta al presionar el botón para asignar a el profesor elegido con la asignatura elegida
        def asignacion():
            #Se obtienen los valores que están en los option menu
            area = self.seccion_area.get()
            semestre = self.entry_semestre.get()
            asignatura = self.seleccion_asignatura.get()
            profesor = self.seleccion_profe.get()
            
            #Se verifica que se haya seleccionado un área
            if area == "Seleccione el área":
                label_area.configure(text="No se ha seleccionado un área.", text_color="red")
                return
            else:
                label_area.configure(text="")
            
            #Se verificca que se haya seleccionado un semestre válido
            if not semestre.isdigit():
                label_semestre.configure(text="Semestre Inválido.", text_color="red")
                return
            else:
                if not (1 <= int(semestre) <= 14):
                    label_semestre.configure(text="Semestre Inválido.", text_color="red")
                    return
                else:
                    label_semestre.configure(text="")

            #Se verifica que se haya seleccionado una asignatura
            if asignatura == "Seleccione la asignatura":
                label_asignatura.configure(text="No se ha seleccionado una asignatura.", text_color="red")
                return
            else:
                label_asignatura.configure(text="")
            
            #Se verificaque se haya seleccionado un profesor
            if profesor == "Seleccione al profesor":
                label_profe.configure(text="No se ha seleccionado un profesor.", text_color="red")
                return
            else:
                label_profe.configure(text="")
            
            #Cargar datos
            datos_asignaturas = cargar_jsons(ASIGNATURAS)
            datos_profes = cargar_jsons(PROFESORES)
            
            #Se añade el profesor en la asignatura y la asignatura en el profesor
            for profe in datos_profes:
                if datos_profes[profe]["nombre"] == profesor:
                    email_profe = profe
            
            datos_profes[email_profe]["asignaturas"].append(asignatura)
            datos_asignaturas[asignatura]["profesores"].append(profesor)
            
            #Se guardan los datos
            guardar_datos(PROFESORES, datos_profes)
            guardar_datos(ASIGNATURAS, datos_asignaturas)
            
            self.destroy()
        
        ctk.CTkButton(frame_interno, text="Asignar Profesor",command=asignacion, font=Fonts.m2bold, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS, text_color=COLOR_FONTS, hover_color=COLOR_AZUL).pack(pady=50)
        
        #Se define el scroll para la ventana
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
        
        self.entry_semestre.bind("<KeyRelease>", self.actualizar_asignaturas)
    
    #Funcion que se ejecuta cada que se selecciona un área
    def habilitar_entry(self, area):
        #Si se seleccionó una opción, entonces se habilita el entry del semestre
        if area != "Seleccione el área":
            self.entry_semestre.configure(state="normal", placeholder_text="Ej: 2")
        
        semestre = self.entry_semestre.get()
        
        #Si el usuario puso un numero
        if semestre.isdigit():
            #Si es un numero válido para ser un semestre
            if (1 <= int(semestre) <= 14):
                #Se habilita la sección de asiganturas y se le entregan las opciones ccorrespondientes
                asignaturas = cargar_jsons(ASIGNATURAS)
                opciones = [asig for asig in asignaturas if area in asignaturas[asig]["especialidad"] and int(semestre) == int(asignaturas[asig]["semestre"])]
                
                self.seleccion_asignatura.configure(state="normal", values=opciones)
                self.seleccion_profe.set("Seleccione al profesor")
                self.seleccion_profe.configure(state="disabled")
            else:
                self.seleccion_asignatura.set("Seleccione la asignatura")
                self.seleccion_asignatura.configure(state="disabled", values=[])
                self.seleccion_profe.set("Seleccione al profesor")
                self.seleccion_profe.configure(state="disabled")
        else:
            self.seleccion_asignatura.set("Seleccione la asignatura")
            self.seleccion_asignatura.configure(state="disabled", values=[])
            self.seleccion_profe.set("Seleccione al profesor")
            self.seleccion_profe.configure(state="disabled")
        
        asignatura = self.seleccion_asignatura.get()
        asignaturas = cargar_jsons(ASIGNATURAS)
        
        if asignatura != "Seleccione la asignatura":
            if area not in asignaturas[asignatura]["especialidad"]:
                self.seleccion_asignatura.set("Seleccione la asignatura")
                self.seleccion_asignatura.configure(state="disabled", values=[])
                self.seleccion_profe.set("Seleccione al profesor")
                self.seleccion_profe.configure(state="disabled")
        
        
        
    #Función que se ejecuta cuando se preciona una tecla en el entry de semestres
    def actualizar_asignaturas(self, event):
        #Se sacan los valores de area y semestre
        area = self.seccion_area.get()
        semestre = self.entry_semestre.get()
        
        #Si el usuario puso un numero
        if semestre.isdigit():
            #Si es un numero válido para ser un semestre
            if (1 <= int(semestre) <= 14):
                #Se habilita la sección de asiganturas y se le entregan las opciones ccorrespondientes
                asignaturas = cargar_jsons(ASIGNATURAS)
                opciones = [asig for asig in asignaturas if area in asignaturas[asig]["especialidad"] and int(semestre) == int(asignaturas[asig]["semestre"])]
                self.seleccion_profe.set("Seleccione al profesor")
                self.seleccion_profe.configure(state="disabled")
                
                self.seleccion_asignatura.configure(state="normal", values=opciones)
            else:
                self.seleccion_asignatura.set("Seleccione la asignatura")
                self.seleccion_asignatura.configure(state="disabled", values=[])
                self.seleccion_profe.set("Seleccione al profesor")
                self.seleccion_profe.configure(state="disabled")
        else:
            self.seleccion_asignatura.set("Seleccione la asignatura")
            self.seleccion_asignatura.configure(state="disabled", values=[])
            self.seleccion_profe.set("Seleccione al profesor")
            self.seleccion_profe.configure(state="disabled")
    
    def actualizar_profes(self, asig):
        area = self.seccion_area.get()
        
        datos_profes = cargar_jsons(PROFESORES)
        
        opciones = [datos_profes[profe]["nombre"] for profe in datos_profes if area in datos_profes[profe]["especialidad"]]
        
        self.seleccion_profe.configure(state="normal", values=opciones)


#Ventana la cual permitirá ver los alumnos que hay en cierta asignatura de un profesor
class VentanaVerAlumnos(ctk.CTkToplevel):
    def __init__(self, email, asignatura):
        super().__init__()
        #Configuración de la ventana
        self.email = email
        self.asignatura = asignatura
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Alumnos")
        
        #Se cargan los datos del profesor
        datos_profes = cargar_jsons(PROFESORES)
        info = datos_profes[email]
        
        #Se crea al profesor
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


#Ventana para añadir una Facultad
class AñadirFacultad(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__()
        
        #Configuración de la ventana
        self.master = master
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Añadir Facultad")
        
        frame_superior = ctk.CTkFrame(self, height=TOPLEVEL_ALTO*0.16, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_superior.pack(fill="x")
        
        ctk.CTkLabel(frame_superior, text="Añadir Facultad", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.5, rely=0.5, anchor="center")
        
        frame_inferior = ctk.CTkFrame(self, height=TOPLEVEL_ALTO*0.84, fg_color=COLOR_AZUL, border_width=2, border_color=COLOR_FONTS)
        frame_inferior.pack(fill="x")
        
        frame_contenedor = ctk.CTkFrame(frame_inferior, fg_color=COLOR_FONDO)
        frame_contenedor.pack()
        
        frame_info = ctk.CTkFrame(frame_contenedor, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
        frame_info.pack()
            
        ctk.CTkLabel(frame_info, text="Ingrese la facultad nueva que tendrá el instituto epsilon, sea completamente conciente al añadirla. Una vez añadido se le podrán asociar a nuevas carreras que sean ingresadas, recuerde seguir el formato de 'Facultad de ____' para una correcta legibilidad y profesionalidad", wraplength=TOPLEVEL_ANCHO* 0.75, font=Fonts.i2, justify="left", text_color=COLOR_FONTS).pack(padx=30, pady=30)
        
        #Ingresar los nombres
        frame_facultad = ctk.CTkFrame(frame_contenedor, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
        frame_facultad.pack(fill="x", expand=True)
        
        
        ctk.CTkLabel(frame_facultad, text="Ingrese el nombre de la Facultad", width=TOPLEVEL_ANCHO*0.75, font=Fonts.i1, anchor="w", text_color=COLOR_FONTS).pack(pady=40)
        
        nombre_facultad = ctk.CTkEntry(frame_facultad, font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, placeholder_text="Ej: Facultad de Ingeniería", border_width=2, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, height=47)
        nombre_facultad.pack()
        
        label_facultad = ctk.CTkLabel(frame_facultad, text="", font=Fonts.i3)
        label_facultad.pack(pady=10)
        
        def añadir_facultad():
            facultad = nombre_facultad.get()
            
            if not verificar_facultad(facultad):
                nombre_facultad.configure(border_color = "red")
                label_facultad.configure(text="Nombre de facultad inválido", text_color="red")
                return

            datos = cargar_jsons(FACULTADES)
            
            datos[facultad] = {
                "nombre": facultad,
                "carreras": []
            }
            guardar_datos(FACULTADES, datos)
            
            master.mostrar_facultades()
            
            self.destroy()
        
        ctk.CTkButton(frame_inferior, text="Añadir Facultad", font=Fonts.m2bold, text_color=COLOR_FONTS, border_width=2, border_color=COLOR_FONTS, fg_color=COLOR_FONDO, hover_color=COLOR_AZUL, command=añadir_facultad).pack(pady=40)


#Ventana para añadir carreras
class AñadirCarreras(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__()
        
        #Configuración de la ventana
        self.master = master
        self.minsize(TOPLEVEL_ANCHO, TOPLEVEL_ALTO)
        self.resizable(False, False)
        self.title("Añadir Carreras")
        
        #Frame del titulo
        frame_superior = ctk.CTkFrame(self, height=TOPLEVEL_ALTO*0.16, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_superior.pack(fill="x")
        #Label con el título
        ctk.CTkLabel(frame_superior, text="Añadir Carreras", font=Fonts.m1, text_color=COLOR_FONTS).place(relx=0.5, rely=0.5, anchor="center")
        
        #   Frame inferior que contendrá todo el formulario
        frame_inferior = ctk.CTkScrollableFrame(self, height=TOPLEVEL_ALTO*0.84, fg_color=COLOR_AZUL, border_width=2, border_color=COLOR_FONTS)
        frame_inferior.pack(fill="x")
        
        #Frame contenedor que contendrá los datos
        frame_contenedor = ctk.CTkFrame(frame_inferior, fg_color=COLOR_FONDO)
        frame_contenedor.pack(pady=20)
        
        #Frame para la información inicial
        frame_info = ctk.CTkFrame(frame_contenedor, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
        frame_info.pack()
            
        ctk.CTkLabel(frame_info, text="Ingrese el nombre de la nueva carrera que se impartirá en el instituto, especificando claramente el nombre de dicha carrera, los semestres de duración y la facultad a la que pertenece.", wraplength=TOPLEVEL_ANCHO* 0.75, font=Fonts.i2, justify="left", text_color=COLOR_FONTS).pack(padx=30, pady=30)
        
        #           Ingresar el nombre de la carrera
        
        #Frame que contendrá el nombre de la carrera
        frame_nombre = ctk.CTkFrame(frame_contenedor, border_width=1, border_color=COLOR_FONTS, fg_color=COLOR_FONDO)
        frame_nombre.pack(fill="x", expand=True)
        
        #Label indicativo
        ctk.CTkLabel(frame_nombre, text="Ingrese el nombre de la Carrera:", width=TOPLEVEL_ANCHO*0.75, font=Fonts.i1, anchor="w", text_color=COLOR_FONTS).pack(pady=40)
        
        #Entrada de texto para el nombre
        nombre_carrera = ctk.CTkEntry(frame_nombre, font=Fonts.i2, width=TOPLEVEL_ANCHO*0.6, placeholder_text="Ej: Ingeniería Civil en Informática", border_width=2, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, height=47)
        nombre_carrera.pack()
        
        #Label por si ocurre un error
        label_nombre = ctk.CTkLabel(frame_nombre, text="", font=Fonts.i3)
        label_nombre.pack(pady=10)
        
        
        #           Semestres de dicha carrera
        
        #Frame que contendrá la información
        frame_semestres = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS)
        frame_semestres.pack(fill="x", expand=True)
        
        ctk.CTkLabel(frame_semestres, text="Ingrese la duración (semestres): ", width=TOPLEVEL_ANCHO*0.75, font=Fonts.i1, anchor="w", text_color=COLOR_FONTS).pack(pady=40)
        
        duracion_semestres = ctk.CTkOptionMenu(frame_semestres, values=["8", "9", "10", "11", "12", "13", "14"])
        duracion_semestres.set("Seleccione la duración")
        duracion_semestres.pack()
        
        label_semestres = ctk.CTkLabel(frame_semestres, text="", font=Fonts.i3)
        label_semestres.pack(pady=10)
        
        #Frame para ver las facultades
        frame_facultades = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, border_width=2)
        frame_facultades.pack(fill="x", expand=True)
        
        ctk.CTkLabel(frame_facultades, text="Seleccione la facultad a la que pertenece:", width=TOPLEVEL_ANCHO*0.75, font=Fonts.i1, anchor="w", text_color=COLOR_FONTS).pack(pady=40)
        
        datos_facultades = cargar_jsons(FACULTADES)
        
        facultades = sorted(datos_facultades.keys())
        
        menu_facultades = ctk.CTkOptionMenu(frame_facultades, values=facultades)
        menu_facultades.set("Seleccione una facultad")
        menu_facultades.pack()
        
        label_facultades = ctk.CTkLabel(frame_facultades, text="", font=Fonts.i3)
        label_facultades.pack(pady=10)

        
        #Función para añadir la carrera en la base de datos
        def añadir_carrera():
            #Se obtienen los valores que se dieron en los campos anteriores
            nombre = nombre_carrera.get()
            semestres = duracion_semestres.get()
            facultad = menu_facultades.get()
            
            #Se verifica que el nombre sea válido
            if len(nombre) < 4 or not es_string(nombre):
                nombre_carrera.configure(border_color="red")
                label_nombre.configure(text="Nombre Inválido", text_color="red")
                return
            else:
                nombre_carrera.configure(border_color="green")
                label_nombre.configure(text="")
            
            #Se verifica que se haya seleccionado los semestres
            if semestres == "Seleccione la duración":
                label_semestres.configure(text="Seleccione un semestre", text_color="red")
                return
            else:
                label_semestres.configure(text="")
            
            #Se verifica que se haya seleccionado una facultad
            if facultad == "Seleccione una facultad":
                label_facultades.configure(text="Seleccione una facultad", text_color="red")
                return
            else:
                label_facultades.configure(text="")
            
            #Cargar los datos que hay en las carreras
            datos_carreras = cargar_jsons(CARRERAS)
            datos_facultades = cargar_jsons(FACULTADES)
            
            #Se agregan los datos de la carrrera
            datos_carreras[nombre] = {
                "nombre": nombre,
                "facultad": facultad,
                "malla": {str(i): [] for i in range(1, int(semestres) + 1)},
                "semestres": int(semestres),
                "alumnos": [],
                "habilitado": False
            }
            
            #Se añade a la base de datos de las facultades la carrera
            datos_facultades[facultad]["carreras"].append(nombre)
            
            #Se guardan los datos
            guardar_datos(CARRERAS, datos_carreras)
            guardar_datos(FACULTADES, datos_facultades)
            
            #Se actualiza la pantalla
            master.mostrar_carreras()
            #Se destruye la ventana
            self.destroy()
        
        ctk.CTkButton(frame_inferior, text="Añadir Carrera", font=Fonts.m2bold, text_color=COLOR_FONTS, border_width=2, border_color=COLOR_FONTS, fg_color=COLOR_FONDO, hover_color=COLOR_AZUL, command=añadir_carrera).pack(pady=40)
        
        #Se define el scroll para la ventana
        def scroll(event):
            #Accerder al scroll
            canvas = frame_inferior._parent_canvas  

            #       Scroll tanto para Windows, MacOS y Linux
            
            #Si el scroll es positivo (en caso de Linux el scroll hacia arriba se considera el boton 4), se realiza el scroll
            if event.num == 4 or event.delta > 0:
                canvas.yview_scroll(-1, "units")
                
            #Si el scroll es negativo (en caso de Linux el scroll hacia abajo se considera el boton 5), se realiza el scroll
            elif event.num == 5 or event.delta < 0:
                canvas.yview_scroll(1, "units")
        
        #Scroll para Windows y MacOS
        frame_inferior.bind_all("<MouseWheel>", scroll)
        
        #Scroll para Linux
        frame_inferior.bind_all("<Button-4>", scroll)
        frame_inferior.bind_all("<Button-5>", scroll)


#Ventana para crear la malla curricular de dicha carrera
class VentanaCrearMalla(ctk.CTkToplevel):
    def __init__(self, master, carrera):
        super().__init__()
        
        #Configuración de la ventana
        self.master = master
        self.carrera = carrera
        self.title("Crear Malla Curricular")
        self.configure(fg_color=COLOR_FONDO)
        self.minsize(MIN_ANCHO, MIN_ALTO)
        self.resizable(False, False)
        
        #Se cargan los datos de la carrera
        self.datos_carrera = cargar_jsons(CARRERAS)
        self.info_carrera = self.datos_carrera[carrera]
        
        #Se carga la malla
        self.malla = self.info_carrera["malla"]
        
        #Se crea un tab para los semestres
        self.tabs = ctk.CTkTabview(self, width=MIN_ANCHO * 0.95, height=MIN_ALTO * 0.85, fg_color=COLOR_AZUL, text_color=COLOR_FONTS, segmented_button_fg_color=COLOR_FONTS, segmented_button_selected_color=COLOR_FONDO, segmented_button_unselected_color=COLOR_AZUL, border_width=2, border_color=COLOR_FONTS)
        self.tabs.pack(pady=10)
        
        #Se crea el primer tab con el primer semestre
        self.i = 1
        self.tabs_semestres(self.i)
        
        #Guardar los datos de todos los semstres en la base de datos
        def guardar_datos_malla():
            
            #Se comprueba si hay algún semestre que no posea asignaturas
            for i in range(self.info_carrera["semestres"]):
                if self.malla[str(i + 1)] == []:
                    label_error.configure(text=f"Falta añadir asignatuars en el {i + 1}° Semestre.", text_color="red")
                    return
            
            #Se cargan los datos de la carrera
            datos_carrera = cargar_jsons(CARRERAS)
            datos_asignaturas = cargar_jsons(ASIGNATURAS)
            datos_mallas = self.comparar_mallas(datos_carrera[carrera]["malla"], self.malla)
            
            if datos_mallas["eliminados"]:
                for asig in datos_mallas["eliminados"]:
                    datos_asignaturas[asig]["carreras"].remove(carrera)
            
            if datos_mallas["añadidos"]:
                for asig in datos_mallas["añadidos"]:
                    datos_asignaturas[asig]["carreras"].append(carrera)
            
            #Se guarda la malla en la base de datos
            datos_carrera[carrera]["malla"] = self.malla
            guardar_datos(CARRERAS, datos_carrera)
            guardar_datos(ASIGNATURAS, datos_asignaturas)
            
            #Se actualiza
            master.mostrar_carreras()
            #Se destruye la ventana
            self.destroy()
        
        #Botón para guardar en la base de datos la malla
        ctk.CTkButton(self, text="Crear Malla", fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS, text_color=COLOR_FONTS, font=Fonts.m2bold, border_spacing=10, hover_color=COLOR_AZUL, command=guardar_datos_malla).pack(pady=40)
        
        label_error = ctk.CTkLabel(self, text="", font=Fonts.i3)
        label_error.pack()
        
    #Función para crear los tabs de los semestres 
    def tabs_semestres(self, semestre):
        
        tab = self.tabs.add(f"{semestre}° Semestre")
        
        #Frame superior que contendrá el título
        frame_superior = ctk.CTkFrame(tab, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, border_width=2, height=MIN_ALTO*0.16)
        frame_superior.pack(fill="x")
        
        #Título
        ctk.CTkLabel(frame_superior, text=f"{semestre}° Semestre", text_color=COLOR_FONTS, font=Fonts.m1).place(relx=0.5, rely=0.5, anchor="center")
        
        #Frame Inferior
        frame_inferior = ctk.CTkFrame(tab, height=MIN_ALTO*0.9, fg_color=COLOR_AZUL)
        frame_inferior.pack(fill="x")
        
        #Frame inferior contenedor
        frame_contenedor = ctk.CTkFrame(frame_inferior, fg_color="transparent")
        frame_contenedor.pack(pady=(30, 0))

        #Frame info
        frame_info = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_width=2,border_color=COLOR_FONTS, width=MIN_ANCHO*0.8)
        frame_info.pack()
        
        ctk.CTkLabel(frame_info, text=f"Ingrese adecuadamente las asignaturas del {semestre}° Semestre. Recuerde que como mínimo se deben ingresar 2 asignatura por semestre y un máximo de 6 asignaturas. Todas deben tener coherencia con la carrera elegida.", text_color=COLOR_FONTS, font=Fonts.i3, wraplength=MIN_ANCHO*0.7).place(relx=0.5, rely=0.5, anchor="center")
        
        #Frame para los option menu de las asignaturas
        frame_asignatura = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_AZUL, height=MIN_ALTO*0.3)
        frame_asignatura.pack(fill="x")
        
        #Se cargan los datos
        datos_asignatura = cargar_jsons(ASIGNATURAS)
        
        #Opciones Iniciales
        opciones = sorted([a for a in datos_asignatura if datos_asignatura[a]["semestre"] == semestre])
        
        #Asignaturas que no pueden estar en las opciones
        asig_invalidas = []
        
        #Si el semestre es mayor que 1 se eliminarán las asignaturas invalidas, las cuales son las que no tienen sus prerequisitos el semestre anterior
        if semestre > 1:
            #Datos del semestre anterior para ver prerequisitos
            datos_anteriores = self.malla[str(semestre - 1)]
            
            #Por cada opcion en opciones se verá si su prerequisito está en el semestre anterior
            for opcion in opciones:
                #Se toma la lista de los prerequisitos que posee cada opcion
                prerequisitos = datos_asignatura[opcion]["prerequisitos"]

                #Si la asignatura posee prerequisitos y no estan sus prerequisitos en el semestre anterior se agrega a las asignaturas invalidas
                if prerequisitos and not all(pre in datos_anteriores for pre in prerequisitos):
                    asig_invalidas.append(opcion)
        
        #Por cada asignatura en asignaturas invalidas se eliminará de las opciones
        for asig in asig_invalidas:
            opciones.remove(asig)
        
        #Se inserta la opción nula
        opciones.insert(0, "--------")
        
        #Variables que guardarán los valores de cada opction menu y además se guardan los option menus
        valores = []
        menus = []
        
        #Función que actualiza todos los opcion menus para evitar repetir asignaturas
        def actualizar_opciones(valor=None):
            #Se ven todas las asignaturas seleccionadas
            seleccionadas = [var.get() for var in valores if var.get() != "--------"]
            
            #Por cada option menu creado se creará una lista nueva de opciones que pueden contener
            for menu in menus:
                #Nuevas opciones por option menu
                nuevas_opciones = ["--------"]
                
                #Pop cada opcion se eliminará solo si la asignatura ya fue seleccionada por otro menu
                for opcion in opciones:
                    if opcion == "--------":
                        continue
                    
                    if opcion not in seleccionadas:
                        nuevas_opciones.append(opcion)

                #Se ordenan las opciones
                nuevas_opciones.sort()
                #Se agregan las nuevas opciones a cada menu
                menu.configure(values=nuevas_opciones)
        
        #Crear los 6 menus para ingresar las asignaturas
        for i in range(7):
            #Variable iniciadora
            var = ctk.StringVar(value="--------")
            #Creando el option menu
            menu = ctk.CTkOptionMenu(frame_asignatura, values=opciones, variable=var, command=lambda valor=None: actualizar_opciones(), font=Fonts.i3, width=MIN_ANCHO*0.35, height=MIN_ALTO*0.05, fg_color=COLOR_FONDO, button_color=COLOR_OSCURO, text_color=COLOR_FONTS, anchor="center", dropdown_font=Fonts.i3, dropdown_fg_color=COLOR_FONDO, dropdown_text_color=COLOR_FONTS, dropdown_hover_color=COLOR_AZUL)
            #Se añaden a las variables creadas anteriormente
            valores.append(var)
            menus.append(menu)
        
        #Se pocisionan en la interfaz
        menus[0].place(relx=0.05, rely=0.1)
        menus[1].place(relx=0.55, rely=0.1)
        menus[2].place(relx=0.05, rely=0.3)
        menus[3].place(relx=0.55, rely=0.3)
        menus[4].place(relx=0.05, rely=0.5)
        menus[5].place(relx=0.55, rely=0.5)
        menus[6].place(relx=0.05, rely=0.7)
        
        
        #Función para guardar por semestre
        def guardar():
            #Se toman todas las asignaturas seleccionadas
            seleccionadas = [v.get() for v in valores if v.get() != "--------"]
            
            #Si hay menos de 2 se le avisa al admin que no cumple con las minimas asignaturas
            if len(seleccionadas) < 2:
                label_error.configure(text="Seleccione al menos 2 Asignaturas.", text_color="red")
                return
            else:
                label_error.configure(text="Asignaturas guardadas.", text_color="green")
            
            #Por cada menu este se desactivará
            for i in range(7):
                menus[i].configure(state="disabled")
            
            #Se actualiza la malla, más no en la base de datos
            self.malla[str(semestre)] = seleccionadas
            
            
            #Se crea un nuevo tab con el siguiente semnestre
            if int(self.info_carrera["semestres"]) == int(self.i):
                return
            else:
                j = int(semestre)
                if self.i < j + 1:
                    self.i += 1
                    self.tabs_semestres(self.i)
                else:
                    return

        #Botón para guardar
        ctk.CTkButton(tab, text="Guardar Semestre", command=guardar, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS, text_color=COLOR_FONTS, font=Fonts.m3, border_spacing=10, hover_color=COLOR_AZUL).place(relx=0.5, rely=0.88, anchor="center")
        #Label de error
        label_error = ctk.CTkLabel(tab, text="", font=Fonts.i3)
        label_error.place(relx=0.5, rely=0.93, anchor="center")
        
    #Función para comparar la malla antigua y la nueva
    def comparar_mallas(self, malla_antigua: dict, malla_nueva: dict):
        
        #Se guardan las asignaturas antiguas en un conjunto
        asig_antigua = set()
        for cursos in malla_antigua.values():
            asig_antigua.update(cursos)
        #Se guardan las asignaturas nuevas en un conjunto
        asig_nueva = set()
        for cursos in malla_nueva.values():
            asig_nueva.update(cursos)

        #Se ven cuales fueron añadidas
        añadidos = asig_nueva - asig_antigua
        #Se ven cuales fueron eliminadas
        eliminados = asig_antigua - asig_nueva

        return {
            "añadidos": añadidos,
            "eliminados": eliminados
        }


#Ventana para la confirmación de eliminación
class VentanaConfirmacion(ctk.CTkToplevel):
    def __init__(self, rol: str, asignatura, master, email_profesor, email_alumno):
        super().__init__()
        
        #Configuración de la ventana
        self.rol = rol
        self.asignatura = asignatura
        self.master = master
        self.email_profesor = email_profesor
        self.email_alumno = email_alumno
        self.title("Confirmación")
        self.configure(fg_color=COLOR_FONDO)
        self.minsize(TOPLEVEL_ANCHO*0.6, TOPLEVEL_ALTO*0.4)
        self.resizable(False, False)
        
        if rol == "Alumno":
            ctk.CTkLabel(self, text="¿Está seguro/a de eliminar al Alumno?", font=Fonts.m2bold, text_color=COLOR_FONTS, wraplength=TOPLEVEL_ANCHO*0.55).place(relx=0.5, rely=0.3, anchor="center")
        elif rol == "Profesor":
            ctk.CTkLabel(self, text="¿Está seguro/a de eliminar al Profesor?", font=Fonts.m2bold, text_color=COLOR_FONTS, wraplength=TOPLEVEL_ANCHO*0.55).place(relx=0.5, rely=0.3, anchor="center")
        elif rol == "Asignatura":
            ctk.CTkLabel(self, text="¿Está seguro/a de eliminar la Asignatura?", font=Fonts.m2bold, text_color=COLOR_FONTS, wraplength=TOPLEVEL_ANCHO*0.55).place(relx=0.5, rely=0.3, anchor="center")
        
        ctk.CTkButton(self, text="Eliminar", fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_ELIMINAR, text_color=COLOR_ELIMINAR , hover_color=COLOR_AZUL, font=Fonts.i1, command=self.eliminar).place(relx=0.1, rely=0.7)
        
        ctk.CTkButton(self, text="Cancelar", fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_CONFIRMACION, text_color=COLOR_CONFIRMACION, hover_color=COLOR_AZUL, font=Fonts.i1, command=lambda: self.destroy()).place(relx=0.6, rely=0.7)
    
    def eliminar(self):
        
        if self.rol == "Alumno":
            eliminar_datos_alumno(self.email_alumno)
            self.master.mostrar_alumnos()
            self.destroy()
        elif self.rol == "Profesor":
            eliminar_datos_profesor(self.email_profesor)
            self.master.mostrar_profesores()
            self.destroy()
            


#Ventana para confirmar la habilitacion de la carrera
class VentanaHabilitacion(ctk.CTkToplevel):
    def __init__(self, boton, carrera, master):
        super().__init__()
        
        #Configuración inicial
        self.boton = boton
        self.carrera = carrera
        self.master = master
        self.configure(fg_color=COLOR_FONDO)
        self.minsize(TOPLEVEL_ANCHO*0.6, TOPLEVEL_ALTO*0.4)
        self.resizable(False, False)
        
        #Se saca el texto que posee el boton
        self.texto_boton = self.boton.cget("text")
        
        #Si el boton dice habilitar se ejecuta su respectiva ventana
        if self.texto_boton == "Habilitar":
            #Se cambia el titulo
            self.title("Habilitar Carrera")
            
            #Label de confirmación
            ctk.CTkLabel(self, text="¿Está seguro/a de Habilitar la carrera?", font=Fonts.m2bold, text_color=COLOR_FONTS, wraplength=TOPLEVEL_ANCHO*0.55).place(relx=0.5, rely=0.3, anchor="center")
            
            #Botones para habilitar y cancelar
            ctk.CTkButton(self, text="Habilitar", fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_CONFIRMACION, text_color=COLOR_CONFIRMACION, hover_color=COLOR_AZUL, font=Fonts.i1, command=self.habilitar).place(relx=0.1, rely=0.7)
        
            ctk.CTkButton(self, text="Cancelar", fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_ELIMINAR, text_color=COLOR_ELIMINAR, hover_color=COLOR_AZUL, font=Fonts.i1, command=lambda: self.destroy()).place(relx=0.6, rely=0.7)
        #Se lo contrario (Si dice Deshabilitar)
        else:
            #Se cambia el titulo
            self.title("Deshabilitar Carrera")
            #Label de confirmación
            ctk.CTkLabel(self, text="¿Está seguro/a de Deshabilitar la carrera?", font=Fonts.m2bold, text_color=COLOR_FONTS, wraplength=TOPLEVEL_ANCHO*0.55).place(relx=0.5, rely=0.3, anchor="center")
            
            #Botones para deshabilitar y cancelar
            ctk.CTkButton(self, text="Deshabilitar", fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_ELIMINAR, text_color=COLOR_ELIMINAR , hover_color=COLOR_AZUL, font=Fonts.i1, command=self.deshabilitar).place(relx=0.1, rely=0.7)
        
            ctk.CTkButton(self, text="Cancelar", fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_CONFIRMACION, text_color=COLOR_CONFIRMACION, hover_color=COLOR_AZUL, font=Fonts.i1, command=lambda: self.destroy()).place(relx=0.6, rely=0.7)
    
    #Función para Habilitar la carrera
    def habilitar(self):
        #Se cargan los datos de la carrera
        datos_carrera = cargar_jsons(CARRERAS)
        #Se cambia el estado de habilitado a Verdadero
        datos_carrera[self.carrera]["habilitado"] = True
        #Se guardan los datos cambiados
        guardar_datos(CARRERAS, datos_carrera)
        #Se carga la página
        self.master.mostrar_carreras()
        #Se destruye la ventana
        self.destroy()
        
    def deshabilitar(self):
        #Se cargan los datos de la carrera
        datos_carrera = cargar_jsons(CARRERAS)
        #Se cambia el estado de habilitado a Falso
        datos_carrera[self.carrera]["habilitado"] = False
        #Se guardan los datos cambiados
        guardar_datos(CARRERAS, datos_carrera)
        #Se carga la página
        self.master.mostrar_carreras()
        #Se destruye la ventana
        self.destroy()
        

#Ventana para aclarar que la carrera seleccionada no posee malla
class VentanaNegacion(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Falta de Malla")
        self.configure(fg_color=COLOR_FONDO)
        self.minsize(TOPLEVEL_ANCHO*0.5, TOPLEVEL_ALTO*0.4)
        self.resizable(False, False)
        
        ctk.CTkLabel(self, text="Esta carrera no posee una malla curricular. Necesita crear una primero", font=Fonts.i2, wraplength=TOPLEVEL_ANCHO*0.45, text_color=COLOR_FONTS).place(relx=0.5, rely=0.5, anchor="center")


#Ventana para crear la malla curricular de dicha carrera
class VentanaModificarMalla(ctk.CTkToplevel):
    def __init__(self, master, carrera):
        super().__init__()
        
        #Configuración de la ventana
        self.master = master
        self.carrera = carrera
        self.title("Modificar Malla Curricular")
        self.configure(fg_color=COLOR_FONDO)
        self.minsize(MIN_ANCHO, MIN_ALTO)
        self.resizable(False, False)
        
        #Se cargan los datos de la carrera
        self.datos_carrera = cargar_jsons(CARRERAS)
        self.info_carrera = self.datos_carrera[carrera]
        
        #Se carga la malla
        self.malla = self.info_carrera["malla"]
        
        #Se crea un tab para los semestres
        self.tabs = ctk.CTkTabview(self, width=MIN_ANCHO * 0.95, height=MIN_ALTO * 0.85, fg_color=COLOR_AZUL, text_color=COLOR_FONTS, segmented_button_fg_color=COLOR_FONTS, segmented_button_selected_color=COLOR_FONDO, segmented_button_unselected_color=COLOR_AZUL, border_width=2, border_color=COLOR_FONTS)
        self.tabs.pack(pady=10)
        
        #Se crea el primer tab con el primer semestre
        self.i = 1
        self.tabs_semestres(self.i)
        
        #Guardar los datos de todos los semstres en la base de datos
        def guardar_datos_malla():
            
            #Se comprueba si hay algún semestre que no posea asignaturas
            for i in range(self.info_carrera["semestres"]):
                if self.malla[str(i + 1)] == []:
                    label_error.configure(text=f"Falta añadir asignatuars en el {i + 1}° Semestre.", text_color="red")
                    return
            
            #Se cargan los datos de la carrera
            datos_carrera = cargar_jsons(CARRERAS)
            datos_asignaturas = cargar_jsons(ASIGNATURAS)
            datos_mallas = self.comparar_mallas(datos_carrera[carrera]["malla"], self.malla)
            
            if datos_mallas["eliminados"]:
                for asig in datos_mallas["eliminados"]:
                    datos_asignaturas[asig]["carreras"].remove(carrera)
            
            if datos_mallas["añadidos"]:
                for asig in datos_mallas["añadidos"]:
                    datos_asignaturas[asig]["carreras"].append(carrera)
            
            #Se guarda la malla en la base de datos
            datos_carrera[carrera]["malla"] = self.malla
            guardar_datos(CARRERAS, datos_carrera)
            guardar_datos(ASIGNATURAS, datos_asignaturas)
            #Se actualiza
            master.mostrar_carreras()
            #Se destruye la ventana
            self.destroy()
        
        #Botón para guardar en la base de datos la malla
        ctk.CTkButton(self, text="Crear Malla", fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS, text_color=COLOR_FONTS, font=Fonts.m2bold, border_spacing=10, hover_color=COLOR_AZUL, command=guardar_datos_malla).pack(pady=40)
        
        label_error = ctk.CTkLabel(self, text="", font=Fonts.i3)
        label_error.pack()
        
    #Función para crear los tabs de los semestres 
    def tabs_semestres(self, semestre):
        
        tab = self.tabs.add(f"{semestre}° Semestre")
        
        #Frame superior que contendrá el título
        frame_superior = ctk.CTkFrame(tab, fg_color=COLOR_FONDO, border_color=COLOR_FONTS, border_width=2, height=MIN_ALTO*0.16)
        frame_superior.pack(fill="x")
        
        #Título
        ctk.CTkLabel(frame_superior, text=f"{semestre}° Semestre", text_color=COLOR_FONTS, font=Fonts.m1).place(relx=0.5, rely=0.5, anchor="center")
        
        #Frame Inferior
        frame_inferior = ctk.CTkFrame(tab, height=MIN_ALTO*0.9, fg_color=COLOR_AZUL)
        frame_inferior.pack(fill="x")
        
        #Frame inferior contenedor
        frame_contenedor = ctk.CTkFrame(frame_inferior, fg_color="transparent")
        frame_contenedor.pack(pady=(30, 0))

        #Frame info
        frame_info = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_FONDO, border_width=2,border_color=COLOR_FONTS, width=MIN_ANCHO*0.8)
        frame_info.pack()
        
        ctk.CTkLabel(frame_info, text=f"Ingrese adecuadamente las asignaturas del {semestre}° Semestre. Recuerde que como mínimo se deben ingresar 2 asignatura por semestre y un máximo de 6 asignaturas. Todas deben tener coherencia con la carrera elegida.", text_color=COLOR_FONTS, font=Fonts.i3, wraplength=MIN_ANCHO*0.7).place(relx=0.5, rely=0.5, anchor="center")
        
        #Frame para los option menu de las asignaturas
        frame_asignatura = ctk.CTkFrame(frame_contenedor, fg_color=COLOR_AZUL, height=MIN_ALTO*0.3)
        frame_asignatura.pack(fill="x")
        
        #Se cargan los datos
        datos_asignatura = cargar_jsons(ASIGNATURAS)
        
        #Opciones Iniciales
        opciones = sorted([a for a in datos_asignatura if datos_asignatura[a]["semestre"] == semestre])
        
        #Asignaturas que no pueden estar en las opciones
        asig_invalidas = []
        
        #Si el semestre es mayor que 1 se eliminarán las asignaturas invalidas, las cuales son las que no tienen sus prerequisitos el semestre anterior
        if semestre > 1:
            #Datos del semestre anterior para ver prerequisitos
            datos_anteriores = self.malla[str(semestre - 1)]
            
            #Por cada opcion en opciones se verá si su prerequisito está en el semestre anterior
            for opcion in opciones:
                #Se toma la lista de los prerequisitos que posee cada opcion
                prerequisitos = datos_asignatura[opcion]["prerequisitos"]

                #Si la asignatura posee prerequisitos y no estan sus prerequisitos en el semestre anterior se agrega a las asignaturas invalidas
                if prerequisitos and not all(pre in datos_anteriores for pre in prerequisitos):
                    asig_invalidas.append(opcion)
        
        #Por cada asignatura en asignaturas invalidas se eliminará de las opciones
        for asig in asig_invalidas:
            opciones.remove(asig)
        
        #Se inserta la opción nula
        opciones.insert(0, "--------")
        
        #Variables que guardarán los valores de cada opction menu y además se guardan los option menus
        valores = []
        menus = []
        
        #Función que actualiza todos los opcion menus para evitar repetir asignaturas
        def actualizar_opciones(valor=None):
            #Se ven todas las asignaturas seleccionadas
            seleccionadas = [var.get() for var in valores if var.get() != "--------"]
            
            #Por cada option menu creado se creará una lista nueva de opciones que pueden contener
            for menu in menus:
                #Nuevas opciones por option menu
                nuevas_opciones = ["--------"]
                
                #Pop cada opcion se eliminará solo si la asignatura ya fue seleccionada por otro menu
                for opcion in opciones:
                    if opcion == "--------":
                        continue
                    
                    if opcion not in seleccionadas:
                        nuevas_opciones.append(opcion)

                #Se ordenan las opciones
                nuevas_opciones.sort()
                #Se agregan las nuevas opciones a cada menu
                menu.configure(values=nuevas_opciones)
        
        datos_carrera = cargar_jsons(CARRERAS)
        asig_semestre = datos_carrera[self.carrera]["malla"][str(semestre)]
        
        opciones_actuales = [opcion for opcion in opciones if opcion not in asig_semestre]
        
        #Crear los 6 menus para ingresar las asignaturas
        for i in range(7):
            #Variable iniciadora
            if i < len(asig_semestre):
                var = ctk.StringVar(value=asig_semestre[i])
            else:
                var = ctk.StringVar(value="--------")
            #Creando el option menu
            menu = ctk.CTkOptionMenu(frame_asignatura, values=opciones_actuales, variable=var, command=lambda valor=None: actualizar_opciones(), font=Fonts.i3, width=MIN_ANCHO*0.35, height=MIN_ALTO*0.05, fg_color=COLOR_FONDO, button_color=COLOR_OSCURO, text_color=COLOR_FONTS, anchor="center", dropdown_font=Fonts.i3, dropdown_fg_color=COLOR_FONDO, dropdown_text_color=COLOR_FONTS, dropdown_hover_color=COLOR_AZUL)
            
            
            #Se añaden a las variables creadas anteriormente
            valores.append(var)
            menus.append(menu)
        
        #Se pocisionan en la interfaz
        menus[0].place(relx=0.05, rely=0.1)
        menus[1].place(relx=0.55, rely=0.1)
        menus[2].place(relx=0.05, rely=0.3)
        menus[3].place(relx=0.55, rely=0.3)
        menus[4].place(relx=0.05, rely=0.5)
        menus[5].place(relx=0.55, rely=0.5)
        menus[6].place(relx=0.05, rely=0.7)
        
        
        #Función para guardar por semestre
        def guardar():
            #Se toman todas las asignaturas seleccionadas
            seleccionadas = [v.get() for v in valores if v.get() != "--------"]
            
            #Si hay menos de 2 se le avisa al admin que no cumple con las minimas asignaturas
            if len(seleccionadas) < 2:
                label_error.configure(text="Seleccione al menos 2 Asignaturas.", text_color="red")
                return
            else:
                label_error.configure(text="Asignaturas guardadas.", text_color="green")
            
            #Por cada menu este se desactivará
            for i in range(6):
                menus[i].configure(state="disabled")
            
            #Se actualiza la malla, más no en la base de datos
            self.malla[str(semestre)] = seleccionadas
            #Se crea un nuevo tab con el siguiente semnestre
            if int(self.info_carrera["semestres"]) == int(self.i):
                return
            else:
                j = int(semestre)
                if self.i < j + 1:
                    self.i += 1
                    self.tabs_semestres(self.i)
                else:
                    return

        #Botón para guardar
        ctk.CTkButton(tab, text="Guardar Semestre", command=guardar, fg_color=COLOR_FONDO, border_width=2, border_color=COLOR_FONTS, text_color=COLOR_FONTS, font=Fonts.m3, border_spacing=10, hover_color=COLOR_AZUL).place(relx=0.5, rely=0.88, anchor="center")
        #Label de error
        label_error = ctk.CTkLabel(tab, text="", font=Fonts.i3)
        label_error.place(relx=0.5, rely=0.93, anchor="center")
    
    #Función para comparar la malla antigua y la nueva
    def comparar_mallas(self, malla_antigua: dict, malla_nueva: dict):
        
        #Se guardan las asignaturas antiguas en un conjunto
        asig_antigua = set()
        for cursos in malla_antigua.values():
            asig_antigua.update(cursos)
        #Se guardan las asignaturas nuevas en un conjunto
        asig_nueva = set()
        for cursos in malla_nueva.values():
            asig_nueva.update(cursos)

        #Se ven cuales fueron añadidas
        añadidos = asig_nueva - asig_antigua
        #Se ven cuales fueron eliminadas
        eliminados = asig_antigua - asig_nueva

        return {
            "añadidos": añadidos,
            "eliminados": eliminados
        }