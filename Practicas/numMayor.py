numeros = []  
print("Ingrese 6 números enteros:")
for i in range(6):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)  # Aquí sí estamos guardando todos

mayor = max(numeros)
print(f"El número mayor es {mayor}")