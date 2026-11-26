class Persona:
    def __init__(self, nombre,apellido, edad,cedula,celular,direccion,correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cedula = cedula
        self.celular = celular
        self.direccion = direccion
        self.correo = correo
    def validad_edad(self):
        if self.edad >= 18:
            return "Es mayor de edad"
        else:
            return "Es menor de edad"
    def __str__(self):
        return f"Nombre: {self.nombre},  , {self.apellido}, Edad: {self.edad}, Cédula: {self.cedula}, Celular: {self.celular}, Dirección: {self.direccion}, Correo: {self.correo}"