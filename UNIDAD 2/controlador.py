class ControladorMedicamentos:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def iniciar(self):
        while True:
            op = self.vista.mostrar_menu()

            if op == "1":
                try:
                    nombre, precio, cajas = self.vista.pedir_medicamento()
                    codigo = self.modelo.registrar(nombre, precio, cajas)
                    self.vista.mostrar_mensaje(f"Medicamento registrado: #{codigo}")
                except ValueError as e:
                    self.vista.mostrar_mensaje(f"Error al registrar medicamento: {e}")

            elif op == "2":
                lista = self.modelo.obtener_todos()
                self.vista.mostrar_medicamentos(lista)

            elif op == "3":
                try:
                    codigo, cantidad = self.vista.pedir_venta()
                    restantes = self.modelo.vender(codigo, cantidad)
                    self.vista.mostrar_mensaje(f"Listo. Quedan {restantes} cajas.")
                except ValueError as e:
                    self.vista.mostrar_mensaje(f"Error en la venta: {e}")
            elif op == "4":
                self.vista.mostrar_mensaje("Salir")
                break
            else:
                self.vista.mostrar_mensaje("Ingrese una opción válida.")