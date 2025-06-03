edad = int(input("Ingresa tu año de nacimiento: "))
edadCalculado = 2025 - edad
if edadCalculado < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")

print(f"Tu edad es {edadCalculado}")

