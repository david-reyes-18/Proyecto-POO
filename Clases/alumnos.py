from Clases.usuario import Usuarios

class Alumno(Usuarios):
    def __init__(self, correo, nombre, rut, carrera, asignaturas, contrasena, profesores, semestre):
        super().__init__(correo, nombre, rut, contrasena)
        self.carrera = carrera
        self.asignaturas = asignaturas
        self.profesores = profesores
        self.semestre = semestre