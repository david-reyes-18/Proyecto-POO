from Clases.usuario import Usuarios

class Alumno(Usuarios):
    def __init__(self, correo, nombre, rut, contrasena, carrera, asignaturas):
        super().__init__(correo, nombre, rut, contrasena)
        self.carrera = carrera
        self.asignaturas = asignaturas