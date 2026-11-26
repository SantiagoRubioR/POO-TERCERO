#DECLARACION DE FUNCIONES
"""
def saludar():
    print("HOLA NASSTI")

saludar()

def calcular_edad(anio_nacimiento, anio_actual):
    print("La edad es: ", anio_actual-anio_nacimiento )

a1 = int(input("INGRESE AÑO de nacimiento: "))
a2 = int(input("INGRESE AÑO actual: "))

calcular_edad(a1,a2)    
"""
#FUNCIONES CON RETORNO
""""
def calcular_iva(precio):
    return(precio*0.15)
resultado = calcular_iva(100)
print("precio con iva es:" ,  resultado)
"""
#FUNCION CON LISTA
'''
def par_o_impar(numero):
    for i in numero:
        if i % 2== 0:
            print(i)
            print("numero par")
        else:
            print(i)
            print("Es impar")
lista_numeros = range(0,1001,2)
lista_numeros2 = range(50,0,-1)
print(lista_numeros2, end=" ")

#
def suma_numeros(*a):
    return sum(a)
print(suma_numeros(1,2,3))
'''
#diccionario
def estudiantes(**lista_estudiates):
    suma_total = 0 
    for nombre,edad in lista_estudiates.items():
        print("El estudiante" , nombre, " tiene " , edad , "años")
        suma_total += edad
    print("La suma total es:" , suma_total)
estudiantes(Santiago=24,Juan=18, Jose= 20, pepe= 55, erika = 19, orisa = 45, kaeas = 18 )

#MENU DE USAURIO

