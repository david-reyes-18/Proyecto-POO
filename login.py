import tkinter as tk
from Utils.utils import x, y, MIN_ANCHO, MIN_ALTO

#Creacion de la ventana de Inicio de secion
class Login():
    def __init__(self):
        #Configuracion de la ventana
        self.root = tk.Tk()
        self.root.title("Iniciar Seción")
        self.root.config(background="#2b2b2b")
        self.root.geometry(f"{MIN_ANCHO}x{MIN_ALTO}+{x}+{y}")
        self.root.minsize(MIN_ANCHO, MIN_ALTO)
        
        #               Iniciar secion
        
        #Label inicio de secion
        label_inicio = tk.Label(self.root, text="Iniciar sesión", font=('Arial', 30), background="#2b2b2b", fg="#ffffff")
        label_inicio.place(relx=0.1, rely=0.1)
        
        #    Seccion de email
        
        label_email = tk.Label(self.root, text="Ingrese su email", font=('Arial', 20), background="#2b2b2b", fg="#ffffff")
        label_email.place(relx=0.1, rely=0.2)
        
        entrada_email = tk.Entry(self.root)
        entrada_email.place(relx=0.1, rely=0.3)
        
        #    Seccion contrasena
        label_contrasena = tk.Label(self.root, text="Ingrese su contraseña", font=('Arial', 20), background="#2b2b2b", fg="#ffffff")
        label_contrasena.place(relx=0.1, rely=0.4)
        
        entrada_contrasena = tk.Entry(self.root, show='*')
        entrada_contrasena.place(relx=0.1, rely=0.5)
        
        #Boton iniciar sesion
        
        def iniciar_sesion():
            pass
        
        boton_sesion = tk.Button(self.root, text="Iniciar sesion")
        boton_sesion.place(relx = 0.1, rely=0.6)
        
        
    def iniciar(self):
        self.root.mainloop()