from Clases.usuario import Usuarios

class Admin(Usuarios):
    def __init__(self, correo, nombre, rut, contrasena):
        super().__init__(correo, nombre, rut, contrasena)