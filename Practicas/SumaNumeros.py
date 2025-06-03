numeros = []
suma = 0
for i in range(5):
    num = int(input("Ingresa los 5 numeros: "))
    numeros.append(num)
    suma = suma + num

print(f"La suma es {suma}")