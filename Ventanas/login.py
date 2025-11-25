#Librerias y modulos que usaremos
import customtkinter as ctk
from Utils.utils import x, y, MIN_ANCHO, MIN_ALTO
from Utils.paths import ALUMNOS, PROFESORES, ADMINISTRADORES
from Utils.funcions import cargar_jsons
from Ventanas.ventana_alumno import VentanaAlumno
from Ventanas.ventana_admin import VentanaAdmin
from Ventanas.ventana_profe import VentanaProfe
from Utils.fonts import Fonts

#Creación de la ventana de Inicio de sesión con customtkinter
class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        #Configuracion de la ventana
        self.title("Iniciar Sesión en el Instituto Epsilon")
        self.geometry(f"{MIN_ANCHO}x{MIN_ALTO}+{x}+{y}")
        self.minsize(MIN_ANCHO, MIN_ALTO)
        
        #Se cargan los tipos de letra que usará la aplicación
        Fonts.cargar()
        
        #                           Iniciar sesión
        
        #       Label inicio de sesión
        label_inicio = ctk.CTkLabel(self, text="Iniciar sesión", font=Fonts.m1)
        label_inicio.place(relx=0.05, rely=0.1)
        
        #       Sección de email
        
        label_email = ctk.CTkLabel(self, text="Ingrese su email:", font=Fonts.i1)
        label_email.place(relx=0.05, rely=0.25)
        
        entrada_email = ctk.CTkEntry(self, placeholder_text="correo.institucional@rol.epsilon.cl", font=Fonts.m3, width=MIN_ANCHO*0.25, border_width=2)
        entrada_email.place(relx=0.05, rely=0.3)
        
        label_error_email = ctk.CTkLabel(self, text="", font=Fonts.i4)
        label_error_email.place(relx=0.07, rely=0.35)
        
        #       Sección contraseña
        
        label_contrasena = ctk.CTkLabel(self, text="Ingrese su contraseña", font=Fonts.i1)
        label_contrasena.place(relx=0.05, rely=0.4)
        
        entrada_contrasena = ctk.CTkEntry(self, show='*', placeholder_text="Contraseña", width=MIN_ANCHO*0.25, border_width=2, font=Fonts.m3)
        entrada_contrasena.place(relx=0.05, rely=0.45)
        
        label_error_contra = ctk.CTkLabel(self, text="", font=Fonts.i4)
        label_error_contra.place(relx=0.07, rely=0.5)
        
        #       Mostrar/Ocultar contraseña
        
        def mostrar_ocultar():
            if check_val.get() == "on":
                entrada_contrasena.configure(show="*")
            elif check_val.get() == "off":
                entrada_contrasena.configure(show="")
        
        check_val = ctk.StringVar(value="on")
        seccion_checkeo = ctk.CTkCheckBox(self, variable=check_val, command=mostrar_ocultar, onvalue="off", offvalue="on", text="Mostrar Contraseña", font=Fonts.i2)
        seccion_checkeo.place(relx = 0.08, rely=0.56)
        
        
        #                  Boton iniciar sesión
        
        #Función que verifica el inicio de sesión, verifica si el correo y la contraseña son correctas para iniciar su ventana correspondiente
        
        def iniciar_sesion():
            #Obtener la información que entrego el usuario
            email = entrada_email.get()
            contrasena = entrada_contrasena.get()
            
            #Cargar los datos que se tienen en la base de datos
            datos_alumnos = cargar_jsons(ALUMNOS)
            datos_profesor = cargar_jsons(PROFESORES)
            datos_administradores = cargar_jsons(ADMINISTRADORES)
            
            #    Verificar el email y la contraseña
            
            #Verificar si es alumno
            if email in datos_alumnos:
                if contrasena == datos_alumnos[email]["contrasena"]:
                    ventanita = VentanaAlumno(email, master=self)
                    self.withdraw()
                else:
                    entrada_email.configure(border_color="green")
                    label_error_email.configure(text="Email correcto", text_color="green")
                    
                    entrada_contrasena.configure(border_color="red")
                    label_error_contra.configure(text="Contraseña Incorrecta", text_color="red")
            
            #Verificar si es profesor
            elif email in datos_profesor:
                if contrasena == datos_profesor[email]["contrasena"]:
                    ventanita = VentanaProfe(email, master=self)
                    self.withdraw
                else:
                    entrada_email.configure(border_color="green")
                    label_error_email.configure(text="Email correcto", text_color="green")
                    
                    entrada_contrasena.configure(border_color="red")
                    label_error_contra.configure(text="Contraseña Incorrecta", text_color="red")
                    
            #Verificar si es administrador
            elif email in datos_administradores:
                if contrasena == datos_administradores[email]["contrasena"]:
                    ventanita = VentanaAdmin(email, master=self)
                    self.withdraw()
                else:
                    entrada_email.configure(border_color="green")
                    label_error_email.configure(text="Email correcto", text_color="green")
                    
                    entrada_contrasena.configure(border_color="red")
                    label_error_contra.configure(text="Contraseña Incorrecta", text_color="red")
            
            #De no estar el correo en la base de datos se le dirá al usuario que el correo esta incorrecto
            else:
                entrada_email.configure(border_color="red")
                label_error_email.configure(text="Email Incorrecto", text_color="red")
                
                entrada_contrasena.configure(border_color="red")
                label_error_contra.configure(text="Contraseña Incorrecta", text_color="red")
        
        #Boton de inicio de sesión
        boton_sesion = ctk.CTkButton(self, text="Iniciar sesión", command=iniciar_sesion, font=Fonts.m3, width=190, height=60)
        boton_sesion.place(relx = 0.09, rely=0.7)
