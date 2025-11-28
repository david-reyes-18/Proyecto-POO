#Libreria y modulo usados
import customtkinter as ctk
from Utils.paths import MONTSERRAT, INTER

#Clase que alberga los tipos de letra
class Fonts:
    #Al inicio todos los tipos de letra no tendrán valor
    
    #Fuentes montserrat
    m1 = None
    m2 = None
    m2bold = None
    m3 = None
    m4 = None
    
    #Fuentes Inter
    i1 = None
    i2 = None
    i3 = None
    i4 = None
    
    #Función que carga todos los tipos de letra
    def cargar():
        
        #Fuentes Montserrat
        Fonts.m1 = ctk.CTkFont(family=MONTSERRAT, size=50, weight="bold")
        Fonts.m2 =ctk.CTkFont(family=MONTSERRAT, size=31)
        Fonts.m2bold =ctk.CTkFont(family=MONTSERRAT, size=31, weight="bold")
        Fonts.m3 = ctk.CTkFont(family=MONTSERRAT, size=20)
        Fonts.m4 = ctk.CTkFont(family=MONTSERRAT, size=15)
        
        #Fuentes Inter
        Fonts.i1 = ctk.CTkFont(family=INTER, size=25, weight="bold")
        Fonts.i2 = ctk.CTkFont(family=INTER, size=19)
        Fonts.i3 = ctk.CTkFont(family=INTER, size=15)
        Fonts.i4 = ctk.CTkFont(family=INTER, size=10)