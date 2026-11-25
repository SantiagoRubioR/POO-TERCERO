class ControladorFarmacia:
    def __init__(self,modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def iniciar(self):
        while True:
            op = self.vista.mostrar_menu()

            if op == "1":
                nombre, precio, cajas = self.vista.pedir_medicamento()
                codigo = self.modelo.registrar(nombre, precio, cajas)
                self.vista.mostrar_mensaje(f"Medicamento registrado: #{codigo}")

            elif op == "2":
                lista = self.modelo.obtener_todos()
                self.vista.mostrar_medicamentos(lista) 
            elif op == "3":
                cod = self.vista.pedir_codigo()
                encontrado = self.modelo.buscar_por_codigo(cod)

                if encontrado is None:
                    self.vista.mostrar_mensaje("Medicamento no encontrado.")    
                else:
                    cant = self.vosta.pedir_cantidad()
                    exito, mensaje = encontrado.vender(cant)
                    self.vista.mostrar_mensaje(mensaje)
            elif op == "4":
                self.vista.mostrar_mensaje("Salir")
                break
            else:
                self.vista.mostrar_mensaje("Ingrese una opción válida.")