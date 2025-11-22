import tkinter as tk

#Visualizar el alto y ancho de la ventana del computador
ventana = tk.Tk()
ventana.withdraw()

ANCHO = ventana.winfo_screenwidth()
ALTO = ventana.winfo_screenheight()

ventana.destroy()

#El minimo alto y ancho que debe tener la ventana
MIN_ANCHO = int(ANCHO * 0.75)
MIN_ALTO = int(ALTO * 0.75)


#Coordenadas para centrar las ventanas
x = int((ANCHO // 2) - (MIN_ANCHO // 2))
y = int((ALTO // 2) - (MIN_ALTO // 2))

#Tamaño de las ventanas Top Level
TOPLEVEL_ANCHO = 600
TOPLEVEL_ALTO = 500