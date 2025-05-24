suma = 0
contPares = 0
contImpares = 0

while True:

    entrada = input("Introduce un número entero de al menos 4 cifras: ")
    try:
        numEnt = int(entrada)
        longitud = len(str(abs(numEnt)))
        if longitud >= 4:
            break
        else:
            print("El número debe tener al menos 4 dígitos. Intenta otra vez.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa solo números enteros.")
digitos = [int(d) for d in str(abs(numEnt))]
for digito in digitos:
    digito = int(digito)
    suma += digito
    if digito % 2 == 0:
        contPares += 1
    else:
        contImpares += 1

print(f"Longitud del número: {longitud}")
print(f"Suma de los dígitos: {suma}")
print(f"Cantidad de dígitos pares: {contPares}")
print(f"Cantidad de dígitos impares: {contImpares}")
