from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre,apellido, edad,cedula,celular,direccion,correo,carrera,notas):
        super().__init__(nombre,apellido, edad,cedula,celular,direccion,correo)
        self.carrera = carrera
        self.notas = notas
    def promedio(self):
        return sum(self.notas)/len(self.notas)
    def validar_edad(self):
        return  f"{super().validad_edad()}, carrera: {self.carrera}"
    def __str__(self):
        return f"{super().__str__()},  Carrera: {self.carrera}, Promedio: {self.promedio()}"