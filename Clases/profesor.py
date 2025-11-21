from Clases.usuario import Usuarios

class Profesor(Usuarios):
    def __init__(self, correo, nombre, rut, asignaturas, contrasena):
        super().__init__(correo, nombre, rut, contrasena)
        self.asignaturas = asignaturas