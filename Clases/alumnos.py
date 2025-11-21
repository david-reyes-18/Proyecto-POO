from usuario import Usuario

class Alumno(Usuario):
    def __init__(self, correo, nombre, rut, contrasena, carrera, asignaturas):
        super().__init__(correo, nombre, rut, contrasena)
        self.carrera = carrera
        self.asignaturas = asignaturas