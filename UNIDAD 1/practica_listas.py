notas = [8, 9, 7, 10, 8]
notas.insert(2, 9) 
notas.insert(4, 6)
print(notas[2])  

print(len(notas))

print(notas[-1])

print(sum(notas))
print(f"maximo: {max(notas)}")
print(min(notas))
print(notas[2:])
print(notas[:3])
print(notas[:-1])

#TUPLAS
meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

estudiante = {
"cedula": "123456789",
"correo": "juan.perez@universidad.edu",
"nombre": "Juan Perez",
"telefono": "555-1234",
"notas": [8, 9, 7, 10, 8]
}   
print(estudiante["nombre"])


print(estudiante.keys())
print(estudiante.get("correo"))

socio = {
    "cedula": "0102030405",                 # str: puede empezar con 0
    "nombre": "  ana lucía pérez ",          # str con espacios y minúsculas
    "edad": 34,                              # int
    "activo": True,                          # bool
    "garante": None,                         # None: todavía no tiene
    "cuentas": [                             # list de dict
        {"numero": "AH-001", "tipo": "ahorros", "saldo": 1520.75},
        {"numero": "PF-010", "tipo": "plazo fijo", "saldo": 5000.0},
        {"numero": "AH-002", "tipo": "ahorros", "saldo": 80.5},
    ],
}
print(socio["nombre"].strip().title())