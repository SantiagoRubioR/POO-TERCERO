class Medicamento:
    def __init__(self, codigo, nombre, precio, cajas):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cajas = cajas

    def vender(self, cantidad):
        if cantidad <= 0:
            return False, "Error: la cantidad debe ser mayor que cero."
        if cantidad > self.cajas:
            return False, f"Error: Hay {self.cajas} cajas disponibles."
        self.cajas -= cantidad
        return True, f"Quedan {self.cajas} cajas disponibles."

    def __str__(self):
        return f"{self.codigo:<6} | {self.nombre:<18} | ${self.precio:<7.2f} | {self.cajas}"


class ListaMedicamentos:
    def __init__(self):
        self.medicamentos = [
            ListaMedicamentos(1, "Paracetamol", 2.50, 30),
            ListaMedicamentos(2, "Ibuprofeno", 3.20, 20)
        ]

    def registrar(self, nombre, precio, cajas):
        codigo = len(self.medicamentos) + 1
        nuevo = ListaMedicamentos(codigo, nombre, precio, cajas)
        self.medicamentos.append(nuevo)
        return codigo

    def obtener_todos(self):
        return self.medicamentos

    def buscar_por_codigo(self, codigo):
        for m in self.medicamentos:
            if m.codigo == codigo:
                return m
        return None