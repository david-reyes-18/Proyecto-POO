import tkinter as tk
import customtkinter as ctk
from PIL import Image
from Utils.paths import *
#Visualizar el alto y ancho de la ventana del computador
ventana = tk.Tk()
ventana.withdraw()

#Alto y ancho de la pantalla
ANCHO = ventana.winfo_screenwidth()
ALTO = ventana.winfo_screenheight()

ventana.destroy()

#El minimo alto y ancho que debe tener la ventana
MIN_ANCHO = int(ANCHO * 0.85)
MIN_ALTO = int(ALTO * 0.85)


#Coordenadas para centrar las ventanas
x = int((ANCHO // 2) - (MIN_ANCHO // 2))
y = int((ALTO // 2) - (MIN_ALTO // 2))

#Tamaño de las ventanas Top Level
TOPLEVEL_ANCHO = 800
TOPLEVEL_ALTO = 700

#Colores Institucionales
COLOR_OSCURO = "#161F24"
COLOR_FONDO = "#1A262D"
COLOR_AZUL = "#2C404B"
COLOR_FONTS = "#98B4C3"
COLOR_ELIMINAR = "#c62222"
COLOR_CONFIRMACION = "#0f9545"

#Imagenes
img_epsilon = ctk.CTkImage(dark_image=Image.open(EPSILON_PNG), size=(125,125))
img_fondo = ctk.CTkImage(dark_image=Image.open(FONDO_INICIO), size=(ANCHO, ALTO))
img_volver = ctk.CTkImage(dark_image=Image.open(VOLVER), size=(80, 80))