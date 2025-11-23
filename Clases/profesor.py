from Clases.usuario import Usuarios

class Profesor(Usuarios):
    def __init__(self, correo, nombre, rut, asignaturas, contrasena, alumnos):
        super().__init__(correo, nombre, rut, contrasena)
        self.asignaturas = asignaturas
        self.alumnos = alumnos