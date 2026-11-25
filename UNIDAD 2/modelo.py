class Medicamento:
    def __init__(self, codigo, nombre, precio, cajas):
        if not nombre.strip():
            raise ValueError("Error: el nombre no puede estar vacío.")
        if precio <= 0:
            raise ValueError("Error: el precio debe ser mayor que cero.")
        if cajas < 0:
            raise ValueError("Error: las cajas no pueden ser negativas.")
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cajas = cajas

    def vender(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Error: la cantidad debe ser mayor que cero.")
        if cantidad > self.cajas:
            raise ValueError(f"Error: solo hay {self.cajas} cajas disponibles.")
        self.cajas -= cantidad
        return self.cajas

    def __str__(self):
        return f"{self.codigo:<6} | {self.nombre:<18} | ${self.precio:<7.2f} | {self.cajas}"


class ListaMedicamentos:
    def __init__(self):
        self.medicamentos = []
        self.cargar_medicamentos()

    def cargar_medicamentos(self):
        self.medicamentos = [
            Medicamento(1, "Paracetamol", 2.50, 30),
            Medicamento(2, "Ibuprofeno", 3.20, 20)
        ]

    def registrar(self, nombre, precio, cajas):
        codigo = len(self.medicamentos) + 1
        nuevo = Medicamento(codigo, nombre, precio, cajas)
        self.medicamentos.append(nuevo)
        return codigo

    def obtener_todos(self):
        return self.medicamentos

    def buscar_por_codigo(self, codigo):
        for m in self.medicamentos:
            if m.codigo == codigo:
                return m
        return None
    def vender(self, codigo, cantidad):
        medicamento = self.buscar_por_codigo(codigo)
        if medicamento is None:
            raise ValueError("Error: no existe un medicamento con ese código.")
        return medicamento.vender(cantidad)