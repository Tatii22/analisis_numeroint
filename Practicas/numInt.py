num = []
cont = 0
print("Ingrese 7 numeros")
for i in range(7):
    numer = int(input(f"Ingrese el numero {i+1} :"))
    num.append(numer)

for numero in num:
    if numero > 50:
        cont += 1

print(f"Hay {cont} numeros mayores a 50")