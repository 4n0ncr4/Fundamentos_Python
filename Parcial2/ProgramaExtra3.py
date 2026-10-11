import random
NUMERO_MAXIMO = 20
INTENTOS_MAXIMOS = 5

def quedan_intentos(intentos):
    return intentos < INTENTOS_MAXIMOS

def jugar():
    secreto = random.randint(1, NUMERO_MAXIMO)
    intentos = 0
    acerto = False
    print("Adivina el número entre 1 y", NUMERO_MAXIMO)
    print("Tienes", INTENTOS_MAXIMOS, "intentos para adivinarlo")

    while quedan_intentos(intentos):
        respuesta = input("Tu número (o 0 para rendirte): ")

        if not respuesta.isdigit():
            print("Escribe solo números")
            continue
        numero = int(respuesta)

        if numero == 0:
            print("Te rendiste")
            break
        intentos += 1

        if numero == secreto:
            acerto = True
            break
        elif numero < secreto:
            print("Muy bajo")
        else:
            print("Muy alto")
    if acerto:
        print("¡Ganaste en", intentos, "intentos!")
    else:
        print("El número era", secreto)

jugar()