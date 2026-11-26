from persona import Persona

class Docente(Persona):
    def __init__(self, nombre, apellido, edad, cedula, celular, direccion, correo, asignatura, horas):
        super().__init__(nombre, apellido, edad, cedula, celular, direccion, correo)
        self.asignatura = asignatura
        self.horas = horas
        self.valor = 20
        self.salario = self.calcular_salario()

    def calcular_salario(self):
        self.salario = self.horas * self.valor
        return self.salario

    def __str__(self):
        return f"{super().__str__()}, Asignatura: {self.asignatura}, Salario: ${self.salario}"