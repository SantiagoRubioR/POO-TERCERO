# Recuperación de la Lección 2

def registrar_nombre():
    global usuario_nombre
    usuario_nombre = input("Ingrese su nombre: ").strip()
    if usuario_nombre:
        print(f"Hola, {usuario_nombre}.\n")
    else:
        print("Ingreso como invitado\n")

def pregunta_1():
    print("\n--- Pregunta 1 ---")
    print('Código:\ntexto = "TEC Azuay"\nprint(texto[4:7])')
    texto = "TEC Azuay"
    resultado = texto[4:7]
    print(f"Resultado de ejecución (Respuesta correcta): {resultado}\n")

def pregunta_2():
    print("\n--- Pregunta 2 ---")
    print('Código:\nsocio = {"nombre": "Ana", "saldo": 120}\nprint(socio.get("correo", "Sin correo"))')
    socio = {"nombre": "Ana", "saldo": 120}
    resultado = socio.get("correo", "Sin correo")
    print(f"Resultado de ejecución (Respuesta correcta): {resultado}\n")

def pregunta_3():
    print("\n--- Pregunta 3 ---")
    print('Código:\nfrase = "aprendo Python en TEC"\nprint(len(frase.split()))')
    frase = "aprendo Python en TEC"
    resultado = len(frase.split())
    print(f"Resultado de ejecución (Respuesta correcta): {resultado}\n")

def pregunta_4():
    print("\n--- Pregunta 4 ---")
    print('Código:\nprint("ab" * 3)')
    resultado = "ab" * 3
    print(f"Resultado de ejecución (Respuesta correcta): {resultado}\n")

def pregunta_5():
    print("\n--- Pregunta 5 ---")
    print("Código:\na = [1, 2, 3]\nb = a\nb[0] = 5\nprint(a)")
    a = [1, 2, 3]
    b = a
    b[0] = 5
    print(f"Resultado de ejecución (Respuesta correcta): {a}\n")

def pregunta_6():
    print("\n--- Pregunta 6 ---")
    print('Código:\nfor n in [1, 2, 3, 4]:\n    if n == 3:\n        break\n    print(n, end=" ")')
    print("Resultado de ejecución (Respuesta correcta): ", end="")
    for n in [1, 2, 3, 4]:
        if n == 3:
            break
        print(n, end=" ")
    print("\n")

def pregunta_7():
    print("\n--- Pregunta 7 ---")
    print("Código:\nsuma = 0\nfor n in range(1, 5):\n    if n % 2 != 0:\n        continue\n    suma += n\nprint(suma)")
    suma = 0
    for n in range(1, 5):
        if n % 2 != 0:
            continue
        suma += n
    print(f"Resultado de ejecución (Respuesta correcta): {suma}\n")

def pregunta_8():
    print("\n--- Pregunta 8 ---")
    print("Código:\ntotal = 0\nn = 1\nwhile n <= 5:\n    total += n\n    n += 1\nprint(total)")
    total = 0
    n = 1
    while n <= 5:
        total += n
        n += 1
    print(f"Resultado de ejecución (Respuesta correcta): {total}\n")

def pregunta_9():
    print("\n--- Pregunta 9 ---")
    print('Código:\nfor i in range(1, 10, 3):\n    print(i, end=" ")')
    print("Resultado de ejecución (Respuesta correcta): ", end="")
    for i in range(1, 10, 3):
        print(i, end=" ")
    print("\n")

def pregunta_10():
    print("\n--- Pregunta 10 ---")
    print('Código:\nfor i in range(3, 0, -1):\n    print(i, end=" ")')
    print("Resultado de ejecución (Respuesta correcta): ", end="")
    for i in range(3, 0, -1):
        print(i, end=" ")
    print("\n")

def pregunta_11():
    print("\n--- Pregunta 11 ---")
    print('Diccionario:\nstock = {"laptop": 4, "mouse": 35, "teclado": 8, "monitor": 12, "webcam": 2}')
    
    stock = {"laptop": 4, "mouse": 35, "teclado": 8, "monitor": 12, "webcam": 2}
    
    print("\nInventario:")
    for producto, unidades in stock.items():
        print(f"{producto:<10} : {unidades:>10} unidades")
        
    poco_stock = [producto for producto, unidades in stock.items() if unidades < 10]
    print(f"\nProductos con poco stock: {poco_stock}")
    
    unidades = sum(stock.values())
    print(f"Total de unidades en stock: {unidades}\n")


def menu_preguntas():
    while True:
        print("================================")
        print("       MENÚ DE PREGUNTAS        ")
        print("       (Lección 2 - POO)        ")
        print("================================")
        print("1. Pregunta 1 ")
        print("2. Pregunta 2 ")
        print("3. Pregunta 3 ")
        print("4. Pregunta 4 ")
        print("5. Pregunta 5 ")
        print("6. Pregunta 6 ")
        print("7. Pregunta 7 ")
        print("8. Pregunta 8 ")
        print("9. Pregunta 9 ")
        print("10. Pregunta 10 ")
        print("11. Pregunta 11 ")
        print("12. Ejecutar TODAS las preguntas")
        print("13. Volver al menú principal")
        
        opc = input("Seleccione una opción (1-13): ").strip()
        
        if opc == "1": pregunta_1()
        elif opc == "2": pregunta_2()
        elif opc == "3": pregunta_3()
        elif opc == "4": pregunta_4()
        elif opc == "5": pregunta_5()
        elif opc == "6": pregunta_6()
        elif opc == "7": pregunta_7()
        elif opc == "8": pregunta_8()
        elif opc == "9": pregunta_9()
        elif opc == "10": pregunta_10()
        elif opc == "11": pregunta_11()
        elif opc == "12":
            pregunta_1()
            pregunta_2()
            pregunta_3()
            pregunta_4()
            pregunta_5()
            pregunta_6()
            pregunta_7()
            pregunta_8()
            pregunta_9()
            pregunta_10()
            pregunta_11()
        elif opc == "13":
            print("MENU PRINCIPAL\n")
            break
        else:
            print("OPCION INVALIDA:)\n")


usuario_nombre = "Invitado"

def menu():
    while True:
        print("********************************")
        print("        MENÚ DE USUARIOS        ")
        print("********************************")
        print(f"Bienvenido: {usuario_nombre}")
        print("1. Ingresar saludo")
        print("2. Menú de preguntas")
        print("3. Salir")
        
        opcion = input("Elija una opción (1-3): ").strip()
        
        if opcion == "1":
            registrar_nombre()
        elif opcion == "2":
            menu_preguntas()
        elif opcion == "3":
            print(f"SALIENDO... ")
            break
        else:
            print("Por favor ingrese 1, 2 o 3, Opcion invalida.\n")
menu()