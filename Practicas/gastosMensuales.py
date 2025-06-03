ingreso = int(input("Ingresa tu ingreso mensual: "))
gastos = []
suma = 0

for i in range(5):
    gasto = int(input(f"Ingresa tu gasto {i+1}: "))
    gastos.append(gasto)
    suma += gasto

total = ingreso - suma
print(f"\nTotal de gastos: {suma:.2f}")

if total < 0:
    print(f"Te quedaste sin dinero. Estás en números rojos: {total:.2f}")
elif total == 0:
    print("Gastaste exactamente todo tu ingreso.")
else:
    print(f"Aún te queda dinero: {total:.2f}")