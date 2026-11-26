class VistaHotel:
    def mostrar_menu(self):
        print("HOTEL DEL CENTRO HISTORICO DE CUENCA")
        print("-"*50)
        print("------MENU------")
        print("1. Registrar Tipo de Habitacion")
        print("2. Mostrar Tipo Habitacion")
        print("3. Reservar Habitacion")
        print("4. Buscar por nombre ")
        print("5. Mostrar Reserva")
        print("6. Anular Reserva")
        print("7. Reporte general ")
        print("8. Salir")
        return input("Ingrese una opción: ")
    
    def ingresar_tipo_habitacion(self):
        tipo = input("Ingrese el tipo de habitacion: \n 1. Simple \n 2. Doble \n 3. Suite \n")
        precio = float(input("Ingrese el precio de la habitacion por noche: "))
        num_disponibles = int(input("Ingrese el número de habitaciones disponibles: "))
        return tipo, precio, num_disponibles

    def pedir_reserva(self):
        codigo = int(input("Código del tipo de habitación: "))
        cantidad = int(input("Cantidad de habitaciones: "))
        noches = int(input("Número de noches (1 a 15): "))
        return codigo, cantidad, noches