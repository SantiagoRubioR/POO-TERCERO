#1 
texto = "TEC Azuay"
print(texto[4:7])

stock = {"laptop": 4, "mouse": 35, "teclado": 8, "monitor": 12, "webcam": 2}
# Escriba su solución aquí

print("Inventario:")
for producto, unidades in stock.items():
    print(f"{producto:<10} : {unidades:>10} unidades")

unidades = sum(stock.values())
print(f"Total de unidades en stock: {unidades}")

def suma(a,b):
    return a+b
resultado = suma(8,412)
print (resultado)