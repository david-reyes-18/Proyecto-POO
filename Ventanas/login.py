#Librerias y modulos que usaremos
import customtkinter as ctk
from Utils.utils import *
from Utils.paths import *
from Utils.functions import cargar_jsons
from Ventanas.ventana_alumno import VentanaAlumno
from Ventanas.ventana_admin import VentanaAdmin
from Ventanas.ventana_profe import VentanaProfe
from Utils.fonts import Fonts
from PIL import Image

#Creación de la ventana de Inicio de sesión con customtkinter
class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        #Configuracion de la ventana
        self.title("Iniciar Sesión en el Instituto Epsilon")
        self.geometry(f"{MIN_ANCHO}x{MIN_ALTO}+{x}+{y}")
        self.configure(fg_color = COLOR_FONDO)
        self.minsize(MIN_ANCHO, MIN_ALTO)
        
        #Se cargan los tipos de letra que usará la aplicación
        Fonts.cargar()
        
        ctk.CTkLabel(self, text="", image=img_fondo).place(relx=0, rely=0, relheight=1, relwidth=1)
        ctk.CTkLabel(self, image=img_epsilon, text="").place(relx=0.9, rely=0.01)
        
        #                           Iniciar sesión
        
        self.frame = ctk.CTkFrame(self, border_color=COLOR_FONTS, border_width=2, fg_color=COLOR_FONDO, width=MIN_ANCHO*0.4)
        self.frame.place(relx=0.5, rely=0.5, anchor="center", relheight = 0.7)
        
        #       Label inicio de sesión
        label_inicio = ctk.CTkLabel(self.frame, text="Iniciar sesión", font=Fonts.m1, text_color=COLOR_FONTS)
        label_inicio.place(relx=0.5, rely=0.15, anchor="center")
        
        #       Sección de email
        
        label_email = ctk.CTkLabel(self.frame, text="Ingrese su email:", font=Fonts.i1, text_color=COLOR_FONTS)
        label_email.place(relx=0.5, rely=0.32, anchor="center")
        
        entrada_email = ctk.CTkEntry(self.frame, placeholder_text="correo.institucional@rol.epsilon.cl", font=Fonts.m3, width=MIN_ANCHO*0.27, border_width=2, height=48, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS)
        entrada_email.place(relx=0.5, rely=0.39, anchor="center")
        
        label_error_email = ctk.CTkLabel(self.frame, text="", font=Fonts.i4)
        label_error_email.place(relx=0.5, rely=0.45, anchor="center")
        
        #       Sección contraseña
        
        label_contrasena = ctk.CTkLabel(self.frame, text="Ingrese su contraseña:", font=Fonts.i1, text_color=COLOR_FONTS)
        label_contrasena.place(relx=0.5, rely=0.54, anchor="center")
        
        entrada_contrasena = ctk.CTkEntry(self.frame, show='*', placeholder_text="Contraseña", width=MIN_ANCHO*0.27, border_width=2, font=Fonts.m3, height=48, text_color=COLOR_FONTS, fg_color=COLOR_FONDO, border_color=COLOR_FONTS)
        entrada_contrasena.place(relx=0.5, rely=0.61, anchor="center")
        
        label_error_contra = ctk.CTkLabel(self.frame, text="", font=Fonts.i4)
        label_error_contra.place(relx=0.5, rely=0.67, anchor="center")

        #       Mostrar/Ocultar contraseña
        
        def mostrar_contrasena():
            if check_val.get() == "on":
                entrada_contrasena.configure(show="*")
            elif check_val.get() == "off":
                entrada_contrasena.configure(show="")
        
        check_val = ctk.StringVar(value="on")
        seccion_checkeo = ctk.CTkCheckBox(self.frame, variable=check_val, command=mostrar_contrasena, onvalue="off", offvalue="on", text="Mostrar Contraseña", font=Fonts.i2, text_color=COLOR_FONTS, border_color=COLOR_FONTS, hover_color=COLOR_AZUL, checkmark_color=COLOR_FONDO)
        seccion_checkeo.place(relx=0.5, rely=0.76, anchor="center")
        
        
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
                    VentanaAlumno(email, master=self)
                    self.withdraw()
                else:
                    entrada_email.configure(border_color=COLOR_CONFIRMACION)
                    label_error_email.configure(text="")
                    
                    entrada_contrasena.configure(border_color=COLOR_ELIMINAR)
                    label_error_contra.configure(text="Contraseña Incorrecta", text_color=COLOR_ELIMINAR)
            
            #Verificar si es profesor
            elif email in datos_profesor:
                if contrasena == datos_profesor[email]["contrasena"]:
                    VentanaProfe(email, master=self)
                    self.withdraw()
                else:
                    entrada_email.configure(border_color=COLOR_CONFIRMACION)
                    label_error_email.configure(text="")
                    
                    entrada_contrasena.configure(border_color=COLOR_ELIMINAR)
                    label_error_contra.configure(text="Contraseña Incorrecta", text_color=COLOR_ELIMINAR)
                    
            #Verificar si es administrador
            elif email in datos_administradores:
                if contrasena == datos_administradores[email]["contrasena"]:
                    VentanaAdmin(email, master=self)
                    self.withdraw()
                else:
                    entrada_email.configure(border_color=COLOR_CONFIRMACION)
                    label_error_email.configure(text="")
                    
                    entrada_contrasena.configure(border_color=COLOR_ELIMINAR)
                    label_error_contra.configure(text="Contraseña Incorrecta", text_color=COLOR_ELIMINAR)
            
            #De no estar el correo en la base de datos se le dirá al usuario que el correo esta incorrecto
            else:
                entrada_email.configure(border_color=COLOR_ELIMINAR)
                label_error_email.configure(text="Email no registrado", text_color=COLOR_ELIMINAR)
                
                entrada_contrasena.configure(border_color=COLOR_ELIMINAR)
        
        #Boton de inicio de sesión
        boton_sesion = ctk.CTkButton(self.frame, text="Iniciar sesión", command=iniciar_sesion, font=Fonts.m3, width=190, height=60,fg_color=COLOR_FONDO, hover_color=COLOR_AZUL,text_color=COLOR_FONTS, border_color=COLOR_FONTS, border_width=2)
        boton_sesion.place(relx=0.5, rely=0.88, anchor="center")
        
        self.bind("<Return>", lambda event: iniciar_sesion())
