class VistaFarmacia:
    def mostrar_menu(self):
        print("\n FARMACIA SAN JOSE")
        print("1. Registrar medicamento")
        print("2. Mostrar medicamentos")
        print("3. Vender medicamento")
        print("4. Salir")
        return input("Elija una opción: ")

    def pedir_medicamento(self):
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cajas = int(input("Cajas: "))
        return nombre, precio, cajas

    def mostrar_medicamentos(self, lista_medicamentos):
        print(f"\n{'Código'} | {'Nombre'} | {'Precio'} | Cajas")
        print(" ")
        for m in lista_medicamentos:
            print(m)

    def pedir_codigo(self):
        return int(input("Código del medicamento: "))

    def pedir_cantidad(self):
        return int(input("Cantidad de cajas: "))

    def mostrar_mensaje(self, mensaje):
        print(mensaje)