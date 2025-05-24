numSecret = 7
while True:
    
    try:    
        numAdivinado = int(input("Adivina el número: "))
        if numAdivinado == numSecret:
            print("¡Has adivinado el número!")
            break
        else:
            print("No es el número, intenta de nuevo.")
    except ValueError:
        print("Por favor, introduce un número válido.")