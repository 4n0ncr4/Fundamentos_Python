# Simulador de Do-While en Python

palabra_secreta = "python"
contador = 0

while True:
    palabra = input("Ingresa la palabra secreta: ").lower()
    contador = contador + 1
    if palabra == palabra_secreta:
        print("Adivinaste la palabra secreta!")
        break
    else:
        print("Te queda(n)", 5 - contador, "intento(s).")
        print("Palabra incorrecta. Intenta de nuevo.")
    if palabra != palabra_secreta and contador > 4:
        print(f"La palabra secreta era: {palabra_secreta}")
        break
