import random




colores = ["rojo","amarillo","azul","verde"]
tamano_codigo = 4
intentos = 12

codigo = random.choices(colores,k=tamano_codigo)

print(codigo)