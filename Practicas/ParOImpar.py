num = []
cont = 0
cont2 = 0
pares = []
impares = []
print("Ingrese 10 numeros")
for i in range(10):
    numer = int(input(f"Ingrese el numero {i+1} :"))
    num.append(numer)
    if numer % 2 == 0:
        cont += 1
        pares.append(numer)
    else:
        cont2 += 1
        impares.append(numer)

print(f"\nCantidad de números pares: {cont}")
print(f"Cantidad de números impares: {cont2}")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")

