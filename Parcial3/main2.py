from carro import Carro

def main():
    murcielago = Carro("Lamborghini", "Murcielago", 2005)
    impala = Carro("Chevrolet", "Impala", 1967)
    kia = Carro("Kia", "K3", 2026)

    while True:

        print("")
        print("1. Encender el carro")
        print("2. Acelerar el carro")
        print("3. Frenar el carro")
        print("4. Mostrar estado del carro")
        print("5. Salir")
        print("--------------------")

        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                murcielago.encender()
            case "2":
                cantidad = int(input("Ingresa la cantidad de veces que deseas acelerar: "))
                murcielago.acelerar(cantidad)
            case "3":
                murcielago.frenar()
            case "4":
                murcielago.mostrar_estado()
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()